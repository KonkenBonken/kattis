# NOT SOLVED

plot_count, budget = (int(x) for x in input().split())
plots = [int(x) for x in input().split()]
start_price = sum(plots)


def main():
    for l in range(plot_count, 0, -1):
        global start_price
        price = start_price
        for i in range(plot_count-l+1):
            if price <= budget:
                print(l)
                return
            if i < plot_count-l:
                price += plots[i+l] - plots[i]
        start_price -= plots[l-1]


main()
