"""
Copyright (C) 2020,  DoAltPlusF4.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pyglet
from pyglet.window import Window
from pyglet.window import key
from pyglet import image
from pyglet import gl

from Lib.dungeon import Room
from Lib import tilesets


room = Room(room_type=1, tileset=tilesets.generateRandom())
print(room)

print("\n\n\n")

window = Window(caption="Arkius", resizable=True, fullscreen=True)
SCALE_FACTOR = window.height/320
tile_batch = pyglet.graphics.Batch()
pyglet.image.Texture.default_mag_filter = gl.GL_NEAREST
pyglet.image.Texture.default_min_filter = gl.GL_NEAREST


def getValue(tileset, x, y):
    """Returns the bitmasking value of a tile."""
    tileID = tileset[(x, y)]
    value = 255
    sides = {
        128: False, 1: False,   2: False,
        64: False,              4: False,
        32: False,  16: False,  8: False
    }

    if y != 14 and tileset[(x, y+1)] != tileID:
        sides[128] = True
        sides[1] = True
        sides[2] = True
    if y != 14 and x != 14 and tileset[(x+1, y+1)] != tileID:
        sides[2] = True
    if x != 14 and tileset[(x+1, y)] != tileID:
        sides[2] = True
        sides[4] = True
        sides[8] = True
    if x != 14 and y != 0 and tileset[(x+1, y-1)] != tileID:
        sides[8] = True
    if y != 0 and tileset[(x, y-1)] != tileID:
        sides[8] = True
        sides[16] = True
        sides[32] = True
    if y != 0 and x != 0 and tileset[(x-1, y-1)] != tileID:
        sides[32] = True
    if x != 0 and tileset[(x-1, y)] != tileID:
        sides[32] = True
        sides[64] = True
        sides[128] = True
    if x != 0 and y != 14 and tileset[(x-1, y+1)] != tileID:
        sides[128] = True

    for side in sides.keys():
        if sides[side]:
            value -= side

    return value


def makeTileSprite(image, batch, x, y):
    global SCALE_FACTOR
    tile = pyglet.sprite.Sprite(
        image,
        batch=batch,
        x=(x*16*SCALE_FACTOR)+(2.5*16*SCALE_FACTOR) +
        (window.width/2)-(20*16*SCALE_FACTOR/2),
        y=(y*16*SCALE_FACTOR)+(2.5*16*SCALE_FACTOR) +
        (window.height/2)-(20*16*SCALE_FACTOR/2),
        usage="static"
    )
    tile.scale = SCALE_FACTOR
    return tile


def drawTiles(dt=None):
    global room
    tiles = {}

    style = 1  # TMP

    for x in range(15):
        for y in range(15):
            room_tiles = room.ground_tiles
            tile_id = room_tiles[(x, y)]

            if tile_id != 0:
                value = getValue(room_tiles, x, y)
                image_path = f"Images/Tiles/{style}/{tile_id}/{value}.png"

            else:
                image_path = f"Images/Tiles/{style}/0.png"
            tile_image = image.load(image_path)
            tile_image.anchor_x = 0
            tile_image.anchor_y = 0
            tile = makeTileSprite(tile_image, tile_batch, x, y)
            tiles[(x, y)] = tile

    # Render room borders.
    for k in range(17):
        for j in range(17):
            x = k-1
            y = j-1

            value = None

            if x == -1 and y == -1:
                value = 253
            elif x == -1 and y == 15:
                value = 247
            elif x == 15 and y == -1:
                value = 127
            elif x == 15 and y == 15:
                value = 223
            elif x == -1:
                value = 241
            elif x == 15:
                value = 31
            elif y == -1:
                value = 124
            elif y == 15:
                value = 199

            if value is not None:
                image_path = f"Images/Tiles/{style}/1/{value}.png"
                tile_image = image.load(image_path)
                tile_image.anchor_x = 0
                tile_image.anchor_y = 0
                tile = makeTileSprite(tile_image, tile_batch, x, y)
                tiles[(x, y)] = tile

    window.clear()
    tile_batch.draw()


@window.event
def on_show():
    global room, SCALE_FACTOR
    SCALE_FACTOR = window.height/320
    drawTiles()


@window.event
def on_key_press(symbol, modifiers):
    global room, SCALE_FACTOR
    if symbol == key._0:
        room = Room(room_type=0, tileset=tilesets.generateRandom())
    elif symbol == key._1:
        room = Room(room_type=1, tileset=tilesets.generateRandom())
    elif symbol == key._2:
        room = Room(room_type=2, tileset=tilesets.generateRandom())
    elif symbol == key._3:
        room = Room(room_type=3, tileset=tilesets.generateRandom())
    elif symbol == key._4:
        room = Room(room_type=4, tileset=tilesets.generateRandom())
    drawTiles()


@window.event
def on_resize(width, height):
    global SCALE_FACTOR, room
    SCALE_FACTOR = window.height/320
    pyglet.clock.schedule_once(drawTiles, 0.1)


@window.event
def on_draw():
    pass


pyglet.app.run()
