# Created by        : MyWork
# Created on        : 2024-06-04
from unittest import TestCase
from configs import logger


class Algorithm:
    pairs = {"}": "{", ")": "(", "]": "["}

    def __init__(self):
        pass

    def run(self, *args, **kwargs):
        if args:
            s = args[0]
            logger.debug(f"input : {s}")
            return self.logic(s)
        else:
            logger.warning("provide input")

    def logic(self, s: str = None) -> bool:
        # Length check
        if len(s) % 2 != 0:
            return False
        lst = []
        for char in s:
            if char in self.pairs.values():
                lst.append(char)
            elif char in self.pairs.keys() and len(lst) > 0:
                if lst[-1] == self.pairs[char]:
                    lst.pop(-1)
                else:
                    return False
            else:
                return False
        if len(lst) > 0:
            return False
        else:
            return True


class TestAlgorithm(TestCase):
    def setUp(self) -> None:
        self.algorithm = Algorithm()

    def test_one(self):
        self.assertTrue(self.algorithm.run("{}()[]"))

    def test_two(self):
        self.assertTrue(self.algorithm.run("{}([]){{(){[()]}}}"))

    def test_three(self):
        self.assertFalse(self.algorithm.run("{}([]){{({)}{[()]}}}"))
