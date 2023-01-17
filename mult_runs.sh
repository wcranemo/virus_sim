#!/bin/zsh
#script to run the program multiple times and output to different files

make     #make sure everything is up to date

rm -r *.txt #delete all old output files

#params
runs=10
runtype="b"
population=10000
runtime=150
# soc_dist_thresh=$population   #change this to a lower number to enact social distancing at some threshold
soc_dist_thresh=1000

# integer percent of 100
connection_reduction=50

touch out{1..$runs}.txt

echo "running $runs tests"
loop_percentage=0

for i in {1..$runs}; do
   # echo "running test ${i}..."
   #trying to make loading bar
   # echo $connection_reduction

   echo out${i}.txt $runtype $population $runtime $soc_dist_thresh $connection_reduction | ./main &
   # sleep 1
   echo -ne "."

   # echo "Done"
done
wait
echo "sims completed"

# sleep 30

echo $runs | python mult_run_analysis.py
