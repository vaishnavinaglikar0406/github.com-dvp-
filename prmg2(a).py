def fibonacci(n):
  if n <= 0: 
    print("Error: N must be greater than 0.") 
    return None
  elif n == 1: 
    return 0 
  elif n == 2: 
    return 1 
  else: 
    return fibonacci(n-1) + fibonacci(n-2) 
    n = int(input("Enter a value for N: ")) 
result = fibonacci(n) 
if result is not None: 
  print("The", n, "th term of the Fibonacci sequence is", result)
