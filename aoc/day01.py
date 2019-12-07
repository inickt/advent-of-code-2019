"""Day 1: The Tyranny of the Rocket Equation"""

from math import floor


def fuel_required(mass: float) -> float:
    """Find fuel required to launch a given module by its mass.

    Take mass, divide by three, round down, and subtract 2.

    Examples:
    >>> fuel_required(12)
    2

    >>> fuel_required(14)
    2

    >>> fuel_required(1969)
    654

    >>> fuel_required(100756)
    33583

    :param mass: Mass of the module
    :return: Fuel required
    """
    return max(floor(mass / 3) - 2, 0)


def total_fuel_required(mass: float) -> float:
    """Find fuel required to launch a given module by its mass (including its fuel).

    Examples:
    >>> total_fuel_required(14)
    2

    >>> total_fuel_required(1969)
    966

    >>> total_fuel_required(100756)
    50346

    :param mass: Mass of the module
    :return: Total fuel required
    """
    if mass > 0:
        fuel_needed = fuel_required(mass)
        return total_fuel_required(fuel_needed) + fuel_needed
    return 0


if __name__ == "__main__":
    # run tests
    import doctest

    doctest.testmod()

    with open("inputs/01.txt") as infile:
        MASSES = [float(mass) for mass in infile.readlines()]

    print("Part 1:", sum(fuel_required(mass) for mass in MASSES))
    print("Part 2:", sum(total_fuel_required(mass) for mass in MASSES))
