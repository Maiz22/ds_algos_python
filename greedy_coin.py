def greedy_coin(amount:int, coins:list) -> tuple:
    """
    Algorithm taking the amount to pay and a list of avaibable coins.
    Returns the total number of coins and the list of coins 
    needed to match the amount.
    """
    coins.sort(reverse=True)
    coin_list = []
    coins_total = 0
    for coin in coins:
        while coin <= amount:
            coin_list.append(coin)
            amount -= coin
            coins_total += 1
    return coins_total, coin_list


if __name__ == "__main__":
    amount = 97
    coins = [50, 10, 5, 2, 1]
    print(greedy_coin(amount, coins))