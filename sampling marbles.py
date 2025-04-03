import math
import random
def factorial(size_n1):
  i = 1
  n = 1
  while (i <= size_n1):
    n = n * i
    i = i + 1
  return (n)
def choose(size_n1,size_r1):
  n1 = float(factorial(size_n1))
  # print (n1)
  r1 = float(factorial(size_r1))
  # print(r1)
  # (n-r)!
  n1_r1 = float(factorial(size_n1 - size_r1))
  combination = n1 / (r1 * (n1_r1))
  return combination
# combination problem
total = 0
total_sel = 0
size_n1 = int(input("Enter the value of red: "))
size_r1 = int(input("Enter the value of selected red: "))
size_n2 = int(input("Enter the value of white: "))
size_r2 = int(input("Enter the value of selected white: "))
comb1=choose(size_n1, size_r1)
# print(comb1)
comb2=choose(size_n2, size_r2)
# print(comb2)
comb3=choose(size_n1+size_n2, size_r1+size_r2)
result = comb1 * comb2 / comb3
print(result)

trial = 1000
success = 0
k = 0
while (k < trial):
  bowl = ['r'] * size_n1 + ['w'] * size_n2
  length = len(bowl)
  number_r = 0
  number_w = 0
  for i in range(size_r1+size_r2):
    pick = random.randint(0,length-1)
    if (bowl[pick] == 'r'):
      number_r = number_r + 1
    else:
      number_w = number_w + 1
    bowl[pick] = bowl[length-1]
    length = length - 1
  if (number_r == size_r1 and number_w == size_r2):
    success = success + 1
  k = k + 1
ratio = success / trial
print(ratio)