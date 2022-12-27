# Players problem: max games for player to play in order to win the tournament
# Using dp


def max_games_played_by_winner(n: int) -> int:
    # Initializing dp arr
    dp: list[int] = [0 for i in range(n)]

    # 1 player == 0 games
    if n == 1:
        return 0

    # Setting dp arr
    # For 0 games 1 player is required
    dp[0] = 1
    # For 1 game 2 players are required
    dp[1] = 2

    i = 1
    # While num of games is less than set games num - looping and using Fibonacci numbers
    while dp[i] < n:
        i = i + 1
        dp[i] = dp[i - 1] + dp[i - 2]  # Fibonacci numbers

    # If dp arr val == set val - returning it
    if dp[i] == n:
        return i

    # Returning max val in dpp arr("i - 1" because of loop)
    return i - 1
