import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Car Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load images and resize based on screen ratio
car_img = pygame.image.load('porscheCar.png')
car_img = pygame.transform.scale(car_img, (int(SCREEN_WIDTH * 0.1), int(SCREEN_HEIGHT * 0.15)))

obstacle1_img = pygame.image.load('deer.png')
obstacle1_img = pygame.transform.scale(obstacle1_img, (int(SCREEN_WIDTH * 0.1), int(SCREEN_HEIGHT * 0.15)))

obstacle2_img = pygame.image.load('lawrence.jpeg')
obstacle2_img = pygame.transform.scale(obstacle2_img, (int(SCREEN_WIDTH * 0.1), int(SCREEN_HEIGHT * 0.15)))

background_img = pygame.image.load('Background.jpg')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

intro_background_img = pygame.image.load('intro_background.jpg')
intro_background_img = pygame.transform.scale(intro_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Car dimensions (adjusted based on scaling)
CAR_WIDTH = car_img.get_width()
CAR_HEIGHT = car_img.get_height()

# Fonts
font = pygame.font.SysFont(None, 55)

# Functions
def text_display(text, color, x, y):
    message = font.render(text, True, color)
    screen.blit(message, [x, y])

def home_page():
    screen.fill(WHITE)
    text_display('Welcome to the Car Game', BLACK, 150, 250)
    text_display('Press any key to continue', BLACK, 200, 350)
    pygame.display.update()
    wait_for_key()

def intro_page():
    screen.blit(intro_background_img, (0, 0))
    text_display('Instructions: Avoid the cars and score points!', WHITE, 50, 300)
    text_display('Press any key to continue or M for menu', WHITE, 100, 400)
    pygame.display.update()
    wait_for_key_menu()

def game_over():
    screen.fill(WHITE)
    text_display('Game Over', RED, 300, 250)
    text_display('Press any key to restart or Q to quit', BLACK, 100, 350)
    pygame.display.update()
    wait_for_key_menu()

def end_page():
    screen.fill(WHITE)
    text_display('Thank you for playing!', BLACK, 200, 250)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return

def wait_for_key_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    home_page()
                else:
                    return

def main_game():
    # Initial player car position
    car_x = (SCREEN_WIDTH * 0.45)
    car_y = (SCREEN_HEIGHT * 0.8)
    car_speed_x = 0
    car_speed_y = 0

    # Initial obstacle positions and speeds
    obstacle1_x = 150
    obstacle1_y = -CAR_HEIGHT
    obstacle2_x = 500
    obstacle2_y = -CAR_HEIGHT * 2
    obstacle_speed = 5

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Keypress handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    car_speed_x = 5
                elif event.key == pygame.K_UP:
                    car_speed_y = -5
                elif event.key == pygame.K_DOWN:
                    car_speed_y = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_speed_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    car_speed_y = 0

        # Move car
        car_x += car_speed_x
        car_y += car_speed_y

        # Redraw background
        screen.blit(background_img, (0, 0))

        # Draw the player's car
        screen.blit(car_img, (car_x, car_y))

        # Move obstacles
        obstacle1_y += obstacle_speed
        obstacle2_y += obstacle_speed

        # Draw obstacles
        screen.blit(obstacle1_img, (obstacle1_x, obstacle1_y))
        screen.blit(obstacle2_img, (obstacle2_x, obstacle2_y))

        # Reset obstacles after they move off-screen
        if obstacle1_y > SCREEN_HEIGHT:
            obstacle1_y = -CAR_HEIGHT
        if obstacle2_y > SCREEN_HEIGHT:
            obstacle2_y = -CAR_HEIGHT * 2

        # Check for collisions
        if car_y < obstacle1_y + CAR_HEIGHT and car_y + CAR_HEIGHT > obstacle1_y:
            if car_x < obstacle1_x + CAR_WIDTH and car_x + CAR_WIDTH > obstacle1_x:
                game_over()
                wait_for_key_menu()

        if car_y < obstacle2_y + CAR_HEIGHT and car_y + CAR_HEIGHT > obstacle2_y:
            if car_x < obstacle2_x + CAR_WIDTH and car_x + CAR_WIDTH > obstacle2_x:
                game_over()
                wait_for_key_menu()

        # Display updates
        pygame.display.update()

        # Frame rate
        pygame.time.Clock().tick(60)

# Game flow
home_page()
intro_page()

while True:
    main_game()
    end_page()
