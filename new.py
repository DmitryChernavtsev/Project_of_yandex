import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

width = 800
height = 600
screen = pygame.display.set_mode((width, width))
pygame.display.set_caption('Змейка')

game_over = False

x1 = width / 2
y1 = height / 2

snake_ = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msge, color):
    mesge = font_style.render(msge, True, color)
    screen.blit(mesge, [width / 2, height / 2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_
                x1_change = 0

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    screen.fill(white)
    pygame.draw.rect(screen, black, [x1, y1, snake_, snake_])

    pygame.display.update()

    clock.tick(snake_speed)

message("Вы проиграли", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()