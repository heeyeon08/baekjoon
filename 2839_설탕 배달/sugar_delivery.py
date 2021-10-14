def Sugar(n):
  r = 0

  while(1):
    if n % 5 == 0:
      r += n // 5
      return r
      
    n = n - 3
    r += 1

    if n < 3 and n != 0:
      return -1

n = int(input())

print(Sugar(n))
