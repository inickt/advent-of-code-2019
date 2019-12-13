"""Day 3: Crossed Wires"""

from typing import List, Tuple


def manhattan_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    """Compute the Manhattan distance between two points"""
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])


def wire_path(wire: List[str]) -> List[Tuple[int, int]]:
    """Get the path of the wire.

    :param wire: List of directions the wire moves
    :return: In order list of points the wire goes through
    """
    path: List[Tuple[int, int]] = []
    position = (0, 0)
    for direction in wire:
        for _ in range(int(direction[1:])):
            if direction[0] == "R":
                position = (position[0] + 1, position[1])
            elif direction[0] == "L":
                position = (position[0] - 1, position[1])
            elif direction[0] == "U":
                position = (position[0], position[1] + 1)
            elif direction[0] == "D":
                position = (position[0], position[1] - 1)
            path.append(position)
    return path


def intersection_distance(
    wire1_path: List[Tuple[int, int]], wire2_path: List[Tuple[int, int]]
) -> int:
    """Find the two wire's Manhattan distance of the intersection point closest to the central port.

    Examples:
    >>> intersection_distance(EX1_W1_PATH, EX1_W2_PATH)
    6

    >>> intersection_distance(EX2_W1_PATH, EX2_W2_PATH)
    159

    >>> intersection_distance(EX3_W1_PATH, EX3_W2_PATH)
    135

    :param wire1_path: The first wire's path
    :param wire2_path: The second wire's path
    :return: Minimum distance to first intersection
    """
    return manhattan_distance(
        (0, 0),
        min(
            set(wire1_path).intersection(set(wire2_path)),
            key=lambda pos: manhattan_distance((0, 0), pos),
        ),
    )


def fewest_steps(
    wire1_path: List[Tuple[int, int]], wire2_path: List[Tuple[int, int]]
) -> int:
    """Find the fewest steps to get to an intersection between two wires.

    >>> fewest_steps(EX2_W1_PATH, EX2_W2_PATH)
    610

    >>> fewest_steps(EX3_W1_PATH, EX3_W2_PATH)
    410

    :param wire1_path: The first wire's path
    :param wire2_path: The second wire's path
    :return: Fewest steps to an intersection
    """
    return min(
        [
            2 + wire1_path.index(intersection) + wire2_path.index(intersection)
            for intersection in set(wire1_path).intersection(set(wire2_path))
        ]
    )


# Examples
EX1_W1_PATH = wire_path(["R8", "U5", "L5", "D3"])
EX1_W2_PATH = wire_path(["U7", "R6", "D4", "L4"])

EX2_W1_PATH = wire_path(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"])
EX2_W2_PATH = wire_path(["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"])

EX3_W1_PATH = wire_path(
    ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
)
EX3_W2_PATH = wire_path(
    ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
)

if __name__ == "__main__":
    # run tests
    import doctest

    doctest.testmod()

    with open("inputs/03.txt") as infile:
        WIRE1 = infile.readline().split(",")
        WIRE2 = infile.readline().split(",")

    WIRE1_PATH = wire_path(WIRE1)
    WIRE2_PATH = wire_path(WIRE2)

    print("Part 1:", intersection_distance(WIRE1_PATH, WIRE2_PATH))
    print("Part 2:", fewest_steps(WIRE1_PATH, WIRE2_PATH))
