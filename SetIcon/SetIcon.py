import pygame, sys
from pygame.locals import *

#NOTE: set 
#python pyinstaller.py --icon=icon.png
#in the packager like pyinstaller for proper icon in taskbar, which shows a python icon when run with python

#settings:

screenWidth=350
screenHeight=40
caption='PyGame Set Icon Example'
screenColorBackground=pygame.Color('green') 
iconFile='icon.png' # you can use a png with alpha channel. Try to size them down to multiples of 8 like 32x32 or 64x64 to prevent stretching errors

def quitElegantly():
	pygame.quit()
	sys.exit()

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((screenWidth, screenHeight))

# place caption
pygame.display.set_caption(caption)

# load iconFile
icon=pygame.image.load(iconFile)

# set icon
pygame.display.set_icon(icon)

# fill background
windowSurface.fill(screenColorBackground)

# show screen
pygame.display.update()

# run the game loop
while True:	
	for event in pygame.event.get(): 
		#detect exits:	
		if event.type == QUIT: # like control-break in the console, or the cross in the top right corner of the window
			quitElegantly()
		elif event.type== KEYDOWN:
			mods=pygame.key.get_mods()
			if event.key== K_ESCAPE: # also quit on escape
				quitElegantly()
			elif (mods & KMOD_LALT or mods & KMOD_RALT) and event.key==K_F4:  #also quit on alt-f4
				quitElegantly()
		