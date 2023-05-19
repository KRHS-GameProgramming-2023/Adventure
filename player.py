import pygame, sys,math

class Player():
    def __init__(self, speed=5,pos=[40,60]):
        self.imageStand = pygame.image.load("player/images/stand.png")
        self.imageRight = pygame.image.load("player/images/right.png")
        self.imageLeft = pygame.image.load("player/images/left.png")
        self.image=self.imageStand 
        self.rect = self.image.get_rect(center=pos)
        self.maxspeed=speed
        self.speedx=0
        self.speedy=0
        self.speed=[self.speedx, self.speedy]
        
        self.kind="player"

        
    def move(self):
        self.speed=[self.speedx, self.speedy]
        self.rect=self.rect.move(self.speed)
        print("moving",self.speed)
        
    def go(self,direction):
        print(direction)
        if direction == "right":
            self.speedx = self.maxspeed
            self.image=self.imageRight
        elif direction == "left":
            self.speedx = -self.maxspeed
            self.image=self.imageLeft
            
            
        elif direction == "sright":
            self.speedx = 0
            self.image=self.imageStand
        elif direction == "sleft":
            self.speedx = 0
            self.image=self.imageStand
        print(self.speedx)
        
    def wallCollide(self,size):
        if self.rect.bottom > size[1]:
            self.speedy = -self.speedy
            self.move()
            self.speedy=0
        if self.rect.top < 0:
            self.speedy = -self.speedy
            self.move()
            self.speedy=0
            
        if self.rect.right > size[0]:
            self.speedx = -self.speedx
            self.move()
            self.speedx=0
        if self.rect.left < 0:
            self.speedx = -self.speedx
            self.move()
            self.speedx=0
