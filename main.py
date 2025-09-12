import pygame as py 
import random

screen_w =  1600
screen_h =  1000



screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("ball ") 
clock  = py.time.Clock()

balls = []

colors = [(250,250,250), (250, 0, 250), (0, 250, 0), (0,250, 250), (0,0,250), (150, 150, 0), (230, 40, 69), (57, 67, 123) ]



class Ball:

    def __init__(self, position):
        self.position = list(position)

        self.velocity = 0
        self.gravity = 9.81
        self.mass = 2
        self.color = random.choice(colors)

        self.counter = 0
    



    def physcis(self):
        fg = self.mass* self.gravity
    

    


        if self.is_coliding():
            self.position[1] = 820
            self.velocity *= -.9

    

        self.velocity += fg 


        self.position[1] += self.velocity * 0.1


        


    def is_coliding(self):
        if self.position[1] >= 820:
            return True

        return False
    


    def draw(self, screen):
        py.draw.circle(screen, self.color, self.position, 30, 0)


    
    def timer(self):
        self.counter += 1
        return self.counter < 500



def rectangle():

    dimensions = [10, 850, 1500, 120] 

    py.draw.rect(screen, (250,250,250), dimensions, 1)


def spawn_ball(x, y):
    balls.append(Ball((x,y)))




running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False

        if event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            spawn_ball(mouse_x, mouse_y)


    screen.fill((0, 0, 0)) 

    rectangle()



    for ball in balls:
        ball.physcis()
        ball.draw(screen)
        if not ball.timer():  balls.remove(ball)


    py.display.flip()   
    clock.tick(100)
