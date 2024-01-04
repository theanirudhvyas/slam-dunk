#!/usr/bin/env python3
import pygame

screen = pygame.display.set_mode((500, 500))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("red")
    pygame.display.flip()
