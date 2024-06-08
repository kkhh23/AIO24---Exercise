def factorial(n):
    # create function to help easy for cal approximate function
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Ví dụ sử dụng
n = 5
result = factorial(n)
print(f"Giai thừa của {n} là: {result}")
