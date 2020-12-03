import unittest

import day_1
import day_2
import day_3

class TestDay1(unittest.TestCase):
    input_example = """1721
979
366
299
675
1456"""
    example_nb = [int(n) for n in input_example.split("\n")]

    def test_part_one(self):
        self.assertEqual(day_1.part_one(TestDay1.example_nb), 514579)

    def test_part_two(self):
        self.assertEqual(day_1.part_two(TestDay1.example_nb), 241861950)

class TestDay2(unittest.TestCase):
    with open("input_example_day_2.txt") as f:
        example = f.read()

    def test_part_one(self):
        self.assertEqual(day_2.part_one(TestDay2.example, verbose=False), 2)
        
    def test_part_two(self):
        self.assertEqual(day_2.part_two(TestDay2.example, verbose=False), 1)

class TestDay3(unittest.TestCase):
    with open("input_example_day_3.txt") as f:
        example = f.read()

    def test_part_one(self):
        self.assertEqual(day_3.part_one(TestDay3.example, verbose=False), 7)
        
    def test_part_two(self):
        self.assertEqual(day_3.part_two(TestDay3.example, verbose=False), 336)


unittest.main()