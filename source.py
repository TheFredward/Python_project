print('hello World! Time to learn a new language\n \n')
import pygame
# NOTE: after importing pygame, initialize pygame
pygame.init()
# constant global variables
S_WIDTH = 500
S_HEIGHT = 500
BLUE_HUE = (29,109,194)
END_DISPLAY = False

# create an object to help maintain time using Clock
time_interval = pygame.time.Clock()
# Update the clock also refers to frame rate
time_rate = 60 #fps
# display blue hue by creating a display with specified WxH
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
screen.fill(BLUE_HUE)
#name of the screen
pygame.display.set_caption('First display Test')

while not END_DISPLAY:
    # we get all events that are occurring, ie mouse clicks, keyboard strokes etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            END_DISPLAY = True
    # as long as the while loop is running we need to show and update the display as well as keep up with the time using .tick()
    pygame.display.update()
    time_interval.tick(time_rate)
# we need to end pygame and quit
pygame.quit()
quit()
