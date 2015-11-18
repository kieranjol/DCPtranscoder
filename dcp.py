
import subprocess
import sys
import filecmp
from glob import glob
import os
from Tkinter import *
import tkFileDialog
root = Tk()
import fnmatch


my_match = []
# Create file-open dialog.
root.update()
# Directory with files that we want to transcode losslessly and generate metadata for
video_dir = tkFileDialog.askdirectory(parent=root)
os.chdir(video_dir)
#csv       = tkFileDialog.asksaveasfile(parent=root, defaultextension='.csv') 
for root, dirs, files in os.walk(video_dir):
   
       
       mxfs = filter(lambda x: x.endswith('.mxf'), os.listdir(video_dir))
       output = mxfs[0] + '.mov'
       subprocess.call(['ffmpeg',
                       '-i', mxfs[0],
                       '-i', mxfs[1],
                       '-c:v', 'libx264',
                       '-crf', '22',
                       '-pix_fmt', 'yuv420p',
                       output])
       
