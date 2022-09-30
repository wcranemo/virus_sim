#!/bin/zsh
#script to run the program multiple times and output to different files

make     #make sure everything is up to date

rm -r *.txt #delete all old output files

#params
runs=2000 
runtype="b"
population=10000
runtime=150
touch out{1..$runs}.txt

echo "running $runs tests"
loop_percentage=0

for i in {1..$runs}; do
   # echo "running test ${i}..."
   echo -ne "."
   #trying to make loading bar
   echo out${i}.txt $runtype $population $runtime | ./main &
   # sleep 1
   # echo "Done"
done
echo "sims completed"

echo $runs | python mult_run_analysis.py
