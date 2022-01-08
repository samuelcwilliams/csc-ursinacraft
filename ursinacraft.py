from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

brick = load_texture('assets/brick_block.png')
grass = load_texture('assets/grass_block.png')
dirt = load_texture('assets/dirt_block.png')
stone = load_texture('assets/stone_block.png')

class Voxel(Button):
    # these buttons are what will make up our platform.
    def __init__(self, position = (0, 0, 0), texture = grass):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            scale = 0.5
            )

    # By creating new button press functionality, we will introduce a
    # more Minecraft-like block breaking experience.
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal, texture = stone)

            if key == 'right mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))

player = FirstPersonController()

app.run()
