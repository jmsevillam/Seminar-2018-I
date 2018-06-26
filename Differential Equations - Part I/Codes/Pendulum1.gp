set terminal pdf size 4,2.5
set output 'Pendulum1.pdf'
set xlabel 'Time'
set ylabel 'Angle {/Symbol q}(t)'
plot 'DataPendulum1.dat' w lp t 'Simulation'
set terminal qt
replot
set terminal pdf size 4,2.5
set output 'Pendulum1PS.pdf'
set ylabel 'Frequency {/Symbol w}(t)'
set xlabel 'Angle {/Symbol q}(t)'
plot 'DataPendulum1.dat' u 2:3 w lp t 'Simulation'
set terminal qt
replot
mod(x,y) = (x-floor(x/y)*y)
set terminal pdf size 4,2.5
set output 'Pendulum1PS2.pdf'
set ylabel 'Frequency {/Symbol w}(t)'
set xlabel 'Angle {/Symbol q}(t)'
plot 'DataPendulum1.dat' u (mod($2,(2*pi))):3 w p t 'Simulation'
set terminal qt
replot
