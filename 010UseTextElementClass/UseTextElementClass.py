import pygame, sys
from pygame.locals import *

# includes simpleText class
from pygameElements import *

class MyPygame():
    def __init__(self, screenWidth=300, screenHeight=250, caption='Pygame Element Class Example', isFullscreen=False):
        #settings:
        self.renderObjects=[]
        self.isFullscreen=isFullscreen
        self.screenWidth=screenWidth
        self.screenHeight=screenHeight
        self.caption=caption
        self.screenColorBackground=pygame.Color('yellow') 
        
        # set up pygame
        pygame.init()
        
        # get display information from user machine
        pgdi=pygame.display.Info()

        # store desktop size
        self.desktopSize=(pgdi.current_w, pgdi.current_h)
        
        # create window
        self.setDisplay()
        
        # blitToSurface=None, name='', text='', colorText=(255,255,255), horizontalMiddlePromille=500, verticalMiddlePromille=500, sysFont=True, fontName='timesnewroman', fontSizePromille=100, isBold=False, isItalic=True, antiAlias=True, alphaValue=150, visible=True)
        self.renderObjects.append(simpleText(self.windowSurface, 'instructionText', 'Click To Count', pygame.Color('black'), 500, 200))
        self.renderObjects.append(simpleText(self.windowSurface, 'instructionText2', 'Right-Click To Count back', pygame.Color('red'), 500, 400, False, 'Ballpointprint.ttf', alphaValue=128))
        
        # toggle flag to signal a screen update is needed
        self.needScreenUpdate=True
        
        self.counter=0
        
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
        for item in self.renderObjects:
            if not item.name=='instructionText':
                item.updateOnScreen()

        # make sure instruction text is painted last, on top
        for item in self.renderObjects:
            if item.name=='instructionText':
                item.updateOnScreen()
        
        # draw the window onto the screen
        pygame.display.update()
        
        # reset flag
        self.needScreenUpdate=False
        
    def setDisplay(self):
    
        if self.isFullscreen:
            self.windowSurface = pygame.display.set_mode(self.desktopSize, pygame.FULLSCREEN ,0)
        else:
            self.windowSurface = pygame.display.set_mode((self.screenWidth, self.screenHeight), pygame.RESIZABLE ,0)
        pygame.display.set_caption(self.caption)
        
#        updateScreen(fontName, message, windowSurface)

    def toggleFullScreen(self):
        self.isFullscreen=not self.isFullscreen
        self.setDisplay()
        
    def getPromille(self, position):
        #converts positon on screen to a promillage
        if self.isFullscreen:
            return ( int((1.0/(self.desktopSize[0]/position[0]))*1000.0), int((1.0/(self.desktopSize[1]/position[1])*1000.0)))
        else:
            return ( int((1.0/(self.screenWidth/position[0]))*1000.0), int((1.0/(self.screenHeight/position[1])*1000.0)))
        
    def hideOldCounter(self):
        for item in self.renderObjects:
            if item.name[:7]=='itemNr:':  # we only want the items with the proper name, not the instructions
                count=int(item.name.split(':')[1]) # names are like itemNr:2 , we split it over the : and want the second part (0=first part). We then cast the string number to an int
                if self.counter-count>4: # if the name is more then 4 below the current number, set it to invisible
                    item.visible=False
                else:
                    item.visible=True # but otherwise, show it

    def handleResize(self, event):
        print(event)
        if self.screenWidth==event.w and self.screenHeight==event.h:
            pass # nothing changed
        else:
            if not self.isFullscreen: 
                self.screenWidth=event.w
                self.screenHeight=event.h
                self.setDisplay()	
        
        for item in self.renderObjects:
            item.resize(self.windowSurface)

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
                    
                    elif event.key== K_f: # f pressed: toggle fullscreen
                        self.toggleFullScreen()
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                
                #detect game events:
                elif event.type == pygame.MOUSEBUTTONUP: # react to the moment the mouse button is going up again
                    if event.button==1: # left click, put new text location to click position
                        self.counter=self.counter+1
                        self.hideOldCounter() # we only want to see the last 5 clicks and the instructions
                        widthPromille, heightPromille=self.getPromille(event.pos) # convert screen pos to promille pos
                        
                        self.renderObjects.append(simpleText(self.windowSurface, 'itemNr:'+repr(self.counter), repr(self.counter)+'!',pygame.Color('darkgreen') ,widthPromille, heightPromille))
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                    elif event.button==3: # right click
                        if len(self.renderObjects) >2: # we can remove all but the first two, since they are instructions
                            self.renderObjects.pop() # removes last added from list
                        self.counter=self.counter-1
                        if self.counter<0: # prevent counter from going below zero
                            self.counter=0
                        self.hideOldCounter() # we only want to see the last 5 clicks and the instructions
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                        
                elif event.type== VIDEORESIZE: # window resize detected
                    self.handleResize(event)
                    self.needScreenUpdate=True # toggle flag to signal a screen update is needed

if __name__=='__main__':
    mpg=MyPygame()
    