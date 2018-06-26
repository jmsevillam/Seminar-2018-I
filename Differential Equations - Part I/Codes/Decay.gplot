set terminal pdf size 4,2.5
set output 'Decay.pdf'
set xlabel 'Time'
set ylabel 'Probability P(t)'
plot 'DataDecay.dat' w lp t 'Simulation', exp(-x) t 'Theoretical'

set terminal qt
replot

