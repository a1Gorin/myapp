import pygame
from os import path


def check(x1, y1, x2, y2, db1, db2): # функция проверяет, было ли столкновение двух объектов
    if x1 > x2-db1 and x1 < x2+db2 and y1 > y2 - db1 and y1 < y2+db2: # один квадратик вошел в другой квадратик
        return 1 # то есть пересеклись
    else:
        return 0


pygame.init() # инициализация библиотеки 

window = pygame.display.set_mode((400, 400)) # создание окна и его размер
screen = pygame.Surface((400, 400)) # создание бэкграунда и такие же размеры
player = pygame.Surface((40,40)) # Создание персонажа
zet = pygame.Surface((40,40)) # Создание цели, куда стрелять
arrow = pygame.Surface((20,40)) # стрела
count = 0 # переменная, для кол-ва очков

zet.set_colorkey((0,0,0))
player.set_colorkey((255,255,255))

img_zet = pygame.image.load('zet.png')
img_arrow = pygame.image.load('arrow.png')
img_player = pygame.image.load('player.png')


myfont = pygame.font.SysFont('Arial', 15) # генерируем шрифт, в скобочках рамзер и навзание

a_x = 1000
a_y = 1000

strike = False

z_x = 0
z_y = 0

x_p = 0
y_p = 360

right = True # логические переменные(для того, чтобы двигать)


done = False # для того чтобы создать игровой цикл, нужно создать переменную для выхода
while done == False:
    for e in pygame.event.get(): # перебор всех событий, которые происходят в игре
        if e.type  == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s: # научим двигаться персонажа, для этого будем обрабатывать события нажатием на е клавишу
            y_p += 12
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            y_p -= 12
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            x_p -= 12
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            x_p += 12
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if strike == False:
                strike = True # если стрела еще не выпущена
                a_x = x_p # отображаем стрелу над головой персонажа
                a_y = y_p - 40


    if strike: # Логика двжиения стрелы
        a_y -= 0.5
        if a_y < 0:
            strike = False
            a_y = 1000
            a_x = 1000


    if check(a_x, a_y, z_x, z_y, 20, 40): # попадание по нашей цели: сначала координаты стрелы, потом координаты цели и указываем ширину
        count += 1
        strike = False
        a_y = 1000
        a_x = 1000

    if right: # Логика двжиения  в право
        z_x += 0.2
        if z_x > 400:
            z_x -= 0.2
            right = False
    else: # Логика двжиения влево
        z_x -= 0.2
        if z_x < 0:
            z_x += 0.2
            right = True

    string = myfont.render('points: ' +str(count), 0, (0,0,0)) # генерируем надпись для игрового цикла и ее цвет
    screen.fill((255,255,0)) # закрашиваем фон и отображаем на окно
    zet.blit(img_zet, (0,0))
    arrow.blit(img_arrow, (0,0))
    player.blit(img_player, (0,0))
    screen.blit(string,(0,50)) # отображаем надпись(чуть ниже цели)
    screen.blit(player,(x_p, y_p)) # отображаем на задний фон(бэкграунд) и там же координаты, координаты задаем перменной
    screen.blit(zet,(z_x,z_y))
    screen.blit(arrow,(a_x, a_y)) # отображаем стрелу
    window.blit(screen, (0, 0)) #отобразить на окно наш бэкграунд
    pygame.display.update()

    
pygame.quit() # выход
