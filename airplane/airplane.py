import cocos
from pyglet.window import key
from cocos.actions import*
from cocos.director import director
import random

class HelloWorld(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super( HelloWorld, self ).__init__()
     
        sprite = cocos.sprite.Sprite('resourses/shoot/hero2.png')
        self.hero=sprite
        sprite.position = 320,240
        self.add( sprite, z=1 )
        
        self.move=[False,False,False,False] #up down left right
        
        self.bullets=[]
        self.enemies=[]
        
        self.schedule( self.step )
        self.schedule_interval(self.shoot,0.5)
        self.schedule_interval(self.makeEnemy,1)
    
    def makeEnemy( self, dt ):
        w,h = director.get_window_size()
        enemy = cocos.sprite.Sprite('resourses/shoot/enemy1.png')
        enemy.position=(w*random.random(), h)
        self.add(enemy)
        self.enemies.append(enemy)        
    
    def shoot( self, dt ):
        bullet = cocos.sprite.Sprite('resourses/shoot/bullet1.png')
        bullet.position=self.hero.position
        self.add(bullet)
        self.bullets.append(bullet)
        
    def on_key_press(self, symbol, modifiers):
        if symbol==key.UP:
            self.move[0]=True
        if symbol==key.DOWN:
            self.move[1]=True
        if symbol==key.LEFT:
            self.move[2]=True            
        if symbol==key.RIGHT:
            self.move[3]=True

            
    def on_key_release(self, symbol, modifiers):        
        if symbol==key.UP:
            self.move[0]=False
        if symbol==key.DOWN:
            self.move[1]=False
        if symbol==key.LEFT:
            self.move[2]=False            
        if symbol==key.RIGHT:
            self.move[3]=False
            
    def step( self, dt ):
        x=0
        y=0
        if self.move[0]:
            y+=2
        if self.move[1]:
            y-=2
        if self.move[2]:
            x-=2
        if self.move[3]:
            x+=2
        self.hero.do(MoveBy((x,y),0))
        
        self.moveBullets()
        self.moveEnemies()
    def moveEnemies(self):
        w,h = director.get_window_size()
        for one in self.enemies:
            one.do(MoveBy((0,-3),0))
            if one.y<0:
                self.remove(one)
                self.enemies.remove(one)
            
    def moveBullets(self):
        w,h = director.get_window_size()
        for one in self.bullets:
            one.do(MoveBy((0,3),0))
            if one.y>h:
                self.remove(one)
                self.bullets.remove(one)


        
director.init()
hello_layer=HelloWorld ()
#hello_layer.do(RotateBy(360, duration=20))
main_scene=cocos.scene.Scene (hello_layer)
director.run (main_scene)