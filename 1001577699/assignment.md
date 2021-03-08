# Assignment 0.0: Computational Methods for Physicists and Astronomers 
## University of Antioquia
### Juan David Salcedo Hernández

#### 1. Implementation of the factorial algorithm
In order to compute the factorial of an arbitrary positive integer `n`, we need not resort to an explicit mathematical definition of such a function, but rather establish a recursive definition by using a list of numbers.

The function receives a value $n$ and builds up a list beginning with the number 1 (that is, $a_1$), with the recursion:
$$
a_n =n\cdot a_{n-1}
$$
this means that the first few iterations yield
\begin{gather*}
a_2 = 2 \cdot a_1 = 2 \cdot 1, \\
a_3 = 3 \cdot a_2 = 3 \cdot 2 \cdot 1, \\
a_4 = 4 \cdot a_3 = 4 \cdot 3 \cdot 2 \cdot 1,
\end{gather*}

and so on and so forth, until $a_n$. The function just returns the last item on the list.
<!-- name: factorial -->
```python
def factorial(n) :
        factorial_list = [1]
        for i in range(1, n+1) : # Python interprets this as an interval [1 .. n] 
                factorial_list.append(i*factorial_list[i-1])
        print(factorial_list[-1])
```
We may now evaluate the factorial function for some values:
Input
<!-- target: output_1, require: factorial -->
```python
factorial(10), factorial(15)
```
<!-- name: output_1 -->
```
3628800 1307674368000
```

#### 2. Algorithms on the divisors of a number

This algorithm resorts to the following definitions:
* __Defective numbers__ A number $n$ is called defective (or deficient) if the sum of its _proper divisors_ is less than $n$.
* __Abundant numbers__ An excessive number is a number that is smaller than the sum of its proper divisors.
* __Amicable numbers__ Two different numbers such that the sum of the proper divisors of each is equal to the other number.
* __Semi-perfect numbers__ There exists a subset of its proper divisors whose sum is equal to the number.
* __Perfect numbers__ The sum of _all_ of its proper divisors is equal to the number.
* __Prime numbers__ The number is only divisible by itself and by 1.

Firstly, we must obtain a list of the divisors of the given numbers. As a justification for the method we shall introduce, we need state explicitly the fact that, for any positive integer $n$, there is a one-to-one correspondence between the divisors of $n$ that are less than $\sqrt{n}$ and those which are greater than $\sqrt{n}$.

Note that if $d$ divides $n$, then $n$ might as well be written as a product of two integers in the following manner: $n=(n/d) \cdot d$. Hence $n/d$ would also divide $n$. Now, if $n$ is a perfect square so that $d=\sqrt{n}$ divides $n$, then $n/d = \sqrt{n} = d$ so both numbers would be exactly the same divisor; otherwise, $d$ and $n/d$ will be different divisors of $n$. With this in mind we may proceed by considering that if we have a divisor $d < \sqrt{n}$, then $d \sqrt{n} < n$, which is to say $n/d > \sqrt{n}$; whereas if $d > \sqrt{n}$, then $n/d < \sqrt{n}$. Hence we have an equivalence:
$$
d < \sqrt{n} \Leftrightarrow n/d > \sqrt{n},
$$
which establishes the desired relation and allows us to find all divisors of an integer by iterating to $\floor{\sqrt{n}}$. 
<!-- name: divisors -->
```python
import math

def div_list(n) :
        div_list = [1]
        i = 2
        while i <= math.sqrt(n) :
                if n % i == 0 :
                        if n//i == i :
                                div_list.append(i)
                        else :
                                div_list.append(i)
                                div_list.append(n//i)
                i += 1
        return div_list
```
In order to decide whether a given positive integer abides by the definition of semi-perfect, we must resort to what is known as the subset sum problem, viz., we must tell if, given an arbitrary set of positive integers, we can extract some subset of it such that the sum of its elements yield a fixed value. In our particular case, we must evaluate subsets of the set of divisors of a number.

