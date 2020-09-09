import pygame
import time
import random

pygame.init()
# the following are constants that will be used throughout the programme

DisplayWidth = 800
DisplayLength = 600

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 100, 0)
RedDark = (100, 0, 0)
GreenLight = (0, 200, 0)

# the following constant are based on the files used
CharacterSize = 73
ZombieSize = 72
ZombieWidth = 87
ZombieLength = 98
Zombie2Width = 75
Zombie2Length = 98
# the following are constants used for the Helmet which will act as the users attack in the game
HelmetWidth = 60
HelmetLength = 54
# the following are the Images used in the game
SkaterImg = pygame.image.load("MainCharacter.png")
ZombieImg = pygame.image.load("Zombie.png")
Zombie2Img = pygame.image.load("Zombie2PNG.png")
StreetBackground = pygame.image.load("StreetBackgroundP.png")
MenuBackgroundImg = pygame.image.load("MenuBackgroundP.png")
HelmetImg = pygame.image.load("SkatingHelmet.png")

GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayLength))
pygame.display.set_caption("Skate Away")
GameClock = pygame.time.Clock()

#the following is the games background music
pygame.mixer.music.load("GameBackgroundMusic.wav")

def ScoreCounter(count):
    Font = pygame.font.Font("Bubblegum_Sans.ttf", 25)
    Text = Font.render("Zombies Count: " + str(count), True, White)
    GameDisplay.blit(Text, (600, 50))


def Skater(x, y):
    GameDisplay.blit(SkaterImg, (x, y))  # (x,y) must have their own brackets to make sure that it is a tuple and not separate parameters.

def Zombies1(x, y):
    GameDisplay.blit(ZombieImg, (x, y))


def Zombies2(x, y):
    GameDisplay.blit(Zombie2Img, (x, y))

def Helmet(x,y):
    GameDisplay.blit(HelmetImg,(x,y))


def MenuBackground(x, y):
    GameDisplay.blit(MenuBackgroundImg, (x, y))


def Background(x, y):
    GameDisplay.blit(StreetBackground, (x, y))


def Background2(x, y):
    GameDisplay.blit(StreetBackground, (x, y))

def MessageObjects(text, font):
    TextSurface = font.render(text, True, White)
    return TextSurface, TextSurface.get_rect()


def DisplayMessage(text):
    TextFont = pygame.font.Font("Bubblegum_Sans.ttf", 100)
    TextSurface, TextRectangle = MessageObjects(text, TextFont)
    TextRectangle.center = ((DisplayWidth / 2), (DisplayLength / 2))
    GameDisplay.blit(TextSurface, TextRectangle)

    pygame.display.update()
    time.sleep(1)

    GameLoop()


def PlayerDead():
    DisplayMessage("They got you")


def ButtionInteraction(Message, x, y, width, length, Ic, Ac, action=None):
    Mouse = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()

    # [0] and [1] refer to (x,y)
    if x + width > Mouse[0] > x and y + length > Mouse[1] > y:
        pygame.draw.rect(GameDisplay, Ac, (x, y, width, length))
        SmallTextFont = pygame.font.Font("Bubblegum_Sans.ttf", 50)
        TextSurface, TextRectangle = MessageObjects(Message, SmallTextFont)
        TextRectangle.center = (x + (width / 2), y + (length / 2))
        GameDisplay.blit(TextSurface, TextRectangle)
        
        if Click[0] == 1 and action != None:
            if action == "play":
                GameLoop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(GameDisplay, Ic, (x, y, width, length))
        SmallTextFont = pygame.font.Font("Bubblegum_Sans.ttf", 50)
        TextSurface, TextRectangle = MessageObjects(Message, SmallTextFont)
        TextRectangle.center = (x + (width / 2), y + (length / 2))
        GameDisplay.blit(TextSurface, TextRectangle)



def GameMainMenu():
    pygame.mixer.music.play()
    MainMenu = True
    while MainMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            else:
                MenuBackground(0, 0)

                TextFont = pygame.font.Font("Bubblegum_Sans.ttf", 70)
                TextSurface, TextRectangle = MessageObjects("Skate Away", TextFont)
                TextRectangle.center = ((DisplayWidth / 2), (DisplayLength / 2))
                GameDisplay.blit(TextSurface, TextRectangle)

                pygame.draw.rect(GameDisplay, Green, (150, 400, 200, 100))
                pygame.draw.rect(GameDisplay, RedDark, (500, 400, 200, 100))

                ButtionInteraction("Play!", 150, 400, 200, 100, Green, GreenLight, "play")
                ButtionInteraction("Quit Game", 500, 400, 200, 100, RedDark, Red, "quit")

                pygame.display.update()

                GameClock.tick(4)


