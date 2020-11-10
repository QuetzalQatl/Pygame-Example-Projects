import pygame, sys
from pygame.locals import *

#settings:

screenWidth=500
screenHeight=400
caption='PyGame Transparent Text Example'
screenColorBackground=pygame.Color('green') 
textColorForground=pygame.Color('black') 
fontSize=24
isBold=False
isItalic=True
useAntiAlias=True # Must be true to be able to use alpha value!
alphaValue=128 # from 0 (totally invisible) to 255 (totally visible)
alphaDefault=128

#fontName=None # uses default system font
fontName='timesnewroman' # other well known fonts are for example arial, helvetica. 

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((screenWidth, screenHeight))

# set caption
pygame.display.set_caption(caption)
	
def renderText(text, alphaValue, fontName):
    # set up font
    basicFont = pygame.font.SysFont(fontName, fontSize, isBold, isItalic) 

    # set up the text. Note: you need to set useAntiAlias to True, or it wont work !
    textRender = basicFont.render(text, useAntiAlias, textColorForground)

    # create alpha channel mask surface with size of textRender
    alphaImg = pygame.Surface(textRender.get_size(), pygame.SRCALPHA)

    # use the entire surface as mask 
    alphaImg.fill((255, 255, 255, alphaValue))

    # blend alpha mask with text
    textRender.blit(alphaImg, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    # get rectangle the text was rendered in
    textRect=textRender.get_rect()

    # set  center of rectangle to center of windowsurface
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
	
    # draw the text onto the surface
    windowSurface.blit(textRender,textRect)
	
def quitElegantly():
    # you could do things like saves here
    pygame.quit()
    sys.exit()

def updateScreen():
    # fill background
    windowSurface.fill(screenColorBackground)
	
    # render objects onto screen:
    renderText(f'This should have a transparency of {alphaValue}/255', alphaValue, fontName)
	
    # draw the window onto the screen
    pygame.display.update()

# render screen at begin
updateScreen()

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
		
        #detect game events:
        elif event.type == pygame.MOUSEBUTTONUP: # react to the moment the mouse button is going up again
            if event.button==1: # left click
                alphaValue=alphaValue+10 # increase alpha value (make more visible) by a lot
            elif event.button==2: # scroll wheel click
                alphaValue=alphaDefault # set alpha value to default 128
            elif event.button==3: # right click
                alphaValue=alphaValue-10  # decrease alpha value (make less visible) by a lot
            elif event.button==4: # scroll up
                alphaValue=alphaValue+1 #  increase alpha value (make more visible) by a little
            elif event.button==5: # scroll down
                alphaValue=alphaValue-1 # decrease alpha value (make less visible) by a little
			
            # keep alphaValue between 0-255
            while alphaValue>255: 
                alphaValue=alphaValue-255
            while alphaValue<0:
                alphaValue=alphaValue+255
			
            # since we have a new alphaValue, we need to update the screen
            updateScreen()
