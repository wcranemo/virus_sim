#!/bin/zsh

make

rm -r *.txt #delete all old output files

# sum=$(echo ".3 + 1.12" | bc -l)
# echo $sum
#test

#params
runs_per_param=2
runtype="b"
population=10000
runtime=150
# soc_dist_thresh=$population   #change this to a lower number to enact social distancing at some threshold
soc_dist_thresh=2000
connection_reduction=$(echo "50/100" | bc -l)

touch out{1..$runs}.txt

echo "running $runs tests"

soc_dis_params=4
# initializing array of param values
soc_dist_arr[1]=1000
soc_dist_arr[2]=2000
soc_dist_arr[3]=5000
soc_dist_arr[4]=$population

#percent as integer out of 100 since shell doesn't play nice with floats
conn_red_params=2
# conn_red_arr[1]=$(echo "80 / 100" | bc -l)
# conn_red_arr[2]=$(echo "50 / 100" | bc -l)
conn_red_arr[1]=80
conn_red_arr[2]=50

# for i in "${soc_dist_arr[@]}"; do
#    echo $i
# done
touch params.txt
printf "social_dist_param, connection_red_param\n" >> params.txt
for k in {1..$conn_red_params}; do
   for j in {1..$soc_dis_params}; do
      for i in {1..$runs_per_param}; do

         # connection_reduction=connection_red_arr[k]
         # echo "shell vals: ${soc_dist_arr[j]}, ${conn_red_arr[k]} || \n"
         echo out_${k}_${j}_${i}.txt $runtype $population $runtime ${soc_dist_arr[j]} ${conn_red_arr[k]} | ./main &
         echo -ne "."

         # echo "conn_red = ${conn_red_arr[k]}, soc_dist_thresh = ${soc_dist_arr[j]}, run # ${i}"
         # echo "Done"
      done
      printf "${soc_dist_arr[j]}, ${conn_red_arr[k]} \n" >> params.txt
      # printf "conn_red = ${conn_red_arr[k]}, soc_dist_thresh = ${soc_dist_arr[j]}" >> params.txt
   done
done
wait
# echo "sleeping 5"
# sleep 5
# echo "sims completed"

# sleep 30
#
echo $runs_per_param $runtime | python social_dist.py
