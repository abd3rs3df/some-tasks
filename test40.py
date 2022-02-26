def solution(n):
    count = 0
    if n // 10 == 0 : 
        return 0
    while True :
        if n //10 == 0:
            return count
        x= [int(i) for i in str(n)]
        print(x)
        count+=1
        if (sum(x))== 1:
            return count
        n = sum(x)


print(solution(99))