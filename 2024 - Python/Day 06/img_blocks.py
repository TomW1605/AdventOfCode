import numpy as np

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
        [S, S, S, S, S],
        [S, S, S, S, S],
        [S, S, S, S, S],
        [S, S, S, S, S],
        [S, S, S, S, S],
    ]).astype(np.uint8)[:, :, :3]

    class Empty:
        NONE = np.array([
            [B, B, B, B, B],
            [B, B, B, B, B],
            [B, B, B, B, B],
            [B, B, B, B, B],
            [B, B, B, B, B],
        ]).astype(np.uint8)[:, :, :3]

        TOP = np.array([
            [C, C, Y, C, C],
            [C, C, Y, C, C],
            [C, C, Y, C, C],
            [C, C, C, C, C],
            [C, C, C, C, C],
        ]).astype(np.uint8)

        BOTTOM = np.array([
            [C, C, C, C, C],
            [C, C, C, C, C],
            [C, C, Y, C, C],
            [C, C, Y, C, C],
            [C, C, Y, C, C],
        ]).astype(np.uint8)

        LEFT = np.array([
            [C, C, C, C, C],
            [C, C, C, C, C],
            [Y, Y, Y, C, C],
            [C, C, C, C, C],
            [C, C, C, C, C],
        ]).astype(np.uint8)

        RIGHT = np.array([
            [C, C, C, C, C],
            [C, C, C, C, C],
            [C, C, Y, Y, Y],
            [C, C, C, C, C],
            [C, C, C, C, C],
        ]).astype(np.uint8)

    # GUARD = np.array([
    #     [C, C, C, C, C],
    #     [C, C, C, C, C],
    #     [C, C, R, C, C],
    #     [C, C, C, C, C],
    #     [C, C, C, C, C],
    # ]).astype(np.uint8)
    #
    # class Guard:
    #     UP = np.array([
    #         [C, C, C, C, C],
    #         [C, C, R, C, C],
    #         [C, R, R, R, C],
    #         [C, R, R, R, C],
    #         [C, C, C, C, C],
    #     ]).astype(np.uint8)
    #
    #     DOWN = np.array([
    #         [C, C, C, C, C],
    #         [C, R, R, R, C],
    #         [C, R, R, R, C],
    #         [C, C, R, C, C],
    #         [C, C, C, C, C],
    #     ]).astype(np.uint8)
    #
    #     LEFT = np.array([
    #         [C, C, C, C, C],
    #         [C, C, R, R, C],
    #         [C, R, R, R, C],
    #         [C, C, R, R, C],
    #         [C, C, C, C, C],
    #     ]).astype(np.uint8)
    #
    #     RIGHT = np.array([
    #         [C, C, C, C, C],
    #         [C, R, R, C, C],
    #         [C, R, R, R, C],
    #         [C, R, R, C, C],
    #         [C, C, C, C, C],
    #     ]).astype(np.uint8)
