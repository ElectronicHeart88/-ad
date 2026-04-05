
import pygame
import random
import math

# nhập hàm vẽ bé heo

from beheochogame import veheo

# nhập hàm vẽ bé heo lúc bắn 

from beheoshootanimationchogame import veheoanimationkhidangshoot

# nhập hàm vẽ bé zom

from bezomchogame import vezom

# khởi tạo hệ thống sound
pygame.init()
pygame.mixer.init()


ThemeNhac = ["musik and sounddd/Graze the Roof (In-Game) - Laura Shigihara (youtube).wav", "musik and sounddd/Loonboon (In-Game) - Laura Shigihara (youtube) copy.wav"]
ThemeNow = 0

pygame.mixer.music.load(ThemeNhac[ThemeNow])
pygame.mixer.music.set_volume(100)
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



# #sound effect hịu ứng âm thanh
# shootsound = pygame.mixer.sound("shoot.wav")


#các màu
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

# FONT
FONTTITLEDAUTIEN = "arquitecta"
FONTNUTBAMVAOGAME = "Pratt Pro"
FONTSCORE = "Bierstadt"

# vẽ logo trái tim máu 

def draw_heart(surface, x, y, size=6):


    pygame.draw.rect(surface,HEALTH,(x,y,size,size))
    pygame.draw.rect(surface,HEALTH,(x+size,y,size,size))

    pygame.draw.rect(surface,HEALTH,(x,y+size,size*2,size))

    pygame.draw.rect(surface,HEALTH,(x+size/2,y+size*2,size,size))


# khởi tạo thanh máu 
pig_health = 10


# ấn định tốc độ chug cho lúc đầu 
speed = 2
ACCELERATION = 10
# đang tính làm cái acceleration tăng tốc dần sau khi chạy, acceleration = true, while acceleration thì speed = speed + 1 tăng theo mỗi tick xí xí ? 

# ấn định người chơi heo cute vị trí ban đầu
heo_x = 400
heo_y = 300

# ấn định căn cứ heo

base_x = 200
base_y = 520

# khởi tạo con zombie cute


zombies = [] 
for zombie in range(10):
    zombies.append([random.randint(50,750), random.randint(50,300)])

# khởi tạo danh sách+ đạn cute bắn zom
bullets = []





def nutvaogamesauhover(LOBBYSCREEN):
     pygame.draw.rect(LOBBYSCREEN,TIMDARK,(300,250,200,80),1)

def nutvaogametruochover(LOBBYSCREEN):
    pygame.draw.rect(LOBBYSCREEN,TimOaiHuong,(300,250,200,80),1)
 

