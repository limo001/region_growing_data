#!/bin/bash



filename= grep PCDs ou_1_1t.txt | cut -d"/" -f2  |cut -d"." -f1   
echo "$filename"
