def solution(prices, notes, t):
      l = []
      for i in range(len(prices)):
            f =notes[i].split('%')
            g = 1 if 'higher' in notes[i] else 2 if 'lower' in  notes[i] else 3
            if g ==3:
                  l.append(0)
            elif g == 1:
                  x = 100 * prices[i] /( 100+float(f[0]))
                  l.append(abs(x-prices[i]))
            elif g==2 :
                  x = 100 * prices[i] / (100 -float(f[0]))

                  l.append((x-prices[i])*-1)

      return sum(l)<=t


print(dir())
f = ["20.00% lower than in-store",
         "10.00% higher than in-store"]
prices = [48, 165]
print(solution(prices,f,2))
print()
print()
print()
print()
print()
f='Same as in-store'
x = f.split('%')
g = 1 if  'higher' in f   else  2 if   'lower' in f else 3
print('higher' in f)
print(g)


print(x)
x = 100 * 48 / 80
print(x)

x = 100 * 165 / 110
print(x)