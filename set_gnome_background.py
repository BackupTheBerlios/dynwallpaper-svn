#!/bin/env python

# written by Martin Winkler (mw@agami.at)
# License: BSD

from datetime import datetime
import sys
try:
    import gconf
except ImportError:
    print 'Error: "gconf" module not installed.\nplease read the file "please_REALLY_readme.txt"!' 
    sys.exit(1)

# these are fixed points in time with the desired colors.
# all times in between will be calculated for a smooth transition
# Values are in the form  (HOUR, (RED,GREEN,BLUE))
# where HOUR= 0..24
# and each color= 0..255
# the tuple must be sorted ascending by hour
COLORS = ( ( 0, (  0,   0,   0))
         , ( 6, (124, 221, 237))
         , (12, ( 82, 157, 255))
         , (18, (207, 115,  33))
         , (24, (  0,   0,   0))
         )

def getColor(floattime):
    """returns a hex-formatted color string representing
    the rgb color for the specified time ( 0.0 <= value < 24.0).
    e.g. floattime=16.5 means 4:30pm and returns #af7d58"""
    for idx, c in enumerate(COLORS):
        if c[0] <= floattime:
            min = c
            max = COLORS[idx+1]
        else:
            break
    color = '#'
    timeframe = float(max[0] - min[0])
    upframe = floattime - min[0]
    for rgbpart in range(3):
        maxcol = max[1][rgbpart]
        mincol = min[1][rgbpart]
        col = (maxcol - mincol) / timeframe * upframe
        color += chr( int(col + mincol) ).encode('hex')
    return color

def checkParams():
    try:
        # do we have a command line parameter indicating a manual time?
        floattime = float(sys.argv[-1])
        if floattime >= 24 or floattime < 0:
            raise ValueError # fail silently and use current time
    except ValueError:
        # fallback to standard behaviour and use current time
        now = datetime.time(datetime.now())
        floattime = now.hour + now.minute/60.0 + now.second/3600.0
    return floattime

floattime = checkParams()
conf = gconf.client_get_default()
bgcolor = conf.get('/desktop/gnome/background/primary_color')
bgcolor.set_string(getColor(floattime))
conf.set('/desktop/gnome/background/primary_color',bgcolor)

