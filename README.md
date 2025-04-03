# Python-Simple-Practice
# Simple calculator n choose K
* N-Choose-K problem:
Design a dynamic programming algorithm for the recursive n-choose-k problem discussed in class and then indicate its time and space complexity.
# Quantity of coin in exchange as minimum
> Base Cases: It handles specific small input values explicitly:
If n is 1, 3, or 4, the function returns 1.
If n is 2, the function returns 2.
> Recursive Cases:
For any other value of n, the function calls itself recursively to calculate:
a = f(n-1)
b = f(n-2)
c = f(n-3)
Then, it compares these values (a, b, and c) to find the smallest among them (s).
> Final Step:
It returns the value of 1 + s, where s is the smallest of a, b, and c.
> Input and Output:
The program prompts the user to input a number (n) and then prints the result of f(n).
> A dynamic programming, such as minimizing some cost or steps while building a sequence.
