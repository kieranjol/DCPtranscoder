# DCPtranscoder
Functional proof of concept, with file open and file save as dialogs! <br>
Tested in Ubuntu and OSX. Should work in windows and if not, why not!? aka I'll test it later. <br>

Future plan: - include the following but allow selection of output codecs.<br>

1. Search for package<br>
2. Check number of mxfs<br>
3. If 2, then just ffmpeg -i video.mxf -i audio.mxf output.mov <br>
4. If greater than two, concat the audio, concat the video, then join the two with ffmpeg -i video.mxf -i audio.mxf <br>
5. There's probably a way to concat and joining the audio and video at same time, but work on proof of concept for now <br>

-
