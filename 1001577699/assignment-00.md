# Assignment 0.0: Computational Methods for Physicists and Astronomers 
## University of Antioquia
### Juan David Salcedo Hernández

#### 1. Implementation of the factorial algorithm
In order to compute the factorial of an arbirtaty positive integer `n`, we need not resort to an explicit mathematical definition of such a function, but rather establish a recursive definition by using a list of numbers.

The function receives a value x and builds up a list beginnig with the number 1 (henceforth a_1), with the recursion:
<p align="center"><img src="https://rawgit.com/in	git@github.com:jdavid-salcedo/Evaluacion_2021-1/main/svgs/d500dd18caaddfecb9c46809d6c04f3f.svg?invert_in_darkmode" align=middle width=94.93532565pt height=11.141563949999998pt/></p>
this means that the first few iterations yield
<p align="center"><img src="https://rawgit.com/in	git@github.com:jdavid-salcedo/Evaluacion_2021-1/main/svgs/896ac255471a33ef16bff5647dac575d.svg?invert_in_darkmode" align=middle width=434.6932986pt height=65.753424pt/></p>

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
