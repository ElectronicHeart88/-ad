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

GREYHON = (180,180,180)

SANDCOLOR = (246,220,189)
PIGGYPLAYER = (255,0,110)
BLUE = (0,0,255)
BULLETCOLOR = (255,100,0)
GREENZOMBI = (0,200,0)
RED = (255,0,0)


GREY = (180,180,180)
BLACK = (255,255,255 )
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


PINK_cute = (255,0,110)
PINK = (255,182,193)
BLACK = (0,0,0)
WHITE = (255,255,255)
PINKY = (255,105,180)
GREY = (128,128,128)
BLUSH_CHEEK = (232,199,200)

KOBIKDATTENMAUGINUAHET = (174,154,98)


# hàm vẽ zombie
def vezom(screen, x, y, scale):
    # Player and NPC bên file kia đều là 20 radius hình tròn

    radius = int(200 * scale)
    
    # heo gốc radius 300 heo mới là 20 ==> 20 / 200 = 0.1 là heo scale xuống kích cỡ 20
    # gọi hàm bên file game thì điền parameter cái scale là 0.1 thì heo gốc là 200 sẽ tự khắc biến thành 20

    # đầu zombie
    pygame.draw.circle(screen, GREENZOMBI, (x, y), radius)

    # mắt
    pygame.draw.circle(screen, BLACK, (int(x-60*scale), int(y-20*scale)), int(20*scale))
    pygame.draw.circle(screen, BLACK, (int(x+60*scale), int(y-20*scale)), int(20*scale))

    # miệng đỏ tròn
    pygame.draw.circle(screen, RED, (x, int(y+60*scale)), int(30*scale))


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

#     screen.fill(WHITE)

#     # vẽ zombie
#     vezom(screen,400,300,0.2)

#     pygame.display.update()
#     clock.tick(144)

# pygame.quit()