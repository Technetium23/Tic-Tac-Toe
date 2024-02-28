import pygame, sys
from pygame.locals import *
import time
import random
from random import randint, choice
pygame.init()

screen = pygame.display.set_mode((750, 450))
screen.fill((255,215,0))
pygame.display.set_caption("Tic-Tac-Toe")
winner = False
first_list = []
user_positions = []
computer_options = []
empty_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
width_line = 2
run = True
temp = ""
temp_choice = ""

#Functions
def text_on_screen(text, coordinates, colour):
    global winner
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 32)
    textsurface = font.render(text, False, colour)
    screen.blit(textsurface, coordinates)
    winner = True
def user_functions(number, x1, y1, x2, y2):
    global first_list
    pygame.draw.line(screen, (0, 0, 0), x1, y1, 2)
    pygame.draw.line(screen, (0, 0, 0), x2, y2, 2)
    first_list.append(number)
def computer_functions(number, xy):
    global computer_options, empty_positions
    computer_options.append(number)
    empty_positions.remove(number)
    pygame.draw.circle(screen, (255, 255, 255), xy, 19, 2)
def last_move(number, X1,Y1,X2,Y2):
    pygame.draw.line(screen, (0, 0, 0), X1, Y1, 2)
    pygame.draw.line(screen, (0, 0, 0), X2, Y2, 2)
    empty_positions.remove(number)
    user_positions.append(number)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    vertical_line1 = pygame.draw.line(screen, (0, 0, 0), (325, 125), (325, 275), width_line)
    vertical_line2 = pygame.draw.line(screen, (0, 0, 0), (375, 125), (375, 275), width_line)

    horizontal_line1 = pygame.draw.line(screen, (0, 0, 0), (275, 175), (425, 175), width_line)
    horizontal_line2 = pygame.draw.line(screen, (0, 0, 0), (275, 225), (425, 225), width_line)
    
