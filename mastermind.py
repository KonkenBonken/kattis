n, code, guess = input().split()
n = int(n)
code = list(code)
guess = list(guess)

r, s, i = 0, 0, 0

while i < len(code):
    if code[i] == guess[i]:
        r += 1
        del code[i]
        del guess[i]
    else:
        i += 1

i = 0
while i < len(code):
    if guess[i] in code:
        s += 1
        del code[code.index(guess[i])]
        del guess[i]
    else:
        i += 1


print(r, s)
