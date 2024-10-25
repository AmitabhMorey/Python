# import pygame
# import time
# import random

# # Initialize pygame and set colors
# pygame.init()
# gray = (119, 118, 110)  # Color for background
# black = (0, 0, 0)       # Color for text
# red = (255, 0, 0)       # Color for quit button
# green = (0, 200, 0)     # Color for start button
# bright_green = (0, 255, 0)  # Bright green for hover effect
# bright_red = (255, 0, 0)     # Bright red for hover effect on quit button
# blue = (50, 50, 255)         # Color for instructions

# # Set display dimensions
# display_width = 800
# display_height = 600

# # Create display window
# gamedisplays = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption("Car Game")  # Set window title
# clock = pygame.time.Clock()  # Create a clock to control frame rate

# # Load and resize images for the car, obstacles, and background
# carimg = pygame.image.load('porscheCar.png')
# carimg = pygame.transform.scale(carimg, (100, 200))  # Increase size of Porsche car

# deer_img = pygame.image.load('deer.png')
# deer_img = pygame.transform.scale(deer_img, (70, 140))  # Resize deer

# lawrence_img = pygame.image.load('lawrence.jpeg')
# lawrence_img = pygame.transform.scale(lawrence_img, (65, 130))  # Resize Lawrence

# background_img = pygame.image.load('background.jpg')
# background_img = pygame.transform.scale(background_img, (display_width, display_height))  # Resize background

# car_width = 100  # Update car width to the resized value
# car_height = 200  # Update car height to the resized value
# pause = False  # Variable to control pause state

# # Function to display intro screen
# def intro_loop():
#     intro = True
#     while intro:  # Loop until the intro is exited
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # Quit if window is closed
#                 pygame.quit()
#                 quit()

#         gamedisplays.blit(background_img, (0, 0))  # Set background image for the intro page
#         largetext = pygame.font.Font('freesansbold.ttf', 115)  # Large font for title
#         TextSurf, TextRect = text_objects("CAR GAME", largetext)  # Create text surface for title
#         TextRect.center = (400, 100)  # Center title
#         gamedisplays.blit(TextSurf, TextRect)  # Draw title on screen
#         button("START", 150, 520, 100, 50, green, bright_green, "play")  # Start button
#         button("INSTRUCTIONS", 325, 520, 150, 50, (0, 150, 0), (0, 255, 0), "instructions")  # Instructions button
#         button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")  # Quit button
#         pygame.display.update()  # Update the display
#         clock.tick(50)  # Control frame rate

# # Function to create buttons
# def button(msg, x, y, w, h, ic, ac, action=None):
#     mouse = pygame.mouse.get_pos()  # Get mouse position
#     click = pygame.mouse.get_pressed()  # Get mouse button states
#     if x + w > mouse[0] > x and y + h > mouse[1] > y:  # Check if mouse is over button
#         pygame.draw.rect(gamedisplays, ac, (x, y, w, h))  # Draw active button
#         if click[0] == 1 and action is not None:  # Check for mouse click
#             if action == "play":
#                 countdown()  # Start the countdown for the game
#             elif action == "instructions":
#                 instructions()  # Show instructions
#             elif action == "quit":
#                 pygame.quit()  # Quit the game
#                 quit()
#     else:
#         pygame.draw.rect(gamedisplays, ic, (x, y, w, h))  # Draw inactive button

#     smalltext = pygame.font.Font("freesansbold.ttf", 20)  # Font for button text
#     textsurf, textrect = text_objects(msg, smalltext)  # Create text surface for button
#     textrect.center = ((x + (w / 2)), (y + (h / 2)))  # Center button text
#     gamedisplays.blit(textsurf, textrect)  # Draw button text on screen

# # Function for countdown before the game starts
# def countdown():
#     countdown = True
#     while countdown:  # Loop for countdown
#         gamedisplays.fill(gray)  # Fill background with gray color
#         largetext = pygame.font.Font('freesansbold.ttf', 115)  # Font for countdown
#         TextSurf, TextRect = text_objects("3", largetext)  # Create text surface for countdown
#         TextRect.center = (display_width / 2, display_height / 2)  # Center countdown
#         gamedisplays.blit(TextSurf, TextRect)  # Draw countdown on screen
#         pygame.display.update()  # Update display
#         clock.tick(1)  # Control frame rate
#         countdown = False  # Exit countdown loop
#     game_loop()  # Start the game loop

