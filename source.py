print('hello World! Time to learn a new language\n \n')
import pygame
# constant global variables
S_WIDTH = 500
S_HEIGHT = 500
BLACK = (255,255,255)
BLUE_HUE = (29,109,194)
# create an object to help maintain time using Clock
time_interval = pygame.time.Clock()
screen = 'First display Test'
class StartScreen(object):
    """docstring for StartScreen."""
    # Update the clock also refers to frame rate
    time_rate = 60 #fps
    # global variable to hold in the user input
    user_input = ''
    def __init__(self, mScreenTitle,mWidth,mHeight):
        self.mScreenTitle = mScreenTitle
        self.mWidth = mWidth
        self.mHeight = mHeight
        # display blue hue by creating a display with specified WxH
        self.screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
        self.screen.fill(BLUE_HUE)
        #name of the screen
        pygame.display.set_caption(mScreenTitle)
    def loadScreen(self):
        END_DISPLAY = False
        font = pygame.font.Font(None,50)
        while not END_DISPLAY:
            # we get all events that are occurring, ie mouse clicks, keyboard strokes etc
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    END_DISPLAY = True
                    # check if the event is a keystroke
                elif event.type == pygame.KEYDOWN:
                    # check if the keystroke is a alphabet and if it is then store to user_input
                    if event.unicode.isalpha():
                        self.user_input += event.unicode
                    # if enter is pressed clear user input then refill the screen with the same color
                    elif event.key == pygame.K_RETURN:
                        self.user_input = ''
                        self.screen.fill(BLUE_HUE)
            # using the font from pygame render the input from the user
            block = font.render(self.user_input,True,BLACK)
            inputBox = block.get_rect()
            self.screen.blit(block,inputBox)
            # as long as the while loop is running we need to show and update the display as well as keep up with the time using .tick()
            pygame.display.update()
            time_interval.tick(self.time_rate)
# NOTE: after importing pygame, initialize pygame
pygame.init()
# CREATE a new object from the class StartScreen and pass in the necessary values for the __init__
newScreen = StartScreen(screen,S_WIDTH,S_HEIGHT)
# call the loadScreen on the variable created from the StartScreen class
newScreen.loadScreen()
# we need to end pygame and quit
pygame.quit()
quit()
