# Task №3. Create a class for calculations on integers
import math
import sympy


class Calculation:
    """Class Calculation performs various operations on integers"""

    def factorial(self, x):
        """The method calculates the factorial of an integer"""
        return f'Factorial of a number {x} = {math.factorial(x)}!'

    def summa(self, n):
        """The method calculates the sum of numbers from 1 to n"""
        result = int(math.fsum(range(1, n + 1)))
        return f'Sum of numbers from 1 to {n} = {result}'

    def test_prim(self, y):
        """The method checks if the number is prime or not"""
        if sympy.isprime(y):
            return f'{y} - prime number'
        else:
            return f'{y} - is not a prime number'

    def test_prims(self, a, b):
        """The method checks whether two integers are coprime"""
        if math.gcd(a, b) == 1:
            return f'Numbers {a} and {b} are coprime'
        else:
            return f'The numbers {a} and {b} are not coprime'

    def table_mult(self, n):
        """The method creates and displays the multiplication table of the given number"""
        print(f'Multiplication table of number {n}')
        for i in range(1, 11):
            print(f'{n} * {i} = {n * i}')

    def all_table_mult(self):
        """The method displays the multiplication table from 1 to 9 """
        print('Multiplication table')
        for i in range(1, 10):
            for k in range(2, 10):
                print(f'{i} * {k} = {i * k}\t', end='')
            print('')

    @staticmethod
    def list_div(n):
        """staticmethod outputs a list of divisors of the given integer number"""
        i = 1
        l_div = []
        while i ** 2 <= n:
            if n % i == 0:
                l_div.append(i)
                if i != n // i:
                    l_div.append(n // i)
            i += 1
        l_div.sort()
        return f'List of divisors of a number {n} = {l_div}'

    @staticmethod
    def list_div_prim(n):
        """staticmethod outputs a list of prime integer divisors of the given number"""
        i = 1
        l_div = []
        while i ** 2 <= n:
            if n % i == 0:
                l_div.append(i)
                if (i != n // i):
                    l_div.append(n // i)
            i += 1

        new_l_div = []
        for i in l_div:
            if sympy.isprime(i):
                new_l_div.append(i)
        new_l_div.sort()
        return f'List of prime divisors of a number {n} = {new_l_div}'


number = Calculation()
print(number.factorial(5))
print('')
print(number.summa(9))
print('')
print(number.test_prim(17))
print('')
print(number.test_prims(3, 11))
print('')
number.table_mult(7)
print('')
number.all_table_mult()
print('')
print(Calculation.list_div(8))
print('')
print(number.list_div_prim(44))
