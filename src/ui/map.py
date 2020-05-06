"""The ui map for a world."""

import pyglet

from .. import constants as c


class Map:
    def __init__(self, window, world):
        """Initialise the map with all rooms/

        Arguments:
            window {Window} -- The application window.
            world {World} -- The world for the map.
        """
        self.window = window
        self.world = world
        map_image = self.window.resources["ui"]["map"]["window"]
        map_layer = self.window.layers["ui"]["map_window"]
        self.map_window = pyglet.sprite.Sprite(
            map_image,
            0, 0,
            batch=self.window.ui_batch,
            group=map_layer
        )
        self.map_window.opacity = 200

        room_max = 0
        for pos in self.world.map.keys():
            for i in range(2):
                if abs(pos[i]) > room_max:
                    room_max = abs(pos[i])

        self.map_rooms = {}
        for pos, room in self.world.map.items():
            image = self.window.resources["ui"]["map"]["rooms"][(
                3, room.door_value
            )]
            icon = self.window.resources["ui"]["map"]["icons"][room.type]
            self.map_rooms[pos] = {}
            self.map_rooms[pos]["sprite"] = pyglet.sprite.Sprite(
                image,
                0, 0,
                batch=self.window.ui_batch,
                group=self.window.layers["ui"]["map_rooms"]
            )
            self.map_rooms[pos]["icon"] = pyglet.sprite.Sprite(
                icon,
                0, 0,
                batch=self.window.ui_batch,
                group=self.window.layers["ui"]["map_icons"]
            )
            self.map_rooms[pos]["icon"].visible = False
            self.map_rooms[pos]["visited"] = False
            self.map_rooms[pos]["room"] = room

        self.update_position()
        self.discover((0, 0))
        self.window.push_handlers(self)

    def update_position(self):
        scale = (min(self.window.width, self.window.height) / c.MIN_SIZE[1])

        self.map_window.scale = scale
        self.map_window.update(
            x=(
                self.window.width -
                self.map_window.width
            ),
            y=(
                self.window.height -
                self.map_window.height
            )
        )

        for pos in self.map_rooms.keys():
            self.map_rooms[pos]["sprite"].scale = (
                scale / (self.world.size / c.DEFAULT_WORLD_SIZE)
            )
            self.map_rooms[pos]["sprite"].update(
                x=(
                    self.map_window.x +
                    self.map_window.width//2 -
                    self.map_rooms[pos]["sprite"].width//2 +
                    pos[0]*12 *
                    scale/(self.world.size/c.DEFAULT_WORLD_SIZE)
                ),
                y=(
                    self.map_window.y +
                    self.map_window.height//2 -
                    self.map_rooms[pos]["sprite"].height//2 +
                    pos[1]*12 *
                    scale/(self.world.size/c.DEFAULT_WORLD_SIZE)
                )
            )
            self.map_rooms[pos]["icon"].scale = (
                scale / (self.world.size / c.DEFAULT_WORLD_SIZE)
            )
            self.map_rooms[pos]["icon"].update(
                x=(
                    self.map_window.x +
                    self.map_window.width//2 -
                    self.map_rooms[pos]["icon"].width//2 +
                    pos[0]*12 *
                    scale/(self.world.size/c.DEFAULT_WORLD_SIZE)
                ),
                y=(
                    self.map_window.y +
                    self.map_window.height//2 -
                    self.map_rooms[pos]["icon"].height//2 +
                    pos[1]*12 *
                    scale/(self.world.size/c.DEFAULT_WORLD_SIZE)
                )
            )

    def discover(self, pos):
        """Discover rooms on the map.

        Arguments:
            pos {tuple} -- The x and y position to discover.
        """
        neighbours = {
            (1, 0): 1,
            (-1, 0): 3,
            (0, -1): 2,
            (0, 1): 0
        }
        image = self.window.resources["ui"]["map"]["rooms"][(
            0, self.map_rooms[pos]["room"].door_value
        )]
        self.map_rooms[pos]["sprite"].image = image
        self.map_rooms[pos]["visited"] = True
        self.map_rooms[pos]["icon"].visible = True

        for (x, y), door in neighbours.items():
            n_x, n_y = x+pos[0], y+pos[1]
            if (
                (n_x, n_y) in self.map_rooms.keys() and
                self.world.map[pos].doors[door]
            ):
                if self.map_rooms[(n_x, n_y)]["visited"]:
                    image = self.window.resources["ui"]["map"]["rooms"][(
                        1, self.map_rooms[(n_x, n_y)]["room"].door_value
                    )]
                else:
                    image = self.window.resources["ui"]["map"]["rooms"][(
                        2, self.map_rooms[(n_x, n_y)]["room"].door_value
                    )]
                self.map_rooms[(
                    n_x, n_y
                )]["sprite"].image = image
                self.map_rooms[(n_x, n_y)]["icon"].visible = True

    def on_resize(self, width, height):
        """Update the position and scale of everything."""
        self.update_position()
