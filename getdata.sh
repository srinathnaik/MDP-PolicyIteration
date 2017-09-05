# echo "hpi"
# sum=0
# for i in $(seq 1 100);
# do
# 	a=`./planner.sh --mdp mdp100/$i.txt --algorithm hpi | grep "Iterations" | awk '{ print $2 }'`
# 	let 'sum=sum+a'
# done
# echo $sum

# echo "rpi"
# sum=0
# for i in $(seq 1 100);
# do
# 	a=`./planner.sh --mdp mdp100/$i.txt --algorithm rpi --randomseed $RANDOM | grep "Iterations" | awk '{ print $2 }'`
# 	let 'sum=sum+a'
# done
# echo $sum

echo "bspi 1"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 1 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 2"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 2 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 3"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 3 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 4"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 4 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 5"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 5 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 6"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 6 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 7"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 7 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 8"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 8 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 9"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 9 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum

echo "bspi 10"
sum=0
for i in $(seq 1 100);
do
	a=`./planner.sh --mdp mdp100/$i.txt --algorithm bspi --batchsize 10 | grep "Iterations" | awk '{ print $2 }'`
	let 'sum=sum+a'
done
echo $sum