def factorial(n):
  fact = 1
  while (n >= 1):
      fact = fact * n
      n = n - 1
  return fact
def my_choose(n,k):
  fact_n = factorial(n)
  fact_k = factorial(k)
  n_k = factorial(n-k)
  ans = fact_n/(fact_k*n_k)
  return ans
ans = 1
print(" Calculator for n choose k")
n = int(input("Enter n: "))
k = int(input("Enter k: "))
ans = my_choose(n,k)
print("Result: ",ans)