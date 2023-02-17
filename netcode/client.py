from telnetlib import NOP
import pygame



WIDTH = 500
HEIGHT = 500



win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

client_number = 0

class Player():
    def __init__(self, x, y, width, height, color, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = vel

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            self.x -= self.vel
            print("left")

        if keys_pressed[pygame.K_RIGHT]:
            self.x += self.vel
            print("right")

        if keys_pressed[pygame.K_UP]:
            self.y -= self.vel
            print("up")

        if keys_pressed[pygame.K_DOWN]:
            self.y += self.vel
            print("down")

        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(win, player):

    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()


def main():
    P1 = Player(50,50,100,100,(0,255,0),2)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        P1.move()
        redrawWindow(win, P1)


main()