def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0

    for current_price in stock_prices:
        # Ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price


        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit


stock_prices = [10, 7, 5, 8, 11, 9]
print(get_max_profit(stock_prices))