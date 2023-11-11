plot_count, budget = (int(x) for x in input().split())
plots = [int(x) for x in input().split()]


def main():
    for l in range(plot_count, 0, -1):
        price = sum(plots[:l])
        for i in range(plot_count-l+1):
            if price <= budget:
                print(l)
                return
            if i < plot_count-l:
                price += plots[i+l] - plots[i]


main()
