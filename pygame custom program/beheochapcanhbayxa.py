import pygame
from math import pi as PI


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

# Màu mới cho cánh thiên thần
GOLDEN = (255, 215, 0) 
LIGHT_GOLDEN = (255, 235, 120)

# hàm vẽ heo
def veheochapcanhbayxa(screen, x, y, scale):
    # Player and NPC bên file kia đều là 20 radius hình tròn
    radius = int(200 * scale)
    
    # heo gốc radius 300 heo mới là 20 ==> 20 / 200 = 0.1 là heo scale xuống kích cỡ 20
    # gọi hàm bên file game thì điền parameter cái scale là 0.1 thì heo gốc là 200 sẽ tự khắc biến thành 20



    # 1. VẼ CÁNH THIÊN THẦN (Vẽ trước để nằm sau đầu heo)

    #PIGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
    
    # Tọa độ các điểm cho cánh trái gồm 3 lớp lông nè
    left_wing_points = [
        (int(x - 120*scale), int(y - 50*scale)),   # Gốc cánh trên
        (int(x - 320*scale), int(y - 180*scale)),  # Lông vũ 1 cao nhất
        (int(x - 250*scale), int(y - 80*scale)),   # Điểm lõm 1
        (int(x - 350*scale), int(y - 50*scale)),   # Lông vũ 2 giữa
        (int(x - 260*scale), int(y + 20*scale)),   # Điểm lõm 2
        (int(x - 310*scale), int(y + 110*scale)),  # Lông vũ 3 thấp nhất
        (int(x - 120*scale), int(y + 80*scale))    # Gốc cánh dưới
    ]
    
    # Tọa độ các điểm mảng sáng bên trong cánh trái glowinggggg
    left_wing_inner = [
        (int(x - 140*scale), int(y - 30*scale)),
        (int(x - 280*scale), int(y - 130*scale)),
        (int(x - 220*scale), int(y - 60*scale)),
        (int(x - 300*scale), int(y - 40*scale)),
        (int(x - 230*scale), int(y + 10*scale)),
        (int(x - 260*scale), int(y + 70*scale)),
        (int(x - 140*scale), int(y + 50*scale))
    ]

    # Tọa độ các điểm cho cánh phải Đối xứng qua trục x
    right_wing_points = [
        (int(x + 120*scale), int(y - 50*scale)),   
        (int(x + 320*scale), int(y - 180*scale)),  
        (int(x + 250*scale), int(y - 80*scale)),   
        (int(x + 350*scale), int(y - 50*scale)),   
        (int(x + 260*scale), int(y + 20*scale)),   
        (int(x + 310*scale), int(y + 110*scale)),  
        (int(x + 120*scale), int(y + 80*scale))    
    ]

    right_wing_inner = [
        (int(x + 140*scale), int(y - 30*scale)),
        (int(x + 280*scale), int(y - 130*scale)),
        (int(x + 220*scale), int(y - 60*scale)),
        (int(x + 300*scale), int(y - 40*scale)),
        (int(x + 230*scale), int(y + 10*scale)),
        (int(x + 260*scale), int(y + 70*scale)),
        (int(x + 140*scale), int(y + 50*scale))
    ]

    # Vẽ khối cánh trái
    pygame.draw.polygon(screen, GOLDEN, left_wing_points)
    pygame.draw.polygon(screen, LIGHT_GOLDEN, left_wing_inner) # Viền sáng bên trong
    
    # Vẽ khối cánh phải
    pygame.draw.polygon(screen, GOLDEN, right_wing_points)
    pygame.draw.polygon(screen, LIGHT_GOLDEN, right_wing_inner)


    # đầu heo
    pygame.draw.circle(screen, PINK, (x, y), radius)

    
    #vẽ 2 chân mày giận dữ
    pygame.draw.polygon(screen, NEON,[(int(x - 150*scale), int(y - 100*scale)), (int(x - 100*scale),int(y - 150*scale)), (int(x - 50*scale), int(y - 50*scale))])

    pygame.draw.polygon(screen, NEON, [(int(x + 50*scale),int(y-50*scale)), (int(x + 100*scale), int(y - 150*scale)),(int(x + 150*scale), int(y - 100*scale))])

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

# pygame.init()
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("Test Wing Pig")
# clock = pygame.time.Clock()

# running = True

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(WHITE)

#     veheo(screen,400,300,1)

#     pygame.display.update()
#     clock.tick(144)

# pygame.quit()