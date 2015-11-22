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

subprocess.call(['ffmpeg',
                         '-f', 'concat',
                         '-i', doc,
                         '-c:v', 'prores',
                         output])
