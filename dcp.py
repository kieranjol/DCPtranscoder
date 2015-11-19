import subprocess
import sys
import os
from Tkinter import Tk
import tkFileDialog
root = Tk()

my_match = []
# Create file-open dialog.
root.update()

video_dir = tkFileDialog.askdirectory(parent=root)
os.chdir(video_dir)
output = tkFileDialog.asksaveasfilename(parent=root)+ '.mov'

mxfs = filter(lambda x: x.endswith('.mxf'), os.listdir(video_dir))
#output is currently within the DCP. This is bad, will add option for output dir later.

subprocess.call(['ffmpeg',
                       '-i', mxfs[0],
                       '-i', mxfs[1],
                       '-c:v', 'libx264',
                       '-crf', '22',
                       '-pix_fmt', 'yuv420p',
                       '-c:a', 'copy',
                       output])
