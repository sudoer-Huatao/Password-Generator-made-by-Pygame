# Password generator
import pygame
from random import randint


TITLE = "Password Generator"
WIDTH = 400
HEIGHT = 400
green = (0, 255, 0)
rect_pos = (100, 100)
character_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_", "+", "[", "]", "{", "}", ";", ":", "'", ",", ".", "<", ">", "/"]
password = []
surface = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont("freesanbold.ttf", 55)

def draw():
    start = pygame.draw.rect(surface, green, pygame.Rect(10, 10, 380, 380))
    text1 = font.render("Generate Password", True, (255, 165, 0))
    textRect1 = text1.get_rect()
    textRect1.center = (200, 200)
    surface.blit(text1, textRect1)

def generate_password():
    pass_length = randint(8, 15)
    for character in range(pass_length):
        password.append(character_list[randint(0, (len(character_list)-1))])
    final_password = "".join(password)
    print("Password:", final_password)

def update_password():
    password.clear()

def on_mouse_down(pos, button):
    update_password()
    generate_password()

draw()
