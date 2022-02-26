def solution(time):
    return 0<=int(time[0:2]) <=23 and 0<=int(time[3:]) <=59

print(solution('12:60'))

a,b,e= map(int , [12,3,444])
print(a,b)