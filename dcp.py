import subprocess
import sys
import os
from Tkinter import Tk
import tkFileDialog
root = Tk()

# Create file-open dialog.
root.update()

# File open dialog will appear. Whatever directory you choose will be stored as video_dir
video_dir = tkFileDialog.askdirectory(parent=root)

# Change directory to video_dir. This is handy cos os.listdir just shows filenames, not path.
os.chdir(video_dir)

# File save as dialog will appear. Whatever filename you enter will be stored as output. .mov will be added.
output = tkFileDialog.asksaveasfilename(parent=root)+ '.mov'

# This creates a list of the filenames.
mxfs = filter(lambda x: x.endswith('.mxf'), os.listdir(video_dir))

# Call ffmpeg to combine audio and video into a h264.mov.
subprocess.call(['ffmpeg',
                       '-i', mxfs[0], # Pick first filename in the mxfs list
                       '-i', mxfs[1], # Pick second filename in the mxfs list
                       '-c:v', 'libx264',
                       '-crf', '22',
                       '-pix_fmt', 'yuv420p',
                       '-c:a', 'copy', # Basic aac encoder was being all wonky with 6 channel input.
                       output])
