def por_cup(n):
  print(n)
  if n==0:
    return "Chai is finished"
  return por_cup(n-1)

print(por_cup(2))