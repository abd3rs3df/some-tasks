def solution(x):
    y =[]
    for i in range(len(x)):
        for j in range(1, 2):
          if x[i][j] == 1:
                y.append(x[i][0])

    return sum(y)/len(y) if y!=[] else 0.0

