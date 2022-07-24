import pygame, math

black = (0, 0, 0)
green = (0, 122, 0)
grey = (80, 80, 80)

WIDTH = 1000
HEIGHT = 650

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

i = 0
check = 1

clock = pygame.time.Clock()
FPS = 60

speed = 10


class Car(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, size, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(3.5 * size, size))
        self.rect = self.image.get_rect(bottomright=(WIDTH, HEIGHT - 94))
        self.x = self.rect.x - 350
        self.y = self.rect.y - 80

class Light(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, size, path, dist):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(2 * size, 2 * size))
        self.rect = self.image.get_rect(bottomright=(WIDTH, HEIGHT))
        self.x = self.rect.x + dist
        self.y = self.rect.y - 166

def draw_wheel(r, i, point_x, point_y):
    angle = i * 3.14 / 180
    a = (r * math.cos(angle)) + point_x
    b = (r * math.sin(angle))  + point_y
    a1 = (r * -math.cos(angle)) + point_x
    b1 = (r * -math.sin(angle))  + point_y

    a2 = (r * -math.cos(angle)) + point_y
    b2 = (r * math.sin(angle))  + point_x
    a3 = (r * math.cos(angle)) + point_y
    b3 = (r * -math.sin(angle))  + point_x

    pygame.draw.line(screen, grey, (int (a), int (b)), (int(a1), int (b1)), 6)
    pygame.draw.line(screen, grey, (int (b2), int (a2)), (int(b3), int (a3)), 6)


def car_move(i):
    global check
    if i % 200 == 0:
        if check == 1:
            check = 0
            car.y += 5
        else:
            check = 1
            car.y -= 5

def light_move(speed, x):
    x -= speed
    if x < -200:
        x = 1110
    return x

background = pygame.image.load("./img/fone.png")
background = pygame.transform.scale(background,size)
car = Car(WIDTH, HEIGHT, 100, './img/car.png')
light1 = Light(WIDTH, HEIGHT, 100, './img/light.png', 0)
light2 = Light(WIDTH, HEIGHT, 100, './img/light.png', 450)
light3 = Light(WIDTH, HEIGHT, 100, './img/light.png', 900)
screen.blit(background, [0,0])

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(light1.image, (light1.x, light1.y))
    screen.blit(light2.image, (light2.x, light2.y))
    screen.blit(light3.image, (light3.x, light3.y))
    screen.blit(car.image, (car.x, car.y))
    pygame.draw.circle(screen, (0, 0, 0), (375, 455), 30)
    pygame.draw.circle(screen, (0, 0, 0), (584, 458), 26)

    car_move(i)
    light1.x = light_move(speed, light1.x)
    light2.x = light_move(speed, light2.x)
    light3.x = light_move(speed, light3.x)

    draw_wheel(25, i, 375, 455)
    draw_wheel(21, i, 584, 458)
    
    i += speed
    
    pygame.display.update()