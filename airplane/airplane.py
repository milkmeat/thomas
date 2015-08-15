import cocos
from pyglet.window import key
from cocos.actions import*
class HelloWorld(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super( HelloWorld, self ).__init__()
     
        sprite = cocos.sprite.Sprite('resourses/shoot/hero2.png')
        self.rabbit=sprite
        sprite.position = 320,240
        self.add( sprite, z=1 )
        self.move=[False,False,False,False] #up down left right
        self.schedule( self.step )
        
    def on_key_press(self, symbol, modifiers):
        if symbol==key.LEFT:
            self.move[2]=True
        if symbol==key.UP:
            self.move[0]=True
        if symbol==key.DOWN:
            self.move[1]=True
        if symbol==key.RIGHT:
            self.move[3]=True

            
    def on_key_release(self, symbol, modifiers):        
        if symbol==key.LEFT:
            self.move[2]=False
        if symbol==key.UP:
            self.move[0]=False
        if symbol==key.DOWN:
            self.move[1]=False
        if symbol==key.RIGHT:
            self.move[3]=False
            
    def step( self, dt ):
        if self.move[2]:
            self.rabbit.do(MoveBy((-2,0),0))
        if self.move[0]:
            self.rabbit.do(MoveBy((0,+2),0))
        if self.move[1]:
            self.rabbit.do(MoveBy((0,-2),0))
        if self.move[3]:
            self.rabbit.do(MoveBy((+2,0),0))

            
cocos.director.director.init()
hello_layer=HelloWorld ()
#hello_layer.do(RotateBy(360, duration=20))
main_scene=cocos.scene.Scene (hello_layer)
cocos.director.director.run (main_scene)