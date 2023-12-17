import numpy as np
from PIL import Image

class Colour:
    BLACK = [0, 0, 0, 255]
    SILVER = [180, 180, 180, 255]
    YELLOW = [0, 242, 255, 255]
    RED = [239, 183, 0, 255]
    CLEAR = [0, 0, 0, 0]

B = Colour.BLACK
S = Colour.SILVER
Y = Colour.YELLOW
R = Colour.SILVER
C = Colour.CLEAR

class Block:
    WALL = np.array([
        [S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S],
    ]).astype(np.uint8)[:, :, :3]
    class Empty:
        NONE = np.array([
            [B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B],
        ]).astype(np.uint8)[:, :, :3]

        HORIZONTAL = np.array([
            [C, C, C, C, C, C, C, C],
            [C, C, C, C, C, C, C, C],
            [C, C, C, C, C, C, C, C],
            [Y, Y, Y, Y, Y, Y, Y, Y],
            [Y, Y, Y, Y, Y, Y, Y, Y],
            [C, C, C, C, C, C, C, C],
            [C, C, C, C, C, C, C, C],
            [C, C, C, C, C, C, C, C],
        ]).astype(np.uint8)

        VERTICAL = np.array([
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
        ]).astype(np.uint8)

        BOTH = np.array([
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [Y, Y, Y, Y, Y, Y, Y, Y],
            [Y, Y, Y, Y, Y, Y, Y, Y],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
            [C, C, C, Y, Y, C, C, C],
        ]).astype(np.uint8)

    class Mirror:
        class Left:
            NONE = np.array([
                [B, B, B, B, B, B, B, B],
                [B, S, S, B, B, B, B, B],
                [B, S, S, S, B, B, B, B],
                [B, B, S, S, S, B, B, B],
                [B, B, B, S, S, S, B, B],
                [B, B, B, B, S, S, S, B],
                [B, B, B, B, B, S, S, B],
                [B, B, B, B, B, B, B, B],
            ]).astype(np.uint8)[:, :, :3]

            LEFT = np.array([
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [Y, Y, C, C, C, C, C, C],
                [Y, Y, Y, C, C, C, C, C],
                [C, C, C, Y, C, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            BOTTOM = LEFT

            RIGHT = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, C, Y, C, C, C],
                [C, C, C, C, C, Y, Y, Y],
                [C, C, C, C, C, C, Y, Y],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
            ]).astype(np.uint8)

            TOP = RIGHT

            BOTH = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, C, Y, C, C, C],
                [Y, Y, C, C, C, Y, Y, Y],
                [Y, Y, Y, C, C, C, Y, Y],
                [C, C, C, Y, C, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)
        class Right:
            NONE = np.array([
                [B, B, B, B, B, B, B, B],
                [B, B, B, B, B, S, S, B],
                [B, B, B, B, S, S, S, B],
                [B, B, B, S, S, S, B, B],
                [B, B, S, S, S, B, B, B],
                [B, S, S, S, B, B, B, B],
                [B, S, S, B, B, B, B, B],
                [B, B, B, B, B, B, B, B],
            ]).astype(np.uint8)[:, :, :3]

            LEFT = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [Y, Y, Y, C, C, C, C, C],
                [Y, Y, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
            ]).astype(np.uint8)

            TOP = LEFT

            RIGHT = np.array([
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, Y, Y],
                [C, C, C, C, C, Y, Y, Y],
                [C, C, C, C, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            BOTTOM = RIGHT

            BOTH = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, C, C, C, C],
                [Y, Y, Y, C, C, C, Y, Y],
                [Y, Y, C, C, C, Y, Y, Y],
                [C, C, C, C, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

    class Splitter:
        class Horizontal:
            NONE = np.array([
                [B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B],
                [B, B, R, R, R, R, B, B],
                [B, B, R, R, R, R, B, B],
                [B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B],
            ]).astype(np.uint8)[:, :, :3]

            TOP = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [Y, Y, C, C, C, C, Y, Y],
                [Y, Y, C, C, C, C, Y, Y],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
            ]).astype(np.uint8)

            BOTTOM = np.array([
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [Y, Y, C, C, C, C, Y, Y],
                [Y, Y, C, C, C, C, Y, Y],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            BOTH = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [Y, Y, C, C, C, C, Y, Y],
                [Y, Y, C, C, C, C, Y, Y],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            LEFT = np.array([
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [Y, Y, C, C, C, C, Y, Y],
                [Y, Y, C, C, C, C, Y, Y],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
            ]).astype(np.uint8)

            RIGHT = LEFT
        class Vertical:
            NONE = np.array([
                [B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B],
                [B, B, B, R, R, B, B, B],
                [B, B, B, R, R, B, B, B],
                [B, B, B, R, R, B, B, B],
                [B, B, B, R, R, B, B, B],
                [B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B],
            ]).astype(np.uint8)[:, :, :3]

            LEFT = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, C, C, C, C, C],
                [Y, Y, Y, C, C, C, C, C],
                [Y, Y, Y, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            RIGHT = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, Y, Y, Y],
                [C, C, C, C, C, Y, Y, Y],
                [C, C, C, C, C, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            BOTH = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, C, C, C, C, C],
                [Y, Y, Y, C, C, Y, Y, Y],
                [Y, Y, Y, C, C, Y, Y, Y],
                [C, C, C, C, C, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            TOP = np.array([
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, C, C, C, C, C],
                [C, C, C, Y, Y, C, C, C],
                [C, C, C, Y, Y, C, C, C],
            ]).astype(np.uint8)

            BOTTOM = TOP
