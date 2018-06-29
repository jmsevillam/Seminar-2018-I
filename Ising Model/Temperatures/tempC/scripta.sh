g++ ising.cpp
for i in `LANG=en_US seq 0.05 0.01 4.5`
do
echo $i
time  ./a.out $i 
done
