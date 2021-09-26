from typing import List


def cycle_min(mass: List[int], cycle: List[int]) -> int:
    """
    Returns the smallest weight of an elephant in a given cycle.

    :param mass: elephant mass list
    :param cycle: list of subsequent cycle elements
    :return: the smallest weight
    """
    minimum = float('inf')
    for element in cycle:
        if minimum > mass[element]:
            minimum = mass[element]
    return minimum


def cycle_mass(mass: List[int], cycle: List[int]) -> int:
    """
    Returns the total weight of all elephants in a given cycle.

    :param mass: elephant mass list
    :param cycle: list of subsequent cycle elements
    :return: minimum: the total weight
    """
    total_mass = 0
    for element in cycle:
        total_mass += mass[element]
    return total_mass


def elephants() -> int:
    """
    Returns minimal effort required to move the elephants.

    :return: minimal effort
    """
    number_of_elephants: int = int(input())
    mass: List[int] = [int(x) for x in input().split()]
    start_pos: List[int] = [int(x) for x in input().split()]
    end_pos: List[int] = [int(x) for x in input().split()]

    permutation = [0] * number_of_elephants
    for i in range(number_of_elephants):
        permutation[end_pos[i] - 1] = start_pos[i] - 1

    cycles = []
    visited_elements = [False] * number_of_elephants
    for i in range(number_of_elephants):
        if not visited_elements[i]:
            current = i
            cycle = []
            while not visited_elements[current]:
                visited_elements[current] = True
                cycle.append(current)
                current = permutation[current]
            cycles.append(cycle)

    min_effort = 0
    minimal_weight = min(mass)
    for i in range(len(cycles)):
        method1 = cycle_mass(mass, cycles[i]) + (len(cycles[i]) - 2) * cycle_min(mass, cycles[i])
        method2 = cycle_mass(mass, cycles[i]) + cycle_min(mass, cycles[i]) + (len(cycles[i]) + 1) * minimal_weight
        min_effort += min(method1, method2)
    return min_effort


if __name__ == '__main__':
    print(elephants())
