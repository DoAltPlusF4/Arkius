"""Contains room configurations."""

GENERATION_OPTIONS = [
    {
        "id": int,
        "overrides": [int, int],
        "seed_amount": int,
        "seed_type": "blob/line",
        "b_spread_amount": int,
        "b_spread_additional": int,
        "b_spread_compound": bool,
        "l_hole_amount": int,
        "l_hole_size_range": (int, int)
    },
]

MAP = {
    "width": int,
    "height": int,
    "door_info": {
        0: {"pos": int, "floor": int},
        1: {"pos": int, "floor": int},
        2: {"pos": int, "floor": int},
        3: {"pos": int, "floor": int},
    },
    "border_type": int,
    "matrix": [
        [int, int, int, ],
        [int, int, int, ],
        [int, int, int, ],
    ]
}

CONFIG = {
    "options": GENERATION_OPTIONS,
    "maps": [MAP, MAP]
}

# Generation Options


# MAPS
M_CROSSROADS_SMALL = {
    "width": 6,
    "height": 6,
    "door_info": {
        0: {"pos": 0, "floor": 4},
        1: {"pos": 0, "floor": 4},
        2: {"pos": 0, "floor": 4},
        3: {"pos": 0, "floor": 4},
    },
    "border_type": 1,
    "matrix": [
        [1, 1, 3, 2, 2, 4, 4, 4, 2, 2, 3, 1, 1, ],
        [1, 3, 3, 2, 2, 4, 4, 4, 2, 2, 3, 3, 1, ],
        [3, 3, 3, 2, 2, 4, 4, 4, 2, 2, 3, 3, 3, ],
        [2, 2, 2, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, ],
        [2, 2, 2, 2, 1, 4, 4, 4, 1, 2, 2, 2, 2, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [2, 2, 2, 2, 1, 4, 4, 4, 1, 2, 2, 2, 2, ],
        [2, 2, 2, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, ],
        [3, 3, 3, 2, 2, 4, 4, 4, 2, 2, 3, 3, 3, ],
        [1, 3, 3, 2, 2, 4, 4, 4, 2, 2, 3, 3, 1, ],
        [1, 1, 3, 2, 2, 4, 4, 4, 2, 2, 3, 1, 1, ],
    ]
}

M_CROSSROADS_LARGE = {
    "width": 15,
    "height": 15,
    "border_type": 1,
    "door_info": {
        0: {"pos": 0, "floor": 4},
        1: {"pos": 0, "floor": 4},
        2: {"pos": 0, "floor": 4},
        3: {"pos": 0, "floor": 4},
    },
    "matrix": [
        [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
            4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, ],
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
            4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, ],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
            4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, ],
        [1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 4, 4,
            4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, ],
        [1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4,
            4, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, ],
        [1, 2, 2, 2, 2, 0, 0, 0, 3, 3, 0, 0, 0, 0, 4, 4,
            4, 0, 0, 0, 3, 3, 3, 0, 0, 0, 2, 2, 2, 2, 1, ],
        [2, 2, 2, 2, 0, 3, 0, 3, 3, 3, 3, 0, 0, 0, 4, 4,
            4, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, 2, ],
        [2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 4,
            4, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 0, 4, 4,
            4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 4, 4,
            4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 4,
            4, 1, 2, 2, 2, 3, 3, 3, 3, 0, 3, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 0, 0, 3, 3, 3, 3, 2, 2, 2, 1, 4, 4,
            4, 1, 2, 2, 2, 0, 3, 3, 0, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 2, 2, 1, 1, 4, 4,
            4, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 4, 4,
            4, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 4, 4,
            4, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 3, 0, 0, 3, 3, 3, 3, 2, 2, 1, 1, 4, 4,
            4, 1, 1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 4,
            4, 1, 2, 2, 2, 3, 3, 0, 3, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 4,
            4, 1, 2, 2, 2, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4,
            4, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 4, 4,
            4, 0, 0, 3, 3, 0, 3, 3, 3, 3, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 4, 4,
            4, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, ],
        [2, 2, 2, 2, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 4, 4,
            4, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 2, 2, 2, 2, ],
        [1, 2, 2, 2, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 4, 4,
            4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 2, 2, 2, 1, ],
        [1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4,
            4, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, ],
        [1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 4, 4,
            4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, ],
        [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
            4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, ],
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
            4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, ],
        [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4,
            4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, ],
    ]
}

