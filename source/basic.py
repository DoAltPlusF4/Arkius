import pyglet
import pymunk

from .cardsprite import CardSprite


class Basic(pymunk.Body):

    def __init__(
        self,
        application,
        x, y,
        image, card_sprite=False,
        collider=None,
        body_type=pymunk.Body.STATIC,
        space=None
    ):
        self.application = application
        if space is None:
            space = self.application.room.space
        super().__init__(
            mass=1,
            moment=float("inf"),
            body_type=body_type
        )
        self.position = (x, y)
        self.collider_data = collider
        if collider is not None:
            if collider["type"] == "rect":
                self.collider = pymunk.Poly(
                    body=self,
                    vertices=[
                        (
                            collider["x"],
                            collider["y"]
                        ),
                        (
                            collider["x"]+collider["width"],
                            collider["y"]
                        ),
                        (
                            collider["x"]+collider["width"],
                            collider["y"]+collider["height"]
                        ),
                        (
                            collider["x"],
                            collider["y"]+collider["height"]
                        )
                    ],
                    radius=collider["radius"]
                )
            elif collider["type"] == "circle":
                self.collider = pymunk.Circle(
                    body=self,
                    radius=collider["radius"],
                    offset=collider["offset"]
                )
            space.add(self, self.collider)

        if card_sprite:
            self.sprite = CardSprite(
                image,
                x=self.position.x, y=self.position.y,
                batch=self.application.world_batch,
                subpixel=True
            )
        else:
            self.sprite = pyglet.sprite.Sprite(
                image,
                x=self.position.x, y=self.position.y,
                batch=self.application.world_batch,
                subpixel=True
            )

    def update(self, dt):
        self.sprite.update(
            x=self.position.x,
            y=self.position.y,
        )