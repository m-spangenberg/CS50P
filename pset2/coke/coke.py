def main():
    """Dr.Pepper is actually amazing too!"""
    valid_coins = [25, 10, 5]
    cost = 50
    tendered = 0
    # This is a fancy loop, this is a fancy loop, this is a...
    while tendered < cost:
        print(f"Amount Due: {cost - tendered}")
        money = int(input(f"Insert Coin: ").strip())
        if money in valid_coins:
            tendered += money
        else:
            continue
    print(f"Change Owed: {tendered - cost}")


main()
