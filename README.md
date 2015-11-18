# DCPtranscoder
Functional, but wonky proof of concept. Output of quicktime is currently IN the DCP, which is not cool! Will fix later when I've time. <br>

1.Search for package<br>
2.check number of mxfs<br>
3.if 2, then just ffmpeg -i video.mxf -i audio.mxf output.mov <br>
4.if greater than two, concat the audio, concat the video, then join the two with ffmpeg -i video.mxf -i audio.mxf <br>
5.There's probably a way to concat and joining the audio and video at same time, but work on proof of concept for now <br>

-
