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

from sys import platform as PLATFORM

import pyglet
from pyglet.window import Window
from pyglet.window import key
from pyglet.text import Label
from pyglet import image
from pyglet import gl

from Lib.dungeon import Room
from Lib import tilesets


room = Room(room_type=1, tileset=tilesets.fightRoom())
print(room)

print("\n\n\n")

window = Window(
    caption="Arkius",
    resizable=True,
    fullscreen=True
)

window.set_minimum_size(1280, 720)

SCALE_FACTOR = window.height/320
tile_batches = {}
for i in range(17):
    y = i - 1
    tile_batches[y] = pyglet.graphics.Batch()
pyglet.image.Texture.default_mag_filter = gl.GL_NEAREST
pyglet.image.Texture.default_min_filter = gl.GL_NEAREST

resized_recently = False


def getValue(tileset, x, y):
    """Returns the bitmasking value of a tile."""
    tileID = tileset[(x, y)]
    value = 0

    sides = {
        128: False, 1: False,   2: False,
        64: False,              4: False,
        32: False,  16: False,  8: False
    }

    edges = [tileID]
    if tileID == 2:
        edges.append(1)

    if y != 14 and tileset[(x, y+1)] not in edges:
        sides[128] = True
        sides[1] = True
        sides[2] = True
    if y != 14 and x != 14 and tileset[(x+1, y+1)] not in edges:
        sides[2] = True
    if x != 14 and tileset[(x+1, y)] not in edges:
        sides[2] = True
        sides[4] = True
        sides[8] = True
    if x != 14 and y != 0 and tileset[(x+1, y-1)] not in edges:
        sides[8] = True
    if y != 0 and tileset[(x, y-1)] not in edges:
        sides[8] = True
        sides[16] = True
        sides[32] = True
    if y != 0 and x != 0 and tileset[(x-1, y-1)] not in edges:
        sides[32] = True
    if x != 0 and tileset[(x-1, y)] not in edges:
        sides[32] = True
        sides[64] = True
        sides[128] = True
    if x != 0 and y != 14 and tileset[(x-1, y+1)] not in edges:
        sides[128] = True

    for side in sides.keys():
        if sides[side]:
            value += side

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
    global room, resized_recently
    resized_recently = False
    tiles = {}

    style = 0  # TMP

    for x in range(15):
        for y in range(15):
            room_tiles = room.ground_tiles
            tile_id = room_tiles[(x, y)]

            if tile_id != 0:
                value = getValue(room_tiles, x, y)
                image_path = f"Images/Tiles/{style}/{tile_id}/{value}.png"
            else:
                floor_type = room.floor_tiles[(x, y)]
                image_path = f"Images/Tiles/{style}/0/{floor_type}.png"
            tile_image = image.load(image_path)
            tile_image.anchor_x = 0
            tile_image.anchor_y = 0
            tile = makeTileSprite(tile_image, tile_batches[y], x, y)
            tiles[(x, y)] = tile

    # Render room borders.
    for k in range(17):
        for j in range(17):
            x = k-1
            y = j-1

            value = None

            values = {(-1, -1): 2, (-1, 15): 8, (15, -1): 128, (15, 15): 32}

            if x == -1:
                value = 14
            elif x == 15:
                value = 224
            elif y == -1:
                value = 131
            elif y == 15:
                value = 56

            if (x, y) in values.keys():
                value = values[(x, y)]

            if value is not None:
                image_path = f"Images/Tiles/{style}/1/{value}.png"
                tile_image = image.load(image_path)
                tile_image.anchor_x = 0
                tile_image.anchor_y = 0
                tile = makeTileSprite(tile_image, tile_batches[y], x, y)
                tiles[(x, y)] = tile

    window.clear()

    help_text = Label(
        text="Keys: 1 - Fight Room, 2 - Treasure Room, 3 - Boss Room, 4 - Shop Room, 0 - Start Room, F11 - Fullscreen/Windowed",  # noqa: E501
        font_name="Helvetica", font_size=7*SCALE_FACTOR,
        x=10*SCALE_FACTOR, y=window.height-10*SCALE_FACTOR,
        anchor_y="top"
    )
    help_text.draw()

    for i in range(17):
        y = 15 - i
        tile_batches[y].draw()


@window.event
def on_show():
    global room, SCALE_FACTOR
    SCALE_FACTOR = window.height/320

    drawTiles()


@window.event
def on_key_press(symbol, modifiers):
    global room, SCALE_FACTOR
    if symbol == key._0:
        room = Room(room_type=0)
    elif symbol == key._1:
        room = Room(room_type=1, tileset=tilesets.fightRoom())
    elif symbol == key._2:
        room = Room(room_type=2)
    elif symbol == key._3:
        room = Room(room_type=3)
    elif symbol == key._4:
        room = Room(room_type=4)

    elif symbol == key.F11:
        window.set_fullscreen(not window.fullscreen)

    drawTiles()


@window.event
def on_resize_stop(width, height):
    global SCALE_FACTOR
    SCALE_FACTOR = window.height/320
    drawTiles()


@window.event
def on_resize(width, height):
    global SCALE_FACTOR, resized_recently

    if PLATFORM == "win32":
        return

    if not resized_recently:
        resized_recently = True
        pyglet.clock.schedule_once(drawTiles, 0.1)


@window.event
def on_draw():
    pass


pyglet.app.run()
