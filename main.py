

import json

import pyglet
import pymunk.pyglet_util
from pyglet.window import key, mouse

import source
from source import constants as c

pyglet.image.Texture.default_mag_filter = pyglet.gl.GL_NEAREST
pyglet.image.Texture.default_min_filter = pyglet.gl.GL_NEAREST


class Application:
    _borderless = False
    _pre_borderless_location = (0, 0)
    _pre_borderless_size = (0, 0)

    def __init__(self):
        self.window = pyglet.window.Window(
            caption="Arkius",
            resizable=True,
            vsync=True,
            width=1400,
            height=800
        )
        self.window.set_minimum_size(*c.MIN_SIZE)

        self.debug_mode = False

        self.key_handler = key.KeyStateHandler()
        self.mouse_handler = mouse.MouseStateHandler()

        self.fps_display = pyglet.window.FPSDisplay(window=self.window)

        self.world_camera = source.camera.Camera(0, 0, 1000)
        self.lock_to_player = False
        self.camera_movement_x = 0
        self.camera_movement_y = 0
        self.zoom = 1

        self.world_batch = pyglet.graphics.Batch()
        self.ui_batch = pyglet.graphics.Batch()

        self.particles = []
        self.handlers = []
        self.trigger_ids = []

        self.push_handlers(self, self.key_handler, self.mouse_handler)

        self.create_layers()
        self.load_resources()

        self.transition = source.ui.transition.Transition(self)
        # self.world = source.hub_world.HubWorld(self)
        self.world = source.dungeon.Dungeon(self, c.HUB)
        self.player = source.player.Player(self)

    def create_layers(self):
        self.layers = {}

        world = {}
        world["master"] = pyglet.graphics.Group()
        for layer in c.WORLD_LAYERS:
            world[layer] = pyglet.graphics.OrderedGroup(
                c.WORLD_LAYERS.index(layer)+1, world["master"]
            )
        self.layers["world"] = world

        ui = {}
        ui["master"] = pyglet.graphics.Group()
        for layer in c.UI_LAYERS:
            ui[layer] = pyglet.graphics.OrderedGroup(
                c.UI_LAYERS.index(layer)+1, ui["master"]
            )
        self.layers["ui"] = ui

    def load_resources(self):
        self.resources = {}

        tiles = {}
        for style in c.STYLES:
            tiles[style] = {}
            for tile in c.TILES.keys():
                tile_width = c.TILES[tile]["sprite"]["width"]
                tile_height = c.TILES[tile]["sprite"]["height"]
                image = pyglet.resource.image(
                    f"resources/tilesets/{style}/{tile}.png"
                )
                try:
                    data_path = f"resources/tilesets/{style}/{tile}.json"
                    with open(data_path, "r") as f:
                        data = json.load(f)

                    sprite_sheet = pyglet.image.ImageGrid(
                        image,
                        len(data["animations"]),
                        data["max_length"],
                        item_width=data["frame"][0],
                        item_height=data["frame"][1]
                    )

                    if c.TILES[tile]["sprite"]["connective"]:
                        frame_grids = []
                        for frame in range(sprite_sheet.__len__()):
                            frame_grids.append(
                                pyglet.image.ImageGrid(
                                    sprite_sheet[frame],
                                    c.TILESET_DIMENSIONS[1],
                                    c.TILESET_DIMENSIONS[0],
                                    item_width=tile_width,
                                    item_height=tile_height
                                )
                            )

                        image_grid = {}
                        for index in range(frame_grids[0].__len__()):
                            tile_frames = []
                            for i in range(data["animations"][0]["length"]):
                                tile_frames.append(
                                    frame_grids[i][index]
                                )
                            frame_length = data["animations"][0]["frame_length"]  # noqa: E501
                            image_grid[index] = pyglet.image.Animation.from_image_sequence(  # noqa: E501
                                tile_frames,
                                frame_length,
                                loop=data["animations"][0]["loop"]
                            )
                    else:
                        frame_grids = []
                        for frame in range(sprite_sheet.__len__()):
                            frame_grids.append(
                                pyglet.image.ImageGrid(
                                    sprite_sheet[frame],
                                    image.height // tile_height,
                                    image.width // tile_width,
                                    item_width=tile_width,
                                    item_height=tile_height
                                )
                            )

                        image_grid = []
                        for index in range(frame_grids[0].__len__()):
                            tile_frames = []
                            for i in range(data["animations"][0]["length"]):
                                tile_frames.append(
                                    frame_grids[i][index]
                                )
                            frame_length = data["animations"][0]["frame_length"]  # noqa: E501
                            image_grid.append(
                                pyglet.image.Animation.from_image_sequence(
                                    tile_frames,
                                    frame_length,
                                    loop=data["animations"][0]["loop"]
                                )
                            )

                except FileNotFoundError:
                    if c.TILES[tile]["sprite"]["connective"]:
                        image_grid = pyglet.image.ImageGrid(
                            image,
                            c.TILESET_DIMENSIONS[1],
                            c.TILESET_DIMENSIONS[0],
                            item_width=c.TILES[tile]["sprite"]["width"],
                            item_height=c.TILES[tile]["sprite"]["height"]
                        )
                    else:
                        image_grid = pyglet.image.ImageGrid(
                            image,
                            image.height // c.TILES[tile]["sprite"]["height"],
                            image.width // c.TILES[tile]["sprite"]["width"],
                            item_width=c.TILES[tile]["sprite"]["width"],
                            item_height=c.TILES[tile]["sprite"]["height"]
                        )

                tiles[style][tile] = image_grid
        self.resources["tiles"] = tiles

        image = pyglet.resource.image(
            "resources/sprites/player.png"
        )
        with open("resources/sprites/player.json", "r") as f:
            data = json.load(f)
        anim = self.load_animation(image, data)
        self.resources["player"] = anim

        image = pyglet.resource.image(
            "resources/sprites/portal_platform.png"
        )
        with open("resources/sprites/portal_platform.json", "r") as f:
            data = json.load(f)
        anim = self.load_animation(image, data)
        self.resources["portal_platform"] = anim

        image = pyglet.resource.image(
            "resources/tilesets/2/particles/bubble.png"
        )
        with open("resources/tilesets/2/particles/bubble.json", "r") as f:
            data = json.load(f)
        anim = self.load_animation(image, data)
        self.resources["lava_bubble"] = anim["main"]

        ui = {}

        ui["map"] = {}
        ui["map"]["window"] = pyglet.resource.image(
            "resources/ui/map_window.png"
        )
        image = pyglet.resource.image(
            "resources/ui/map_rooms.png"
        )
        image_grid = pyglet.image.ImageGrid(
            image,
            4, 16
        )
        ui["map"]["rooms"] = pyglet.image.TextureGrid(image_grid)
        image = pyglet.resource.image(
            "resources/ui/map_icons.png"
        )
        image_grid = pyglet.image.ImageGrid(
            image,
            1, 5
        )
        ui["map"]["icons"] = pyglet.image.TextureGrid(image_grid)

        image = pyglet.resource.image("resources/transition.png")
        with open("resources/transition.json", "r") as f:
            data = json.load(f)
        ui["transition"] = self.load_animation(image, data)

        self.resources["ui"] = ui

    def load_animation(self, image, data):
        sprite_sheet = pyglet.image.ImageGrid(
            image,
            len(data["animations"]),
            data["max_length"]
        )
        animations = {}
        for a in range(len(data["animations"])):
            animation_data = data["animations"][a]
            frames = []
            for i in range(animation_data["length"]):
                frame_length = data["animations"][a]["frame_length"]
                frames.append(
                    sprite_sheet[(a, i)]
                )
            animations[
                data["animations"][a]["alias"]
            ] = pyglet.image.Animation.from_image_sequence(
                frames,
                frame_length,
                loop=data["animations"][a]["loop"]
            )
        return animations

    def update(self, dt):
        self.room.space.step(dt)
        rezoom = False
        if self.key_handler[key.EQUAL]:
            self.zoom += 2 * dt
            rezoom = True
        elif self.key_handler[key.MINUS]:
            self.zoom -= 2 * dt
            rezoom = True

        if rezoom:
            self.zoom = max(c.MIN_ZOOM, min(c.MAX_ZOOM, self.zoom))
            zoom = (
                (min(self.window.width, self.window.height) / c.MIN_SIZE[1]) *
                self.zoom
            )
            if zoom >= 1:
                self.world_camera.zoom = round(zoom)
            else:
                self.world_camera.zoom = round(zoom*4)/4

        self.position_camera(dt=dt)
        self.player.update(dt)

    def on_draw(self):
        self.window.clear()
        with self.world_camera:
            self.world_batch.draw()
            if self.debug_mode:
                debug_options = pymunk.pyglet_util.DrawOptions()
                self.room.space.debug_draw(debug_options)
        self.ui_batch.draw()
        self.fps_display.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.F11:
            if not self.borderless:
                self.borderless = True
            elif self.borderless:
                self.borderless = False
        elif symbol == key.F3:
            self.debug_mode = not self.debug_mode
        elif symbol == key.F5:
            self.lock_to_player = not self.lock_to_player
        elif symbol == key.F1:
            def on_black():
                style = self.world.style
                style += 1
                if style > c.VOLCANO:
                    style = c.HUB

                self.world.delete()
                del self.world
                self.world = source.dungeon.Dungeon(self, style)
                self.player.room = (0, 0)
                self.player.position = (0, 0)
                self.room.space.add(self.player, self.player.collider)

            self.transition.begin(on_black=on_black)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT and self.debug_mode:
            world_x, world_y = self.screen_to_world(x, y)
            self.player.position = (world_x-c.TILE_SIZE/2, world_y)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_handler["x"] = x
        self.mouse_handler["y"] = y

    def on_resize(self, width, height):
        zoom = (
            (min(width, height) / c.MIN_SIZE[1]) *
            self.zoom
        )
        if zoom >= 1:
            self.world_camera.zoom = round(zoom)
        else:
            self.world_camera.zoom = round(zoom*4)/4

    def screen_to_world(self, x, y):
        world_x = (
            (x+self.world_camera.offset_x*self.world_camera.zoom) /
            self.world_camera.zoom
        )
        world_y = (
            (y+self.world_camera.offset_y*self.world_camera.zoom) /
            self.world_camera.zoom
        )

        return world_x, world_y

    def position_camera(self, parallax=True, dt=1/60):
        x = (-self.window.width//2 + c.TILE_SIZE/2)/self.world_camera.zoom
        y = (-self.window.height//2 + c.TILE_SIZE/2)/self.world_camera.zoom

        if parallax:
            # Player Position
            if self.lock_to_player:
                x += self.player.position.x + c.TILE_SIZE/2
                y += self.player.position.y
            else:
                x += (
                    (self.player.position.x) * 0.5 *
                    self.room.width/c.PARALLAX_X
                )
                y += (
                    (self.player.position.y) * 0.5 *
                    self.room.height/c.PARALLAX_Y
                )

            # Player Velocity
            if self.camera_movement_x < self.player.vx:
                self.camera_movement_x += c.PLAYER_SPEED*dt*3
                self.camera_movement_x = min(
                    self.player.vx,
                    self.camera_movement_x
                )
            elif self.camera_movement_x > self.player.vx:
                self.camera_movement_x -= c.PLAYER_SPEED*dt*3
                self.camera_movement_x = max(
                    self.player.vx,
                    self.camera_movement_x
                )

            if self.camera_movement_y < self.player.vy:
                self.camera_movement_y += c.PLAYER_SPEED*dt*3
                self.camera_movement_y = min(
                    self.player.vy,
                    self.camera_movement_y
                )
            elif self.camera_movement_y > self.player.vy:
                self.camera_movement_y -= c.PLAYER_SPEED*dt*3
                self.camera_movement_y = max(
                    self.player.vy,
                    self.camera_movement_y
                )

            x += self.camera_movement_x/(200/(self.room.width/c.PARALLAX_X))
            y += self.camera_movement_y/(200/(self.room.height/c.PARALLAX_Y))

            # Mouse Position
            m_x = self.mouse_handler["x"] - self.window.width//2
            m_y = self.mouse_handler["y"] - self.window.height//2
            x += m_x/self.world_camera.zoom/16
            y += m_y/self.world_camera.zoom/16

        x = round(x)
        y = round(y)

        self.world_camera.position = (x, y)

    def push_handlers(self, *handlers):
        for handler in handlers:
            self.handlers.append(handler)
            self.window.push_handlers(handler)

    def remove_handlers(self, *handlers):
        for handler in handlers:
            if handler in self.handlers:
                self.handlers.remove(handler)
            self.window.remove_handlers(handler)

    @property
    def room(self):
        room = self.world.map[self.player.room]
        return room

    @room.setter
    def room(self, pos):
        room = self.world.map[pos]
        self.room.visibility = False
        self.player.room = pos
        room.visibility = True

    @property
    def borderless(self):
        return self._borderless

    @borderless.setter
    def borderless(self, borderless):
        if borderless == self.borderless:
            return

        if borderless:
            self._pre_borderless_location = self.window.get_location()
            self._pre_borderless_size = self.window.get_size()

            window = pyglet.window.Window(
                caption="Arkius",
                vsync=True,
                style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS
            )
            self.window.close()
            self.window = window
            self.window.set_minimum_size(*c.MIN_SIZE)
            self.fps_display = pyglet.window.FPSDisplay(window=window)
            for handler in self.handlers:
                self.window.push_handlers(handler)

            self.window.maximize()
        else:
            window = pyglet.window.Window(
                caption="Arkius",
                resizable=True,
                vsync=True,
                style=pyglet.window.Window.WINDOW_STYLE_DEFAULT
            )
            self.window.close()
            self.window = window
            self.window.set_minimum_size(*c.MIN_SIZE)
            self.fps_display = pyglet.window.FPSDisplay(window=window)
            for handler in self.handlers:
                self.window.push_handlers(handler)

            self.window.set_location(*self._pre_borderless_location)
            self.window.set_size(*self._pre_borderless_size)

        self.position_camera(parallax=False)
        self._borderless = borderless

    def run(self):
        pyglet.clock.schedule_interval(self.update, c.UPDATE_SPEED)
        pyglet.app.run()


if __name__ == "__main__":
    application = Application()
    application.run()
