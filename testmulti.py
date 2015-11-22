import subprocess
import sys
import os

filename = sys.argv[1]
output = filename + '_concattt.mov'
doc = filename + '.txt'
wd = os.path.dirname(filename)
print wd
acodec_raw1 = subprocess.check_output(['xml', 'sel', '-N', 'x=http://www.digicine.com/PROTO-ASDCP-PKL-20040311#', '-t', '-m', "//x:Asset[contains(x:Type,'Picture')]", '-v', 'x:OriginalFileName', '-n', filename ]).splitlines() 
dir_append = wd + '/'
concat_string = 'file \'' 
concat_append = '\''
acodec_raw = [dir_append + x for x in acodec_raw1]
# http://stackoverflow.com/a/2050721/2188572
newlist = [concat_string + x for x in acodec_raw]
finalpic = [x + concat_append for x in newlist]
print finalpic
#http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
file = open(doc, "w")
for item in finalpic:
  file.write("%s\n" % item)
file.close()  


docaudio = filename + 'audio.txt'
outputaudio = filename + '.wav'
wd = os.path.dirname(filename)
print wd
audio = subprocess.check_output(['xml', 'sel', '-N', 'x=http://www.digicine.com/PROTO-ASDCP-PKL-20040311#', '-t', '-m', "//x:Asset[contains(x:Type,'Sound')]", '-v', 'x:OriginalFileName', '-n', filename ]).splitlines() 
dir_append = wd + '/'
concat_string = 'file \'' 
concat_append = '\''
audio_raw = [dir_append + x for x in audio]
# http://stackoverflow.com/a/2050721/2188572
newaudio = [concat_string + x for x in audio_raw]
finalaudio = [x + concat_append for x in newaudio]
print finalaudio
#http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
file = open(docaudio, "w")
for item in finalaudio:
  file.write("%s\n" % item)
file.close()  
outputmuxed = filename + '_muxed.mov'

subprocess.call(['ffmpeg',
                         '-f', 'concat',
                         '-i', docaudio,
                         '-c:a', 'copy',
                         outputaudio])
subprocess.call(['ffmpeg',
                         '-f', 'concat',
                         '-i', doc,
                         '-c:v', 'prores',
                         output])
                         
subprocess.call(['ffmpeg',
                         '-i', output,
                         '-i', outputaudio,
                         '-c', 'copy',
                         outputmuxed])
                         
