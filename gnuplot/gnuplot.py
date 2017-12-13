import Gnuplot
import argparse
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


parser = argparse.ArgumentParser(description="Estimating image features using pre-trained deep learning models from the Caffe library.",
                                 epilog="NOTE: this was tested so far for bvlc_reference_caffenet (trained on ILSVRC12 classes)")
                                
parser.add_argument('-p', '--pdf', metavar='output.pdf', default='output.pdf', dest='output_pdf',
                    help='PDF file holding the visualization plots')

rgs = parser.parse_args()

print("Output plots will be written to: %s" % args.output_pdf)
pdf_pages = PdfPages(args.output_pdf)





from numpy import *

file=open('D00022_v4.data','r')

arr=[]

for i in file.readlines():

    temp=[]
    for j in i.strip().split('\t'):

        temp.append(float(j))

    arr.append(temp)

import random

import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d  import Axes3D

mpl.rcParams['font.size']=10

fig=plt.figure()

ax=fig.add_subplot(111,projection='3d')

xs=range(len(arr))

ys=range(len(arr[0]))

for z in range(len(arr)):
    xs=range(len(arr))
    ys=arr[z]

    color=plt.cm.Set2(random.choice(range(plt.cm.Set2.N)))

    ax.bar(xs,ys,zs=z,zdir='y',color=color,alpha=0.5)

    ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(xs))

    ax.yaxis.set_major_locator(mpl.ticker.FixedLocator(ys))

ax.set_xlabel('x')

ax.set_ylabel('y')

ax.set_zlabel('copies')

plt.show()