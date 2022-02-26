def solution(n):
  l =[]
  ll=[]
  while  n!=0 :
      l.insert(0 ,n%(10))
      n//=10

  for i in range(len(l)):
      s = [str(i) for i in l[:i]+l[i+1:len(l)]]
      ll.append(int(''.join(s)))
  return max(ll)

print(solution(1234))

print(max(['111111','4444','1']))