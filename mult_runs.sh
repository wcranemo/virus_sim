#!/bin/zsh
#script to run the program multiple times and output to different files

make     #make sure everything is up to date

#params
runs=5
runtype="b"
population=10000
runtime=300
touch out{1..$runs}.txt

for i in {1..$runs}; do
   echo out${i}.txt $runtype $population $runtime | ./main
   sleep 1
done
