# DCPtranscoder

Search for package<br>
check number of mxfs<br>
if 2, then just ffmpeg -i twice for audio and video <br>
if greater than two, concat the audio, concat the video, then join the two with ffmpeg -i video.mxf -i audio.mxf <br>
There's probably a way to concat and joining the audio and video at same time, but work on proof of concept for now <br>

-
