def solution(grid):
    l=[]

    for i in range(0,9,3):

        for j in range(9):
            if j % 3 == 0:
                if j!=0:
                    if len(set(l)) < 9:
                        print('333')
                        return False
                    l = []



            for k in grid[j][i:i+3]:
                  l.append(k)
            print(l)

            if len(set(grid[j][0:9]))<9:
                return False
            summ=[]
            for f in range(9):
                summ.append(grid[f][j])
            if len(set(summ))<9:
                return False

    return True


grid=\
[[1,3,2,5,4,6,9,8,7],
 [4,6,5,8,7,9,3,2,1],
 [7,9,8,2,1,3,6,5,4],
 [9,2,1,4,3,5,8,7,6],
 [3,5,4,7,6,8,2,1,9],
 [6,8,7,1,9,2,5,4,3],
 [5,7,6,9,8,1,4,3,2],
 [2,4,3,6,5,7,1,9,8],
 [8,1,9,3,2,4,7,6,5]]

print(solution(grid))

l = [12,12,1]
print(set(l)==len(l))