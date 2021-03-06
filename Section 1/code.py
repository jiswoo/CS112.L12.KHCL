def solve():

  n      = 0
  arr    = []
  q      = 0
  profit = -1e9
  p      = 0
  start  = 0


  n = int(input())
  arr = [int(x) for x in input().split()]

  
  if n == 1:
    print(f'{1} {1} {arr[0]}')
    return

  
  for i in range(1, n):
    if arr[i-1] + arr[i] >= arr[i]:
      arr[i] = arr[i-1] + arr[i]
    else:
      start = i

    if arr[i] > profit:
      profit = arr[i]
      p = start
      q = i

  print(f'{p+1} {q+1} {profit}')

solve()