def GameLoop():
    Bx = 0
    By = 0
    Bx2 = 800
    By2 = 0

    Playerx = (DisplayWidth * 0.05)
    Playery = (DisplayLength * 0.45)
    yChange = 0



    # the following is the Zombie generating parameters
    ZombieStarty = random.randrange(0,DisplayLength)  # the random function is important to ensure the Zombie inst being generated in the same place repeatedly
    ZombieStartx = 1000
    ZombieSpeed = -25  # this is a negative value because 1000 is off the screen on the right hand side. for the zombie to come towards the left we have to move in the -Playerx direction

    Zombie2Starty = random.randrange(0, DisplayLength)
    Zombie2Startx = random.randrange(1000, 1500)
    Zombie2Speed = (-1) * random.randrange(25, 40)

    HelmetX = (DisplayWidth * 0.05)
    HelmetY = (DisplayLength * 0.45)
    xChange = 0
    HelmetYChange=0


    Score = 0


    EndGame = False

    # this loop is to handle events and let the game function
    while not EndGame:

        for event in pygame.event.get():  # what this does is collect events happening in the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # this corresponds to the Up arrow key found on the keyboard.
                    yChange = -20
                    HelmetYChange=-20
                if event.key == pygame.K_DOWN:
                    yChange = 20
                    HelmetYChange= 20
                if event.key == pygame.K_SPACE:
                    xChange = 60
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yChange = 0
                    HelmetYChange=0

        Playery += yChange
        HelmetY += HelmetYChange
        HelmetX += xChange






        # in this part we are calling all the display functions
        Background(Bx, By)  # its important to choose the display before displaying the main characters so its not overwritten
        Bx -= 20

        Background2(Bx2, By2)
        Bx2 -= 20

        Skater(Playerx, Playery)


        Helmet(HelmetX, HelmetY)


        ScoreCounter(Score)

        Zombies1(ZombieStartx, ZombieStarty)
        ZombieStartx += ZombieSpeed  # this can be thought of as the starting difficulty of the game, Allows the zombie character to move towards the skater

        Zombies2(Zombie2Startx, Zombie2Starty)
        Zombie2Startx += Zombie2Speed


        # The first two if statements allow the in-game background to move and give the illusion of movement of the  main character
        if Bx < -800:
            Bx = 0

        if Bx2 < 0:
            Bx2 = 800

        if Playery > DisplayLength - CharacterSize or Playery < 0:  # this statement limits the player from going off screen. in this programme going off screen will result in a loss
            PlayerDead()

        if HelmetX-HelmetWidth>800:
            xChange=0
            HelmetX=Playerx

        if xChange==0:
            HelmetY=Playery

        #This is to avoid a bug experinced with the helmets re-starting position after throwing it a first time
        if HelmetX>Playerx:
            HelmetYChange=0

        if ZombieStartx < 0 - ZombieSize:
            ZombieStartx = 800 + ZombieSize
            ZombieStarty = random.randrange(0 + ZombieSize,DisplayLength - ZombieSize)  # this range allows the Zombie to stay on screen
            Score += 1
            ZombieSpeed -= 1

        if Zombie2Startx < 0 - Zombie2Width:
            Zombie2Startx = random.randrange(1500, 3000)
            Zombie2Starty = random.randrange(0 + Zombie2Length, DisplayLength - Zombie2Length)
            Score += 1
            Zombie2Speed -= 1


        # the following are conditions which allow for a clash in the coordinates , when the player or helmet overlap the zombies

        if Playerx > ZombieStartx + ZombieWidth:
            if Playery< ZombieStarty and Playery > ZombieStarty - ZombieLength or Playery - ZombieLength < ZombieStarty and Playery - ZombieLength > ZombieStarty - ZombieLength:
                PlayerDead()

        if Playerx > Zombie2Startx + Zombie2Width:
            if Playery < Zombie2Starty and Playery > Zombie2Starty - Zombie2Length or Playery - Zombie2Length < Zombie2Starty and Playery - Zombie2Length > Zombie2Starty - Zombie2Length:
                PlayerDead()

        if HelmetX > ZombieStartx + ZombieWidth:
            if HelmetY < ZombieStarty and HelmetY > ZombieStarty - ZombieLength or HelmetY - ZombieLength < ZombieStarty and HelmetY - ZombieLength > ZombieStarty - ZombieLength:
                ZombieStartx = 1000 + ZombieSize
                ZombieStarty = random.randrange(0 + ZombieSize, DisplayLength - ZombieSize)
                Score += 1
                ZombieSpeed -= 1

        if HelmetX > Zombie2Startx + Zombie2Width:
            if HelmetY < Zombie2Starty and HelmetY > Zombie2Starty - Zombie2Length or HelmetY - Zombie2Length < Zombie2Starty and HelmetY - Zombie2Length > Zombie2Starty - Zombie2Length:
                Zombie2Startx = 1000 + Zombie2Width
                Zombie2Starty = random.randrange(0 + Zombie2Length, DisplayLength - Zombie2Length)
                Score += 1
                ZombieSpeed -= 1

        pygame.display.update()  # This will allow us to update a parameter that we input or update the entire display window

        GameClock.tick(90)  # This is how fast the game moves or its fps



GameMainMenu()
pygame.quit()
quit()
