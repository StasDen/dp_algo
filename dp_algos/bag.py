# Weighted bag problem: buy goods to store exactly bag weight with min cost
# Using dp memoization


import sys


# Helper func
def bag_helper(cost: list[int], weight: list[int], n: int, w: int, dp: list[list[int]]) -> int:
    # If weight is 0 - returning 0 cost
    if w == 0:
        return 0

    # If w < 0 or cost list is empty - returning max val
    if w < 0 or n <= 0:
        return sys.maxsize  # sys.maxsize == 2^63

    # If we have already computed val in dp arr - returning it
    if dp[n][w] != -1:
        return dp[n][w]

    # If val in cost list < 0 - storing min val in dp and returning it
    if cost[n - 1] < 0:
        dp[n][w] = min(sys.maxsize, bag_helper(cost, weight, n - 1, w, dp))
        return dp[n][w]

    # If val in weight list < weight in bag - returning min between current including previous val AND current val(
    # without previous)
    if weight[n - 1] <= w:
        dp[n][w] = min(cost[n - 1] + bag_helper(cost, weight, n, w - weight[n - 1], dp),
                       bag_helper(cost, weight, n - 1, w, dp))
        return dp[n][w]

    # Storing val in dp arr and returning it
    dp[n][w] = bag_helper(cost, weight, n - 1, w, dp)
    return dp[n][w]


# Main func
def bag_min_cost(cost: list[int], w: int) -> int:
    # Getting necessary param val in order to use helper func
    n: int = len(cost)

    # Creating weight arr
    weight: list[int] = [0 for i in range(n)]
    for i in range(1, n + 1):
        weight[i - 1] = i

    # Initializing default dp arr
    dp: list[list[int]] = [[-1 for i in range(w + 1)] for j in range(n + 1)]

    res: int = bag_helper(cost, weight, n - 1, w, dp)

    # Returning res if res != sys.maxsize
    return -1 if res == sys.maxsize else res
