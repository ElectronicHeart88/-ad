import pygame
import math
from random import randint


# bắt đầu game Màn hình hall chính

pygame.init()


game_choosen = False


WIDTH = 800
HEIGHT = 600

fps = pygame.time.Clock()
MainHall = pygame.display.set_mode((WIDTH, HEIGHT))


# các màu
GREY = (180, 180, 180)
BLACK = (0, 0, 0)
SANDCOLOR = (246, 220, 189)
PIGGYPLAYER = (255, 0, 110)
BLUE = (0, 0, 255)
BULLETCOLOR = (255, 100, 0)
GREENZOMBI = (0, 200, 0)
PURPLE = (120, 81, 169)
aaa = (100, 100, 100)
YELLOW = (226, 154, 63)
NEON = (223, 255, 0)
TimOaiHuong = (200, 160, 255)
TIMMACDINH = (128, 0, 128)
TIMDARK = (75, 0, 130)
HEALTH = (200, 0, 80)

CRIMSON = (220, 20, 60)
RED = (244, 67, 54)
REDD = (183, 28, 28)
LittleRED = (255, 205, 210)

BLUE = (227, 242, 253)
BLUEER = (66, 165, 245)
BLUEeeer = (25, 118, 210)
BLUEEST = (13, 71, 161)

KOBIKDATTENMAUGINUAHET = (174, 154, 98)

# FONT
FONTTITLEDAUTIEN = "arquitecta"
FONTSUBTITLE = "Bierstadt"
FONTNUTBAMCHONGAME = "Pratt Pro"

font_title = pygame.font.SysFont(FONTTITLEDAUTIEN, 50, bold=True)
font_subtitle = pygame.font.SysFont(FONTTITLEDAUTIEN, 30)
font_button = pygame.font.SysFont(FONTNUTBAMCHONGAME, 25)


def NUTCHONGAME1TRUOCHOVER(HALLSCREEN):
    pygame.draw.rect(HALLSCREEN, TimOaiHuong, (300, 200, 200, 80), 1)


def NUTCHONGAME1SAUHOVER(HALLSCREEN):
    pygame.draw.rect(HALLSCREEN, TIMDARK, (300, 200, 200, 80), 1)


def NUTCHONGAME2TRUOCHOVER(HALLSCREEN):
    pygame.draw.rect(HALLSCREEN, TimOaiHuong, (300, 300, 200, 80), 1)


def NUTCHONGAME2SAUHOVER(HALLSCREEN):
    pygame.draw.rect(HALLSCREEN, TIMDARK, (300, 300, 200, 80), 1)


class MainHallMenuCute:

    def __init__(self):

        self.color = TimOaiHuong
        self.HALLSCREEN = MainHall

        # Tạo 2 nút bấm ở vị trí khác nhau same trục X chỉ khác trục y hihiiihihi
        self.btn_game1 = pygame.Rect(300, 200, 200, 80)
        self.btn_game2 = pygame.Rect(300, 300, 200, 80)

        self.color1 = TimOaiHuong
        self.color2 = TIMMACDINH

    def draw_GUI_HALL(self, HALLSCREEN):

        HALLSCREEN.fill(NEON)

        # vẽ tiêu đề của game hall
        title = font_title.render("WELCOME TO PIGGY FRANCHISE", True, PIGGYPLAYER)
        # tiêu đề nhỏ hơn kêu chọn game :)
        subtitle = font_subtitle.render("CHOOSE YOUR GAME !!", True, BLACK)

        HALLSCREEN.blit(title, (230, 90))
        HALLSCREEN.blit(subtitle, (230, 120))

        # Vẽ Nút Game 1
        pygame.draw.rect(HALLSCREEN, TimOaiHuong, self.btn_game1)
        txt1 = font_button.render("FLAPPY PIG", True, YELLOW)
        HALLSCREEN.blit(txt1, (320, 220))

        # Vẽ Nút Game 2
        pygame.draw.rect(HALLSCREEN, TIMMACDINH, self.btn_game2)
        txt2 = font_button.render("PIGGY SHOOTER", True, HEALTH)
        HALLSCREEN.blit(txt2, (340, 220))

        HALLText = self.small_font.render("CHOOSE YOUR GAME !", True, (0, 0, 0))

        HALLSCREEN.blit(HALLText, (370, 280))

    def BAMNUTCHONGAME(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            maox, maoy = pygame.mouse.get_pos()

            if self.button.collidepoint(maox, maoy):
                color = TIMDARK
                return True
            else:
                color = TimOaiHuong
                return False
        return False

    def HOVERCHOBAMNUTCHONGAME(self):
        maox, maoy = pygame.mouse.get_pos()

        if (maox >= 300 and maox <= 500) and (maoy >= 250 and maoy <= 330):
            NUTCHONGAMESAUHOVER(self.HALLSCREEN)
        else:
            NUTCHONGAMETRUOCHOVER(self.HALLSCREEN)


menuhall = MainHallMenuCute()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # add cái cục mới cho menu game
    if not game_choosen:
        if menuhall.BAMNUTCHONGAME(event):
            game_choosen = True
            if event.type == pygame.QUIT:
                running = False

    if menuhall.BAMNUTCHONGAME(event):

        game_choosen = True

        menuhall.HALLSCREEN.fill(CRIMSON)

        menuhall.draw_GUI_HALL(MainHall)

    pygame.display.update()
    fps.tick(144)
    continue
