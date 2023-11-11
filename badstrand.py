plot_count, budget = (int(x) for x in input().split())
plots = [int(x) for x in input().split()]

for l in range(plot_count+1, 0, -1):
    for i in range(plot_count-l+1):
        if sum(plots[i:i+l]) <= budget:
            print(l)
            exit()
