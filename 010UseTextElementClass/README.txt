These two examples use the simpleText class imported from pygameElements.py

The simpleText element has the following default parameters:

(blitToSurface=None, name='', text='', colorText=(255,255,255), horizontalMiddlePromille=500, verticalMiddlePromille=500, sysFont=True, fontName='timesnewroman', fontSizePromille=100, isBold=False, isItalic=True, antiAlias=True, alphaValue=255, visible=True)

Note that only system fonts can have their bold and italic set
also note that to use alphaValue, you cant set antiAlias to False (or it wont work)

the Promille values are from 0 to 1000, and will scale to whatever size the screen is. 

You can toggle fullscreen with F
and change size of the screen
the elements will scale along

in ClickCounter you can click on places on the window, and the next count number will appear. It will only show the last 5 counted numbers: the rest will be invisible. 
If you right click, you will count back: removing the latest number, and showing the five before them in stead.

In ShowSystemFonts we iterate over all the fonts found in the system, and display them ten per page
Click to go to the next page, rightclick to go to the previous page.
I will toggle italic
B will toggle bold
A will toggle anti-alias (which can take a while)




