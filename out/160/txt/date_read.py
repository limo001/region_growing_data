import os
from PIL import Image
from array import *
from random import shuffle
import glob
import argparse





# Load from and save to
Names = [['./data_1'], ['./data_2']]
0.07

for name in Names:	
    data_image = array('B')
    
    FileList = []
    for dirname in os.listdir(name[0])[0:]:
        path = os.path.join(name[0],dirname)
        print dirname
        for filename in os.listdir(path):
            if filename.endswith(".txt"):
                print ("filename: ",filename)
                FileList.append(os.path.join(name[0],dirname,filename))
                
   # print FileList  
    for filename in FileList:
        file_name = filename.split('/')[3]  
        print "file_name", file_name 
        #with open(file_name) as f:
        #    content = f.readlines()
        outpath = os.path.join("gnuplot/",file_name[0:9]+".data")
        print outpath
        fi = open(outpath, 'a+')
        fo = open(filename, "r")
        #print fo.read()
        for line in fo.readlines():
            if line != '\n':
                #print line 
                data = line.split()
                name = data[0]
                #print name
               # num = data[1]
                #print name
            #data = inhalt[1]
                if (name == "cluster_tolerance_:" ):
                    num = data[1]
                    fi.write(''.join([num, "\t"] ))
                    print num
                   
                    
                if (name == "eps_angle_threshold_:" ):
                    num = data[1]
                    fi.write(''.join([num, "\t"] ))
                    
                if (name == "clusters_size:" ):
                    num = data[1]
                    fi.write(''.join([num, "\n"] ) ) 
                    
                
                    
                    
                    #print name, num
            #if  line in ['\n' ,'\r\n']:
            #    print "leer", line 
        fi.close
        fo.close
     
                
               
               
              

