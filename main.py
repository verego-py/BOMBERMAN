import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,],
         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
         [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2,],
         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
         [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2,],
         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
         [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2,],
         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
         [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2,],
         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
         [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2,],
         [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,],
         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,],]

title_size = 32
TITLE = 32
green = (18, 115, 16)

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]


class Bomb:
    def __init__(self, color, px, py):
        objects.append(self)
        self.type = "character"

        self.color = color
        self.rect = pygame.Rect(px, py, 25, 25)
        self.moveSpeed = 3
        self.hp = 1

        self.shotTimer = 0
        self.shotDelay = 60
        self.boomSpeed = 5
        self.boomDamage = 1


    def update(self):
        if self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * 30
            dy = DIRECTS[self.direct][1] * self.boomSpeed
            Boom(self, self.rect.x, self.rect.y, dx, dy, self.boomDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0:
            self.shotTimer -= 1

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect,)
        x = self.rect.centerx + DIRECTS[self.direct][0] * 20
        y = self.rect.centery + DIRECTS[self.direct][1] * 20
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
             objects.remove(self)


class Character:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = "character"

        self.color = color
        self.rect = pygame.Rect(px, py, 25, 25)
        self.direct = direct
        self.moveSpeed = 3
        self.hp = 1

        self.shotTimer = 0
        self.shotDelay = 60
        self.boomSpeed = 5
        self.boomDamage = 1

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]
        self.keySHIFT = keyList[5]

    def update(self):
        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        if keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        if keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        if keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects:
            if obj != self:
                if self.rect.colliderect(obj.rect):
                    self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * 30
            dy = DIRECTS[self.direct][1] * self.boomSpeed
            Boom(self, self.rect.x, self.rect.y, dx, dy, self.boomDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0:
            self.shotTimer -= 1


    def draw(self):
        pygame.draw.rect(window, self.color, self.rect,)
        x = self.rect.centerx + DIRECTS[self.direct][0] * 20
        y = self.rect.centery + DIRECTS[self.direct][1] * 20
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
             objects.remove(self)


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
        if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
            booms.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    booms.remove(self)
                    break

    def draw(self):
        pygame.draw.rect(window, 'red', (self.px, self.py, TITLE, TITLE), 2)


class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(window, 'gray', self.rect)
        pygame.draw.rect(window, 'black', self.rect, 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)


class HardBlock:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 99999

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(window, 'gray', self.rect)
        pygame.draw.rect(window, 'black', self.rect, 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)


booms = []
objects = []


Character('blue', 32, 32, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE, pygame.K_LSHIFT))



for row in range(len(world)):
    for col in range(len(world[row])):
        x = col * title_size
        y = row * title_size
        if world[row][col] == 1:
            Block(x, y, title_size)
        if world[row][col] == 2:
            HardBlock(x, y, title_size)


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
    # for row in range(len(world)):
    #     for col in range(len(world[row])):
    #         x = col * title_size
    #         y = row * title_size
    #         if world[row][col] == 1:
    #             Block(x, y, title_size)

    for obj in objects:
        obj.draw()

    for boom in booms:
        boom.draw()

    pygame.display.update()
    clock.tick(FPS)
