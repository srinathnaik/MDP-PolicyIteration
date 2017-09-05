#!/bin/bash
echo "hpi"
echo "	MDP2.txt"
./planner.sh --mdp data/MDP2.txt --algorithm hpi > results/2hpi.txt
python test.py results/2hpi.txt data/sol2.txt
echo "	MDP10.txt"
./planner.sh --mdp data/MDP10.txt --algorithm hpi > results/10hpi.txt
python test.py results/10hpi.txt data/sol10.txt
echo "	MDP50.txt"
./planner.sh --mdp data/MDP50.txt --algorithm hpi > results/50hpi.txt
python test.py results/50hpi.txt data/sol50.txt

echo "rpi"
echo "	MDP2.txt"
./planner.sh --mdp data/MDP2.txt --algorithm rpi  --randomseed 34 > results/2rpi.txt
python test.py results/2rpi.txt data/sol2.txt
echo "	MDP10.txt"
./planner.sh --mdp data/MDP10.txt --algorithm rpi --randomseed 34 > results/10rpi.txt
python test.py results/10rpi.txt data/sol10.txt
echo "	MDP50.txt"
./planner.sh --mdp data/MDP50.txt --algorithm rpi --randomseed 34 > results/50rpi.txt
python test.py results/50rpi.txt data/sol50.txt

echo "lp"
echo "	MDP2.txt"
./planner.sh --mdp data/MDP2.txt --algorithm lp > results/2lp.txt
python test.py results/2lp.txt data/sol2.txt
echo "	MDP10.txt"
./planner.sh --mdp data/MDP10.txt --algorithm lp > results/10lp.txt
python test.py results/10lp.txt data/sol10.txt
echo "	MDP50.txt"
./planner.sh --mdp data/MDP50.txt --algorithm lp > results/50lp.txt
python test.py results/50lp.txt data/sol50.txt

echo "bspi"
echo "	MDP2.txt"
./planner.sh --mdp data/MDP2.txt --algorithm bspi  --batchsize 3 > results/2bspi.txt
python test.py results/2bspi.txt data/sol2.txt
echo "	MDP10.txt"
./planner.sh --mdp data/MDP10.txt --algorithm bspi --batchsize 3 > results/10bspi.txt
python test.py results/10bspi.txt data/sol10.txt
echo "	MDP50.txt"
./planner.sh --mdp data/MDP50.txt --algorithm bspi --batchsize 3 > results/50bspi.txt
python test.py results/50bspi.txt data/sol50.txt