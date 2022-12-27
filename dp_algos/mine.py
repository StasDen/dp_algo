# Gold mine problem: collect max gold with given 2-D arr
# You can move either right, right up or right bottom
# Using dp


# Helper func
def collect_gold(gold: list[list[int]], x: int, y: int, n: int, m: int, dp: list[list[int]]) -> int:
    # Base case
    if x < 0 or x == n or y == m:
        return 0

    # If we have already computed value in dp arr - returning it
    if dp[x][y] != -1:
        return dp[x][y]

    # Possible moves from current position
    right_upper: int = collect_gold(gold, x - 1, y + 1, n, m, dp)
    right: int = collect_gold(gold, x, y + 1, n, m, dp)
    right_bottom: int = collect_gold(gold, x + 1, y + 1, n, m, dp)

    # Storing move which get us max gold and returning it
    dp[x][y]: int = gold[x][y] + max(max(right_upper, right_bottom), right)
    return dp[x][y]


# Main func
def get_max_gold(gold: list[list[int]], n: int, m: int) -> int:
    # Def val
    max_gold: int = 0

    # Initializing dp arr
    dp: list[list[int]] = [[-1 for i in range(m)] for j in range(n)]

    # Starting from every col
    for i in range(n):
        col_gold: int = collect_gold(gold, i, 0, n, m, dp)

        # Storing(in order to compare with previous res) and returning max val
        max_gold: int = max(max_gold, col_gold)
    return max_gold
