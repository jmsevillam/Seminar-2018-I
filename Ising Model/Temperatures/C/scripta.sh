g++ ising.cpp
rm sus/*
rm mag/*
for i in `LANG=en_US seq 0.05 0.05 4.5`
do
echo $i
time  ./a.out $i sus$i
mv sus$i sus/$i
mv $i mag/$i
done
rm sus/*,*
rm mag/*,*