class MainLobbyMenuCute:

    def __init__(self):

        self.button = pygame.Rect(300, 250, 200, 80)

        self.font = pygame.font.SysFont(FONTTITLEDAUTIEN, 40)

        self.small_font = pygame.font.SysFont(FONTNUTBAMVAOGAME, 20)

        self.color = TimOaiHuong
        self.LOBBYSCREEN = screen

    def draw_GUI_lobby(self,LOBBYSCREEN):

        LOBBYSCREEN.fill(NEON)

        title = self.font.render("PIGGY FIGHT ZOMBIE ", True, (PIGGYPLAYER))

        LOBBYSCREEN.blit(title,(230,90))

        pygame.draw.rect(LOBBYSCREEN,TimOaiHuong,self.button)

        text = self.small_font.render("FIGHT NOW !", True, (0,0,0))

        LOBBYSCREEN.blit(text, (370,280))

    def bamnutvaogame(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            maox, maoy = pygame.mouse.get_pos()


            if self.button.collidepoint(maox,maoy):
                 color = TIMDARK
                 return True
            else:
                color = TimOaiHuong
                return False
            
        
    def nutvaogametruochover(self, LOBBYSCREEN):
    # TRẠNG THÁI BÌNH THƯỜNG: Chỉ là một khối màu tím oải hương đặc (không có số 1 ở cuối)
    pygame.draw.rect(LOBBYSCREEN, TimOaiHuong, (300, 250, 200, 80))

    def nutvaogamesauhover(self, LOBBYSCREEN):
    # TRẠNG THÁI HOVER: Đổi sang màu TÍM DARK (đặc) và thêm VIỀN ĐEN
    # 1. Vẽ nền tím dark đặc
    pygame.draw.rect(LOBBYSCREEN, TIMDARK, (300, 250, 200, 80))
    # 2. Vẽ thêm cái viền đen bao quanh (độ dày 3 cho rõ nét)
    pygame.draw.rect(LOBBYSCREEN, BLACK, (300, 250, 200, 80), 3)

    def hoverchobamnutvaogame(self):
            maox, maoy = pygame.mouse.get_pos()

            if (maox >= 300 and maox <= 500) and (maoy >= 250 and maoy <= 330):
                nutvaogamesauhover(self.LOBBYSCREEN)
            else:
                nutvaogametruochover(self.LOBBYSCREEN)

    


    
    # cho ban đầu là nút vào game chính sẽ màu tím có viền đen nếu hover là ra màu hồng nhạt

# mouse = pygame.mouse.get_pos()

# if self.button.collidepoint(mouse):
#     color = (150,255,150)   # sáng hơn
# else:
#     color = (100,200,100)

# pygame.draw.rect(screen, color, self.button)

# set điểm score

fontscore = pygame.font.SysFont(None, 30,True,True)
score = 0
textscore = fontscore.render(f"Score: {score}", True, (0,0,0))
screen.blit(textscore, (650,10))

menulobby = MainLobbyMenuCute()


# CHẠY LUN LUN ĐÚM
running = True

# cục menu

game_started = False

# TROG LÚC CHẠY lặp
while running:

    # add cái cục mới cho menu game
    if not game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if menulobby.bamnutvaogame(event):
                game_started = True

        screen.fill(NEON)
        
        menulobby.draw_GUI_lobby(screen)

        menulobby.hoverchobamnutvaogame()
            
        pygame.display.update()
        clock.tick(144)
        continue   
    

        # vẽ mần hình game CHÍNH !!
    screen.fill((SANDCOLOR))
        
        # event chính
    for event in pygame.event.get():

            if menulobby.bamnutvaogame(event):
                game_started = True

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_e:

                    heo_body = pygame.Rect(heo_x,heo_y,30,30)
                    nha = pygame.Rect(base_x+220,base_y,80,50)

                    if heo_body.colliderect(nha):
                        
                        zombierect= not zombierect

        # cơ chế bắn bấm chuột
    if event.type == pygame.MOUSEBUTTONDOWN:
            
            pigshoot = True
            if pigshoot == True:
                veheoanimationkhidangshoot(screen,400,300,0.1)

            maox,maoy = pygame.mouse.get_pos()

            dx = maox - heo_x
            dy = maoy - heo_y

            length = math.sqrt(dx*dx + dy*dy)

            dx /= length
            dy /= length

            bullets.append([heo_x,heo_y,dx,dy])



    # di chuyển 4 hướng
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        heo_y -= speed

    if keys[pygame.K_s]:
        heo_y += speed

    if keys[pygame.K_a]:
        heo_x -= speed

    if keys[pygame.K_d]:
        heo_x += speed


    # AI zombie tự di chuyển
    for zombie in zombies:

        dx = heo_x - zombie[0]
        dy = heo_y - zombie[1]

        dist = math.sqrt(dx*dx + dy*dy)

        if dist != 0:
            
            zombie[0] += dx/dist * 1.1
            zombie[1] += dy/dist * 1.1


    # di chuyển đạn
    for bullet in bullets:
        bullet[0] += bullet[2] * 10
        bullet[1] += bullet[3] * 10


    # tính điểm bắn hitbox
    
    for bullet in bullets:
        
        bulletrect = pygame.Rect(bullet[0],bullet[1],6,6)

        for zombie in zombies:

            zombierect = pygame.Rect(zombie[0],zombie[1],30,30)


            if bulletrect.colliderect(zombierect):

                zombies.remove(zombie)
                
                bullets.remove(bullet)

                score = score + 1 
                break
    

        # kiến tạo thanh máuuu 
    # Vẽ 10 trái tim rỗng nền xám để contrast dễ nhìn
    for i in range(10):
        draw_heart(screen, 10 + i * 20, 10, size=4) # Dùng màu GREY 

    # Vẽ số máu hiện tại đè lên (màu đỏ)
    for hp in range(pig_health):
        draw_heart(screen, 10 + hp * 20, 10, size=4) # size=4 và cách nhau 20px sẽ dễ nhìn hơn
    
    # for hp in range(pig_health) :
    #     draw_heart(screen,10+hp*5,10)




    # Zombie cắn Heo die
    if PiggyHitbox.colliderect(zombierect):
        if pig_health > 0:
            pig_health -= 1 # Trừ máu
        else:
            piggyalive = False

    # phát theme nhạc lặp 
    if not pygame.mixer.music.get_busy():
        ThemeNow = (ThemeNow + 1) % len(ThemeNhac)
        pygame.mixer.music.load(ThemeNhac[ThemeNow])
        pygame.mixer.music.play()

    
    if not piggyalive and not deathsound:
        die_sound.play()
        deathsound = True

    
    # vẽ cái base
    pygame.draw.rect(screen,GREY,(base_x,base_y,300,50))
    pygame.draw.rect(screen,BLUE,(base_x+220,base_y,80,50))


    # vẽ ng chs bằng cái circle bình thường trog file game này ( obsolete rồi vứt đi :)) 

    # pygame.draw.circle(screen,PIGGYPLAYER,(heo_x,heo_y),20,0)
    
    #vẽ người chơi xài hàm mặt heo hôm trước 
    PiggyPlayer = veheo(screen, heo_x, heo_y, 0.1)

    # canh hitbox cục vuông hình tròn nên trừ 15 qua trái xíu trừ 15 lên trên, width height là 25 đủ bọc cái con heo player là 20 !!
    
    PiggyHitbox = pygame.Rect(heo_x - 15, heo_y - 15, 25, 25)
    
    PiggyPlayer.collide

    # vẽ cái hitbox lên ? 
    pygame.draw.rect(screen, (255,0,0), PiggyHitbox,1)

    # vẽ tạo hình zom
    for zombie in zombies:
     pygame.draw.circle(screen,GREENZOMBI,(zombie[0],zombie[1]),10,0)

    #  vẽ zom = hàm import 

    # for zombie in zombies: 

    #     vezom(screen,(zombie[0],zombie[1],0.1))

    # tạo đạn

    for bullet in bullets:
        pygame.draw.circle(screen,BULLETCOLOR,(int(bullet[0]),int(bullet[1])),4)

# cập nhật màn hình liên tục và llock fps 144 
    pygame.display.update()
    clock.tick(144)
    continue

# thêm joystick nữa
def themdieukhiencontroller():
    pygame.joystick.init
pass

# nếu pro thì thêm delta time : dt = clock.tick( whatever the fuck FPS is ) / 10000 
# cái này để lock fps lại và tính theo second dù framerate có high thì physics trog game render vẫn theo time}