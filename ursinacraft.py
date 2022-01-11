from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# loading in our textures
grass = load_texture('assets/grass_block.png')
stone = load_texture('assets/stone_block.png')
brick = load_texture('assets/brick_block.png')
dirt = load_texture('assets/dirt_block.png')

block_pick = 1

# update function which checks to see what block is selected
def update():
    global block_pick

    # the following lines check for keypresses on 1, 2, 3, and 4
    # if there is a keypress, it updates the block_pick variable
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

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
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt)

            if key == 'right mouse down':
                destroy(self)

# responsible for generating the voxels which make up the platform 
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x, 0, z))


# enables a first person perspective
player = FirstPersonController()

app.run()
