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
HEAVYCRIMSON = (230, 10, 40)
RED =   (244, 67, 54)
REDD =  (183, 28, 28)
LittleRED = (255, 205, 210)
REDBRIGHT =  (255, 50, 50) 

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


# hàm vẽ heo 
# hàm này là hàm căn theo biến scaling dựa vào X Y là tâm của đường tròn và offset left right 2 con mắt, chứ cái hàm gốc file gốc là static nên nếu import qua game là nó bị bự
def veheoanimationkhidangshoot(screen, x, y, scale):

    # Player and NPC bên file kia đều là 20 radius hình tròn
    radius = int(200 * scale)
    # heo gốc radius 300 heo mới là 20 ==> 20 / 200 = 0.1 là heo scale xuống kích cỡ 20
    # gọi hàm bên file game thì điền parameter cái scale là 0.1 thì heo gốc là 200 sẽ tự khắc biến thành 20

    # đầu heo
    # đầu heo là cái phần bự nhất lấy X Y của cái hàm này luôn là 400 300 cái
    pygame.draw.circle(screen, PINK, (x, y), radius)

    pygame.draw.circle(screen,REDBRIGHT, (x, y), radius,8)
    

    # mắt
    pygame.draw.circle(screen, BLACK, (int(x-70*scale), int(y-20*scale)), int(20*scale))
    pygame.draw.circle(screen, BLACK, (int(x+70*scale), int(y-20*scale)), int(20*scale))

    # highlight mắt
    pygame.draw.circle(screen, WHITE, (int(x-76*scale), int(y-26*scale)), int(6*scale))
    pygame.draw.circle(screen, WHITE, (int(x+64*scale), int(y-26*scale)), int(6*scale))
    

    #vẽ 2 chân mày giận dữ
    pygame.draw.polygon(screen, CRIMSON,[(int(x - 150*scale), int(y - 100*scale)), (int(x - 100*scale),int(y - 150*scale)), (int(x - 50*scale), int(y - 50*scale))])

    pygame.draw.polygon(screen, CRIMSON, [(int(x + 50*scale),int(y-50*scale)), (int(x + 100*scale), int(y - 150*scale)),(int(x + 150*scale), int(y - 100*scale))])


    # 2 tai trái and phải 
    pygame.draw.polygon(screen, PINKY,[(int(x-150*scale), int(y-135*scale)), (int(x-130*scale), int(y-230*scale)),(int(x-50*scale), int(y-180*scale))])

    pygame.draw.polygon(screen, PINKY,[(int(x+50*scale), int(y-180*scale)), (int(x+125*scale), int(y-230*scale)),  (int(x+150*scale), int(y-135*scale))])

    # mũi
    pygame.draw.ellipse(screen,PINK_cute,
        (int(x-60*scale), int(y+30*scale), int(120*scale), int(80*scale)))

    pygame.draw.circle(screen, BLACK, (int(x-20*scale), int(y+70*scale)), int(10*scale))
    pygame.draw.circle(screen, BLACK, (int(x+20*scale), int(y+70*scale)), int(10*scale))


    # vẽ miệng căn X là giữa tâm đường tròn ngay giữa face, y là lệch xuống so vs tâm 150 pixel xún dưới vertically

    # vòm miệng ngoài màu đen là nòng súng miệng
    pygame.draw.circle(screen, BLACK,(x,int(y+150*scale)),(int(40*scale)))

    # vòm miệng bên trong màu vàng 
    pygame.draw.circle(screen, BULLETCOLOR,(x,int(y+150*scale)), (int(30*scale)))
    # cục đỏ ở giữa
    pygame.draw.circle(screen,HEAVYCRIMSON, (x,int(y+150*scale)), int(20*scale))


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

#     veheoanimationkhidangshoot(screen,400,300,1)

#     pygame.display.update()
#     clock.tick(144)

# pygame.quit()