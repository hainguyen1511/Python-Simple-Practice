def f(n):
    if(n == 1 or n == 3 or n == 4):
        return 1
    elif (n == 2):
        return 2
    a = f(n-1)
    b = f(n-2)
    c = f(n-3)
    s = a
    if (b < s):
        s = b
    if (c < s):
        s = c
    return 1+s
n = int(input("Enter a number: "))
print (f(n))