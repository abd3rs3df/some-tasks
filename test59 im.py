def solution(n):
    ll=[]
    f=1
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
            f+=1
        ll.append(l)

    x = 0
    y = 0
    v = 1


    Right = True
    down = False
    up = False
    Left = False
    cheRight = len(ll) - 1
    chedown = len(ll) - 1
    cheLeft = 0
    cheup = 0
    while v < len(ll) * len(ll) + 1:
        if Right:
            ll[x][y] = v
            y += 1
            if y - 1 == cheRight:
                y -= 1
                cheup += 1
                Right = False
                down = True
                x += 1
        elif down:
            ll[x][y] = v
            x += 1
            if x == chedown + 1:
                cheRight -= 1
                down = False
                Left = True
                y -= 1
                x -= 1
        elif Left:
            ll[x][y] = v
            y -= 1
            if y == cheLeft - 1:
                Left = False
                up = True
                chedown -= 1
                y += 1
                x -= 1


        elif up:
            ll[x][y] = v
            x -= 1
            if x == cheup - 1:
                up = False
                Right = True
                cheLeft += 1
                x += 1
                y += 1
        v += 1



    return ll


print(solution(6))