To compute this in an effective way, we resort to dynamic programming. Suppose we have the number $n$ and a list of its proper divisors, the idea is to construct a boolean matrix that relates subsets up to a certain value of the list of divisors with the possibility of them summing up to a quantity between 0 and $n$. To be fair it is not so simple to put in words, but an image may clear things up:
$$
  \begin{blockarray}{cccccc}
     & 0 & 1 & 2 & \cdots & n \\
  \begin{block}{c\Left{}{(\mkern7mu}ccccc<{\mkern7mu})}
        0 & T & F & F & \cdots & F \\
  \cline{3-6}
  \begin{block*}{cc|cccc}
        d_1    & T &  &  &  &   \\
        d_2    & T &  &  &  &   \\
        d_3    & T &  &  &  &   \\
        \vdots & T &  &  &  &   \\
        d_m    & T &  &  &  & \\
  \end{block*}
  \end{block}
  \end{blockarray}
$$
Each row is associated to an element on the ordered list of divisors $(0,d_1,d_2,\dots,d_m)$, which can be truncated up to the k-th element as $(0,a_1,\dots,a_k)$. Each column is associated to an integer between 0 and $n$. 

An element in the $(i,j)$ position in this array is True ($T$) if there is a subset of the truncated list up to the i-th element (viz., a subset of $(0,a_1,\dots,a_i)$) which adds up to $j$.

Here the first column tells us that for a list truncated up to any element of the divisor list, there is a subset that can add up to 0, this is taken as a tautology for we defined the 0-th element to be 0. On the other hand, 0 cannot add up to a number greater than itself, that is why the elements on the first row must be False ($F$).

The empty matrix shown above will be filled according to two simple rules, which are indeed plausible. Suppose we require the value of an element in the $(i,j)$ position:
* If $j < d_i$ and the element $(i-1,j)$ is False, then there is no way we can add up to $j$ with a number that is greater than $j$, hence $(i,j)$ would be False too. On the other hand, if the element $(i-1,j)$ is True, then it follows that any truncated list past $d_{i-1}$ will contain at least one subset that adds up to $j$, hence $(i,j)$ would be true.
* If $j \geq d_i$ and the value of $(i-1,j)$ is True, we already know that $(i,j)$ will be also True; but even if $(i,j)$ is False there is the possibility that some subset of $(0,d_1,\dots,d_{i-1})$ give the value $j - d_i$, if such a subset happens to exist, then the value of $(i,j)$ must be True. Hence $(i,j)$ will be False if both the above conditions are False.

Simply, put:
* If $j < d_i$, then $(i,j) = (i-1,j)$.
* If $j \geq d_i $, then $(i,j) = (i-1,j) or (i-1,j-d_i)$.

<!-- name: semi-perfect, require: divisors -->
```python
def is_semiperfect(m) :
        divisors_list = []
        divisors_list = div_list(m)
        divisors_list.sort()
        
        n = len(divisors_list)
        
        # We create an (n x m) matrix.
        bool_matrix = [[0 for i in range(m + 1)] for j in range(n + 1)]
        
        # set first column to True
        for i in range(n + 1) :
                bool_matrix[i][0] = True

        # set first column to False
        for i in range(1, m + 1) :
                bool_matrix[0][i] = False
        
        # evaluation through the boolean matrix as described 
        for i in range(1, n+1) :
                for j in range(1, m+1) :
                        if j < divisors_list[i-1] : # we subtract 1 because we appended 0 at the beginning of the array
                                bool_matrix[i][j] = bool_matrix[i-1][j] 
                        else :
                                bool_matrix[i][j] = bool_matrix[i-1][j] or bool_matrix[i-1][j-divisors_list[i-1]]
        
        if bool_matrix[n][m] == True :
                print(f'{m} is semi-perfect')
```
The following are just trivial definitions.
<!-- name: easy_statements, require: semi-perfect -->
```python
def are_amicable(n, m, div_sum_n, div_sum_m) :
        if n == div_sum_m and m == div_sum_n :
                print(f'{n} and {m} are amicable') 

def is_prime(n, div) :
        if len(div) == 1 :
                print(f'{n} is prime') 

def is_defective(n, div_sum) :
        if div_sum < n :
                print(f'{n} is defective')

def is_abundant(n, div_sum) :
        if div_sum > n :
                print(f'{n} is abundant')

def is_perfect(n, div_sum) :
        if div_sum == n :
                print(f'{n} is perfect')
```
Finally all comes together:
<!-- require:easy_statements, name: kind -->
```python
def kind_of_number(a,b) :
        # we gather together the variables we require
        div_a = div_list(a)
        div_b = div_list(b)
        sum_a = sum(div_a)
        sum_b = sum(div_b)

        # print the statements 
        are_amicable(a,b,sum_a,sum_b)

        is_prime(a, div_a)
        is_prime(b, div_b)

        is_defective(a, sum_a)
        is_defective(b, sum_b)

        is_abundant(a, sum_a)
        is_abundant(b, sum_b)

        is_perfect(a, sum_a)
        is_perfect(b, sum_b)

        is_semiperfect(a)
        is_semiperfect(b)
```
Execution example:

