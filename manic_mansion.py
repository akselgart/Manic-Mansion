import pygame as pg
import random

WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60

pg.init()

pg.display.set_caption('Manic Mansion')

minplus = [-1,1]

surface = pg.display.set_mode(SIZE)

clock = pg.time.Clock()

run = True
poeng = 0

font = pg.font.SysFont("Arial", 32)

def vis_poeng(tekst):
    textImg = font.render(tekst, True, BLACK)
    surface.blit(textImg, (15, 15))

class Objekt:
    def __init__(self):
        self.w = 40
        self.h = 40
        
    def tegn(self):
        pg.draw.rect(surface, self.farge, (self.x,self.y,self.w,self.h))
    
    def beveg_x(self):
        self.x += self.vx
    
    def beveg_y(self):
        self.y += self.vy

class Spiller(Objekt):
    def __init__(self):
        super().__init__()
        self.farge = GREEN
        self.x = 100-(self.w/2)
        self.y = (HEIGHT/2)-(self.h/2)
        self.bare = False
        

class Spokelse(Objekt):
    def __init__(self):
        super().__init__()
        self.farge = BLUE
        self.vx = minplus[random.randint(0,1)] * 4
        self.vy = minplus[random.randint(0,1)] * 2
        self.x = random.randint(250,750)
        self.y = random.randint(0,HEIGHT-self.h)

class Hindring(Objekt):
    def __init__(self):
        self.farge = BLACK
        self.w = random.randint(40,80)
        self.h = random.randint(40,80)
        self.x = random.randint(250,750-self.w)
        self.y = random.randint(0,HEIGHT-self.h)

class Sau(Objekt):
    def __init__(self):
        super().__init__()
        self.farge = RED
        self.x = random.randint(800, 1000-self.w)
        self.y = random.randint(0, 600-self.h)
        
        
    

spiller = Spiller()
hindringer = [Hindring(), Hindring(), Hindring()]
sauer = [Sau(),Sau(),Sau()]
spokelser = [Spokelse()]



while run:
    clock.tick(FPS)
    
    keys = pg.key.get_pressed()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    surface.fill(WHITE)
    
    pg.draw.rect(surface, BLACK, (200,0,5,600))
    pg.draw.rect(surface, BLACK, (795,0,5,600))
    
    if keys[pg.K_RIGHT]:
        if spiller.bare == False:
            spiller.vx = 5
        else:
            spiller.vx = 2.5
        spiller.beveg_x()
    if keys[pg.K_LEFT]:
        if spiller.bare == False:
            spiller.vx = -5
        else:
            spiller.vx = -2.5
        spiller.beveg_x()
    if keys[pg.K_DOWN]:
        if spiller.bare == False:
            spiller.vy = 3
        else:
            spiller.vy = 1.5
        spiller.beveg_y()
    if keys[pg.K_UP]:
        if spiller.bare == False:
            spiller.vy = -3
        else:
            spiller.vy = -1.5
        spiller.beveg_y()
    
    if spiller.x >= WIDTH-spiller.w:
        spiller.x = WIDTH-spiller.w
    if spiller.x <= 0:
        spiller.x = 0
    if spiller.y >= HEIGHT-spiller.h:
        spiller.y = HEIGHT-spiller.h
    if spiller.y <= 0:
        spiller.y = 0
    
    if spiller.bare == True:
        spiller.farge = RED
        if spiller.x <= 195-spiller.w:
            spiller.bare = False
            spiller.farge = GREEN
            spokelser.append(Spokelse())
            hindringer.append(Hindring())
            sauer.append(Sau())
            poeng += 1
    
    spiller.tegn()
    
    
    for spokelse in spokelser:
        spokelse.tegn()
        spokelse.beveg_x()
        spokelse.beveg_y()
        
        if spokelse.y <= spiller.y <= spokelse.y + spokelse.h and spokelse.x <= spiller.x <= spokelse.x + spokelse.w:
            run = False
        if spokelse.y <= spiller.y+spiller.h <= spokelse.y + spokelse.h and spokelse.x <= spiller.x <= spokelse.x + spokelse.w:
            run = False
        if spokelse.y <= spiller.y <= spokelse.y + spokelse.h and spokelse.x <= spiller.x+spiller.w <= spokelse.x + spokelse.w:
            run = False
        if spokelse.y <= spiller.y+spiller.h <= spokelse.y + spokelse.h and spokelse.x <= spiller.x+spiller.w <= spokelse.x + spokelse.w:
            run = False
    
    
        if spokelse.x >= 795-spokelse.w or spokelse.x <= 205:
            spokelse.vx *= -1
        if spokelse.y >= 600-spokelse.h or spokelse.y <= 0:
            spokelse.vy *= -1
    
    for hindring in hindringer:
        hindring.tegn()
        
        if hindring.y <= spiller.y <= hindring.y + hindring.h and hindring.x <= spiller.x <= hindring.x + hindring.w:
            run = False
        if hindring.y <= spiller.y+spiller.h <= hindring.y + hindring.h and hindring.x <= spiller.x <= hindring.x + hindring.w:
            run = False
        if hindring.y <= spiller.y <= hindring.y + hindring.h and hindring.x <= spiller.x+spiller.w <= hindring.x + hindring.w:
            run = False
        if hindring.y <= spiller.y+spiller.h <= hindring.y + hindring.h and hindring.x <= spiller.x+spiller.w <= hindring.x + hindring.w:
            run = False
        
    for sau in sauer:
        sau.tegn()
        
        
        if spiller.bare == False:
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                sau.x = -WIDTH
                spiller.bare = True
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                sau.x = -WIDTH
                spiller.bare = True
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                sau.x = -WIDTH
                spiller.bare = True
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                sau.x = -WIDTH
                spiller.bare = True
                
        elif spiller.bare == True:
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                run = False
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x <= sau.x + sau.w:
                run = False
            if sau.y <= spiller.y <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                run = False
            if sau.y <= spiller.y+spiller.h <= sau.y + sau.h and sau.x <= spiller.x+spiller.w <= sau.x + sau.w:
                run = False
        
            
    vis_poeng(f"Poeng: {poeng}")
    pg.display.flip()
    
    
pg.quit()
print(f"Du endte med {poeng} poeng")




