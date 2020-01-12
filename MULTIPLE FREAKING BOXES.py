"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (72,209,204)
REDGREEN = (255,255,0)
REDBLUE = (255,0,255)
GREENBLUE = (0,255,255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Creates attributes of a bouncer
class Bouncer():
    x=0
    y=0
    changex=0
    changey=0
    color = [0,0,0]
    size = 50
    #automatically runs when a bouncer is created
    def __init__(self):
        self.x=random.randrange(0,649)
        self.y=random.randrange(0,449)
        self.changex=random.choice(changes)
        self.changey=random.choice(changes)
        self.color=[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)]
        self.size=random.randrange(25,50)
                
   
       

        

    #draws the bouncer with its new attributes
    
class Rect(Bouncer):
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, [self.x,self.y,self.size,self.size])
    #moves the bouncer and bounces it off sides
    def move(self):
        if self.x > 699-self.size or self.x <0:
            self.changex *= -1
        if self.y > 499-self.size or self.y <0:
            self.changey *= -1
        self.x += self.changex
        self.y += self.changey

        if self.x+self.size > xpos-coll and self.x < xpos and self.y < ypos+coll and self.y+self.size > ypos-coll and self.changex>0:
            self.changex *= -1
            self.color=BLUE
        if self.x > xpos and self.x < xpos+coll and self.y < ypos+coll and self.y+self.size > ypos-coll and self.changex<0:
            self.changex *= -1
            self.color=BLUE
        if self.y < ypos+coll and self.y > ypos and self.x < xpos+coll and self.x+self.size > xpos-coll and self.changey<0:
            self.changey *= -1
            self.color=BLUE
        if self.y+self.size> ypos-coll and self.y+self.size<ypos and self.x < xpos+coll and self.x+self.size > xpos-coll and self.changey>0:
            self.changey *= -1
            self.color=BLUE

class Circ(Bouncer):
    def draw(self,screen):
        pygame.draw.ellipse(screen, self.color, [self.x,self.y,self.size,self.size])
    def move(self):
        if self.x > 699-self.size or self.x <0:
            self.changex *= -1
        if self.y > 499-self.size or self.y <0:
            self.changey *= -1
        self.x += self.changex
        self.y += self.changey
        
        

            
changes = []
#speed range for each bouncer
for i in range(5):
    if i != 0:
        changes.append(i)
        changes.append(-i)
rectangles = []
circles = []


#number of boxes
for i in range(25):
    rectangles.append(Rect())

#number of circles
for i in range(10):
    circles.append(Circ())
sizeP=30
coll=sizeP//2


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    xpos= pos[0]
    ypos= pos[1]

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    
                     
    for i in range(len(rectangles)):
        rectangles[i].draw(screen)
        rectangles[i].move()
    for i in range(len(circles)):
        circles[i].draw(screen)
        circles[i].move()

    

    pygame.draw.rect(screen, BLUE, [xpos-(coll),ypos-(coll),sizeP,sizeP])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
