set terminal pdf size 4,2.5
set output 'Harmonic2.pdf'
set xlabel 'Time'
set ylabel 'Angle {/Symbol q}(t)'
plot 'DataHarmonic2.dat' w lp t 'Simulation', sin(x) t 'Theoretical'

set terminal qt
replot

