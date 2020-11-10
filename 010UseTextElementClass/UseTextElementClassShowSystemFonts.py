import pygame, sys
from pygame.locals import *

# includes simpleText class
from pygameElements import *

class MyPygame():
    def __init__(self, screenWidth=300, screenHeight=250, caption='Pygame Show System Fonts Example, click for next page, toggle italic bold antialias with i, b and a', isFullscreen=False):
        #settings:
        self.renderObjects=[]
        self.isFullscreen=isFullscreen
        self.screenWidth=screenWidth
        self.screenHeight=screenHeight
        self.caption=caption
        self.screenColorBackground=pygame.Color('yellow') 
        self.currentPage=0
        # set up pygame
        pygame.init()
        self.italic=True
        self.bold=False
        self.antiAlias=True
        
        # get display information from user machine
        pgdi=pygame.display.Info()

        # store desktop size
        self.desktopSize=(pgdi.current_w, pgdi.current_h)
        
        # create window
        self.setDisplay()
        
        self.systemFonts=sorted(pygame.font.get_fonts())
        count=0
        page=0
        isBlack=True
        for f in self.systemFonts:
            #print(f)
            if isBlack: 
                color=pygame.Color('black')
            else:
                color=pygame.Color('red')
            isBlack=not isBlack
                
            self.renderObjects.append(simpleText(self.windowSurface, 'page:'+repr(page), f, color, 500, count*100+25, True, f, fontSizePromille=45))
            self.renderObjects.append(simpleText(self.windowSurface, 'page:'+repr(page), 'The quick brown fox jumps over the lazy dog?0123456789!', color, 500, count*100+75, True, f, fontSizePromille=45))
            count=count+1
            if count>9:
                count=0
                page=page+1
        self.maxPage=page
        
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
        
        print(f'showing page {self.currentPage}')
        #render all objects on screen
        for item in self.renderObjects:
            if item.name[:5]=='page:':
                pageNr=int(item.name.split(':')[1])
                if pageNr==self.currentPage:
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
        
    def toggleItalic(self):
        print('toggling Italic')
        self.italic=not self.italic
        for item in self.renderObjects:
            item.isItalic=self.italic
            item.createFont()
            item.renderText(item.text)
    
    def toggleBold(self):
        print('toggling Bold')
        self.bold=not self.bold
        for item in self.renderObjects:
            item.isBold=self.bold
            item.createFont()
            item.renderText(item.text)
    
    def toggleAntiAlias(self):
        print('toggling anti-alias (can take a while)')
        self.antiAlias=not self.antiAlias
        for item in self.renderObjects:
            item.antiAlias=self.antiAlias
            item.createFont()
            item.renderText(item.text)    

    def handleResize(self, event):
        #print(event)
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
                    elif event.key== K_i: # f pressed: toggle italic
                        self.toggleItalic()
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                    elif event.key== K_b: # f pressed: toggle bold
                        self.toggleBold()
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                    elif event.key== K_a: # f pressed: toggle anti alias
                        self.toggleAntiAlias()
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                
                #detect game events:
                elif event.type == pygame.MOUSEBUTTONUP: # react to the moment the mouse button is going up again
                    if event.button==1: # left click, put new text location to click position
                        self.currentPage=self.currentPage+1
                        if self.currentPage==self.maxPage:
                            self.currentPage=0
                            
                        
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                    elif event.button==3: # right click
                        self.currentPage=self.currentPage-1
                        if self.currentPage==-1:
                            self.currentPage=self.maxPage-1
                        
                        self.needScreenUpdate=True # toggle flag to signal a screen update is needed
                        
                elif event.type== VIDEORESIZE: # window resize detected
                    self.handleResize(event)
                    self.needScreenUpdate=True # toggle flag to signal a screen update is needed

if __name__=='__main__':
    mpg=MyPygame()
    