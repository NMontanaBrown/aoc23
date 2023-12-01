# codin=utf-8

"""
AOC day 1.
"""

import os
import re

def read_txt_input(day):
    """
    Read the input for the given day and return it as a list of strings.
    """
    with open(os.path.join(os.path.dirname(__file__), f"input_1.txt")) as input_file:
        return input_file.read().splitlines()


def part_1():
    """
    Solution for part 1.
    """
    input = read_txt_input(1)

    numbers = [list(re.findall(r'\d+', test_string)) for test_string in input]
    has_numbers = [item for item in numbers if item]
    join_numbers = ["".join(item) for item in has_numbers]
    calib = [eval("".join([item[0], item[-1]])) for item in join_numbers]
    value = sum(calib)
    return value

value = part_1()
print("Part 1: ", value)

def part_2():
    """
    Solution for part 2.
    """
    input = read_txt_input(1)
    dict_r = {"one": "one1one",
              "two": "two2two",
              "three": "three3three",
              "four": "four4four",
              "five": "five5five",
              "six": "six6six",
              "seven": "seven7seven",
              "eight": "eight8eight",
              "nine": "nine9nine"}
    for key, value in dict_r.items():
        input = [item.replace(key, value) for item in input]
    numbers = [list(re.findall(r'\d+', test_string)) for test_string in input]
    has_numbers = [item for item in numbers if item]
    join_numbers = ["".join(item) for item in has_numbers]
    calib = [eval("".join([item[0], item[-1]])) for item in join_numbers]
    value = sum(calib)
    return value

value = part_2()
print("Part 2: ", value)