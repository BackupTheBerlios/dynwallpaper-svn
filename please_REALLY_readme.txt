set_gnome_background.py
=======================

Written by Martin Winkler martin.j.winkler@gmx.at
License: BSD

This script changes the primary background color of your Gnome desktop
according to the current time of day.


REQUIREMENTS:
=============
this script requires python-gconf to be installed.
Your Linux distribution should already have a package. E.g. in Fedora
use "yum install python-gconf" for installation.

Python-gconf is also available for (at least) the distributions Debian
and Ubuntu. (look for someting like "pygtk", "python gconf", 
"python bindings for gconf" or similar)

If everything fails, you can download pyGTK from www.pyGTK.org


USAGE:
======
For interesting results use 
 * a semi-transparent desktop background image, like one of the pictures
   that came with this script.
 * and a gradient for desktop colors

Example:
* Open "Desktop Background Preferences" by right-clicking on your desktop
* drag the picture "gasometer.png" from a nautilus window onto the list
  of desktop wallpapers.
* choose Style: scaled
* choose Desktop Colors: Vertical Gradient
* select white as the secondary color (the right color button)
* run "set_gnome_background" and enjoy!

If you want to update the color during the day, make sure to edit your
crontab file:

in a Terminal window start
$ crontab -e

and add the following line:
*/10 * * * * /PATH/TO/THE/SCRIPT/set_gnome_background.py

save the crontab with ":wq" and your desktop background will update
every ten minutes. with a slightly different color.

For testing purposes you can also start the script with a numeric parameter:
$ set_gnome_background 7.5  # set color for 7.30 am
$ set_gnome_background 18   # set color for 6.00 pm

ADJUSTMENTS
===========
You can edit the "COLORS" list in the file set_gnome_background.py
as described in the script for different color effects.


GIMP TIPPS
==========

I have added a larger version of the "business" image, so feel free to
use whichever part of the picture using the "Canvas size" and "Scale Image"
commands of the gimp :)

Wonder how you can add transparency to your own pictures?
There are quite a few websites with good gimp tipps:

http://glscene.schtuff.com/tips_alphachannel
http://members.home.nl/m.weisbeek/gimp/

or let your favourite search engine look for "alpha channel",
"transparency" or similar search terms.


THANKS
======
Many thanks to Miroslav Bakos for his great pictures. Have a look at
http://www.mirez.sk - there are plenty more fantastic photos made by him!

