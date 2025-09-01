'''
Implement the Fraction Abstract Data Type.
'''

from math import gcd

class Fraction:
    '''
    The simplest form of a fraction, obbeying 
    regular algebra rules for basic math operations.
    '''
    def __init__(self, numerator, denominator=1):
        # Exception handling
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("The numerator and the denominator must be integer numbers.")
        if denominator == 0:
            raise ZeroDivisionError("The denominator must not be equal to zero.")

        # Fraction's signal handling
        if numerator * denominator >= 0:
            signal = 1
        else: signal = -1

        numerator, denominator = abs(numerator), abs(denominator)
        factor = gcd(numerator, denominator)

        self.numerator = signal * numerator // factor
        self.denominator = denominator // factor

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        if self.numerator == 0:
            return "0"
        return f"{self.numerator} / {self.denominator}"

    def __add__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only add to a fraction another fraction or an integer.")

        numerator = other.denominator * self.numerator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __iadd__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only add to a fraction another fraction or an integer.")

        return self + other

    def __sub__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only subtract from a fraction another fraction or an integer.")

        return self + Fraction(-1) * other

    def __isub__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only subtract from a fraction another fraction or an integer.")

        return self - other

    def __mul__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only multiply a fraction by another fraction or an integer.")

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __imul__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only multiply a fraction by another fraction or an integer.")

        return self * other

    def __truediv__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only divide a fraction by another fraction or by an integer.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __itruediv__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only divide a fraction by another fraction or by an integer.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        return self / other

    def __floordiv__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only divide a fraction by another fraction or by an integer.")

        floordiv =  (self.numerator * other.denominator) // (other.numerator * self.denominator)

        return Fraction(floordiv)

    def __ifloordiv__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only divide a fraction by another fraction or by an integer.")

        return self // other

    def __mod__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only take the module between a fraction and another " +
            "fraction or a fraction and an integer.")

        mod = (self.numerator * other.denominator) % (other.numerator * self.denominator)

        return Fraction(mod)

    def __imod__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only take the module between a fraction and another " +
            "fraction or a fraction and an integer.")

        return self % other

    def __pow__(self, power):
        # Exception handling
        if not isinstance(power, int):
            raise TypeError("The power must be an integer.")

        if power < 0:
            numerator = self.denominator ** abs(power)
            denominator = self.numerator ** abs(power)
        else:
            numerator = self.numerator ** power
            denominator = self.denominator ** power
        return Fraction(numerator, denominator)

    def __ipow__(self, power):
         # Exception handling
        if not isinstance(power, int):
            raise TypeError("The power must be an integer.")

        return self ** power

    def __eq__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __ne__(self, other):
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return not self == other

    def __neg__(self):
        return Fraction(-1) * self

    def __pos__(self):
        return self

    def __abs__(self):
        numerator = abs(self.numerator)
        denominator = self.denominator
        return Fraction(numerator, denominator)

    def __complex__(self):
        return complex(self.numerator / self.denominator)

    def __int__(self):
        return int(self.numerator / self.denominator)

    def __float__(self):
        return self.numerator / self.denominator
