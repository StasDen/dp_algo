# Tiling problem: num of ways to place 2 * 1 tile in 2 * n board
# Using recursion


def num_of_ways(n: int) -> int:
    # Base cases
    if n <= 2:
        return n

    # Placing horizontally(n - 2) or vertically(n - 1)
    return num_of_ways(n - 2) + num_of_ways(n - 1)
