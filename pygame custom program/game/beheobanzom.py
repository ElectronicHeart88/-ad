import pygame
import random
import math


# khởi tạo game cute :3
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GREY = (180,180,180)
BLACK = (255,255,255 )
SANDCOLOR = (246,220,189)
PIGGYPLAYER = (255,0,110)
BLUE = (0,0,255)
BULLETCOLOR = (255,100,0)
GREENZOMBI = (0,200,0)

# ấn định người chơi cute vị trí ban đầu

heo_x = 400

heo_y = 300

speed = 5

# ấn định căn cứ heo
base_x = 200
base_y = 520
train_moving = False

# khởi tạo con zombie cute

zombies = [] 

for i in range(5):
    zombies.append([random.randint(50,750), random.randint(50,300)])



# khởi tạo danh sách+ đạn cute bắn zom
bullets = []

running = True

while running:

    # vẽ mần hình lên
    screen.fill((SANDCOLOR))
    
    # event chính
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:

                heo_body = pygame.Rect(heo_x,heo_y,30,30)
                cabin_rect = pygame.Rect(train_x+220,train_y,80,50)

                if heo_body.colliderect(cabin_rect):
                    train_moving = not train_moving

        # cơ chế bắn bấm chuột
        if event.type == pygame.MOUSEBUTTONDOWN:

            maox,maoy = pygame.mouse.get_pos()

            dx = maox - heo_x
            dy = maoy - heo_y

            length = math.sqrt(dx*dx + dy*dy)

            dx /= length
            dy /= length

            bullets.append([heo_x,heo_y,dx,dy])



    # MOVEMENT
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        heo_y -= speed

    if keys[pygame.K_s]:
        heo_y += speed

    if keys[pygame.K_a]:
        heo_x -= speed

    if keys[pygame.K_d]:
        heo_x += speed


    # TRAIN MOVE
    if train_moving:
        train_x += train_speed
    pass 

    # AI zombie tự di chuyển
    for zombie in zombies:

        dx = heo_x - zombie[0]
        dy = heo_y - zombie[1]

        dist = math.sqrt(dx*dx + dy*dy)

        if dist != 0:

            zombie[0] += dx/dist * 1.2
            zombie[1] += dy/dist * 1.2


    # di chuyển đạn
    for bullet in bullets:
        bullet[0] += bullet[2] * 10
        bullet[1] += bullet[3] * 10


    # tính điểm bắn
    for bullet in bullets:
        bulletrect = pygame.Rect(bullet[0],bullet[1],6,6)

        for zombie in zombies:

            zombierect = pygame.Rect(zombie[0],zombie[1],30,30)

            if bulletrect.colliderect(zombierect):

                zombies.remove(zombie)
                bullets.remove(bullet)
                break


    # vẽ cái train
    pygame.draw.rect(screen,GREY,(base_x,base_y,300,50))
    pygame.draw.rect(screen,BLUE,(base_x+220,base_y,80,50))


    # vẽ ng chs
    pygame.draw.circle(screen,PIGGYPLAYER,(heo_x,heo_y),20,0)


    # vẽ tạo hình zom
    for zombie in zombies:
        pygame.draw.rect(screen,GREENZOMBI,(zombie[0],zombie[1],30,30))


    # tạo đạn

    for bullet in bullets:
        pygame.draw.circle(screen,BULLETCOLOR,(int(bullet[0]),int(bullet[1])),4)


# end 
    pygame.display.update()
    clock.tick(144)