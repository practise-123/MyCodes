# Created by        : MyWork
# Created on        : 2024-06-05

from unittest import TestCase
from configs import logger

"""
Inputs : mxn Matrix, r:int -> rotations
Assuming m,n>=2
Assuming r>=0
rotate the matrix layers r times

layers in 4x4
* * * *
* $ $ *
* $ $ *
* * * *

ALGO -> 0:
1. Find the layers
2. Rotate the layers
3. Form Matrix from layers
"""


class Algorithm:

    def __init__(self):
        pass

    def run(self, *args, **kwargs):
        if kwargs:
            matrix = kwargs.get('matrix', [])
            r = kwargs.get('r', 0)
            logger.debug(f"matrix : {matrix} rotations :{r}")
            return self.logic(matrix, r)
        else:
            logger.warning("provide input")

    @staticmethod
    def no_of_layers(m: int, n: int) -> int:
        layers = 0
        if m and n:
            layers = (min(m, n) // 2) + (min(m, n) % 2)
        logger.debug(f"total layers : {layers}")
        return layers

    @staticmethod
    def get_layers(m, n, lc, matrix):
        m, n = m - 1, n - 1
        c = 0
        idx_layers = []
        layers = []
        while c < lc:
            idx, val = [], []
            for j in range(c, n - c):
                idx.append((c, j))
                val.append(matrix[c][j])

            for i in range(c, m - c):
                idx.append((i, n - c))
                val.append(matrix[i][n - c])

            for j in range(c, n - c):
                idx.append((m - c, n - j))
                val.append(matrix[m - c][n - j])

            for i in range(c, m - c):
                idx.append((m - i, c))
                val.append(matrix[m - i][c])

            logger.debug(f"layer {c} : {idx}")
            if idx and len(idx) > 0:
                idx_layers.append(idx)
            if val and len(val) > 0:
                layers.append(val)
            c += 1
        return idx_layers, layers

    @staticmethod
    def shift(layers: list[list[int]], rotations: int) -> list[list[int]]:
        logger.info(f"rotations : {rotations}")
        new_layers = []
        for layer in layers:
            if layer and len(layer) > rotations:
                layer = layer[-rotations:] + layer[:-rotations]
            elif layer and len(layer) < rotations and rotations // len(layer):
                rotations = rotations // len(layer)
                layer = layer[-rotations:] + layer[:-rotations]
            new_layers.append(layer)
        return new_layers

    @staticmethod
    def form_matrix(idx: list[list[(int, int)]],
                    vals: list[list[int]], matrix: list[list[int]]) -> list[list[int]]:
        for lyr in range(len(idx)):
            for x in range(len(idx[lyr])):
                p = idx[lyr][x]
                matrix[p[0]][p[1]] = vals[lyr][x]
        return matrix

    def logic(self, matrix, rotations: int) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        lc = self.no_of_layers(m, n)
        idx, layers = self.get_layers(m, n, lc, matrix)
        after_shift = self.shift(layers, rotations)
        rotated_matrix = self.form_matrix(idx, after_shift, matrix)
        return rotated_matrix


class TestAlgorithm(TestCase):
    def setUp(self) -> None:
        self.algorithm = Algorithm()

    def test_2x2(self):
        matrix = [[1, 2], [3, 4]]
        m, n = len(matrix), len(matrix[0])
        lc = self.algorithm.no_of_layers(m, n)
        idx, layers = self.algorithm.get_layers(m, n, lc, matrix)
        after_shift = self.algorithm.shift(layers, rotations=1)

        self.assertEqual(lc, 1)
        self.assertEqual(idx, [[(0, 0), (0, 1), (1, 1), (1, 0)]])
        self.assertEqual(after_shift, [[3, 1, 2, 4]])

    def test_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m, n = len(matrix), len(matrix[0])
        lc = self.algorithm.no_of_layers(m, n)
        idx, layers = self.algorithm.get_layers(m, n, lc, matrix)
        after_shift = self.algorithm.shift(layers, rotations=1)
        self.assertEqual(lc, 2)
        self.assertEqual(idx, [
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)],
            # [(2,2)]
        ])
        self.assertEqual(after_shift, [
            [4, 1, 2, 3, 6, 9, 8, 7],
            # [5]
        ])

    def test_4x4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        m, n = len(matrix), len(matrix[0])
        lc = self.algorithm.no_of_layers(m, n)
        idx, layers = self.algorithm.get_layers(m, n, lc, matrix)
        after_shift = self.algorithm.shift(layers, rotations=1)
        self.assertEqual(lc, 2)
        self.assertEqual(idx, [
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0)],
            [(1, 1), (1, 2), (2, 2), (2, 1)]
        ])
        self.assertEqual(after_shift, [
            [5, 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9],
            [10, 6, 7, 11]
        ])

    def test_5x5(self):
        matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        m, n = len(matrix), len(matrix[0])
        lc = self.algorithm.no_of_layers(m, n)
        idx, layers = self.algorithm.get_layers(m, n, lc, matrix)
        after_shift = self.algorithm.shift(layers, rotations=1)
        self.assertEqual(lc, 3)
        self.assertEqual(idx, [
            [(0, 0), (0, 1), (0, 2), (0, 3),
             (0, 4), (1, 4), (2, 4), (3, 4),
             (4, 4), (4, 3), (4, 2), (4, 1),
             (4, 0), (3, 0), (2, 0), (1, 0)],
            [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)],
            # [13]
        ])
        self.assertEqual(after_shift, [
            [6, 1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11],
            [12, 7, 8, 9, 14, 19, 18, 17],
            # [13]
        ])


if __name__ == "__main__":
    # mtx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # mtx = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    mtx = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    r = 3
    alg = Algorithm()
    result = alg.run(matrix=mtx, r=r)
    logger.info(f"result : {result}")
