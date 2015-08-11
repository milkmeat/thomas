import cocos
from cocos.actions import*
class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super( HelloWorld, self ).__init__()
        label=cocos.text.Label('thomas',
                                font_name='Times new roman',
                                font_size=64,
                                anchor_x='center', anchor_y='center' )
        label.position=320,240
        self.add(label)

cocos.director.director.init()
hello_layer=HelloWorld ()
hello_layer.do(RotateBy(360, duration=20))
main_scene=cocos.scene.Scene (hello_layer)
cocos.director.director.run (main_scene)