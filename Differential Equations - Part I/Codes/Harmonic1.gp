set terminal pdf size 4,2.5
set output 'Harmonic1.pdf'
set xlabel 'Time'
set ylabel 'Angle {/Symbol q}(t)'
plot 'DataHarmonic1.dat' w lp t 'Simulation', sin(x) t 'Theoretical'

set terminal qt
replot

