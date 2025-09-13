import pygame as py 
import random

screen_w =  1600
screen_h =  1000

py.init()  

screen = py.display.set_mode((screen_w, screen_h))
py.display.set_caption("ball ") 
clock  = py.time.Clock()

balls = []

colors = [
    (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (0, 255, 255), (255, 0, 255), (192, 192, 192), (128, 128, 128),
    (128, 0, 0), (128, 128, 0), (0, 128, 0), (128, 0, 128), (0, 128, 128), (0, 0, 128),
    (255, 165, 0), (255, 215, 0), (173, 255, 47), (50, 205, 50), (34, 139, 34),
    (60, 179, 113), (46, 139, 87), (144, 238, 144), (152, 251, 152), (143, 188, 143),
    (0, 100, 0), (0, 250, 154), (0, 255, 127), (127, 255, 0), (124, 252, 0),
    (0, 191, 255), (30, 144, 255), (100, 149, 237), (70, 130, 180), (176, 196, 222),
    (65, 105, 225), (138, 43, 226), (75, 0, 130), (106, 90, 205), (123, 104, 238),
    (221, 160, 221), (238, 130, 238), (218, 112, 214), (199, 21, 133), (255, 105, 180),
    (255, 20, 147), (219, 112, 147), (139, 69, 19), (160, 82, 45), (210, 105, 30),
    (205, 92, 92), (233, 150, 122), (250, 128, 114), (255, 160, 122), (255, 99, 71)
]


gravity = 9
mass = 2
font = py.font.SysFont('Arial', 20)

class Ball:

    def __init__(self, position):
        self.position = list(position)
        self.velocity = 0
        self.color = random.choice(colors)

        self.counter = 0
    



    def physcis(self):
        fg = mass* gravity
    

    


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
        return self.counter < 1000



def rectangle():

    dimensions = [10, 850, 1500, 120] 

    py.draw.rect(screen, (250,250,250), dimensions, 1)


def spawn_ball(x, y):
    balls.append(Ball((x,y)))



def text():
    txt = f"gravity: {gravity} (press arrow keys to change)"
    text_surface_1 = font.render(txt, True, (250,250,250)) 
    text_rect_1 = text_surface_1.get_rect()
    text_rect_1.center = (250, 25)
    screen.blit(text_surface_1, text_rect_1)



    txt_2 = f"mass: {mass} (press w and/ or  s to change)"
    text_surface_2 = font.render(txt_2, True, (250,250,250)) 
    text_rect_2 = text_surface_2.get_rect()
    text_rect_2.center = (248, 45)
    screen.blit(text_surface_2, text_rect_2)    


running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False

        if event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            spawn_ball(mouse_x, mouse_y)


        if event.type == py.KEYDOWN:
            if event.key == py.K_UP:
                gravity += 1
            elif event.key == py.K_DOWN:
                    gravity -= 1

            
            if event.key == py.K_w:
                mass += 0.5
            elif event.key == py.K_s:
                if mass == 0: break
                
                mass -= 0.5






    screen.fill((0, 0, 0)) 

    rectangle()



    for ball in balls:
        ball.physcis()
        ball.draw(screen)
        if not ball.timer():  balls.remove(ball)


    text()

    py.display.flip()   
    clock.tick(100)
