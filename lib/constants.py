"""Contains constants used for the game."""

# Window
MIN_SIZE = (568, 320)
UPDATE_SPEED = 1/120
DEFAULT_SCALE_DIVISOR = 320

# Player
PLAYER_SPEED = 4
DIAGONAL_MULTIPLIER = 0.7
PLAYER_COLLIDER = {
    "x": 1/16,
    "y": -1/16,
    "width": 14/16,
    "height": 10/16
}

# Tile Types
FLOOR = 0
WALL = 1
PIT = 2
SECONDARY_FLOOR = 3
PAVEMENT = 4
TILES = {
    FLOOR: {
        "sprite": {
            "width": 16,
            "height": 16,
            "connective": False
        },
        "collider": None
    },
    WALL: {
        "sprite": {
            "width": 16,
            "height": 25,
            "connective": True
        },
        "collider": {
            "x": 0,
            "y": 0,
            "width": 1,
            "height": 1
        }
    },
    PIT: {
        "sprite": {
            "width": 16,
            "height": 16,
            "connective": True
        },
        "collider": {
            "x": 2/16,
            "y": 3/16,
            "width": 11/16,
            "height": 11/16
        }
    },
    SECONDARY_FLOOR: {
        "sprite": {
            "width": 16,
            "height": 16,
            "connective": True
        },
        "collider": None
    },
    PAVEMENT: {
        "sprite": {
            "width": 16,
            "height": 16,
            "connective": True
        },
        "collider": None
    }
}

