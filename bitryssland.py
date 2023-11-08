N, M = (int(x)for x in input().split())
coins = (int(x)for x in input().split())
products = (int(x)for x in input().split())

balance = sum(count * 2**i for i, count in enumerate(coins))

for price in products:
    balance -= price
    if balance < 0:
        print('nej')
        break
else:
    print('ja' if balance == 0 else 'nej')
