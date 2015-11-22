import subprocess
import sys
import os
from Tkinter import Tk
import tkFileDialog
root = Tk()

# Create file-open dialog.
root.update()

# File open dialog will appear. Whatever directory you choose will be stored as video_dir
filename = tkFileDialog.askopenfilename(parent=root)

# Set variables for various filenames.
output = filename + '_concattt.mov'
video_concat_textfile = filename + '.txt'
wd = os.path.dirname(filename)
audio_concat_textfile = filename + 'audio.txt'
outputaudio = filename + '.wav'
outputmuxed = filename + '_muxed.mov'

# Search through XML for filenames containing picture.
def get_files(variable,typee):
    variable = subprocess.check_output(['xml', 'sel', 
                                             '-N', 'x=http://www.digicine.com/PROTO-ASDCP-PKL-20040311#',
                                             '-t', '-m', typee,
                                             '-v', 'x:OriginalFileName',
                                             '-n', filename ]).splitlines() 
    return variable
picture_files = get_files('picture_files',"//x:Asset[contains(x:Type,'Picture')]")
# Transformations to picture_files in order to fit the ffmpeg concat text standard.
dir_append = wd + '/'
concat_string = 'file \'' 
concat_append = '\''
picture_files_fix1 = [dir_append + x for x in picture_files]
# http://stackoverflow.com/a/2050721/2188572
picture_files_fix2 = [concat_string + x for x in picture_files_fix1]
finalpic = [x + concat_append for x in picture_files_fix2]

# Write the list of filenames containing picture to a textfile. 
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
file = open(video_concat_textfile, "w")
for item in finalpic:
  file.write("%s\n" % item)
file.close()  # ffmpeg can't access the textfile until it's closed.

# Search through XML for filenames containing audio.
audio_files = get_files('audio_files',"//x:Asset[contains(x:Type,'Sound')]")
# Transformations to picture_files in order to fit the ffmpeg concat text standard.
dir_append = wd + '/'
concat_string = 'file \'' 
concat_append = '\''
audio_raw = [dir_append + x for x in audio_files]
# http://stackoverflow.com/a/2050721/2188572
newaudio = [concat_string + x for x in audio_raw]
finalaudio = [x + concat_append for x in newaudio]

# Write the list of filenames containing picture to a textfile. 
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
file = open(audio_concat_textfile, "w")
for item in finalaudio:
  file.write("%s\n" % item)
file.close()  

# Call ffmpeg to join all audio files into one WAV file
subprocess.call(['ffmpeg',
                         '-f', 'concat',
                         '-i', audio_concat_textfile,
                         '-c:a', 'copy',
                         outputaudio])
                         
# Call ffmpeg to join all video files into one prores.mov
subprocess.call(['ffmpeg',
                         '-f', 'concat',
                         '-i', video_concat_textfile,
                         '-c:v', 'prores',
                         output])

# Call ffmpeg to create one final muxed audiovisual asset in a .mov wrapper.
subprocess.call(['ffmpeg',
                         '-i', output,
                         '-i', outputaudio,
                         '-c', 'copy',
                         outputmuxed])
                         
