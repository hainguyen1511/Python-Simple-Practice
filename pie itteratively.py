num1 = float(input("Enter a number: "))
ans = 1.0
pie = 0.0
while num1 != 1:
    ans = 2 + ((num1*num1)/ans)
    num1 = num1 - 2
ans = 1 + ((num1*num1)/ans)
pie = 4 / ans
print(pie)