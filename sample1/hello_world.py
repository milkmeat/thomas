import cocos
from pyglet.window import key
from cocos.actions import*
class HelloWorld(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super( HelloWorld, self ).__init__()
        label=cocos.text.Label('thomas',
                                font_name='Times new roman',
                                font_size=64,
                                anchor_x='center', anchor_y='center' )
        label.position=320,240
        self.add(label)
        
        sprite = cocos.sprite.Sprite('dude.png')
        self.rabbit=sprite
        sprite.position = 320,240
        self.add( sprite, z=1 )
        
    def on_key_press(self, symbol, modifiers):
        if symbol==key.LEFT:
            self.rabbit.do(MoveBy((-5,0),0.1))
        if symbol==key.UP:
            self.rabbit.do(MoveBy((0,+5),0.1))
        if symbol==key.DOWN:
            self.rabbit.do(MoveBy((0,-5),0.1))
        if symbol==key.RIGHT:
            self.rabbit.do(MoveBy((+5,0),0.1))
cocos.director.director.init()
hello_layer=HelloWorld ()
#hello_layer.do(RotateBy(360, duration=20))
main_scene=cocos.scene.Scene (hello_layer)
cocos.director.director.run (main_scene)