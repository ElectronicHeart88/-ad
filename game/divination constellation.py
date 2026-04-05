import pygame

import pygame
import sys

pygame.init()

# màn hình chính
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fortune Teller Divinationnnn")

# màu
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (200, 200, 200)
BLUE = (100, 150, 255)

SANDCOLOR = (246,220,189)
PIGGcolor = (255,0,110)
BLUEblue = (0,0,255)
BULLETCOLOR = (255,100,0)
GREENZOMBI = (0,200,0)
PURPLE = (120, 81, 169) 
aaa    = (100,100,100)
YELLOW = (226, 154, 63)
NEON = ( 223, 255, 0)
TimOaiHuong = (200,160,255)
TIMMACDINH = (128,0,128)
TIMDARK = (75,0,130)

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

# setup font
font = pygame.font.SysFont("arial", 24)

# cái phần cho người ta điền vô
class InputBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        txt_surface = font.render(self.text, True, WHITE)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))


# ===== BUTTON CLASS =====
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
        txt_surface = font.render(self.text, True, WHITE)
        screen.blit(txt_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False


# ===== CREATE UI ELEMENTS =====
name_box = InputBox(200, 100, 200, 40)
dob_box = InputBox(200, 160, 200, 40)

predict_button = Button(200, 230, 200, 50, "Predict")

result_text = "Your result will appear here..."

# ===== MAIN LOOP =====
clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)

    # Labels
    screen.blit(font.render("Enter Your Name:", True, WHITE), (100, 110))
    screen.blit(font.render("Enter Your Birth Date (dd/mm/yyyy):", True, WHITE), (100, 170))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        name_box.handle_event(event)
        dob_box.handle_event(event)

        if predict_button.is_clicked(event):
            # Placeholder logic
            result_text = f"Hello {name_box.text}, your future is bright ✨"

    # Draw UI
    name_box.draw(screen)
    dob_box.draw(screen)
    predict_button.draw(screen)

    # Output
    result_surface = font.render(result_text, True, WHITE)
    screen.blit(result_surface, (100, 320))

    pygame.display.flip()
    clock.tick(60)
