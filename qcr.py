#!python3
''' AUTHORS: Stephen Antymis
VERSION: 0.1
DESCRIPTION: Quick Chaos Recipe is designed as a tool for Path of Exile to quickly find chaos recipe items in a specific stash tab and click them in to your inventory. Due to macro
				limitations of one action per click, this tool will have to cycle equipment slots per button press in accordance to PoE's ToS 

INSTRUCTIONS: Run this file in cmd prompt with "Py qcr.py"

RESOURCES: https://www.reddit.com/r/pathofexiledev/comments/6mwll6/possible_to_get_public_stash_tabs_of_only_a/?st=j58t1ghq&sh=11a368c1

'''

import os
import win32api, win32con
import time

#Globals
#----------------------------------
#These are the coordinates of the top left and bottom right cells of a QUAD tab
topLeftX = 30
topLeftY = 175
bottomRightX = 635
bottomRightY = 780

StashDim = 24 #QUAD tabs are 24x24, NORMAL tabs are 12x12
#----------------------------------


def mousePos(coord):
	win32api.SetCursorPos((x_pad + coord[0], y_pad + coord[1]))

def get_coords():
	x,y = win32api.GetCursorPos()
	#x = x - x_pad
	#y = y - y_pad
	print x,y

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print "Left Click." #Optional, strictly for debugging

def main():
	print 'Hello!'
	while True:
		get_coords()
		time.sleep(1)

if __name__ == '__main__':
	main()