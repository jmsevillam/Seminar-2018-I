g++ ising.cpp
for i in `seq 0.1 0.2 3.5`
do
echo $i
time  ./a.out $i 
done
