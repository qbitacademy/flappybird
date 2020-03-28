import pgzrun
import random

TITLE = 'Flappy bird'
WIDTH = 397
HEIGHT = 708
puntuacion = 0
bird = Actor('bird1',(75,200))
bird.vy = 0  #La velocidad del pájaro (v) en el eje y
GRAVEDAD = 0.3
bird.muerto = False
#WIDTH = 397
#HEIGHT = 708

def reset_pipes():
    pos_hueco = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pos_hueco - 130 //2 )
    pipe_bottom.pos = (WIDTH, pos_hueco + 130 //2 )

pipe_top = Actor('top', anchor = ('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
reset_pipes()



def update_bird():
    copia = bird.vy
    bird.vy += GRAVEDAD
    bird.x = 75
    bird.y += copia + bird.vy / 2
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.image = 'birddead'
        bird.muerto = True
    
    if not bird.muerto:
        if bird.vy < -3:
            bird.image = 'bird2'
        else:
            bird.image = 'bird1'
    if bird.y < 0 or bird.y > 720:
        global puntuacion
        puntuacion = 0
        bird.y = 200
        bird.vy = 0
        bird.muerto = False
        reset_pipes()
        

       
def update():
    update_pipes()
    update_bird()


def update_pipes():
    pipe_top.left -= 6.5
    pipe_bottom.left -= 6.5
    if pipe_top.right < 0:
        reset_pipes()
        if not bird.muerto:
            global puntuacion
            puntuacion += 1
            
def on_key_down():
    if not bird.muerto:
        bird.vy -= 6.5
    
def draw():
    screen.blit('background',(0,0))
    global puntuacion
    bird.draw()
    pipe_top.draw()
    pipe_bottom.draw()
    screen.draw.text(str(puntuacion), color = 'white',fontsize = 70, shadow=(1,1), midtop=(WIDTH // 2,10)) #Escribe texto
    


pgzrun.go()