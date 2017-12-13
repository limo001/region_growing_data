#!/usr/bin/env python
from time import time
import argparse
import os
from PIL import Image
from array import *
from random import shuffle
import glob





# TODO: USAGE DISPLAYED IF CALLED WITH -h OPTION (OR WITHOUT PARAMETERS)
# TODO:  python caffe_labels.py /home/li_mo/3rd-party/caffe/PCDs-train .txt  caffe.labels

parser = argparse.ArgumentParser(description="Estimating image features using pre-trained deep learning models from the Caffe library.",
                                 epilog="NOTE: this was tested so far for bvlc_reference_caffenet (trained on ILSVRC12 classes)")
parser.add_argument('input_directory',
                   help='input directory containig the image files')
                      
parser.add_argument('input_extension',
                   help='extension (or other ending / full name) for input image files')                       

                   
                   
args = parser.parse_args()


###############################################################################
# save bild labels
###############################################################################


#input_image = ''.join([args.input_directory, "/", args.input_extension])
os.chdir(args.input_directory)
#counter=0
#t_start = time()
 # TODO: wildcard as part of extension => rename to filter/regex/???
  






# Load from and save to
Name = [args.input_directory]
print("\nInput Names: %s" % Name)
#for name in Names:	
      
FileList = []
#for dirname in os.listdir(Name):
for filename in glob.glob(''.join(["*", args.input_extension])) :    
   # path = os.path.join(Name,dirname)
    print filename
    #  for filename in os.listdir(path):
            #if filename.endswith(".txt"):
    print ("filename: ",filename)
    FileList.append(os.path.join(args.input_directory,filename))
                
print FileList  
for filename in FileList:
    file_name = filename.split('/')[2]  
    print "file_name", file_name 
    print filename
    outpath = os.path.join("gnuplot/",file_name[0:9]+".data")
    print outpath

   # fi = open(outpath, 'a+')





fo = open("D00001_v1_out.txt", "r")
print fo
for line in fo.readlines():
    if line != '\n' :
        data = line.split()
        name = data[0]
        print name
            # num = data[1]
            #print name
            #data = inhalt[1]
          #  if (name == "cluster_tolerance_:" ):
          #      num = data[1]
                # fi.write(''.join([num, "\t"] )) 
                    
          #  if (name == "eps_angle_threshold_:" ):
          #      num = data[1]
             #   fi.write(''.join([num, "\t"] ))
                    
          #  if (name == "clusters_size:" ):
          #      num = data[1]
              #  fi.write(''.join([num, "\n"] ))
                                        
                    #print name, num
            #if  line in ['\n' ,'\r\n']:
            #    print "leer", line 
   # fi.close
fo.close
     
                
               
               
              

