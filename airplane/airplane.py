import cocos
from pyglet.window import key
from cocos.actions import*
from cocos.director import director
import random
import cocos.collision_model as cm
import cocos.euclid as eu


class GameOver(cocos.layer.Layer):
    def __init__(self):
        super( GameOver, self ).__init__()
        
        background=cocos.sprite.Sprite('resourses/shoot/gameover.png')
        background.position = 320,240
        self.add(background)

class HelloWorld(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super( HelloWorld, self ).__init__()
     
        scoreLabel=cocos.text.Label('0',
                        font_name='Times new roman',
                        font_size=64,
                        anchor_x='center', anchor_y='center' )
        w,h = director.get_window_size()
        scoreLabel.position=w-100,h-100
        self.scoreLabel=scoreLabel
        self.add(scoreLabel)
        self.score=0
        
     
        sprite = cocos.sprite.Sprite('resourses/shoot/hero2.png')
        self.hero=sprite
        sprite.position = 320,240
        self.add( sprite, z=1 )
        
        self.move=[False,False,False,False] #up down left right
        
        self.bullets=cocos.batch.BatchNode()
        self.add(self.bullets)                           
        self.enemies=cocos.batch.BatchNode()
        self.add(self.enemies)
        
        self.schedule( self.step )
        self.schedule_interval(self.shoot,0.5)
        self.schedule_interval(self.makeEnemy,1)
    
    def makeEnemy( self, dt ):
        w,h = director.get_window_size()
        type = random.randint(1, 3)
        enemy = cocos.sprite.Sprite('resourses/shoot/enemy'+str(type)+'.png')
        enemy.type=type
        enemy.position=(w*random.random(), h)
        self.enemies.add(enemy)        
    
    def shoot( self, dt ):
        bullet = cocos.sprite.Sprite('resourses/shoot/bullet1.png')
        bullet.position=self.hero.position        
        self.bullets.add(bullet)
        
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
        self.bump()
        
        self.scoreLabel.element.document.text=str(self.score)
        
    def bump(self):
        w,h = director.get_window_size()
        collman = cm.CollisionManagerGrid(0.0, w,
                                               0.0, h,
                                               10,10)
                                               
        self.hero.cshape = cm.CircleShape(eu.Vector2(self.hero.x, self.hero.y), 50)     
        collman.add(self.hero)
        
        for one in self.bullets.get_children():
            one.cshape=cm.AARectShape(eu.Vector2(one.x, one.y), 5,10 )
            collman.add(one)
        for oneEnemy in self.enemies.get_children():
            oneEnemy.cshape=cm.AARectShape(eu.Vector2(oneEnemy.x, oneEnemy.y), 25*oneEnemy.type,25*oneEnemy.type )
            collman.add(oneEnemy)
        for oneEnemy in self.enemies.get_children():
            for oneBullet in self.bullets.get_children():
                if collman.they_collide(oneEnemy, oneBullet):
                    self.enemies.remove(oneEnemy)
                    self.bullets.remove(oneBullet)
                    self.score+=50
                    break
        for oneEnemy in self.enemies.get_children():
            if collman.they_collide(oneEnemy,self.hero):
                self.enemies.remove(oneEnemy)
                #self.remove(hero)
                #print "you lose!!!!!!!"
                GameOverLayer=GameOver ()
                gameover=cocos.scene.Scene (GameOverLayer)
                director.replace (gameover)

               
    def moveEnemies(self):
        w,h = director.get_window_size()
        for one in self.enemies.get_children():
            one.do(MoveBy((0,-3),0))
            if one.y<0:
                self.enemies.remove(one)
            
    def moveBullets(self):
        w,h = director.get_window_size()
        for one in self.bullets.get_children():
            one.do(MoveBy((0,3),0))
            if one.y>h:
                self.bullets.remove(one)


        
director.init(width=768, height=1024)
hello_layer=HelloWorld ()
#hello_layer.do(RotateBy(360, duration=20))
main_scene=cocos.scene.Scene (hello_layer)
director.run (main_scene)