from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self): #생성자
        #생성자를 이용해서 객체의 초기 상태를 정의상태 정의
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass



class BigBall:
    def __init__(self):
        self.x, self.y =random.randint(20,880), 599
        self.speed=random.randint(3,23)
       # self.frame=random.randint(0,7) #동기화던 랜더링처럼 보이지 안게하기 위해

        self.image=load_image('ball41x41.png')
    def update(self):
       # self.frame = (self.frame+1)%8
        self.y-=self.speed
        if self.y<=60:
            self.y=60
    def draw(self):
        self.image.draw(self.x,self.y)
        #self.image.clip_draw(0,0,100,100,self.x,self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y =random.randint(20,880), 599
        self.speed=random.randint(3,23)
       # self.frame=random.randint(0,7) #동기화던 랜더링처럼 보이지 안게하기 위해
        self.image=load_image('ball21x21.png')

    def update(self):
       # self.frame = (self.frame+1)%8
        self.y-=self.speed
        if self.y<=60:
            self.y=60
    def draw(self):
        self.image.draw(self.x,self.y)
        #self.image.clip_draw(0,0,100,100,self.x,self.y)

class Boy:
    def __init__(self):
        self.x, self.y =random.randint(100,700), 90
        self.frame=random.randint(0,7) #동기화던 랜더링처럼 보이지 안게하기 위해
        self.image=load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame+1)%8
        self.x+=5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
   global world
   for o in world:
       o.update()


def render_world():
    global world

    clear_canvas()
    for o in world:
       o.draw()
    update_canvas()


def reset_world():  #초기화하는 함수
    global running
    global world


    world=[]
    running = True
    team = [Boy() for i in range(11)]#List Comprehension
    grass=Grass()   #Grass 클래스를 이용해서 grass 객체를 생성
    world.append(grass)
    world+=team
    for i in range(20):
        if random.randint(0,1)==0:
            world+=[BigBall()]
        else:
            world+=[SmallBall()]
    

open_canvas()

# initialization code
reset_world()
grass = Grass()
# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code


close_canvas()
