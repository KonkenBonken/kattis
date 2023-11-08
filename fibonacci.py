def F(n):
    if n <= 1:
        return str(n)
    return F(n-1) + F(n-2)
