import pygame, sys
from pygame.locals import *

#settings:

screenWidth=500
screenHeight=400

caption='PyGame Detect Screen Size Changes Example'
screenColorBackground=pygame.Color('blue') 
textColorForground=pygame.Color('white') 
textColorBackground=pygame.Color('blue') 
fontSize=24
isBold=False
isItalic=True
useAntiAlias=True
isFullscreen=False

#fontName=None # uses default system font
fontName='timesnewroman' # other well known fonts are for example arial, helvetica. 

# set up pygame
pygame.init()

# get display information from user machine
pgdi=pygame.display.Info()

# store desktop size
desktopSize=(pgdi.current_w, pgdi.current_h)

def updateScreen(fontName, text, windowSurface):
	# draw the screenColorBackground onto the surface
	windowSurface.fill(screenColorBackground)
	
	# set up font
	basicFont = pygame.font.SysFont(fontName, fontSize, isBold, isItalic) 

	# render the text
	textRender = basicFont.render(text, useAntiAlias, textColorForground, textColorBackground)

	# get rectangle the text was rendered in
	textRect=textRender.get_rect()

	# set  center of rectangle to center of windowsurface
	textRect.centerx = windowSurface.get_rect().centerx
	textRect.centery = windowSurface.get_rect().centery

	# draw the text onto the surface
	windowSurface.blit(textRender,textRect)

	# draw the surface onto the screen
	pygame.display.update()

def setDisplay():
	if isFullscreen:
		windowSurface = pygame.display.set_mode(desktopSize, pygame.FULLSCREEN ,0)
		message=f'Current Size:  w { pgdi.current_w} x h { pgdi.current_h}'
	else:
		windowSurface = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE ,0)
		message=f'Current Size:  w { screenWidth} x h { screenHeight}'
	pygame.display.set_caption(caption)
	updateScreen(fontName, message, windowSurface)
	
	return windowSurface
	
def toggleFullScreen():
	global isFullscreen
	isFullscreen=not isFullscreen
	windowSurface=setDisplay()

def handleResize(event):
	global screenWidth, screenHeight
	if screenWidth==event.w and screenHeight==event.h:
		pass # nothing changed
	else:
		if not isFullscreen: 
			screenWidth=event.w
			screenHeight=event.h
			windowSurface=setDisplay()	
		
def quitElegantly():
	pygame.quit()
	sys.exit()		

# create window
windowSurface=setDisplay()

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
			
			elif event.key== K_f: # f pressed: toggle fullscreen
				toggleFullScreen()
				
		elif event.type== VIDEORESIZE: # window resize detected
			handleResize(event)
