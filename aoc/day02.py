"""Day 2: 1202 Program Alarm"""

from typing import List


def run_intcode(code: List[int]) -> List[int]:
    """Runs an intcode program.

    An Intcode program is a list of integers separated by commas.
    Valid opcodes are either 1, 2, or 99.

    Opcode 1 adds together numbers read from two positions and stores the result in a
    third position, while 2 does the same but multiplies instead. In either case after
    performing the insteuction the next opcode is found by stepping forward 4 positions.
    Opcode 99 terminatesthe program.

    Examples:
    >>> run_intcode([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]

    >>> run_intcode([2, 3, 0, 3, 99])
    [2, 3, 0, 6, 99]

    >>> run_intcode([2, 4, 4, 5, 99, 0])
    [2, 4, 4, 5, 99, 9801]

    >>> run_intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
    [30, 1, 1, 4, 2, 5, 6, 0, 99]

    >>> run_intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

    :param code: Intcode program in list form
    :returns: New list of program output
    """
    code = code.copy()
    index = 0

    while index < len(code):
        opcode = code[index]
        if opcode == 1:
            code[code[index + 3]] = code[code[index + 1]] + code[code[index + 2]]
        elif opcode == 2:
            code[code[index + 3]] = code[code[index + 1]] * code[code[index + 2]]
        elif opcode == 99:
            break
        else:
            raise RuntimeError(f"Unexpected opcode {opcode} at position {index}.")

        index = index + 4

    return code


if __name__ == "__main__":
    # run tests
    import doctest

    doctest.testmod()

    with open("inputs/02.txt") as infile:
        PROGRAM = [int(code) for code in infile.readline().split(",")]

    PROGRAM[1] = 12
    PROGRAM[2] = 2
    print("Part 1:", run_intcode(PROGRAM)[0])

    for possible_noun in range(99):
        for possible_verb in range(99):
            PROGRAM[1] = possible_noun
            PROGRAM[2] = possible_verb
            if run_intcode(PROGRAM)[0] == 19690720:
                print("Part 2:", 100 * possible_noun + possible_verb)
