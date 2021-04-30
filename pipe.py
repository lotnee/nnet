import pygame
import random
from defs import *

class Pipe():
    def __init__(self,gameDisplay,x,y,pipe_type):
        self.gameDisplay = gameDisplay
        self.state = PIPE_MOVING
        self.pipe_type = pipe_type
        self.img = pygame.image.load(PIPE_FILE)
        # reference to teh reactangle of the image
        self.rect = self.img.get_rect()
        if pipe_type == PIPE_UPPER:
            y = y - self.rect.height
        self.set_position(x, y)
        print("our pipes are moving")
    
    def set_position(self,x,y):
        self.rect.left = x
        self.rect.top = y
    def move_position(self,dx,dy):
        self.rect.centerx += dx
        self.rect.centery += dy
    def draw(self):
        self.gameDisplay.blit(self.img,self.rect)

    def check_status(self):
        if self.rect.right < 0:
            self.state = PIPE_DONE
            print('The pipe is no longer visible - moved off to the left')
    def update(self, dt):
        if self.state == PIPE_MOVING:
            #moves left
            self.move_position(-(PIPE_SPEED * dt),0)
            self.draw()
            self.check_status()

class PipeCollection():
    def __init__(self,gameDisplay):
        self.gameDisplay = gameDisplay
        self.pipes = []
    
    def add_new_pipe_pair(self,x):
        top_y = random.randint(PIPE_MIN, PIPE_MAX - PIPE_GAP_SIZE)
        bottom_y = top_y + PIPE_GAP_SIZE

        pipe1 = Pipe(self.gameDisplay,x,top_y,PIPE_UPPER)
        pipe2 = Pipe(self.gameDisplay,x,bottom_y,PIPE_LOWER)

        self.pipes.append(pipe1)
        self.pipes.append(pipe2)
    def create_new_set(self):
        self.pipes = []
        placed = PIPE_FIRST

        while placed < DISPLAY_WIDTH:
            self.add_new_pipe_pair(placed)
            placed += PIPE_ADD_GAP
    def update(self,dt):
        rightmost = 0
        for pipe in self.pipes:
            pipe.update(dt)
            if pipe.pipe_type == PIPE_UPPER:
                if pipe.rect.left > rightmost:
                    rightmost = pipe.rect.left 
        if rightmost < (DISPLAY_WIDTH - PIPE_ADD_GAP):
            self.add_new_pipe_pair(DISPLAY_WIDTH)
        self.pipes = [pipe for pipe in self.pipes if pipe.state == PIPE_MOVING]

