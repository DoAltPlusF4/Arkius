"""Contains constants used for the game."""

# Window
MIN_SIZE = (568, 320)
UPDATE_SPEED = 1/120
DEFAULT_SCALE_DIVISOR = 320

# Tile Types
FLOOR = 0
WALL = 1
PIT = 2
SECONDARY_FLOOR = 3
TILE_TYPES = [FLOOR, WALL, PIT, SECONDARY_FLOOR]

# Tilemaps
DEFAULT_ROOM_SIZE = 7
DEFAULT_MAP_SETTINGS = {
    WALL: {
        "base_chance": 10,
        "spread_chance": 20,
        "spread_type": "wall"
    },
    SECONDARY_FLOOR: {
        "base_chance": 15,
        "spread_chance": 25,
        "spread_type": "blob",
        "favour_centre": False
    },
    PIT: {
        "base_chance": 20,
        "spread_chance": 15,
        "spread_type": "blob",
        "favour_centre": True
    }
}
START_ROOM_MAPS = [
    [
        [1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1],
        [1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 2, 0, 0, 0, 3, 3, 3, 0, 0, 0, 2, 2],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [2, 2, 0, 0, 0, 3, 3, 3, 0, 0, 0, 2, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
        [1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1],
        [1, 1, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 1]
    ]
]
TREASURE_ROOM_MAPS = [
    [
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 0, 0, 1, 1, 3, 3, 3, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 3, 3, 3, 1, 1, 0, 0, 0],
        [2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2]
    ]
]
BOSS_ROOM_MAPS = [
    [
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 2, 0, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, 2, 0, 0, 2, 2],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [3, 3, 3, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 3, 3, 3],
        [3, 3, 3, 0, 1, 0, 0, 2, 2, 2, 2, 2, 0, 0, 1, 0, 3, 3, 3],
        [3, 3, 3, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 3, 3, 3],
        [3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [2, 2, 0, 0, 2, 1, 0, 0, 1, 1, 1, 0, 0, 1, 2, 0, 0, 2, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 2, 2],
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 1, 0, 3, 3, 3, 3, 3, 0, 1, 2, 2, 2, 2, 2]
    ]
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
        "generation_options": {},
        "base": START_ROOM_MAPS
    },
    1: {
        "dimensions": (7, 7),
        "generation_options": DEFAULT_MAP_SETTINGS,
        "base": None
    },
    2: {
        "dimensions": (6, 5),
        "generation_options": {},
        "base": TREASURE_ROOM_MAPS
    },
    3: {
        "dimensions": (9, 9),
        "generation_options": {},
        "base": BOSS_ROOM_MAPS
    },
    4: {
        "dimensions": (10, 7),
        "generation_options": DEFAULT_MAP_SETTINGS,
        "base": None
    }
}

# Styles
ICE = 0
VOLCANO = 1
STYLES = [ICE, VOLCANO]

# Player
PLAYER_SPEED = 4
DIAGONAL_MULTIPLIER = 0.7
