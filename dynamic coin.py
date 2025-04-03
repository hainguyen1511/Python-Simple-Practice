def f(n,t):
    if(t[n] != -1):
        return t[n]
    a = f(n-1,t)
    b = f(n-3,t)
    c = f(n-4,t)
    s = a
    if (b < s):
        s = b
    if (c < s):
        s = c
    t[n] = 1 + s
    return t[n]
n = int(input("Enter a number: "))
t = [-1]*(n+1)
t[1] = 1
t[2] = 2
t[3] = 1
t[4] = 1
print (f(n,t))