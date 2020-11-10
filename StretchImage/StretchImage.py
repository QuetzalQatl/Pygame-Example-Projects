import pygame, sys
from pygame.locals import *

#settings:

screenWidth=500
screenHeight=400
caption='PyGame Stretch Image Example'
screenColorBackground=pygame.Color('blue') 
imageFile='someImage.png'

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((screenWidth, screenHeight))

# set caption
pygame.display.set_caption(caption)

# draw the screenColorBackground onto the surface
windowSurface.fill(screenColorBackground)

# load image from file
loadedImage = pygame.image.load(imageFile)

# stretch image to fit screen
loadedImage=pygame.transform.scale(loadedImage, (screenWidth, screenHeight))

# blit image on screen
windowSurface.blit(loadedImage,(0,0)) # we use coordinates 0,0 (top left) because the image is now as large as the screen

# draw the screen onto window
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
