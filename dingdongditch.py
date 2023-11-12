input()
houses = sorted(int(x) for x in input().split())
friends = (int(x) for x in input().split())

for count in friends:
    print(sum(houses[:count]))