# Button Functioning
    buttons = pygame.key.get_pressed()
    if buttons[pygame.K_SPACE]:
            first_list = []
            user_positions = []
            computer_options = []
            empty_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            screen.fill((255,215,0))
            winner = False
            vertical_line1 = pygame.draw.line(screen, (0, 0, 0), (325, 125), (325, 275), width_line)
            vertical_line2 = pygame.draw.line(screen, (0, 0, 0), (375, 125), (375, 275), width_line)                

            horizontal_line1 = pygame.draw.line(screen, (0, 0, 0), (275, 175), (425, 175), width_line)
            horizontal_line2 = pygame.draw.line(screen, (0, 0, 0), (275, 225), (425, 225), width_line)            
    if buttons[pygame.K_TAB]:
        run = False
    
    if len(empty_positions) > 1 and winner != True:
        buttons = pygame.key.get_pressed()
        if 1 in empty_positions:
            if buttons[pygame.K_1]:
                user_functions(1, (285, 135), (315, 165), (315, 135), (285, 165))
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        # Computer Wins
                        # Vertical Position 2
                        if 2 in computer_options and 5 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))                            
                        elif 8 in computer_options and 5 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))                            
                        elif 2 in computer_options and 8 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                            

                        # Vertical Position 3
                        elif 3 in computer_options and 6 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))                                                        
                        elif 9 in computer_options and 6 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))                            
                        elif 3 in computer_options and 9 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))                                                                   

                        # Horizontal position 2
                        elif 4 in computer_options and 5 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))                        
                        elif 6 in computer_options and 5 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))                            
                        elif 4 in computer_options and 6 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                            
                        
                        # Horizontal Position 3
                        elif 7 in computer_options and 8 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))                            
                        elif 9 in computer_options and 8 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))                            
                        elif 7 in computer_options and 9 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))                                                 

                        # Diagonal Position 3 to 7
                        elif 3 in computer_options and 5 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))                            
                        elif 7 in computer_options and 5 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))                        
                        elif 3 in computer_options and 7 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                                                                            
                        
                        # Special Cases
                        # For 6
                        elif len(empty_positions) == 6 and 6 in user_positions:
                            temp_choice = [2, 8]
                            temp = choice(temp_choice)
                            if temp == 2:
                                computer_functions(2, (350, 150))                                
                            elif temp == 8:
                                computer_functions(8, (350, 250))                                
                        # For 8
                        elif len(empty_positions) == 6 and 8 in user_positions:
                            temp_choice = [4, 6]
                            temp = choice(temp_choice)
                            if temp == 4:
                                computer_functions(4, (300, 200))                                
                            elif temp == 6:
                                computer_functions(6, (400, 200))                                

                        elif 5 in user_positions and 9 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))                            
                        elif 5 in user_positions and 9 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))                            

                        # Other Cases
                        elif 2 in user_positions and 3 in empty_positions:
                            computer_functions(3, (400, 150))                                                                        
                        elif 4 in user_positions and 7 in empty_positions:
                            computer_functions(7, (300, 250))                                                                            
                        elif 5 in user_positions and 9 in empty_positions:
                            computer_functions(9, (300, 250))                            
                        elif 3 in user_positions and 2 in empty_positions:
                            computer_functions(2, (350, 150))                                                                      
                        elif 7 in user_positions and 4 in empty_positions:
                            computer_functions(4, (300, 200))                                                                           
                        elif 9 in user_positions and 5 in empty_positions:
                            computer_functions(5, (350, 200))                            
                        
                        # Corner Cases
                        elif len(empty_positions) == 8:
                            computer_functions(5, (350, 200))                            
                        elif len(empty_positions) == 6 and 9 in user_positions and 5 in computer_options:
                            computer_functions(2, (350, 150))                            
                        else:
                            a = choice(empty_positions)
                            if a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))                            
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))                                
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))                                
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))                                
                            elif a == 6 and a in empty_positions:
                                computer_functions(6, (400, 200))                                                                                
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                                
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))                                
                            elif a == 9 and a in empty_positions:
                                computer_functions(9, (400, 250))
        else:
            pass
        if 2 in empty_positions:              
            if buttons[pygame.K_2]:
                user_functions(2, (335, 135), (365, 165), (365, 135), (335, 165))                
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        # Computer wins
                        # Vertical Position 1
                        if 1 in computer_options and 4 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))                            
                        elif 7 in computer_options and 4 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))                            
                        elif 1 in computer_options and 7 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))                            

                        # Vertical Position 3
                        elif 3 in computer_options and 6 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))                            
                        elif 9 in computer_options and 6 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))                           
                        elif 3 in computer_options and 9 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))                                                

                        # Horizontal position 2
                        elif 4 in computer_options and 5 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))                            
                        elif 6 in computer_options and 5 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))                            
                        elif 4 in computer_options and 6 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                        
                        
                        # Horizontal Position 3
                        elif 7 in computer_options and 8 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 8 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 9 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))                            

                        # Diagonal Position 1 to 9
                        elif 1 in computer_options and 5 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 5 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))                            
                        elif 1 in computer_options and 9 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Diagonal Position 3 to 7
                        elif 3 in computer_options and 5 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 5 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 7 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Special Middle Cases
                        # For 6                        
                        elif len(empty_positions) == 6 and 6 in user_positions:
                            temp_choice = [1, 3, 9]
                            temp = choice(temp_choice)
                            if temp == 1:
                                computer_functions(1, (300, 150))
                            elif temp == 3:
                                computer_functions(3, (400, 150))
                            elif temp == 9:
                                computer_functions(9, (400, 250))

                        # For 4
                        elif len(empty_positions) == 6 and 4 in user_positions:
                            temp_choice = [1, 3, 7]
                            temp = choice(temp_choice)
                            if temp == 1:
                                computer_functions(1, (300, 150))
                            elif temp == 3:
                                computer_functions(3, (400, 150))
                            elif temp == 7:
                                computer_functions(7, (300, 250))

                        # Special Cases
                        elif len (empty_positions) == 8:
                            computer_functions(5, (350, 200))

                        # Other Cases
                        elif 1 in user_positions and 3 in empty_positions:
                            computer_functions(3, (400, 150))                                            
                        elif 3 in user_positions and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 5 in user_positions and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 8 in user_positions and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        else:
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))                                
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))                                
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))
                            elif a == 6 and a in empty_positions:
                                computer_functions(6, (400, 200))
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))
                            elif a == 9 and a in empty_positions:                        
                                computer_functions(9, (400, 250))
        else:
            pass
        if 3 in empty_positions:
            if buttons[pygame.K_3]:
                user_functions(3, (385, 135), (415, 165), (415, 135), (385, 165))                
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        #Computer Wins
                        # Vertical Position 1
                        if 1 in computer_options and 4 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 4 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 7 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))

                        # Vertical Position 2
                        if 2 in computer_options and 5 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 8 in computer_options and 5 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        elif 2 in computer_options and 8 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Horizontal position 2
                        elif 4 in computer_options and 5 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        elif 6 in computer_options and 5 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))
                        elif 4 in computer_options and 6 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        
                        # Horizontal Position 3
                        elif 7 in computer_options and 8 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 8 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 9 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))

                        # Diagonal Position 1 to 9
                        elif 1 in computer_options and 5 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 5 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 9 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Special Cases
                        # For 4
                        elif len(empty_positions) == 6 and 4 in user_positions:
                            temp_choice = [2, 8]
                            temp = choice(temp_choice)
                            if temp == 2:
                                computer_functions(2, (350, 150))
                            elif temp == 8:
                                computer_functions(8, (350, 250))
                        # For 8
                        elif len(empty_positions) == 6 and 8 in user_positions:
                            temp_choice = [4, 6]
                            temp = choice(temp_choice)
                            if temp == 4:
                                computer_functions(4, (300, 200))
                            elif temp == 6:
                                computer_functions(6, (400, 200))

                        elif 5 in user_positions and 7 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 5 in user_positions and 7 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))

                        #Other Cases
                        elif 2 in user_positions and 1 in empty_positions:
                            computer_functions(1, (300, 150))                                            
                        elif 5 in user_positions and 7 in empty_positions:
                            computer_functions(7, (300, 250))                                                
                        elif 6 in user_positions and 9 in empty_positions:
                            computer_functions(9, (400, 250))

                        elif 1 in user_positions and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        elif 7 in user_positions and 5 in empty_positions:
                             computer_functions(5, (350, 200))
                        elif 9 in user_positions and 6 in empty_positions:
                            computer_functions(6, (400, 200))

                        # Corner Cases
                        elif len(empty_positions) == 8:
                            computer_functions(5, (350, 200))
                        elif len(empty_positions) == 6 and 7 in user_positions and 5 in computer_options:
                            computer_functions(6, (400, 200))
                        else:
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))
                            elif a == 5 and a in empty_positions:
                               computer_functions(5, (350, 200))
                            elif a == 6 and a in empty_positions:                        
                                computer_functions(6, (400, 200))                        
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))
                            elif a == 9 and a in empty_positions:                        
                                computer_functions(9, (400, 250))
        else:
            pass
        if 4 in empty_positions:
            if buttons[pygame.K_4]:
                user_functions(4, (315, 185), (285, 215), (285, 185), (315, 215))
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        # Computer Wins
                        # Vertical Position 2
                        if 2 in computer_options and 5 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 8 in computer_options and 5 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        elif 2 in computer_options and 8 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Vertical Position 3
                        elif 3 in computer_options and 6 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 6 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 9 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        
                        # Horizontal Position 1
                        elif 1 in computer_options and 2 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 2 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 3 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))                
                        
                        # Horizontal Position 3
                        elif 7 in computer_options and 8 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 8 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 9 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))

                        # Diagonal Position 1 to 9
                        elif 1 in computer_options and 5 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 5 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 9 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Diagonal Position 3 to 7
                        elif 3 in computer_options and 5 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 5 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 7 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Special Middle Cases
                        # For 8
                        elif len(empty_positions) == 6 and 8 in user_positions:
                            temp_choice = [1, 7, 9]
                            temp = choice(temp_choice)
                            if temp == 1:
                                computer_functions(1, (300, 150))
                            elif temp == 7:
                                computer_functions(7, (300, 250))
                            elif temp == 9:
                                computer_functions(9, (400, 250))
                        # For 2
                        elif len(empty_positions) == 6 and 2 in user_positions:
                            temp_choice = [1, 3, 7]
                            temp = choice(temp_choice)
                            if temp == 1:
                                computer_functions(1, (300, 150))
                            elif temp == 3:
                                computer_functions(3, (400, 150))
                            elif temp == 7:
                                computer_functions(7, (300, 250))

                        # Special Cases
                        elif len (empty_positions) == 8:
                            computer_functions(5, (350, 200))

                        # Other Cases
                        elif 1 in user_positions and 7 in empty_positions:
                            computer_functions(7, (300, 250))                                            
                        elif 7 in user_positions and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 5 in user_positions and 6 in empty_positions:
                            computer_functions(6, (400, 200))                        
                        elif 6 in user_positions and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        else:                            
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))                                
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))
                            elif a == 6 and a in empty_positions:                        
                                computer_functions(6, (400, 200))                       
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))
                            elif a == 9 and a in empty_positions:                        
                                computer_functions(9, (400, 250))
        else:
            pass
        if 5 in empty_positions:
            if buttons[pygame.K_5]:
                user_functions(5, (335, 185), (365, 215), (365, 185), (335, 215))                
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        # Computer Wins
                        # Vertical Position 1
                        if 1 in computer_options and 4 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 4 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 7 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))                        

                        # Vertical Position 3
                        elif 3 in computer_options and 6 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 6 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 9 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        
                        # Horizontal Position 1
                        elif 1 in computer_options and 2 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 2 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 3 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))                        
                        
                        # Horizontal Position 3
                        elif 7 in computer_options and 8 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 8 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 9 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))                

                    # Corner Cases
                        elif len(empty_positions) == 8:
                            temp_choice = [1, 3, 7, 9]
                            temp = choice(temp_choice)
                            if temp == 9:
                                computer_functions(9, (400, 250))
                            elif temp == 3:
                                computer_functions(3, (400, 150))
                            elif temp == 7:
                                computer_functions(7, (300, 250))
                            elif temp == 1:
                                computer_functions(1, (300, 150))

                #   Diagonals                        
                        elif 1 in user_positions and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in user_positions and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 3 in user_positions and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in user_positions and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                #   Verticals
                        elif 2 in user_positions and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 8 in user_positions and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                #   Horizontals
                        elif 4 in user_positions and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        elif 6 in user_positions and 4 in empty_positions:
                            computer_functions(4, (300, 200))
                        else:
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))                                
                            elif a == 6 and a in empty_positions:                        
                                computer_functions(6, (400, 200))                        
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))
                            elif a == 9 and a in empty_positions:                        
                                computer_functions(9, (400, 250))
        else:
            pass
        if 6 in empty_positions:
            if buttons[pygame.K_6]:
                user_functions(6, (385, 185), (415, 215), (415, 185), (385, 215))                
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        # Computer Wins
                        # Vertical Position 1
                        if 1 in computer_options and 4 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 4 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 7 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))

                        # Vertical Position 2
                        elif 2 in computer_options and 5 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 8 in computer_options and 5 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        elif 2 in computer_options and 8 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        
                        # Horizontal Position 1
                        elif 1 in computer_options and 2 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 2 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 3 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        
                        # Horizontal Position 3
                        elif 7 in computer_options and 8 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 8 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 9 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))

                        # Diagonal Position 1 to 9
                        elif 1 in computer_options and 5 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 5 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 9 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Diagonal Position 3 to 7
                        elif 3 in computer_options and 5 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 5 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 7 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Special Middle Cases
                        # For 8
                        elif len(empty_positions) == 6 and 8 in user_positions:
                            temp_choice = [3, 7, 9]
                            temp = choice(temp_choice)
                            if temp == 3:
                                computer_functions(3, (400, 150))
                            elif temp == 7:
                                computer_functions(7, (300, 250))
                            elif temp == 9:
                                computer_functions(9, (400, 250))

                        # For 2
                        elif len(empty_positions) == 6 and 2 in user_positions:
                            temp_choice = [1, 3, 9]
                            temp = choice(temp_choice)
                            if temp == 1:
                                computer_functions(1, (300, 150))
                            elif temp == 3:
                                computer_functions(3, (400, 150))
                            elif temp == 9:
                                computer_functions(9, (400, 250))

                        # Special Cases
                        elif len (empty_positions) == 8:
                            computer_functions(5, (350, 200))

                        # Other Cases
                        elif 3 in user_positions and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in user_positions and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 5 in user_positions and 4 in empty_positions:
                            computer_functions(4, (300, 200))
                        elif 4 in user_positions and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        else:
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))
                            elif a == 6 and a in empty_positions:
                                computer_functions(6, (400, 200))
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))
                            elif a == 9 and a in empty_positions:                        
                                computer_functions(9, (400, 250))
        else:
            pass
        if 7 in empty_positions:
            if buttons[pygame.K_7]:
                user_functions(7, (285, 235), (315, 265), (315, 235), (285, 265))                
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        # Computer Wins
                        # Vertical Position 2
                        if 2 in computer_options and 5 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 8 in computer_options and 5 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        elif 2 in computer_options and 8 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Vertical Position 3
                        elif 3 in computer_options and 6 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 6 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 9 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        
                        # Horizontal Position 1
                        elif 1 in computer_options and 2 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 2 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 3 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))

                        # Horizontal position 2
                        elif 4 in computer_options and 5 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        elif 6 in computer_options and 5 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))
                        elif 4 in computer_options and 6 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                    

                        # Diagonal Position 1 to 9
                        elif 1 in computer_options and 5 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 5 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 9 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                        
                            
                        # Special Cases
                        # For 2
                        elif len(empty_positions) == 6 and 2 in user_positions:
                            temp_choice = [4, 6]
                            temp = choice(temp_choice)
                            if temp == 4:
                                computer_functions(4, (300, 200))
                            elif temp == 6:
                                computer_functions(6, (400, 200))
                        # For 6
                        elif len(empty_positions) == 6 and 6 in user_positions:
                            temp_choice = [2, 8]
                            temp = choice(temp_choice)
                            if temp == 2:
                                computer_functions(2, (350, 150))
                            elif temp == 8:
                                computer_functions(8, (350, 250))

                        elif 5 in user_positions and 3 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 5 in user_positions and 3 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))

                        elif 8 in user_positions and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in user_positions and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 4 in user_positions and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in user_positions and 4 in empty_positions:
                            computer_functions(4, (300, 200))
                        elif 5 in user_positions and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in user_positions and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        
                        # Corner Cases
                        elif len(empty_positions) == 8:
                            computer_functions(5, (350, 200))
                        elif len(empty_positions) == 6 and 3 in user_positions and 5 in computer_options:
                            computer_functions(4, (300, 200))
                        else:
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))
                            elif a == 6 and a in empty_positions:                        
                                computer_functions(6, (400, 200))                        
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                                                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))
                            elif a == 9 and a in empty_positions:                        
                                computer_functions(9, (400, 250))
        else:
            pass
        if 8 in empty_positions:
            if buttons[pygame.K_8]:
                user_functions(8,  (335, 235), (365, 265), (365, 235), (335, 265))                
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                       
                        # Computer Wins
                        # Vertical Position 1
                        if 1 in computer_options and 4 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 4 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 7 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))

                        # Vertical Position 3
                        elif 3 in computer_options and 6 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 6 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 9 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        
                        # Horizontal Position 1
                        elif 1 in computer_options and 2 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 2 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 3 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))

                        # Horizontal position 2
                        elif 4 in computer_options and 5 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        elif 6 in computer_options and 5 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))
                        elif 4 in computer_options and 6 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                        

                        # Diagonal Position 1 to 9
                        elif 1 in computer_options and 5 in computer_options and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in computer_options and 5 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 9 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Diagonal Position 3 to 7
                        elif 3 in computer_options and 5 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 5 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 7 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Special Middle Cases                        
                        # For 6                        
                        elif len(empty_positions) == 6 and 6 in user_positions:
                            temp_choice = [3, 7, 9]
                            temp = choice(temp_choice)
                            if temp == 3:
                                computer_functions(3, (400, 150))
                            elif temp == 7:
                                computer_functions(7, (300, 250))
                            elif temp == 9:
                                computer_functions(9, (400, 250))

                        # For 4
                        elif len(empty_positions) == 6 and 4 in user_positions:
                            temp_choice = [1, 7, 9]
                            temp = choice(temp_choice)
                            if temp == 1:
                                computer_functions(1, (300, 150))
                            elif temp == 7:
                                computer_functions(7, (300, 250))
                            elif temp == 9:
                                computer_functions(9, (400, 250))
                            
                        # Special Cases
                        elif len (empty_positions) == 8:
                            computer_functions(5, (350, 200))
                        
                        # Other Cases
                        elif 2 in user_positions and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        elif 5 in user_positions and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        elif 7 in user_positions and 9 in empty_positions:
                            computer_functions(9, (400, 250))
                        elif 9 in user_positions and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        else:
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))
                            elif a == 6 and a in empty_positions:                        
                                computer_functions(6, (400, 200))                        
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))                                
                            elif a == 9 and a in empty_positions:                        
                                computer_functions(9, (400, 250))
        else:
            pass
        if 9 in empty_positions:
            if buttons[pygame.K_9]:
                user_functions(9,  (385, 235), (415, 265), (415, 235), (385, 265))                
                for num in first_list:
                    if num not in user_positions and num in empty_positions:
                        first_list = []
                        user_positions.append(num)
                        empty_positions.remove(num)                        
                        # Computer Wins
                        # Vertical Position 1
                        if 1 in computer_options and 4 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 4 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 7 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))

                        # Vertical Position 2
                        elif 2 in computer_options and 5 in computer_options and 8 in empty_positions:
                            computer_functions(8, (350, 250))
                        elif 8 in computer_options and 5 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))
                        elif 2 in computer_options and 8 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                
                        
                        # Horizontal Position 1
                        elif 1 in computer_options and 2 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 2 in computer_options and 1 in empty_positions:
                            computer_functions(1, (300, 150))
                        elif 1 in computer_options and 3 in computer_options and 2 in empty_positions:
                            computer_functions(2, (350, 150))

                        # Horizontal position 2
                        elif 4 in computer_options and 5 in computer_options and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        elif 6 in computer_options and 5 in computer_options and 4 in empty_positions:
                            computer_functions(4, (300, 200))
                        elif 4 in computer_options and 6 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))                            

                        # Diagonal Position 3 to 7
                        elif 3 in computer_options and 5 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in computer_options and 5 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 3 in computer_options and 7 in computer_options and 5 in empty_positions:
                            computer_functions(5, (350, 200))

                        # Special Cases
                        # For 4
                        elif len(empty_positions) == 6 and 4 in user_positions:
                            temp_choice = [2, 8]
                            temp = choice(temp_choice)
                            if temp == 2:
                                computer_functions(2, (350, 150))
                            elif temp == 8:
                                computer_functions(8, (350, 250))
                        # For 2
                        elif len(empty_positions) == 6 and 2 in user_positions:
                            temp_choice = [4, 6]
                            temp = choice(temp_choice)
                            if temp == 4:
                                computer_functions(4, (300, 200))
                            elif temp == 6:
                                computer_functions(6, (400, 200))

                        elif 5 in user_positions and 1 in computer_options and 3 in empty_positions:
                            computer_functions(3, (400, 150))
                        elif 5 in user_positions and 1 in computer_options and 7 in empty_positions:
                            computer_functions(7, (300, 250))

                        # Other Cases
                        elif 3 in user_positions and 6 in empty_positions:
                            computer_functions(6, (400, 200))
                        elif 6 in user_positions and 3 in empty_positions:
                            computer_functions(3, (400, 150))                        
                        elif 8 in user_positions and 7 in empty_positions:
                            computer_functions(7, (300, 250))
                        elif 7 in user_positions and 8 in empty_positions:
                            computer_functions(8, (350, 250))                        
                        elif 1 in user_positions and 5 in empty_positions:
                            computer_functions(5, (350, 200))
                        elif 5 in user_positions and 1 in empty_positions:
                            computer_functions(1, (300, 150))

                        # Corner Cases
                        elif len(empty_positions) == 8:
                            computer_functions(5, (350, 200))
                        elif len(empty_positions) == 6 and 1 in user_positions and 5 in computer_options:
                            computer_functions(8, (350, 250))    
                        else:
                            a = choice(empty_positions)
                            if a == 1 and a in empty_positions:
                                computer_functions(1, (300, 150))
                            elif a == 2 and a in empty_positions:
                                computer_functions(2, (350, 150))
                            elif a == 3 and a in empty_positions:
                                computer_functions(3, (400, 150))
                            elif a == 4 and a in empty_positions:
                                computer_functions(4, (300, 200))
                            elif a == 5 and a in empty_positions:
                                computer_functions(5, (350, 200))
                            elif a == 6 and a in empty_positions:                        
                                computer_functions(6, (400, 200))                        
                            elif a == 7 and a in empty_positions:
                                computer_functions(7, (300, 250))                        
                            elif a == 8 and a in empty_positions:
                                computer_functions(8, (350, 250))
        else:
            pass
    elif len(empty_positions) == 1 and winner != True:
        buttons = pygame.key.get_pressed()
        if 1 in empty_positions:
            if buttons[pygame.K_1]:
                last_move(1, (285, 135), (315, 165), (315, 135), (285, 165))            
        else:
            pass
        if 2 in empty_positions:              
            if buttons[pygame.K_2]:
                last_move(2, (335, 135), (365, 165), (365, 135), (335, 165))                 
        else:
            pass
        if 3 in empty_positions:
            if buttons[pygame.K_3]:
                last_move(3, (385, 135), (415, 165), (415, 135), (385, 165))                
        else:
            pass
        if 4 in empty_positions:
            if buttons[pygame.K_4]:
                last_move(4, (315, 185), (285, 215), (285, 185), (315, 215))                
        else:
            pass
        if 5 in empty_positions:
            if buttons[pygame.K_5]:
                last_move(5, (335, 185), (365, 215), (365, 185), (335, 215))                
        else:
            pass
        if 6 in empty_positions:
            if buttons[pygame.K_6]:
                last_move(6, (385, 185), (415, 215), (415, 185), (385, 215))                
        else:
            pass
        if 7 in empty_positions:
            if buttons[pygame.K_7]:
                last_move(7, (285, 235), (315, 265), (315, 235), (285, 265))               
        else:
            pass
        if 8 in empty_positions:
            if buttons[pygame.K_8]:
                last_move(8, (335, 235), (365, 265), (365, 235), (335, 265))                
        else:
            pass
        if 9 in empty_positions:
            if buttons[pygame.K_9]:
                last_move(9, (385, 235), (415, 265), (415, 235), (385, 265))               
        else:
            pass
    elif len(empty_positions) == 0 and winner != True:
        text_on_screen("It's A Draw", (265,300), (218,112,214))