Input
<!-- require: kind, target: output_2 -->
```python
kind_of_number(40,12), kind_of_number(220,284)
```
Output
<!-- name:output_2 -->
```
40 is abundant
12 is abundant
40 is semi-perfect
12 is semi-perfect
220 and 284 are amicable
284 is defective
220 is abundant
220 is semi-perfect
```

#### 3. Palindrome number

This is an easy one, we need only evaluate a given number as if it is a string of characters, thus as if it is a list. We just decide whether the reversed list is exactly the same as the original one.
<!-- name: palindrome -->
```python
def palindrome(number) :
        string = str(number)
        if string[0:] == string[::-1] :
                print(True)
        else : 
                print(False)
```
Execution example:

Input
<!-- require: palindrome, target: output_3 -->
```python
palindrome(3333333), palindrome(2323), palindrome(1111349111111)
```
Output
<!-- name: output_3 -->
```
True
False
False
```

#### 4. Evaluating a string

This equally comes down to manipulating a list of characters.
<!-- name: string -->
```python
def string(string) :
        chars = []
        vocals = 'aeiou'
        
        if len(string) % 2 == 0 :
                 chars.append(False)
        elif string[int(len(string) / 2)] in vocals :
                chars.append(True)
        else :
                chars.append(False)

        vocals_in_str = 0
        consonants_in_str = 0
        for i in string :
                if i in vocals :
                        vocals_in_str += 1
                else :
                        consonants_in_str += 1
        chars.append(vocals_in_str)
        chars.append(consonants_in_str) 
        
        chars.append(string[::-1])
        
        print(chars)
```
Execution example:

Input
<!-- require: string, target: output_4 -->
```python
string('perro'), string('murcielago')
```
Output
<!-- name: output_4 -->
```
[False, 2, 3, 'orrep']
[False, 5, 5, 'ogaleicrum']
```

#### 5. The Fibonacci sequence

Much like the first exercise, this is a recursion, which in this case is given by the formula ...
<!-- name: Fibonacci -->
```python
def fib(n) :
        fib_list = [1,1]
        for i in range(2, n+1) :
                fib_list.append(fib_list[i-1] + fib_list[i-2])
        print(fib_list[-2])
```
Execution example:
Input 
<!-- require: Fibonacci, target: output_5 -->
```python
fib(50), fib(63)
```
Output
<!-- name: output_5 -->
```
12586269025
6557470319842
```

<!-- name: recurrence -->
```python
import matplotlib.pyplot as plt
def recurrence(n) :
        r = 3.5
        recurrence_list = [0.2]
        for i in range(1, n+1) : # Python interprets this as an interval [1 .. n] 
                recurrence_list.append(r*recurrence_list[i-1]*(1-recurrence_list[i-1]))
        
        t = range(n+1)
        fig, ax = plt.subplots(1)
        ax.plot(t, recurrence_list, 'b-', markersize=2)
        plt.show()
```
<!-- require: recurrence, target: output_6 -->
```python
recurrence(10)
```
<!-- name: output_6 -->
```
```
