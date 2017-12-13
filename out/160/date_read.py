import os
from PIL import Image
from array import *
from random import shuffle
import glob
import argparse





# Load from and save to
FileList = []

path = "./out"
for filename in os.listdir(path):
    if filename.endswith(".txt"):
        print ("filename: ",filename)
        FileList.append(os.path.join(path,filename))
        
print FileList  

# print FileList  
for filename in FileList:
    
    
    
    file_name = filename.split('/')[2]  
    print "file_name", file_name 
        #with open(file_name) as f:
        #    content = f.readlines()
    inpath = os.path.join(filename)
    print inpath
    fi = open(inpath)
    
    TxtList = []
    OutPath = []
    for line in fi:
        if line != "\n":
            data = line.split()
            if data[0][0:4] == "pcds":
                
                txt = data[0].split('/')[1].split('.')[0]
                outpath = os.path.join("txt/", txt+".txt")
                TxtList.append(line)
                OutPath.append(outpath)
                print outpath
                fo = open(outpath, 'a+')
                fo.write(line)
                #fo.close
                
            if data[0][0:4] != "pcds":
                fo.write(line)
                fo.close
                
                
                
                
    print TxtList
    print OutPath  
    #while len(TxtList)>0:
        

  
               
               
              

