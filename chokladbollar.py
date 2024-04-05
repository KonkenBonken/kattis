bags = int(input())
B, S = (int(x) for x in input().split())

total = B + S
per_bag, overflow = divmod(total, bags)

if bags == 2:
    print(abs(B-S)//2)
