input()
coins = (int(x) for x in input().split())
products = (int(x) for x in input().split())

balance = sum(count * 2**i for i, count in enumerate(coins))
price = sum(products)

print('ja' if balance-price == 0 else 'nej')