M_CORNER_LARGE = {
    "width": 12,
    "height": 12,
    "door_info": {
        0: {"pos": 5, "floor": 0},
        1: {"pos": 8, "floor": 4},
        2: {"pos": -7, "floor": 4},
        3: {"pos": 4, "floor": 0},
    },
    "border_type": 1,
    "matrix": [
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 0, 0, 4, 2, 2, 2, 2, 2, 2, ],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 4, 4, 0, 2, 2, 2, 2, 2, 2, ],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, ],
        [2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0, ],
        [0, 4, 4, 4, 4, 4, 4, 0, 3, 3, 0, 0, 0,
            3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 3, 3, ],
        [0, 4, 0, 4, 4, 4, 4, 0, 3, 0, 0, 3, 0,
            3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [4, 0, 4, 4, 4, 4, 4, 0, 0, 3, 0, 0, 0,
            0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 3, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 3, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 3, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 3, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 3, 3, 3, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 3, 3, 3, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 3, 3, 3, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 3, 3, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 3, 3, 3, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 3, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 3, 3, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
    ]
}

M_QUARTERS_LARGE = {
    "width": 20,
    "height": 20,
    "border_type": 1,
    "door_info": {
        0: {"pos": -11, "floor": 4},
        1: {"pos": 11, "floor": 4},
        2: {"pos": 11, "floor": 4},
        3: {"pos": -11, "floor": 4},
    },
    "matrix": [
        [1, 1, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
        [1, 3, 0, 0, 3, 0, 3, 3, 4, 4, 4, 3, 0, 0, 0, 3, 0, 0, 1, 1, 1,
            1, 1, 0, 3, 0, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [0, 0, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 0, 3, 3, 0, 3, 0, 0, 1, 1,
            1, 0, 0, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, ],
        [3, 0, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 0, 3, 3, 3, 3, 0, 0, 1, 1,
            1, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, ],
        [3, 0, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 0, 3, 3, 0, 0, 0, 1, 1,
            1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, ],
        [3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 0, 0, 0, 0, 0, 0, 1, 1,
            1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, ],
        [3, 0, 0, 3, 3, 3, 3, 3, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
            1, 0, 0, 3, 0, 3, 3, 0, 0, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, ],
        [3, 0, 3, 3, 3, 3, 3, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
        [0, 0, 0, 3, 3, 0, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 3, 3, 3, 0, 0, ],
        [0, 3, 3, 3, 3, 3, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 3, 3, 3, 3, 0, ],
        [3, 3, 3, 3, 3, 3, 0, 3, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 3, 0, 3, 3, 3, 3, 0, ],
        [0, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 3, 3, 3, 0, 0, ],
        [0, 0, 3, 3, 3, 3, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 0, 3, 0, 0, 0, ],
        [0, 0, 0, 0, 3, 3, 0, 3, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1,
            1, 1, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 1, 0, 0, 0, 0, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
            1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 1, ],
        [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, ],
        [1, 1, 0, 0, 0, 3, 3, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
            1, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 1, ],
        [1, 0, 3, 0, 3, 0, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1,
            1, 1, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 1, ],
        [3, 0, 3, 3, 3, 3, 3, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 0, 0, 3, 3, 0, 0, ],
        [3, 3, 3, 3, 3, 3, 0, 3, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 0, 3, 3, 3, 3, 3, 0, ],
        [3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 3, 3, 3, 3, 3, 3, 0, ],
        [3, 3, 3, 3, 3, 3, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 3, 3, 3, 3, 3, 3, 0, ],
        [0, 3, 3, 3, 3, 3, 0, 0, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1,
            1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 0, 3, 3, 3, 3, 3, 0, 3, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 3, 3, 3, 3, 3, 3, 0, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 3, 0, 3, 3, 3, 0, ],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 3, 3, 0, 3, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 3, 0, 3, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 3, 0, 0, 1, 1,
            1, 0, 0, 0, 0, 0, 3, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 3, 3, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 1,
            1, 0, 0, 3, 3, 3, 3, 3, 3, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 1, 1,
            1, 0, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 1,
            1, 0, 0, 0, 3, 3, 3, 3, 3, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 1, 1,
            1, 0, 0, 3, 3, 3, 3, 3, 3, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 0, 0, 1, 1, 1,
            1, 1, 0, 0, 0, 0, 3, 0, 3, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 1, ],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 1, ],
    ]
}


# Config
C_EMPTY = {
    "options": [],
    "maps": [
        None
    ]
}

C_START = {
    "options": [],
    "maps": [
        M_CROSSROADS_SMALL
    ]
}

C_FIGHT_LARGE = {
    "options": [],
    "maps": [
        M_QUARTERS_LARGE,
        M_CORNER_LARGE
    ]
}
