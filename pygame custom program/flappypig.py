
import pygame
from random import randint
import math

# nhập hàm vẽ bé heo lúc bình thường 
from beheochapcanhbayxa import veheochapcanhbayxa

# # nhập hàm vẽ bé heo lúc bay lên

# from beheoanimationchapcanhbaylentren import veheoanimationchapcanhbaylentren

# # nhập hàm vẽ bé heo lúc bay xún dưới ó 
# from beheoanimationchapcanhbayxunduoi import veheoanimationchapcanhbayxunduoi


# khởi tạo hệ thống sound
pygame.init()
pygame.mixer.init()


ThemeNhac = ["musik and sounddd/Graze the Roof (In-Game) - Laura Shigihara (youtube).wav", "musik and sounddd/Loonboon (In-Game) - Laura Shigihara (youtube) copy.wav"]
ThemeNow = 0

pygame.mixer.music.load(ThemeNhac[ThemeNow])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

piggyalive = True
deathsound = False
die_sound = pygame.mixer.Sound("musik and sounddd/PIGGYDEATH.wav")
die_sound.set_volume(0.5)


# khởi tạo game cute :3
    
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Pig')

running = True


# #sound effect hịu ứng âm thanh
# shootsound = pygame.mixer.sound("shoot.wav")


#các màu


GREEN = (0,200,0)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
YELLOW= (255,255,0)

GREY = (180,180,180)
SANDCOLOR = (246,220,189)
PIGGYPLAYER = (255,0,110)
BLUE = (0,0,255)
BULLETCOLOR = (255,100,0)
GREENZOMBI = (0,200,0)
PURPLE = (120, 81, 169) 
aaa    = (100,100,100)
YELLOWlow = (226, 154, 63)
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

# FONT
FONTTITLEDAUTIEN = "arquitecta"
FONTNUTBAMVAOGAME = "Pratt Pro"
FONTSCORE = "Bierstadt"


TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 150

tube1_x = 600
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

Pig_X = 50
Pig_y = 400
Pig_WIDTH = 20
Pig_HEIGHT = 20

Pig_drop_velocity=0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont('sans', 20)

tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False

# nềnheo = pygame.image.load("Vuonheocute")



while running:		
	screen.fill(GREEN)
	# screen.blit(nềnheo, (0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:	
			if event.key == pygame.K_SPACE:
				# reset lại nếu mà bấm nhảy lên 1 lần thì cái velocity nó reset lại = 0 and gravity cx rì sét
				if pausing:
					Pig_y = 400
					TUBE_VELOCITY = 3
					tube1_x = 600
					tube2_x = 800
					tube3_x = 1000
					score = 0
					pausing = False

				Pig_drop_velocity = 0	
				Pig_drop_velocity -= 6.5

	# Draw tube
	tube1_rect = pygame.draw.rect(screen,BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
	tube2_rect = pygame.draw.rect(screen,BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))	
	tube3_rect = pygame.draw.rect(screen,BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

	# Draw tube inverse
	tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP))
	tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - TUBE_GAP))
	tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - TUBE_GAP))

	# move tube to the left
	tube1_x = tube1_x - TUBE_VELOCITY
	tube2_x = tube2_x - TUBE_VELOCITY
	tube3_x = tube3_x - TUBE_VELOCITY

	# draw sand
	sand_rect = pygame.draw.rect(screen, YELLOW, (0,550,400,50))

	# draw Pigggg

	# pig_X và pig_y đang đóng vai trò là tâm của bé heo
	veheochapcanhbayxa(screen, Pig_X, int(Pig_y), 0.1) 

	# kín tạo hít box cho bé heo 
	# Vì heo scale 0.1 (từ 200) nên bán kính đầu heo là 20. Khung va chạm sẽ là 30x30
	# Trừ đi 20 để hitbox nằm ngay chính giữa tâm của đầu heo.
	hitbox_x = Pig_X - 20
	hitbox_y = int(Pig_y - 20)
	# Hit box x là tâm của bé heo x cái tâm mà dựa để vẽ hình tròn heo á, trừ đi 20, tương tự với y nhưng y là thay đổi giá trị mạnh nên phải cast sang integ để render hít bóc
	Pig_rect = pygame.Rect(hitbox_x, hitbox_y, 23, 23)
	+
	pygame.draw.rect(screen,PINK,Pig_rect,1)
	# Pig falls cho toạ độ Y bé heo cộng bằng tốc độ rớt của bé heo VÀ VẬN TỐC RỚT BÉ HEO SẼ + THÊM GRAVITY THEO TIME CHO TỚI KHI DC BẤM SPACE LẦN NỮA BAY LÊN MỚI RESET !!
	Pig_y += Pig_drop_velocity
	Pig_drop_velocity += GRAVITY

	# tạo mấy cái ống đối lập nè :)
	if tube1_x < -TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(100,400)
		tube1_pass = False	
	if tube2_x < -TUBE_WIDTH:
		tube2_x = 550	
		tube2_height = randint(100,400)	
		tube2_pass = False	
	if tube3_x < -TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(100,400)	
		tube3_pass = False	


	score_txt = font.render("Score: " + str(score), True, BLACK)
	screen.blit(score_txt, (5,5))

	# ucập nhật cái số điểm dựa trên vị trí X của cái gốc trên tube cộng với widht của tub mà bé heo vượt qua được 
	if tube1_x + TUBE_WIDTH <= Pig_X and tube1_pass == False:
		score += 1 
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= Pig_X and tube2_pass == False:
		score += 1 
		tube2_pass = True
	if tube3_x + TUBE_WIDTH <= Pig_X and tube3_pass == False:
		score += 1 
		tube3_pass = True

	# check collision
	for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv, sand_rect]:
		if Pig_rect.colliderect(tube):
			pausing = True
			TUBE_VELOCITY = 0
			Pig_drop_velocity = 0
			game_over_txt = font.render("Game over, score: " + str(score), True, BLACK)
			screen.blit(game_over_txt, (200,300))
			press_space_txt = font.render("Press Space to Continue", True, BLACK)
			screen.blit(press_space_txt, (200,400))

    
	clock.tick(60)
	pygame.display.flip()
	pygame.display.update()
pygame.quit()