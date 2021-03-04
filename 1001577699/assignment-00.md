# Assignment 0.0: Computational Methods for Physicists and Astronomers 
## University of Antioquia
### Juan David Salcedo Hernández

#### 1. Implementation of the factorial algorithm
In order to compute the factorial of an arbirtaty positive integer `n`, we need not resort to an explicit mathematical definition of such a function, but rather establish a recursive definition by using a list of numbers.

The function receives a value x and builds up a list beginnig with the number 1 (henceforth a_1), with the recursion:
```math
a_n = n \cdot a_{n-1};
```
this means that the first few iterations yield
```math
\begin{gather}
a_2 = 2 \cdot a_1 = 2 \cdot 1, \\
a_3 = 3 \cdot a_2 = 3 \cdot 2 \cdot 1, \\
a_4 = 4 \cdot a_3 = 4 \cdot 3 \cdot 2 \cdot 1,
\end{gather}
```
and so on and so forth. The function just returns the last item on the list.
<!-- name: factorial -->
```python
def factorial(n):
        factorial_list = [1]
        for i in range (1, n+1):
                factorial_list.append(i*factorial_list[i-1])
        return factorial_list[-1]
```
We may now evaluate the factorial function for some values:
<!-- target: output1, require: factorial -->
```python
print(factorial(10), factorial(15))
```
<!-- name: output1 -->
```
3628800 1307674368000
```