# Tilemaps
DEFAULT_ROOM_SIZE = 7
DEFAULT_MAP_SETTINGS = [
    {
        "id": SECONDARY_FLOOR,
        "overrides": [FLOOR],
        "seed_amount": 3,
        "seed_type": "blob",
        "b_spread_amount": 20,
        "b_spread_additional": 20
    },
    {
        "id": PIT,
        "overrides": [FLOOR, SECONDARY_FLOOR],
        "seed_amount": 1,
        "seed_type": "blob",
        "b_spread_amount": 50,
        "b_spread_additional": 50
    },
    {
        "id": WALL,
        "overrides": [FLOOR, PIT, SECONDARY_FLOOR],
        "seed_amount": 2,
        "seed_type": "line",
        "l_hole_amount": 3,
        "l_hole_size_range": (2, 4)
    },
]
START_ROOM_MAPS = [
    [
        [1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1, ],
        [1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, ],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 3, 3, 3, 0, 0, 0, 2, 2, ],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, ],
        [2, 2, 0, 0, 0, 3, 3, 3, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
        [1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, ],
        [1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1, ],
    ],
    [
        [2, 2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 2, 2, ],
        [2, 2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 2, 2, ],
        [1, 1, 1, 2, 3, 3, 3, 3, 3, 2, 1, 1, 1, ],
        [2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, ],
        [3, 3, 3, 2, 2, 3, 3, 3, 2, 2, 3, 3, 3, ],
        [3, 3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, ],
        [3, 3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, ],
        [3, 3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, ],
        [3, 3, 3, 2, 2, 3, 3, 3, 2, 2, 3, 3, 3, ],
        [2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, ],
        [1, 1, 1, 2, 3, 3, 3, 3, 3, 2, 1, 1, 1, ],
        [2, 2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 2, 2, ],
        [2, 2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 2, 2, ],
    ],
]
FIGHT_ROOM_MAPS = [
    [
        [2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, ],
        [2, 2, 1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 1, 2, 2, ],
        [1, 1, 1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 1, 1, 1, ],
        [3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 3, 3, 3, 3, 3, ],
        [3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, ],
        [3, 3, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 3, ],
        [3, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0, 2, 2, 2, 3, ],
        [3, 2, 2, 2, 0, 3, 3, 1, 3, 3, 0, 2, 2, 2, 3, ],
        [3, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0, 2, 2, 2, 3, ],
        [3, 3, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 3, ],
        [3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, ],
        [3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 3, 3, 3, 3, 3, ],
        [1, 1, 1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 1, 1, 1, ],
        [2, 2, 1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 1, 2, 2, ],
        [2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 2, 2, ],
    ],
    [
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, ],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, ],
        [0, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 2, 2, 1, 2, 1, 2, 2, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 2, 2, 1, 2, 1, 2, 2, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 0, ],
        [0, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 0, ],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, ],
        [1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, ],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
    ],
]
TREASURE_ROOM_MAPS = [
    [
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, ],
        [0, 0, 0, 1, 1, 3, 3, 3, 1, 1, 0, 0, 0, ],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, ],
        [0, 0, 0, 1, 1, 3, 3, 3, 1, 1, 0, 0, 0, ],
        [2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
    ],
    [
        [1, 1, 1, 1, 2, 3, 3, 3, 2, 1, 1, 1, 1, ],
        [1, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, ],
        [1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1, ],
        [1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, ],
        [3, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, ],
        [3, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, ],
        [3, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, ],
        [1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, ],
        [1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1, ],
        [1, 1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1, 1, ],
        [1, 1, 1, 1, 2, 3, 3, 3, 2, 1, 1, 1, 1, ],
    ],
]
BOSS_ROOM_MAPS = [
    [
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2, ],
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, 2, 0, 0, 2, 2, ],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 3, ],
        [3, 3, 3, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 3, 3, 3, ],
        [3, 3, 3, 0, 1, 0, 0, 2, 2, 2, 2, 2, 0, 0, 1, 0, 3, 3, 3, ],
        [3, 3, 3, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 3, 3, 3, ],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 3, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, ],
        [2, 2, 0, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, 2, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 2, 2, ],
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2, ],
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2, ],
    ],
    [
        [1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 1, 1, 1, ],
        [1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1, 1, ],
        [1, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 2, 1, ],
        [2, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 2, 2, ],
        [2, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 2, 2, ],
        [2, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 1, 1, 1, 3, 3, 3, 1, 1, 1, 0, 0, 0, 2, 2, ],
        [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, ],
        [2, 2, 0, 0, 0, 1, 1, 1, 3, 3, 3, 1, 1, 1, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 2, 2, ],
        [2, 2, 0, 0, 0, 2, 2, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 2, 2, ],
        [2, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 2, 2, ],
        [2, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 2, 2, ],
        [1, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 2, 1, ],
        [1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1, 1, ],
        [1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 1, 1, 1, ],
    ],
]
SHOP_ROOM_MAPS = [
    [
        [1, 3, 0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 1, 1, 0, 0, 0, 0, 0, 3, 1, ],
        [3, 3, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 3, 3, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, ],
        [3, 3, 3, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, ],
        [3, 3, 3, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, ],
        [3, 3, 3, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, ],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [3, 3, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 3, 3, ],
        [1, 3, 0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 1, 1, 0, 0, 0, 0, 0, 3, 1, ],
    ],
]

# Room Types
START_ROOM = 0
FIGHT_ROOM = 1
TREASURE_ROOM = 2
BOSS_ROOM = 3
SHOP_ROOM = 4
ROOM_INFO = {
    0: {
        "dimensions": (6, 6),
        "generation_options": [],
        "base": START_ROOM_MAPS
    },
    1: {
        "dimensions": (7, 7),
        "generation_options": [],
        "base": FIGHT_ROOM_MAPS
    },
    2: {
        "dimensions": (6, 5),
        "generation_options": [],
        "base": TREASURE_ROOM_MAPS
    },
    3: {
        "dimensions": (9, 9),
        "generation_options": [],
        "base": BOSS_ROOM_MAPS
    },
    4: {
        "dimensions": (10, 7),
        "generation_options": [
            {
                "id": SECONDARY_FLOOR,
                "overrides": [FLOOR],
                "seed_amount": 3,
                "seed_type": "blob",
                "b_spread_amount": 5,
                "b_spread_additional": 90
            }
        ],
        "base": SHOP_ROOM_MAPS
    }
}

# Styles
TILESET_DIMENSIONS = (10, 5)
ICE = 0
VOLCANO = 1
STYLES = [ICE, VOLCANO]
