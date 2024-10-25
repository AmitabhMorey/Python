import pygame
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Changing the caption (title) of the window
pygame.display.set_caption("Car Game")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Dimensions of the car and obstacle
car_width = 92
car_height = 150
obstacle_width = 75
obstacle_height = 75

car_passed = 0
score = 0
level = 1

# Background Colour
background_colour = (119, 119, 119)

# Loading image
car_image = pygame.image.load("porscheCar.png")
road = pygame.image.load("road_.jpeg")
obstacle_image = pygame.image.load("deer.png")  

car_image = pygame.transform.scale(car_image, (car_width + 158, car_height))
road = pygame.transform.scale(road, (width, height))
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

# Car Crash Message
myfont = pygame.font.SysFont(None, 100)
render_text = myfont.render("Car Crashed!", 1, red)
score_font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()

def road_image():
    screen.blit(road, (0, 0))

def car(x, y):
    screen.blit(car_image, (x, y))

def draw_obstacle(obstacle_x, obstacle_y):
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

def display_score(car_passed, score, level):
    passed_text = score_font.render(f"Passed: {car_passed}", True, black)
    score_text = score_font.render(f"Score: {score}", True, black)
    level_text = score_font.render(f"Level: {level}", True, black)
    screen.blit(passed_text, (10, 10))
    screen.blit(score_text, (10, 40))
    screen.blit(level_text, (10, 70))

# Function to display game over message
def game_over_message():
    screen.blit(render_text, (200, 250))
    pygame.display.flip()
    pygame.time.delay(2000)

# Function to create buttons
def draw_button(text, x, y, width, height, color, action=None):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_font = pygame.font.SysFont(None, 60)
    button_text = button_font.render(text, True, black)
    screen.blit(button_text, (x + 10, y + 10))

    # Check for mouse click
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1 and action is not None:
            action()

# Function to handle the intro screen
def intro_screen():
    intro = True
    while intro:
        screen.fill(yellow)  # Background color for intro screen
        intro_font = pygame.font.SysFont(None, 100)
        title_text = intro_font.render("Car Game", True, black)
        screen.blit(title_text, (250, 100))

        # Draw buttons
        draw_button("Start Game", 300, 300, 200, 60, green, game_restart)
        draw_button("Instructions", 300, 400, 200, 60, blue)
        draw_button("Quit", 300, 500, 200, 60, red, pygame.quit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()

        pygame.display.update()
        clock.tick(15)

# Main game loop
def game_loop():
    running = True
    x_change = 0
    y_change = 0  # Add vertical movement
    x = width * 0.4  # Starting position of the car (x-axis)
    y = height - 160  # Starting position of the car (y-axis)

    # Obstacle parameters
    obstacle_x = random.randint(0, width - obstacle_width)
    obstacle_y = -600  # Start off-screen
    obstacle_speed = 5  # Initial speed of the obstacle

    global car_passed, score, level

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Detect key presses to move the car
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5

            # Stop movement when the key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        # Update the car's position
        x += x_change
        y += y_change

        # Fill the screen and draw the road background
        screen.fill(background_colour)
        road_image()

        # Draw the car
        car(x, y)

        # Display the score and cars passed
        display_score(car_passed, score, level)

        # Draw the obstacle and move it down the screen
        draw_obstacle(obstacle_x, obstacle_y)
        obstacle_y += obstacle_speed

        # Check if the obstacle moves off the screen
        if obstacle_y > height:
            obstacle_y = -obstacle_height  # Reset obstacle to the top
            obstacle_x = random.randint(0, width - obstacle_width)  # New random position
            car_passed += 1  # Increment cars passed
            score += 1  # Increment score
            # Increase difficulty level
            if car_passed % 10 == 0:
                level += 1
                obstacle_speed += 1  # Increase obstacle speed as levels increase

        # Check for boundary collision (left, right, top, bottom)
        if x > width - car_width or x < 0 or y > height - car_height or y < 0:
            game_over_message()
            running = False  # Stop the game when the car hits the boundary

        # Check for collision with the obstacle
        if y < obstacle_y + obstacle_height:
            if (x > obstacle_x and x < obstacle_x + obstacle_width) or (x + car_width > obstacle_x and x + car_width < obstacle_x + obstacle_width):
                game_over_message()
                running = False  # Stop the game if the car hits the obstacle

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)  # Set frame rate to 60 frames per second

# Function to handle restarting the game after game over
def game_restart():
    global car_passed, score, level
    car_passed = 0
    score = 0
    level = 1
    game_loop()

# Start the game with intro screen
intro_screen()

pygame.quit()
