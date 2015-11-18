# DCPtranscoder

1.Search for package<br>
2.check number of mxfs<br>
3.if 2, then just ffmpeg -i twice for audio and video <br>
4.if greater than two, concat the audio, concat the video, then join the two with ffmpeg -i video.mxf -i audio.mxf <br>
5.There's probably a way to concat and joining the audio and video at same time, but work on proof of concept for now <br>

-
