# Python Simple Practice
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
# Quantity of coin in exchange as minimum with memoization--—a technique that optimizes recursive functions by storing previously computed results.
* Storing the base case in an array
* t is an array that stores computed values to avoid redundant calculations.
* If t[n] isn't -1, that means n has already been processed and can be returned directly.
* The function recursively finds the minimum steps needed to reach n by comparing results from n-1, n-3, and n-4.
* The base cases are predefined (t[1] = 1, t[2] = 2, etc.) to provide direct answers for small values of n.
* Best to process huge amount of coins
# Problem : Sampling Without Replacement
![Screenshot 2025-04-03 202722](https://github.com/user-attachments/assets/9b65d130-d9c5-4dd5-b98d-d1238fc8c08a)
* Create two functions, one for factorial and the other for combination process.
* Create three values to store result of combination function.
* Also using 1000 trials to test the ratio of success/ trial
# Binary search
* Binary search operates in O(log n) time complexity
* The function might fail if mid exceeds the valid index range due to improper bounds.
