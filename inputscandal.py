out = []

while True:
    try:
        out.append(input())
    except:
        print(len(out))
        print('\n'.join(out))
        break
