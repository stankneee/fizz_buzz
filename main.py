for n in range (1,101):
  if n % 3 == 0 and n % 5 == 0:
    n = "fizzbuzz"
  elif n % 5 == 0:
    n = "buzz"
  elif n % 3 == 0:
    n = "fizz"
  print(n)