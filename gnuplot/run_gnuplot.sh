#!/bin/bash
minval=0    # the result of some (omitted) calculation
maxval=4219   # ditto


for file in *.data; do

    #name= echo "$file"|cut -d'.'  -f1
    #echo "$name"
    echo "$file"

     

gnuplot -persist <<-EOFMarker
       set title "$file" font ",14" textcolor rgbcolor "royalblue"
       set terminal wxt  enhanced title "$file " persist raise
       set xlabel "distance"
       set ylabel "angle"
       set zlabel "region" 
       splot "$file" using 1:2:3 with linespoints
       set term png             
       set output "$file.png" 
       replot
       set term x11
EOFMarker


done
