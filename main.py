import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],]

title_size = 32
TITLE = 32
green = (18, 115, 16)

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
class Character:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = "character"

        self.color = color
        self.rect = pygame.Rect(px, py, TITLE, TITLE)
        self.direct = direct
        self.moveSpeed = 2

        self.boomSpeed = 5
        self.boomDamage = 1

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]
        self.keySHIFT = keyList[5]

    def update(self):
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        if keys[self.keySHOT]:
            dx = DIRECTS[self.direct][0] * 30
            dy = DIRECTS[self.direct][1] * self.boomSpeed
            Boom(self, self.rect.x, self.rect.y, dx, dy, self.boomDamage)


    def draw(self):
        pygame.draw.rect(window, self.color, self.rect,)
        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 4)

class Boom:
    def __init__(self, parent, px, py, dx, dy, damage):
        booms.append(self)
        self.parent = parent
        self.px = px
        self.py = py
        self.dx, self.dy = dx, dy
        self.damage = damage
        self.rect = pygame.Rect(px, py, TITLE, TITLE)


    def update(self):
        self.px += self.dx
        self.py += self.dy

    def draw(self):
        pygame.draw.rect(window, 'red', (self.px, self.py, TITLE, TITLE), 2)


booms = []
objects = []


Character('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE, pygame.K_LSHIFT))

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    for obj in objects:
        obj.update()
    for boom in booms:
        boom.update()

    window.fill(green)
    for row in range(len(world)):
        for col in range(len(world[row])):
            x = col * title_size
            y = row * title_size
            if world[row][col] == 1:
                pygame.draw.rect(window, 'gray', (x, y, title_size, title_size))

    for obj in objects:
        obj.draw()

    for boom in booms:
        boom.draw()

    pygame.display.update()
    clock.tick(FPS)