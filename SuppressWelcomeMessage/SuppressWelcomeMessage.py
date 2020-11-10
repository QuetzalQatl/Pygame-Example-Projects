import os

#placing this environment variable before importing pygame will suppress the welcome message, if you really need to 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, sys
from pygame.locals import *

#settings:

screenWidth=500
screenHeight=400
caption='PyGame Suppress Welcome Message Example'
screenColorBackground=pygame.Color('blue') 

# set up pygame
pygame.init()

# set up the window surface
windowSurface = pygame.display.set_mode((screenWidth, screenHeight))

# set caption
pygame.display.set_caption(caption)

# draw the screenColorBackground onto the surface
windowSurface.fill(screenColorBackground)

# draw surface onto the window
pygame.display.update()

def quitElegantly():
	pygame.quit()
	sys.exit()

# run the game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT: # like control-break in the console, or the cross in the top right corner of the window
			quitElegantly()
		elif event.type== KEYDOWN:
			mods=pygame.key.get_mods()
			if event.key== K_ESCAPE: # also quit on escape
				quitElegantly()
			elif (mods & KMOD_LALT or mods & KMOD_RALT) and event.key==K_F4:  #also quit on alt-f4
				quitElegantly()
