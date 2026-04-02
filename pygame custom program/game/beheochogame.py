import pygame
from math import pi as PI

# màu
PINK_cute = (255,0,110)
PINK = (255,182,193)
BLACK = (0,0,0)
WHITE = (255,255,255)
PINKY = (255,105,180)
GREY = (128,128,128)
BLUSH_CHEEK = (232,199,200)

def draw_pig(screen, x, y, scale=1):

    r = int(200 * scale)

    # đầu heo
    pygame.draw.circle(screen, PINK, (x, y), r)

    # mắt
    pygame.draw.circle(screen, BLACK, (x-70*scale, y-20*scale), int(20*scale))
    pygame.draw.circle(screen, BLACK, (x+70*scale, y-20*scale), int(20*scale))

    # highlight mắt
    pygame.draw.circle(screen, WHITE, (x-76*scale, y-26*scale), int(6*scale))
    pygame.draw.circle(screen, WHITE, (x+64*scale, y-26*scale), int(6*scale))

    # tai
    pygame.draw.polygon(screen, PINKY,
        [(x-150*scale, y-135*scale),
         (x-130*scale, y-230*scale),
         (x-50*scale, y-180*scale)])

    pygame.draw.polygon(screen, PINKY,
        [(x+50*scale, y-180*scale),
         (x+125*scale, y-230*scale),
         (x+150*scale, y-135*scale)])

    # lông mày
    pygame.draw.polygon(screen, GREY,
        [(x-150*scale,y-100*scale),
         (x-100*scale,y-150*scale),
         (x-50*scale,y-50*scale)])

    pygame.draw.polygon(screen, GREY,
        [(x+50*scale,y-50*scale),
         (x+100*scale,y-150*scale),
         (x+150*scale,y-100*scale)])

    # mũi
    pygame.draw.ellipse(screen,PINK_cute,
        (x-60*scale, y+30*scale, 120*scale, 80*scale))

    pygame.draw.circle(screen, BLACK, (x-20*scale, y+70*scale), int(10*scale))
    pygame.draw.circle(screen, BLACK, (x+20*scale, y+70*scale), int(10*scale))

    # miệng
    pygame.draw.arc(screen, BLACK,
        (x-66*scale, y+124*scale, 120*scale, 80*scale),
        0, PI, int(4*scale))