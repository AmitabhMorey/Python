import pygame
import time
import random

# Initialize pygame and set colors
pygame.init()
gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
blue = (50, 50, 255)

display_width = 800
display_height = 600

gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()

# Load and resize images
carimg = pygame.image.load('porscheCar.png')
carimg = pygame.transform.scale(carimg, (100, 200))  # Increased size of Porsche car

deer_img = pygame.image.load('deer.png')
deer_img = pygame.transform.scale(deer_img, (70, 140))  # Resize deer

lawrence_img = pygame.image.load('lawrence.jpeg')
lawrence_img = pygame.transform.scale(lawrence_img, (65, 130))  # Resize Lawrence

background_img = pygame.image.load('background.jpg')
background_img = pygame.transform.scale(background_img, (display_width, display_height))  # Resize background

car_width = 100  # Update car width to the resized value
car_height = 200  # Update car height to the resized value
pause = False

# Intro screen
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplays.blit(background_img, (0, 0))  # Set background image for the intro page
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("CAR GAME", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)
        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("INSTRUCTIONS", 325, 520, 150, 50, (0, 150, 0), (0, 255, 0), "instructions")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        pygame.display.update()
        clock.tick(50)

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "play":
                countdown()
            elif action == "instructions":
                instructions()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))

    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)

def countdown():
    countdown = True
    while countdown:
        gamedisplays.fill(gray)
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = (display_width / 2, display_height / 2)
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        countdown = False
    game_loop()

def instructions():
    instruct = True
    while instruct:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplays.fill(gray)
        largetext = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Instructions", largetext)
        TextRect.center = (display_width / 2, 50)
        gamedisplays.blit(TextSurf, TextRect)

        instruction_text = [
            "Use left and right arrow keys to move the car.",
            "Use up and down arrow keys to move the car up and down.",
            "Avoid obstacles like deer and Lawrence.",
            "Score points by passing obstacles.",
            "Good luck!"
        ]
        
        smalltext = pygame.font.Font('freesansbold.ttf', 30)
        for i, line in enumerate(instruction_text):
            textsurf, textrect = text_objects(line, smalltext)
            textrect.center = (display_width / 2, 150 + i * 40)
            gamedisplays.blit(textsurf, textrect)

        button("BACK", 350, 520, 100, 50, green, bright_green, "play")
        pygame.display.update()
        clock.tick(50)

def obstacle(obs_startx, obs_starty, obs_type):
    if obs_type == "deer":
        obs_pic = deer_img
    else:
        obs_pic = lawrence_img
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))

def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed: " + str(passed), True, black)
    score_text = font.render("Score: " + str(score), True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score_text, (0, 30))

def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = (display_width / 2, display_height / 2)
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display("YOU CRASHED")

def car(x, y):
    gamedisplays.blit(carimg, (x, y))

def game_loop():
    x = display_width * 0.45
    y = display_height * 0.6  # Adjust initial position
    x_change = 0
    y_change = 0  # New variable for vertical movement
    obstacle_speed = 7
    obs_startx = random.randrange(200, display_width - 200)
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    score = 0
    fps = 60
    bumped = False

    # Determine obstacle type (Lawrence has a lower probability)
    obs_type = "deer" if random.random() > 0.1 else "lawrence"

    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5  # Move up
                if event.key == pygame.K_DOWN:
                    y_change = 5  # Move down
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change  # Update vertical position
        gamedisplays.fill(gray)  # Set background color for the game

        obs_starty += obstacle_speed
        obstacle(obs_startx, obs_starty, obs_type)
        car(x, y)
        score_system(passed, score)

        if x > display_width - car_width or x < 0 or y > display_height - car_height or y < 0:
            crash()

        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(200, display_width - 200)
            passed += 1
            score = passed * 10
            obs_type = "deer" if random.random() > 0.1 else "lawrence"  # 10% chance for Lawrence

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()

        pygame.display.update()
        clock.tick(fps)

intro_loop()
pygame.quit()
quit()