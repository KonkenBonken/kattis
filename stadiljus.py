N, price, max_mean = int(input()), int(input()), int(input())
places = [int(x)*price for x in input().split()]

places.sort()
sum = 0

for i, place in enumerate(places):
    if (sum+place)//(i+1) <= max_mean:
        sum += place
    else:
        print(i)
        break
else:
    print(N)
