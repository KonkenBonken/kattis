input()
coins = dict((1 << i, int(x))
             for i, x in enumerate(input().split()))
products = (int(x) for x in input().split())

reversed_keys = list(reversed(coins.keys()))

for price in products:
    for value in reversed_keys:
        if value == 0:
            continue
        div, price = divmod(price, value)
        coins[value] -= div

for value in reversed_keys[:-1]:
    while coins[value] < 0:
        coins[value >> 1] -= 1
        coins[value] += 2

print('nej' if any(x < 0 for x in coins.values()) else 'ja')