# # Function to show instructions
# def instructions():
#     instruct = True
#     while instruct:  # Loop until exiting instructions
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:  # Quit if window is closed
#                 pygame.quit()
#                 quit()

#         gamedisplays.fill(gray)  # Fill background with gray color
#         largetext = pygame.font.Font('freesansbold.ttf', 50)  # Font for instructions title
#         TextSurf, TextRect = text_objects("Instructions", largetext)  # Create text surface for title
#         TextRect.center = (display_width / 2, 50)  # Center title
#         gamedisplays.blit(TextSurf, TextRect)  # Draw title on screen

#         # List of instruction text
#         instruction_text = [
#             "Use left and right arrow keys to move the car.",
#             "Use up and down arrow keys to move the car up and down.",
#             "Avoid obstacles like deer and Lawrence.",
#             "Score points by passing obstacles.",
#             "Good luck!"
#         ]
        
#         smalltext = pygame.font.Font('freesansbold.ttf', 30)  # Font for instruction text
#         for i, line in enumerate(instruction_text):  # Loop through instruction lines
#             textsurf, textrect = text_objects(line, smalltext)  # Create text surface for each line
#             textrect.center = (display_width / 2, 150 + i * 40)  # Center each line
#             gamedisplays.blit(textsurf, textrect)  # Draw instruction line on screen

#         button("BACK", 350, 520, 100, 50, green, bright_green, "play")  # Back button
#         pygame.display.update()  # Update display
#         clock.tick(50)  # Control frame rate

# # Function to draw obstacles
# def obstacle(obs_startx, obs_starty, obs_type):
#     if obs_type == "deer":
#         obs_pic = deer_img  # Select deer image
#     else:
#         obs_pic = lawrence_img  # Select Lawrence image
#     gamedisplays.blit(obs_pic, (obs_startx, obs_starty))  # Draw obstacle on screen

# # Function to display score
# def score_system(passed, score):
#     font = pygame.font.SysFont(None, 25)  # Font for displaying score
#     text = font.render("Passed: " + str(passed), True, black)  # Create text surface for passed count
#     score_text = font.render("Score: " + str(score), True, red)  # Create text surface for score
#     gamedisplays.blit(text, (0, 50))  # Draw passed count on screen
#     gamedisplays.blit(score_text, (0, 30))  # Draw score on screen

# # Function to create text objects
# def text_objects(text, font):
#     textsurface = font.render(text, True, black)  # Create text surface
#     return textsurface, textsurface.get_rect()  # Return surface and its rectangle

# # Function to display a message and pause
# def message_display(text):
#     largetext = pygame.font.Font("freesansbold.ttf", 80)  # Font for message
#     textsurf, textrect = text_objects(text, largetext)  # Create text surface for message
#     textrect.center = (display_width / 2, display_height / 2)  # Center message
#     gamedisplays.blit(textsurf, textrect)  # Draw message on screen
#     pygame.display.update()  # Update display
#     time.sleep(2)  # Pause for 2 seconds
#     game_loop()  # Restart the game loop

# # Function to handle crashes
# def crash():
#     message_display("YOU CRASHED")  # Display crash message

# # Function to draw the car
# def car(x, y):
#     gamedisplays.blit(carimg, (x, y))  # Draw car on screen

# # Main

# def add_member(group):
#     member = input("Enter the member name: ")
#     group.append(member)
#     print("Member added successfully!")
#     return group

# def view_member(group):
#     print("The members in the group are: ", group)

# def remove_member(group):
#     member = input("Enter the member name to remove: ")
#     if member in group:
#         group.remove(member)
#         print("Member removed successfully!")
#     else:
#         print("Member not found in the group!")
#     return group

# group = []
# while True:
#     print("1. Add member")
#     print("2. View member")
#     print("3. Remove member")
#     print("4. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         group = add_member(group)
#     elif choice == 2:
#         view_member(group)
#     elif choice == 3:
#         group = remove_member(group)
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice! Please enter a valid choice.")