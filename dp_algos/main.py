# Studying dynamic programming
# Different dp problems are here


# from tiles import num_of_ways
# from mine import get_max_gold
# from coins import repr_ways
# from rod import get_max_profit
# from subsequence import find_lcs
# from players import max_games_played_by_winner
# from min_cost import min_cost
from bag import bag_min_cost


def main():
    # ======================= Tiles =======================
    # print(num_of_ways(3))
    # print(num_of_ways(4))

    # ======================= Mine =======================
    # gold = [[1, 3, 1, 5],
    #         [2, 2, 4, 1],
    #         [5, 0, 2, 3],
    #         [0, 6, 1, 2]]
    # n, m = 4, 4
    #
    # print(get_max_gold(gold, n, m))

    # ======================= Coins =======================
    # coins = [1, 2, 3]
    # n = len(coins)
    # s = 4
    #
    # print(repr_ways(coins, n, s))

    # ======================= Rod =======================
    # prices = [1, 5, 8, 9, 10, 17, 17, 20]
    # n = len(prices)
    #
    # print(get_max_profit(prices, n))

    # ======================= Subsequence =======================
    # x = "AGGTAB"
    # y = "GXTXAYB"
    # n = len(x)
    # m = len(y)
    # dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    #
    # print(find_lcs(x, y, n, m, dp))

    # ======================= Players =======================
    # n = 4
    # print(max_games_played_by_winner(n))

    # ======================= Min cost =======================
    # cost = [[1, 2, 3],
    #         [4, 8, 2],
    #         [1, 5, 3]]
    # m, n = 2, 2
    #
    # print(min_cost(cost, 2, 2))

    # ======================= Bag =======================
    cost = [1, 10, 4, 50, 100]
    w = 5

    print(bag_min_cost(cost, w))


if __name__ == "__main__":
    main()
