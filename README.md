# DCPtranscoder
Transcode those DCPs to a single file!<br>
Instructions:<br>
single_reel.py:         Select a directory and ffmpeg will combine your audio and video to a prores.mov<br>
Interop_multireeler.py: Select the PKL.XML to transcode your audio and video mxfs to a prores.mov.<br>

EEk! New files are currently saved within the package for multireel.py. Will fix tomorrow! <br>

Single_reel.py works with all SMPTE/INTEROP DCPS that I have tested, if audio is present. <br>
Interop_multireeler.py currently only works with Interop DCPS with audio<br>

Functional proof of concept, with file open and file save as dialogs! <br>
Tested in Ubuntu and OSX. Should work in windows and if not, why not!? aka I'll test it later. <br>

Future plan: - include the following but allow selection of output codecs.<br>
SMPTE support for multiple reels.
