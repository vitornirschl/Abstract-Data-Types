'''
Implements the Fraction Abstract Data Type.

Classes
-------
Fraction
    A fraction in its simplest form.
'''

from math import gcd

class Fraction:
    '''
    A Fraction in its simplest form.

    Attributes
    ----------
    numerator : int
        The numerator of the simplified fraction.
    denominator : int
        The denominator of the simplified fraction.
    '''
    def __init__(self, numerator, denominator=1):
        '''
        Initializes a Fraction instance.

        Parameters
        ----------
        numerator : int
            The numerator of the fraction.
        denominator : int, optional
            The denominator of the fraction (default = 1).

        Raises
        ------
        TypeError
            If the numerator or the denominator aren't integers.
        ZeroDivisionError
            If the denominator is set to zero.  
        '''
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
        # Using greatest common divisor to simplify the fraction.
        factor = gcd(numerator, denominator)

        self.numerator = signal * numerator // factor
        self.denominator = denominator // factor

    def __repr__(self):
        '''
        The abstract representation of an instance of Fraction

        Returns
        -------
        str
            Fraction({self.numerator}, {self.denominator})
        '''
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        '''
        The string object of an instance of Fraction.

        Returns
        -------
        str
            A visual representation of a simplified fraction.
        '''
        if self.denominator == 1:
            return f"{self.numerator}"
        if self.numerator == 0:
            return "0"
        return f"{self.numerator} / {self.denominator}"

    def __add__(self, other):
        '''
        The sum of two instances of Fraction.

        Args
        ----
        other : Fraction or int
            A fraction or integer to sum to the current fraction.

        Returns
        -------
        Fraction
            The sum of the two fractions.
        
        Raises
        ------
        TypeError
            If other is not an instance of Fraction or int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only add to a fraction another fraction or an integer.")

        numerator = other.denominator * self.numerator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __iadd__(self, other):
        '''
        The sum of two instances of Fraction.

        Args
        ----
        other : Fraction or int
            A fraction or integer to sum to the current fraction.

        Returns
        -------
        Fraction
            The sum of the two fractions.
        
        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only add to a fraction another fraction or an integer.")

        return self + other

    def __sub__(self, other):
        '''
        The subtraction of two instances of Fraction.

        Args
        ----
        other : Fraction or int
            A fraction or integer to substract from the current fraction.
        
        Returns
        -------
        Fraction
            The subtraction of the two fractions.
        
        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only subtract from a fraction another fraction or an integer.")

        return self + Fraction(-1) * other

    def __isub__(self, other):
        '''
        The subtraction of two instances of Fraction.

        Args
        ----
        other : Fraction or int
            A fraction or integer to substract from the current fraction.
        
        Returns
        -------
        Fraction
            The subtraction of the two fractions.
        
        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only subtract from a fraction another fraction or an integer.")

        return self - other

    def __mul__(self, other):
        '''
        The multiplication of two instances of Fraction.
        
        Args
        ----
        other : Fraction or int
            A fraction or integer to multiply the current fraction.

        Returns
        -------
        Fraction
            The result of the multiplication.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int. 
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only multiply a fraction by another fraction or an integer.")

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __imul__(self, other):
        '''
        The multiplication of two instances of Fraction.
        
        Args
        ----
        other : Fraction or int
            A fraction or integer to multiply the current fraction.

        Returns
        -------
        Fraction
            The result of the multiplication.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int. 
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only multiply a fraction by another fraction or an integer.")

        return self * other

    def __truediv__(self, other):
        '''
        The division of two fractions.

        Args
        ----
        other : Fraction or int
            A fraction or integer to divide the current fraction.
        
        Returns
        -------
        Fraction
            The result of the division.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        ZeroDivisionError
            If other is equal to zero.
        '''
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
        '''
        The division of two fractions.

        Args
        ----
        other : Fraction or int
            A fraction or integer to divide the current fraction.
        
        Returns
        -------
        Fraction
            The result of the division.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        ZeroDivisionError
            If other is equal to zero.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only divide a fraction by another fraction or by an integer.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        return self / other

    def __floordiv__(self, other):
        '''
        The floor division of two fractions.

        Args
        ----
        other : Fraction or int
            A fraction or integer to divide with remainder the current fraction.

        Returns
        -------
        Fraction
            The result of the floor division.
        
        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        ZeroDivisionError
            If other is equal to zero.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only divide a fraction by another fraction or by an integer.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        floordiv =  (self.numerator * other.denominator) // (other.numerator * self.denominator)

        return Fraction(floordiv)

    def __ifloordiv__(self, other):
        '''
        The floor division of two fractions.

        Args
        ----
        other : Fraction or int
            A fraction or integer to divide with remainder the current fraction.

        Returns
        -------
        Fraction
            The result of the floor division.
        
        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        ZeroDivisionError
            If other is equal to zero.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only divide a fraction by another fraction or by an integer.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        return self // other

    def __mod__(self, other):
        '''
        The remainder of the floor division of two fractions.

        Args
        ----
        other : Fraction or int
            A fraction or integer to divide the current fraction.
        
        Returns
        -------
        Fraction
            The remainder of the floor division of the current fraction by other.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        ZeroDivisionError
            If other is equal to zero.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only take the module between a fraction and another " +
            "fraction or a fraction and an integer.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        mod = (self.numerator * other.denominator) % (other.numerator * self.denominator)

        return Fraction(mod)

    def __imod__(self, other):
        '''
        The remainder of the floor division of two fractions.

        Args
        ----
        other : Fraction or int
            A fraction or integer to divide the current fraction.
        
        Returns
        -------
        Fraction
            The remainder of the floor division of the current fraction by other.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        ZeroDivisionError
            If other is equal to zero.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only take the module between a fraction and another " +
            "fraction or a fraction and an integer.")
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero is undefined.")

        return self % other

    def __pow__(self, power):
        '''
        Raises the fraction to any given power.

        Args
        ----
        power : int
            The power to raise the fraction.

        Returns
        -------
        Fraction
            The result of the exponentiation.
        
        Raises
        ------
        TypeError
            If power is not an instance of int.    
        '''
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
        '''
        Raises the fraction to any given power.

        Args
        ----
        power : int
            The power to raise the fraction.

        Returns
        -------
        Fraction
            The result of the exponentiation.
        
        Raises
        ------
        TypeError
            If power is not an instance of int.    
        '''
         # Exception handling
        if not isinstance(power, int):
            raise TypeError("The power must be an integer.")

        return self ** power

    def __eq__(self, other):
        '''
        Checks if two fractions are equal.

        Args
        ----
        other : Fraction or int
            A fraction or integer to be compared with the current fraction.

        Returns
        -------
        Bool
            The result of the comparison.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        '''
        Checks if the current fraction is smaller than other.

        Args
        ----
        other : Fraction or int
            A fraction or integer to be compared with the current fraction.

        Returns
        -------
        Bool
            The result of the comparison.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other):
        '''
        Checks if the current fraction is smaller or equal than other.

        Args
        ----
        other : Fraction or int
            A fraction or integer to be compared with the current fraction.

        Returns
        -------
        Bool
            The result of the comparison.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other):
        '''
        Checks if the current fraction is greater than other.

        Args
        ----
        other : Fraction or int
            A fraction or integer to be compared with the current fraction.

        Returns
        -------
        Bool
            The result of the comparison.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other):
        '''
        Checks if the current fraction is greater or equal than other.

        Args
        ----
        other : Fraction or int
            A fraction or integer to be compared with the current fraction.

        Returns
        -------
        Bool
            The result of the comparison.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __ne__(self, other):
        '''
        Checks if two fractions are not equal.

        Args
        ----
        other : Fraction or int
            A fraction or integer to be compared with the current fraction.

        Returns
        -------
        Bool
            The result of the comparison.

        Raises
        ------
        TypeError
            If other is not an instance of Fraction or of int.
        '''
        # Exception handling
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise TypeError("You can only compare a fraction with another fraction or an integer.")

        return not self == other

    def __neg__(self):
        '''
        Returns the negative of the fraction.
        '''
        return Fraction(-1) * self

    def __pos__(self):
        '''
        Returns the positive of the fraction.
        '''
        return self

    def __abs__(self):
        '''
        Returns the absolute value of the fraction.
        '''
        numerator = abs(self.numerator)
        denominator = self.denominator
        return Fraction(numerator, denominator)

    def __complex__(self):
        '''
        Returns the evaluated fraction as a complex. 
        '''
        return complex(self.numerator / self.denominator)

    def __int__(self):
        '''
        Returns the approximation of the evaluated fraction as an integer.
        '''
        return int(self.numerator / self.denominator)

    def __float__(self):
        '''
        Returns the evaluated fraction as a float.
        '''
        return self.numerator / self.denominator