#   Deciding the winner
    if 1 in user_positions and 2 in user_positions and 3 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))
    elif 1 in user_positions and 4 in user_positions and 7 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))        
    elif 1 in user_positions and 5 in user_positions and 9 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))                
    elif 2 in user_positions and 5 in user_positions and 8 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))              
    elif 3 in user_positions and 5 in user_positions and 7 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))               
    elif 3 in user_positions and 6 in user_positions and 9 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))                
    elif 4 in user_positions and 5 in user_positions and 6 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))                
    elif 7 in user_positions and 8 in user_positions and 9 in user_positions:
        text_on_screen('You Win!!', (280,300), (25,25,112))                
    
#   Computer
    elif 1 in computer_options and 2 in computer_options and 3 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))

    elif 1 in computer_options and 4 in computer_options and 7 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))

    elif 1 in computer_options and 5 in computer_options and 9 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))

    elif 2 in computer_options and 5 in computer_options and 8 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))

    elif 3 in computer_options and 5 in computer_options and 7 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))

    elif 3 in computer_options and 6 in computer_options and 9 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))

    elif 4 in computer_options and 5 in computer_options and 6 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))

    elif 7 in computer_options and 8 in computer_options and 9 in computer_options:
        text_on_screen('The Computer Wins!!', (200,300), (255,69,0))
    pygame.display.update()
pygame.quit()

# Installing Pygame
# python -m pip install -U pygame --user

# Updating Pip

# In command prompt
    # 1) pip --version
    # 2) python -m pip install --upgrade pip
