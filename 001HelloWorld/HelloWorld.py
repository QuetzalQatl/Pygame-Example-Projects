import pygame, sys
from pygame.locals import *

#settings:

screenWidth=300
screenHeight=250
caption='PyGame Hello World Example'
message='Hello World!'
screenColorBackground=pygame.Color('blue') 
textColorForground=pygame.Color('white') 
textColorBackground=pygame.Color('blue') 
fontSize=48
isBold=False
isItalic=True
useAntiAlias=True

#fontName=None # uses default system font
fontName='timesnewroman' # other well known fonts are for example arial, helvetica. 

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((screenWidth, screenHeight))

# set caption
pygame.display.set_caption(caption)

# set up font
basicFont = pygame.font.SysFont(fontName, fontSize, isBold, isItalic) 

# render the text
textRender = basicFont.render(message, useAntiAlias, textColorForground, textColorBackground)

# get rectangle the text was rendered in
textRect=textRender.get_rect()

# set  center of rectangle to center of windowsurface
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the screenColorBackground onto the surface
windowSurface.fill(screenColorBackground)

# draw the text onto the surface
windowSurface.blit(textRender,textRect)

# draw the window onto the screen
pygame.display.update()

def quitElegantly():
	# you could do things like saves here
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
