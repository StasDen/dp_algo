# LCS problem: longest common subsequence of two given strings
# Using dp


def find_lcs(x: str, y: str, m: int, n: int, dp: list[list[int]]) -> int:
    # Basic cases
    if m == 0 or n == 0:
        return 0

    # If we have already computed val in dp arr - returning it
    if dp[m][n] != -1:
        return dp[m][n]

    # If letters are the same - using recursion and returning it
    if x[m - 1] == y[n - 1]:
        dp[m][n] = 1 + find_lcs(x, y, m - 1, n - 1, dp)
        return dp[m][n]

    # If letters are diff - going through both str and returning max lcs
    dp[m][n] = max(find_lcs(x, y, m - 1, n, dp),
                   find_lcs(x, y, m, n - 1, dp))

    return dp[m][n]
