import pygame
from defs import *
from pipe import PipeCollection
from bird import BirdCollection
def update_label(data,title,font,x,y,gameDisplay):
    # the 1 makes antialiasing available
    label = font.render('{} {}'.format(title,data),1,DATA_FONT_COLOR)
    gameDisplay.blit(label,(x,y))
    return y

def update_data_labels(gameDisplay,dt,game_time,num_iterations,num_alive,font):
    y_pos = 10
    gap = 20
    x_pos = 10
    y_pos = update_label(round(1000/dt,2), 'FPS', font, x_pos, y_pos+gap, gameDisplay)
    y_pos = update_label(round(game_time/1000,2), 'Game Time', font, x_pos, y_pos+gap, gameDisplay)
    y_pos = update_label(num_iterations, 'Iterations', font, x_pos, y_pos+gap, gameDisplay)
    y_pos = update_label(num_alive, 'Alive Birbs', font, x_pos, y_pos+gap, gameDisplay)



def start_game():
    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
    pygame.display.set_caption('learn to fly')
    label_font = pygame.font.SysFont("monospace", DATA_FONT_SIZE)
    
    background = pygame.image.load(BG_FILE)
    pipes = PipeCollection(gameDisplay)
    pipes.create_new_set()
    birds = BirdCollection(gameDisplay)
    running = True
    num_iterations = 1
    #creates the pipe here
    clock = pygame.time.Clock()
    dt = 0
    game_time = 0
    while running:
        # draws the background
        dt = clock.tick(FPS)
        game_time += dt
        gameDisplay.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
        
        pipes.update(dt)
        num_alive = birds.update(dt,pipes.pipes)
        if num_alive == 0 or (num_alive >= 1 and game_time >= 8000 and num_alive <6):
            pipes.create_new_set()
            game_time = 0
            birds.evolve_population()
            num_iterations += 1
        print("tjhe game time is",game_time)

        update_data_labels(gameDisplay, dt, game_time,num_iterations,num_alive, label_font)
        pygame.display.update()
        
        




if __name__ == '__main__':
    start_game()