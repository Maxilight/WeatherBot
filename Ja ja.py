import telebot
import pygame, sys
from random import randrange

pygame.init()

RES = 700
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
print(apple)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 3
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
surface = pygame.display.set_caption('SNAKE') 
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()


def close_game():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while True:
    surface.fill((0, 0, 0))
    clock.tick(fps)
    close_game()
    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE -1, SIZE-1)) for i,j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True}
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    if snake[-1] == apple:
        x = x + 20
        y = y + 20
        apple = x, y
        pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
        close_game()
        pygame.display.update()
        print(apple)

        bot = telebot.TeleBot('6206013686:AAF7d0KhEp8KODOmotcYa0MgfJKgetI172k')

        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):

            bot.send_message(message.from_user.id, "координаты кубика компа: ")
            bot.send_message(message.from_user.id, {x})
            bot.send_message(message.from_user.id, {y})

        bot.polling(none_stop=True)


    pygame.display.flip()
