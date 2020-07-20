import pygame
import random
import time
num1 = pygame.image.load('1-1.png')
num2 = pygame.image.load('1-2.png') 
num3 = pygame.image.load('1-3.png')
num4 = pygame.image.load('1-4.png') 
num5 = pygame.image.load('1-5.png')
num6 = pygame.image.load('1-6.png')
dice1_set = [num1, num2, num3, num4, num5, num6]
dice2_set = [num1, num2, num3, num4, num5, num6]
SPACE_COUNTER = 0

users = open('/Users/Humayra/Documents/PYGAME/dice_game/users.txt', 'r+')

class player:
    def __init__(self, name, x, y, diceSet, score=0):
        self.name = name
        self.x = x
        self.y = y
        self.rollCount = 0
        self.rollDice = False
        self.score = score
        self.set = diceSet

    def draw_dice(self, win):
        if self.rollCount + 1 >= 18:
            self.rollDice = False
            self.rollCount = 0

        elif self.rollDice:
            random.shuffle(self.set)
            win.blit(self.set[self.rollCount//3], (self.x,self.y))
            self.rollCount += 1

        elif not self.rollDice:
            win.blit(self.set[0], (self.x,self.y))
        
    def new_score(self):
        if self.set[0] == num1:
            self.score += 1
        elif self.set[0] == num2:
            self.score = self.score + 2
        elif self.set[0] == num3:
            self.score = self.score + 3
        elif self.set[0] == num4:
            self.score = self.score + 4
        elif self.set[0] == num5:
            self.score = self.score + 5
        elif self.set[0] == num6:
            self.score = self.score + 6

    def winner(self):
        winner_text = font.render(self.name + " is the winner with " + str(self.score) + " points!", 1, (0,200,0))
        win.blit(winner_text, (100, 500))
        pygame.display.update()
        
def existing_username():
    username = input("Enter your username: ")
    username = username.capitalize()
    with open('/Users/Humayra/Documents/PYGAME/dice_game/users.txt') as users:
        if username in users.read():
            print(f"Welcome back {username.capitalize()}!")
            return username.capitalize()
        else:
            print("That is not an existing username.")

def create_username():
    username = input("Enter a new username: ")
    username = username.capitalize()
    with open('/Users/Humayra/Documents/PYGAME/dice_game/users.txt', 'a') as users:
        users.write("\n")
        users.write(username.capitalize())
        print(f"Welcome {username.capitalize()}! You now have a username.")
    return username.capitalize()

def draw():
    draw_text = font.render("Oh no! It is a draw :(", 1, (200,0,0))
    win.blit(draw_text, (100, 500))
    pygame.display.update()

def redraw_window():
    win.fill((255,255,255))
    player1.draw_dice(win)
    player2.draw_dice(win)
    player1_score_text = font.render(player1.name + "'s Score: " + str(player1.score), 1, (0,0,0))
    player2_score_text = font.render(player2.name + "'s  Score: " + str(player2.score), 1, (0,0,0))
    win.blit(player1_score_text, (10,10))
    win.blit(player2_score_text, (350,10))
    pygame.display.update()

player1_name = input("PLAYER ONE: Do you have an account? (y/n) ")
if player1_name.lower() == "y":
   player1_name = existing_username()
elif player1_name.lower()  == 'n':
   player1_name = create_username()

player2_name = input("PLAYER TWO: Do you have an account? (y/n) ")
if player2_name.lower() == "y":
   player2_name = existing_username()
elif player2_name.lower() == 'n':
   player2_name = create_username()

pygame.init()

win = pygame.display.set_mode((600,600))

pygame.display.set_caption("Dice game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("comic sans", 30, True, False)
player1 = player(player1_name, 160, 230, dice1_set)
player2 = player(player2_name, 340, 230, dice2_set)
run = True
while run:
    clock.tick(18)
    redraw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and SPACE_COUNTER < 5:
                player1.rollDice = True
                player2.rollDice = True
                if SPACE_COUNTER >= 1:
                    player1.new_score()
                    player2.new_score()
                SPACE_COUNTER +=1

    if SPACE_COUNTER == 5:
        if player1.score > player2.score:
            player1.winner()
        elif player2.score > player1.score:
            player2.winner()
        else:
            draw()

pygame.quit()

users.close()