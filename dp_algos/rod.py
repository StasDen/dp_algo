# Rod cutting problem: cut rod to get max profit val
# Using dp


# Just very small needed num
MIN_INT: int = -32767


def get_max_profit(price: list[int], n: int) -> int:
    # Initializing val arr
    val: list[int] = [0 for x in range(n + 1)]
    val[0] = 0

    for i in range(1, n + 1):
        # Def val
        max_val: int = MIN_INT

        # Comparing previous max val and current
        for j in range(i):
            max_val: int = max(max_val, price[j] + val[i - j - 1])

        # Storing new max val in dp arr and returning it
        val[i] = max_val
    return val[n]
