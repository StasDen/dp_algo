# Coins problem: how many ways to represent sum by given coins
# Using dp


def repr_ways(coins: list[int], n: int, s: int) -> int:  # s == sum
    # Initializing dp arr
    table = [[0 for x in range(n)] for x in range(s + 1)]

    # Setting val for first row
    for i in range(n):
        table[0][i] = 1

    # Setting left val
    for i in range(1, s + 1):
        for j in range(n):
            # Num of ways including coins[j]
            x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0

            # Num of ways excluding coins[j]
            y = table[i][j - 1] if j >= 1 else 0

            # Res = possible ways when including + excluding coin
            table[i][j] = x + y

    # Returning last val in dp arr
    return table[s][n - 1]
