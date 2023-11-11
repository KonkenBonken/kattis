plot_count, budget = (int(x) for x in input().split())
plots = [int(x) for x in input().split()]


def total(start, length):
    sum = 0
    for i in range(length):
        sum += plots[start+i]
    return sum


def main():
    for l in range(plot_count+1, 0, -1):
        for i in range(plot_count-l+1):
            if total(i, l) <= budget:
                print(l)
                return


main()
