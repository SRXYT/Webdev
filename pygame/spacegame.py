from os import system
import pygame, random, math

from pygame.event import wait

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

background = pygame.image.load('BG.jpg')

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('Enemy.png')
enemyX = 370
enemyY = 50
enemyX_change = 0

def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))

def enemy(enemyX, enemyY):
    screen.blit(enemyImg, (enemyX, enemyY))

run = True
while run:
    screen.blit(background, (0, 0))
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            print("A key is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5      
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX+=playerX_change
    pygame.display.update()