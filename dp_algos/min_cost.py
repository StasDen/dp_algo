# Min cost path: find min cost path to reach arr[m][n] from arr[0][0]
# You can move either left, top or top left
# Using dp


# Needed size vars
r, c = 3, 3


def min_cost(cost: list[list[int]], m: int, n: int) -> int:
    # Initializing dp arr
    tc: list[list[int]] = [[0 for x in range(c)] for x in range(r)]

    # Base case
    tc[0][0] = cost[0][0]

    # Setting first col of dp arr
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]  # Next val = previous + present

    # Setting first row of dp arr
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    # Setting the rest of dp arr
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j], tc[i][j - 1], tc[i - 1][j - 1]) + cost[i][j]  # Possible ways to move

    # Returning last val
    return tc[m][n]
