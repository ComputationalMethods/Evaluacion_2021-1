# Assignment 0.0: Computational Methods for Physicists and Astronomers 
## University of Antioquia
### Juan David Salcedo Hernández

#### 1. Implementation of the factorial algorithm
In order to compute the factorial of an arbitrary positive integer `n`, we need not resort to an explicit mathematical definition of such a function, but rather establish a recursive definition by using a list of numbers.

The function receives a value <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> and builds up a list beginning with the number 1 (that is, <img src="./svgs/8e830a5ab471143f1bb80e525c09bbaa.svg?invert_in_darkmode" align=middle width=15.24170009999999pt height=14.15524440000002pt/>), with the recursion:
<p align="center"><img src="./svgs/d500dd18caaddfecb9c46809d6c04f3f.svg?invert_in_darkmode" align=middle width=94.93532565pt height=11.141563949999998pt/></p>
this means that the first few iterations yield
<p align="center"><img src="./svgs/e39cf063209e1ecd6fb0db1a1863cc91.svg?invert_in_darkmode" align=middle width=169.11268604999998pt height=63.10502715pt/></p>

and so on and so forth, until <img src="./svgs/6512cbd0d448700a036bf3a691c37acc.svg?invert_in_darkmode" align=middle width=16.81517804999999pt height=14.15524440000002pt/>. The function just returns the last item on the list.
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
* __Defective numbers__ A number <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> is called defective (or deficient) if the sum of its _proper divisors_ is less than <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>.
* __Abundant numbers__ An excessive number is a number that is smaller than the sum of its proper divisors.
* __Amicable numbers__ Two different numbers such that the sum of the proper divisors of each is equal to the other number.
* __Semi-perfect numbers__ There exists a subset of its proper divisors whose sum is equal to the number.
* __Perfect numbers__ The sum of _all_ of its proper divisors is equal to the number.
* __Prime numbers__ The number is only divisible by itself and by 1.

Firstly, we must obtain a list of the divisors of the given numbers. As a justification for the method we shall introduce, we need state explicitly the fact that, for any positive integer <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, there is a one-to-one correspondence between the divisors of <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> that are less than <img src="./svgs/4fd78aba72015f7697ab298a89ec8a9c.svg?invert_in_darkmode" align=middle width=23.565549149999992pt height=24.995338500000003pt/> and those which are greater than <img src="./svgs/4fd78aba72015f7697ab298a89ec8a9c.svg?invert_in_darkmode" align=middle width=23.565549149999992pt height=24.995338500000003pt/>.

Note that if <img src="./svgs/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode" align=middle width=8.55596444999999pt height=22.831056599999986pt/> divides <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, then <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> might as well be written as a product of two integers in the following manner: <img src="./svgs/781916121019488b7603bdcd0c367841.svg?invert_in_darkmode" align=middle width=91.63993574999998pt height=24.65753399999998pt/>. Hence <img src="./svgs/af80af3501f12b7de376be991cca1bcc.svg?invert_in_darkmode" align=middle width=26.64205004999999pt height=24.65753399999998pt/> would also divide <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>. Now, if <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> is a perfect square so that <img src="./svgs/c5cdf648421b2dd55174e0ccf98e4420.svg?invert_in_darkmode" align=middle width=54.039143399999986pt height=24.995338500000003pt/> divides <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, then <img src="./svgs/5e5786fb13f4d6afc6e7b0c316638757.svg?invert_in_darkmode" align=middle width=102.59882324999998pt height=24.995338500000003pt/> so both numbers would be exactly the same divisor; otherwise, <img src="./svgs/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode" align=middle width=8.55596444999999pt height=22.831056599999986pt/> and <img src="./svgs/af80af3501f12b7de376be991cca1bcc.svg?invert_in_darkmode" align=middle width=26.64205004999999pt height=24.65753399999998pt/> will be different divisors of <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>. With this in mind we may proceed by considering that if we have a divisor <img src="./svgs/6d72787396f0fb2835ab0496be5b6030.svg?invert_in_darkmode" align=middle width=54.039143399999986pt height=24.995338500000003pt/>, then <img src="./svgs/aa3d280c7569f74b36f828a11bda8e48.svg?invert_in_darkmode" align=middle width=63.90601964999999pt height=24.995338500000003pt/>, which is to say <img src="./svgs/ba6839e5dd9a48e50c66781f683a015a.svg?invert_in_darkmode" align=middle width=72.12522899999999pt height=24.995338500000003pt/>; whereas if <img src="./svgs/64b4af190beb8d9723287ec699b27692.svg?invert_in_darkmode" align=middle width=54.039143399999986pt height=24.995338500000003pt/>, then <img src="./svgs/1677939e3661f8ebe9d300b125cbdae8.svg?invert_in_darkmode" align=middle width=72.12522899999999pt height=24.995338500000003pt/>. Hence we have an equivalence:
<p align="center"><img src="./svgs/a8f6a8c2d1659949e6fd936f1ef479bc.svg?invert_in_darkmode" align=middle width=156.30119505pt height=17.4097869pt/></p>
which establishes the desired relation and allows us to find all divisors of an integer by iterating to <img src="./svgs/d12a0737370c512d2be42efc7c4d279f.svg?invert_in_darkmode" align=middle width=23.565549149999992pt height=24.995338500000003pt/>. Here is the implementation 

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

