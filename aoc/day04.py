"""Day 4: Secure Container"""

from collections import Counter
from typing import List


def has_adjacent(num: int) -> bool:
    """Does the number have at least one grouping of 2 or more digits?

    >>> has_adjacent(0)
    False

    >>> has_adjacent(11)
    True

    >>> has_adjacent(15)
    False

    >>> has_adjacent(123345)
    True

    >>> has_adjacent(123455)
    True
    """
    str_num = str(num)
    return any(str_num[i] == str_num[i + 1] for i in range(len(str_num) - 1))


def never_decreases(num: int) -> bool:
    """Does the number have digits that never decrease left to right?

    >>> never_decreases(0)
    True

    >>> never_decreases(9)
    True

    >>> never_decreases(1111)
    True

    >>> never_decreases(13579)
    True

    >>> never_decreases(1235672)
    False
    """
    digits = [int(digit) for digit in str(num)]
    last = 0
    for digit in digits:
        if last > digit:
            return False
        last = digit
    return True


def is_valid_password(num: int) -> bool:
    """Is the given number a valid password?
    
    >>> is_valid_password(111111)
    True

    >>> is_valid_password(122345)
    True
        
    >>> is_valid_password(111123)
    True

    >>> is_valid_password(135679)
    False

    >>> is_valid_password(223450)
    False

    >>> is_valid_password(123789)
    False
    """
    return len(str(num)) == 6 and has_adjacent(num) and never_decreases(num)


def valid_passwords(start: int, stop: int) -> List[int]:
    """Get all valid passwords in the given range"""
    return [num for num in range(start, stop + 1) if is_valid_password(num)]


def has_adjacent_grouping(num: int) -> bool:
    """Does the number have at least one grouping of 2 digits?

    >>> has_adjacent_grouping(0)
    False

    >>> has_adjacent_grouping(11)
    True

    >>> has_adjacent_grouping(15)
    False

    >>> has_adjacent_grouping(123345)
    True

    >>> has_adjacent_grouping(123455)
    True

    >>> has_adjacent_grouping(123444)
    False
    
    :param num: [description]
    :return: [description]
    """
    return any(
        count == 2 for count in Counter(int(digit) for digit in str(num)).values()
    )


if __name__ == "__main__":
    # run tests
    import doctest

    doctest.testmod()

    with open("inputs/04.txt") as infile:
        start, stop = [int(num) for num in infile.readline().split("-")]

    part1_passwords = valid_passwords(start, stop)
    part2_passwords = [num for num in part1_passwords if has_adjacent_grouping(num)]

    print("Part 1:", len(part1_passwords))
    print("Part 2:", len(part2_passwords))
