UltimakerUtils
==============

Miscellaneous utilities for use with Ultimaker 3D printers.  (I am not
affiliated with Ultimaker, other than as a happy customer.)


Leveling Rings
--------------

Discussion, tips, and background at: http://umforum.ultimaker.com/index.php?/topic/5951-um2-calibration-utility-leveling-ringsgcode/

This little snippet of g-code helps greatly when checking bed
leveling, and gives you a chance to twist the thumbscrews in real time
for fine-tuning.  I wrote the UM2 version of this while
troubleshooting a Z homing bug in Marlin 14.03, and it's become my
standard quick "warm-up" print at the beginning of each session.
The UM1 version was promptly and humorously contributed by a gracious
anonymous user -- see our discussion at the above URL.

What this thing does is lay down a concentric set of rings, 150 mm
diameter, in a single .1 mm layer.  When your printer is calibrated
correctly, you'll see these rings' edges touching, or nearly so.
Glass too high means you mash the glass into the nozzle and get little
or no plastic, glass too low means you get dribbles.

You'll quickly get good at twiddling the bed height thumbscrews while
it's slowly circling; your goal is to make the rings nice and even all
the way around; see the example photos in this repository or in the
discussion thread.


Steve Traugott
https://github.com/stevegt