To compute this in an effective way, we resort to dynamic programming. Suppose we have the number <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> and a list of its proper divisors, the idea is to construct a boolean matrix that relates subsets up to a certain value of the list of divisors with the possibility of them summing up to a quantity between 0 and <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>. To be fair it is not so simple to put in words, but an image may clear things up:
<p align="center"><img src="./svgs/68c06b8987000e2ba02c6a0c4dcd114b.svg?invert_in_darkmode" align=middle width=210.73550354999998pt height=145.80831705pt/></p>
Each row is associated to an element on the ordered list of divisors <img src="./svgs/045964e4e4493e6f8530552c9bda18e1.svg?invert_in_darkmode" align=middle width=125.04939974999999pt height=24.65753399999998pt/>, which can be truncated up to the k-th element as <img src="./svgs/18bc6e4d1677aa5b15be8a35e9c9f68a.svg?invert_in_darkmode" align=middle width=97.6806534pt height=24.65753399999998pt/>. Each column is associated to an integer between 0 and <img src="./svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/>. 

An element in the <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> position in this array is True (<img src="./svgs/2f118ee06d05f3c2d98361d9c30e38ce.svg?invert_in_darkmode" align=middle width=11.889314249999991pt height=22.465723500000017pt/>) if there is a subset of the truncated list up to the i-th element (viz., a subset of <img src="./svgs/79748e641bd977ef40a105f5932513d8.svg?invert_in_darkmode" align=middle width=95.06550569999999pt height=24.65753399999998pt/>) which adds up to <img src="./svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.710416999999989pt height=21.68300969999999pt/>.

Here the first column tells us that for a list truncated up to any element of the divisor list, there is a subset that can add up to 0, this is taken as a tautology for we defined the 0-th element to be 0. On the other hand, 0 cannot add up to a number greater than itself, that is why the elements on the first row must be False (<img src="./svgs/b8bc815b5e9d5177af01fd4d3d3c2f10.svg?invert_in_darkmode" align=middle width=12.85392569999999pt height=22.465723500000017pt/>).

The empty matrix shown above will be filled according to two simple rules, which are indeed plausible. Suppose we require the value of an element in the <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> position:
* If <img src="./svgs/2864b52933f6cff87e9047574051d386.svg?invert_in_darkmode" align=middle width=42.83491079999999pt height=22.831056599999986pt/> and the element <img src="./svgs/b2e950ac70590a1096832516babcedd0.svg?invert_in_darkmode" align=middle width=61.775361449999984pt height=24.65753399999998pt/> is False, then there is no way we can add up to <img src="./svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.710416999999989pt height=21.68300969999999pt/> with a number that is greater than <img src="./svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.710416999999989pt height=21.68300969999999pt/>, hence <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> would be False too. On the other hand, if the element <img src="./svgs/b2e950ac70590a1096832516babcedd0.svg?invert_in_darkmode" align=middle width=61.775361449999984pt height=24.65753399999998pt/> is True, then it follows that any truncated list past <img src="./svgs/d635f47719485e84d076bb51ff86bbca.svg?invert_in_darkmode" align=middle width=30.03343034999999pt height=22.831056599999986pt/> will contain at least one subset that adds up to <img src="./svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.710416999999989pt height=21.68300969999999pt/>, hence <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> would be true.
* If <img src="./svgs/f126487f4ea798e16fc3011e446e062f.svg?invert_in_darkmode" align=middle width=42.83491079999999pt height=22.831056599999986pt/> and the value of <img src="./svgs/b2e950ac70590a1096832516babcedd0.svg?invert_in_darkmode" align=middle width=61.775361449999984pt height=24.65753399999998pt/> is True, we already know that <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> will be also True; but even if <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> is False there is the possibility that some subset of <img src="./svgs/a5099b427a7d39293e0d471ca9fad410.svg?invert_in_darkmode" align=middle width=111.62566469999999pt height=24.65753399999998pt/> give the value <img src="./svgs/b2d0f15c665063d9c5dddfa3712c967e.svg?invert_in_darkmode" align=middle width=41.008471349999986pt height=22.831056599999986pt/>, if such a subset happens to exist, then the value of <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> must be True. Hence <img src="./svgs/aa20264597f5a63b51587e0581c48f2c.svg?invert_in_darkmode" align=middle width=33.46496009999999pt height=24.65753399999998pt/> will be False if both the above conditions are False.

Simply, put:
* If <img src="./svgs/2864b52933f6cff87e9047574051d386.svg?invert_in_darkmode" align=middle width=42.83491079999999pt height=22.831056599999986pt/>, then <img src="./svgs/813fdbfc47330d170db2c9c96b555c21.svg?invert_in_darkmode" align=middle width=117.15795299999999pt height=24.65753399999998pt/>.
* If <img src="./svgs/fe17a02a723042e4b243aec1abfc80d6.svg?invert_in_darkmode" align=middle width=42.83491079999999pt height=22.831056599999986pt/>, then <img src="./svgs/552f1770ca5cafc1bb6efe2183cafc5e.svg?invert_in_darkmode" align=middle width=228.89427164999995pt height=24.65753399999998pt/>.

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
