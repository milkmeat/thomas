import cocos
from cocos.actions import*

class  HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        super(HelloWorld,self).__init__( 64,64,224,255)
        label = cocos.text.Label('Hello, World!',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center')
        label.position=320,420
        self.add(label)
        
        sprite = cocos.sprite.Sprite('grossini.png')
        sprite.position = 320,240
        sprite.scale=3
        self.add( sprite, z=1 )
        
        scale = ScaleBy(3, duration=2)
        label.do( Repeat( scale + Reverse( scale) ) )
        
        
cocos.director.director.init()
hello_layer = HelloWorld ()
hello_layer.do( RotateBy(360, duration=20) )
main_scene = cocos.scene.Scene (hello_layer)
cocos.director.director.run (main_scene)