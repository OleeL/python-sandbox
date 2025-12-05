import math
import pygame
from pygame import Rect

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

MY_NAME = "OLI"

x, y = 320, 240
speed = 200  # pixels per second
running = True

print(pygame.font.get_default_font())
my_font = pygame.font.SysFont(pygame.font.get_default_font(), 30)

def py_process(clock):
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return (dt, True)
    return (dt, False)

def input_handling(speed, dt, playerPos):
    (x, y) = playerPos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed * dt
    if keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_UP]:
        y -= speed * dt
    if keys[pygame.K_DOWN]:
        y += speed * dt
    return (x, y)

time = 0

def draw(screen, playerPosition, dt):
    global time
    (x, y) = playerPosition
    color = (20, 20, 30)
    screen.fill(color)
    (w, h) = (40, 40)
    
    time = time + dt
    text_to_render = 'Time alive '+str(math.floor(time))+"s"
    text_surface = my_font.render(text_to_render, True, (255, 255, 255))
    screen.blit(text_surface, (0,0))
    
    pygame.font.init()
    pygame.draw.rect(
        screen,
        (200, 60, 60),
        Rect(
            int(x)-(w * 0.5),
            int(y)-(h * 0.5),
            w,
            h
        )
    )
    pygame.display.flip()

while running:
    (dt, shouldQuit) = py_process(clock)
    if shouldQuit:
        running = False
    x, y = input_handling(speed, dt, (x, y))
    draw(screen, (x, y), dt)

pygame.quit()
