N, price, max_mean = int(input()), int(input()), int(input())
places = [int(x)*price for x in input().split()]

places.sort()
sum = 0

for i, place in enumerate(places):
    sum += place
    if sum//(i+1) > max_mean:
        print(i)
        break
else:
    print(N)
