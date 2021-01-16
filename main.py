import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SNAKE by ANUKUL')

# position of snake
x_position = 100
y_position = 100
length_of_snake = 20
change_in_x = 0
change_in_y = 0

score_value = 0

# loading image of snake
rotate_image = pygame.image.load('snake.png')

# position of food
food_x = random.randint(10, 500)
food_y = random.randint(10, 500)

# loading images
food_img = pygame.image.load('orange.png')

# loading game over text
over_font = pygame.font.SysFont(None, 100)
over_text = over_font.render('GAME OVER', True, (200, 0, 0))


# movement of snake
def movement_of_snake():
    # rotate_image = pygame.transform.scale(snake_image,(length_of_snake,24))
    screen.blit(rotate_image, (x_position, y_position))


def movement_of_food(food_x, food_y):
    screen.blit(food_img, (food_x, food_y))


def collisons(x_position, y_position, food_x, food_y):
    distance2 = math.sqrt(math.pow(x_position - food_x, 2)) + math.sqrt(math.pow(y_position - food_y, 2))
    if distance2 < 20:
        return True


def game_over_text():
    screen.blit(over_text, (100, 300))


running = True
while running:
    screen.fill((200, 200, 200))
    s_font = pygame.font.SysFont(None, 40)
    s_text = s_font.render(f'score:{score_value}', True, (0, 200, 0))
    screen.blit(s_text, (480, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                change_in_x = 0.3
                change_in_y = 0
            if event.key == pygame.K_RIGHT:
                # rotate_image = pygame.transform.rotate(pygame.image.load('snake.png'), 90)
                # screen.blit(rotate_image,(x_position,y_position))
                rotate_image = pygame.transform.rotate(pygame.image.load('snake.png'), -180)

                change_in_x = 0.3
                change_in_y = 0

            if event.key == pygame.K_LEFT:
                # screen.blit(rotate_image,(x_position,y_position))
                rotate_image = pygame.transform.rotate(pygame.image.load('snake.png'), 0)

                change_in_x = -0.3
                change_in_y = 0
            if event.key == pygame.K_UP:
                # rotate_image = pygame.transform.rotate(pygame.image.load('snake.png'), 90)
                # screen.blit(rotate_image, (x_position, y_position))
                rotate_image = pygame.transform.rotate(pygame.image.load('snake.png'), 90)

                change_in_y = -0.3
                change_in_x = 0

            if event.key == pygame.K_DOWN:
                # rotate_image = pygame.transform.rotate(pygame.image.load('snake.png'), -90)
                # screen.blit(rotate_image, (x_position, y_position))
                rotate_image = pygame.transform.rotate(pygame.image.load('snake.png'), -90)

                change_in_y = 0.3
                change_in_x = 0

    if x_position <= 0 or y_position >= 576 or x_position >= 576 or y_position <= 0:
        change_in_x = 0
        change_in_y = 0
        game_over_text()

    x_position += change_in_x
    y_position += change_in_y

    movement_of_food(food_x, food_y)

    if collisons(x_position, y_position, food_x, food_y):
        food_x = random.randint(10, 500)
        food_y = random.randint(10, 500)
        score_value += 1
        length_of_snake += 8
        # rotate_image = pygame.transform.scale(pygame.image.load('snake.png'), (length_of_snake, 24))
    movement_of_snake()

    pygame.display.update()
