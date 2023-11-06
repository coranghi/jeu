h, w = 10, 10
p = [[' ']*w for _ in range(h)]
bx1, bx2, by1, by2 = 0, 1, 0, 0
cx1, cx2, cy1, cy2 = 9, 9, 9, 8
p[by1][bx1] = p[by2][bx2] = 'B'
p[cy1][cx1] = p[cy2][cx2] = 'C'

def s():
    for l in p: print(' '.join(l))
    if (bx1 == cx1 and bx2 == cx2 and by1 == cy1 and by2 == cy2) or (bx1 == cx2 and bx2 == cx1 and by1 == cy2 and by2 == cy1): print("Vous avez gagné !"); return True

while True:
    s()
    m = input("Déplacez le bloc (g pour gauche, d pour droite, h pour haut, b pour bas, t pour tourner): ").lower()
    if m == 'g':
        if bx1 > 0 and bx2 > 0:
            p[by1][bx1] = p[by2][bx2] = ' '
            bx1 -= 1
            bx2 -= 1
    elif m == 'd':
        if bx1 < w-1 and bx2 < w-1:
            p[by1][bx1] = p[by2][bx2] = ' '
            bx1 += 1
            bx2 += 1
    elif m == 'h':
        if by1 > 0 and by2 > 0:
            p[by1][bx1] = p[by2][bx2] = ' '
            by1 -= 1
            by2 -= 1
    elif m == 'b':
        if by1 < h-1 and by2 < h-1 and p[by1+1][bx1] == ' ' and p[by1+1][bx2] == ' ':
            p[by1][bx1] = p[by2][bx2] = ' '
            by1 += 1
            by2 += 1
    elif m == 't':
        p[by1][bx1] = p[by2][bx2] = ' '
        if bx1 == bx2:
            bx2 += 1
            by2 -= 1
        else:
            bx2 = bx1
            by2 = by1 + 1
    p[by1][bx1] = p[by2][bx2] = 'B'
    if s():
        break
