import pygame, sys
from pygame.locals import *

class MyPygame():
    def __init__(self, screenWidth=300, screenHeight=250, caption='Pygame Inside Class Example'):
        #settings:

        self.screenWidth=screenWidth
        self.screenHeight=screenHeight
        self.caption=caption
        self.message='Click to Move!'
        self.screenColorBackground=pygame.Color('blue') 
        self.textColorForground=pygame.Color('white') 
        self.textColorBackground=pygame.Color('blue') 
        self.fontSize=48
        self.isBold=False
        self.isItalic=True
        self.useAntiAlias=True
        #self.fontName=None # uses default system font
        self.fontName='timesnewroman' # other well known fonts are for example arial, helvetica. 
        
        # set up pygame
        pygame.init()
        
        # set up font
        self.basicFont = pygame.font.SysFont(self.fontName, self.fontSize, self.isBold, self.isItalic) 
        
        # create window
        self.setDisplay()
        
        # place text location to middle window
        self.newCenterX = self.windowSurface.get_rect().centerx
        self.newCenterY = self.windowSurface.get_rect().centery
        
        # toggle flag to signal a screen update is needed
        self.needScreenUpdate=True

        # start main loop
        self.MainLoop()
        
    def quitElegantly(self):
        # you could do things like saves here
        pygame.quit()
        sys.exit()
        
    def updateScreen(self):
        # draw the screenColorBackground onto the surface
        self.windowSurface.fill(self.screenColorBackground)
        
        #render all objects on screen
        self.renderObjects()
        
        # draw the window onto the screen
        pygame.display.update()
        
        # reset flag
        self.needScreenUpdate=False
        
    def renderObjects(self):
        # render the text
        self.textRender = self.basicFont.render(self.message, self.useAntiAlias, self.textColorForground, self.textColorBackground)

        # get rectangle the text was rendered in
        self.textRect=self.textRender.get_rect()

        # set  center of rectangle to center of windowsurface
        self.textRect.centerx = self.newCenterX # horizontal
        self.textRect.centery = self.newCenterY # vertical
        
        # draw the text onto the surface
        self.windowSurface.blit(self.textRender,self.textRect)
        
    def setDisplay(self):
        # set up the window
        self.windowSurface = pygame.display.set_mode((self.screenWidth, self.screenHeight))

        # set caption
        pygame.display.set_caption(self.caption)
        
    def MainLoop(self):
        
        # run the game loop
        while True:
        
            # check to see if we need a screen update. If so, update the screen. 
            if self.needScreenUpdate:
                self.updateScreen()
            
            # check for quit events
            for event in pygame.event.get():
                if event.type == QUIT: # like control-break in the console, or the cross in the top right corner of the window
                    self.quitElegantly()
                elif event.type== KEYDOWN:
                    mods=pygame.key.get_mods()
                    if event.key== K_ESCAPE: # also quit on escape
                        self.quitElegantly()
                    elif (mods & KMOD_LALT or mods & KMOD_RALT) and event.key==K_F4:  #also quit on alt-f4
                        self.quitElegantly()
                
                #detect game events:
                elif event.type == pygame.MOUSEBUTTONUP: # react to the moment the mouse button is going up again
                    if event.button==1: # left click, put new text location to click position
                        # print (event)
                        self.newCenterX=event.pos[0] # horizontal
                        self.newCenterY=event.pos[1] # vertical
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed

if __name__=='__main__':
    mpg=MyPygame()
    