from math import sqrt

Ax, Ay = (int(x) for x in input().split())
Bx, By = (int(x) for x in input().split())
Cx, Cy = (int(x) for x in input().split())

AB = sqrt((Ax-Bx)**2+(Ay-By)**2)
BC = sqrt((Bx-Cx)**2+(By-Cy)**2)
CA = sqrt((Cx-Ax)**2+(Cy-Ay)**2)

if BC > AB and BC > CA:
    Ax += Cx-Ax + Bx-Ax
    Ay += Cy-Ay + By-Ay
    print(Ax, Ay)
if CA > BC and CA > AB:
    Bx += Ax-Bx + Cx-Bx
    By += Ay-By + Cy-By
    print(Bx, By)
if AB > BC and AB > CA:
    Cx += Ax-Cx + Bx-Cx
    Cy += Ay-Cy + By-Cy
    print(Cx, Cy)
