from pygame import *

Width = 800
Height = 600
TILE = 32

window = display.set_mode((Width, Height))
display.set_caption('Танчики')

clock = time.Clock()
FPS = 60

Directs = [[0, -1], [1, 0], [0, 1], [-1, 0]]


class Tank():
    def __init__(self, color, px, py, direct, KeyList):
        object1.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = Rect(px, py, TILE,TILE)
        self.direct = direct
        self.moveSpeed = 2

        self.keyLEFT = KeyList[0]
        self.keyRIGHT = KeyList[1]
        self.keyUP = KeyList[2]
        self.keyDOWN = KeyList[3]
        self.keySHOT = KeyList[4]
    
    def update(self):
        if keys(self.keyLEFT):
            self.rect.x -= self.moveSpeed
            self.direct = 3
        if keys(self.keyRIGHT):       
            self.rect.x += self.moveSpeed
            self.direct = 1
        if keys(self.keyUP):
            self.rect.y -= self.moveSpeed
            self.direct = 0
        if keys(self.keyLEFT):
            self.rect.y += self.moveSpeed
            self.direct = 2

    def draw(self):
        draw.rect(window, self.color, self.rect)
        
        x = self.rect.centerx + Directs[self.direct][0]*30
        y = self.rect.centery + Directs[self.direct][1]*30
        draw.line(window, (255, 255, 255), self.rect.center, (x, y), 4)

object1 = []
Tank((255,255,255), 100, 275, 0, (K_a, K_d, K_w, K_s, K_SPACE))

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            def update(self):
                if keys(self.keyLEFT):
                    self.rect.x -= self.moveSpeed
                    self.direct = 3
                if keys(self.keyRIGHT):
                    self.rect.x += self.moveSpeed
                    self.direct = 1
                if keys(self.keyUP):
                    self.rect.y -= self.moveSpeed
                    self.direct = 0
                if keys(self.keyLEFT):
                    self.rect.y += self.moveSpeed
                    self.direct = 2
        

    keys = key.get_pressed()
    print(object1)
    window.fill((0,0,0))
    for obj in object1:
        obj.draw()

    display.update()
    clock.tick(FPS)

