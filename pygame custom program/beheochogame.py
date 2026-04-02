import pygame
from math import pi as PI

pygame.init()

# màu
PINK_cute = (255,0,110)
PINK = (255,182,193)
BLACK = (0,0,0)
WHITE = (255,255,255)
PINKY = (255,105,180)
GREY = (128,128,128)

GREY = (180,180,180)
SANDCOLOR = (246,220,189)
PIGGYPLAYER = (255,0,110)
BLUE = (0,0,255)
BULLETCOLOR = (255,100,0)
GREENZOMBI = (0,200,0)
PURPLE = (120, 81, 169) 
aaa    = (100,100,100)
YELLOW = (226, 154, 63)
NEON = ( 223, 255, 0)
TimOaiHuong = (200,160,255)
TIMMACDINH = (128,0,128)
TIMDARK = (75,0,130)
HEALTH = (200,0,80)


CRIMSON = (220, 20, 60)
RED =   (244, 67, 54)
REDD =  (183, 28, 28)
LittleRED = (255, 205, 210)

BLUE = (227, 242, 253)
BLUEER = (66, 165, 245)
BLUEeeer = (25, 118, 210)
BLUEEST = (13, 71, 161)

KOBIKDATTENMAUGINUAHET = (174,154,98)

# hàm vẽ heo
def veheo(screen, x, y, scale):
    # Player and NPC bên file kia đều là 20 radius hình tròn
    radius = int(200 * scale)
    
    # heo gốc radius 300 heo mới là 20 ==> 20 / 200 = 0.1 là heo scale xuống kích cỡ 20
    # gọi hàm bên file game thì điền parameter cái scale là 0.1 thì heo gốc là 200 sẽ tự khắc biến thành 20

    # đầu heo
    pygame.draw.circle(screen, PINK, (x, y), radius)

    # mắt
    pygame.draw.circle(screen, BLACK, (int(x-70*scale), int(y-20*scale)), int(20*scale))
    pygame.draw.circle(screen, BLACK, (int(x+70*scale), int(y-20*scale)), int(20*scale))

    # highlight mắt
    pygame.draw.circle(screen, WHITE, (int(x-76*scale), int(y-26*scale)), int(6*scale))
    pygame.draw.circle(screen, WHITE, (int(x+64*scale), int(y-26*scale)), int(6*scale))

    # tai
    pygame.draw.polygon(screen, PINKY,
        [(int(x-150*scale), int(y-135*scale)),
         (int(x-130*scale), int(y-230*scale)),
         (int(x-50*scale), int(y-180*scale))])

    pygame.draw.polygon(screen, PINKY,
        [(int(x+50*scale), int(y-180*scale)),
         (int(x+125*scale), int(y-230*scale)),
         (int(x+150*scale), int(y-135*scale))])

    # mũi
    pygame.draw.ellipse(screen,PINK_cute,
        (int(x-60*scale), int(y+30*scale), int(120*scale), int(80*scale)))

    pygame.draw.circle(screen, BLACK, (int(x-20*scale), int(y+70*scale)), int(10*scale))
    pygame.draw.circle(screen, BLACK, (int(x+20*scale), int(y+70*scale)), int(10*scale))

    # miệng
    pygame.draw.arc(screen, BLACK,
        (int(x-66*scale), int(y+124*scale), int(120*scale), int(80*scale)),
        0, PI, int(4*scale))


# # phần này để file tự chạy dc 
# WIDTH = 800
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# clock = pygame.time.Clock()

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((255,255,255))

#     veheo(screen,400,300,0.2)

#     pygame.display.update()
#     clock.tick(144)

# pygame.quit()