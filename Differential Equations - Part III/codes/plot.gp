set vew map
set term pdf
set output 'plot.pdf'
splot 'data.dat' matrix w image
set term qt
replot
