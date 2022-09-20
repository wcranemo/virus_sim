#!/bin/zsh
#script to run the program multiple times and output to different files

make     #make sure everything is up to date

rm -r *.txt #delete all old output files

#params
runs=5
runtype="b"
population=10000
runtime=150
touch out{1..$runs}.txt

for i in {1..$runs}; do
   echo "running test ${i}..."
   echo out${i}.txt $runtype $population $runtime | ./main
   # sleep 1
   echo "Done"
done

echo $runs | python mult_run_analysis.py
