'''
Implements the Complex Numbers Data Type
'''

import math

class Complex:
    '''
    An approach to complex numbers.

    Attributes
    ----------
    real : int or float
        The real part of the complex number.
    imaginary : int or float
        The imaginary part of the complex number.

    '''
    def __init__(self, real, imaginary=0):
        '''
        Initialization of an instance of Complex.

        Args
        ----
        real : int or float
            The real part of the complex number.
        imaginary : int or float
            The imaginary part of the complex number (default = 0).

        Raises
        ------
        TypeError
            If real or imaginary aren't instances of float or int.
        '''
        if not isinstance(real, (int, float)) or not isinstance(imaginary, (int, float)):
            raise TypeError("As partes real e imaginária do número complexo devem ser float" + 
            "ou int.")

        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        '''
        The abstract representation of a complex number.
        '''
        return f"Complex({self.real}, {self.imaginary})"

    def __str__(self):
        '''
        The string representation of a complex number.

        Returns
        -------
        str
            The complex number in the form a + bi.
        '''
        if self.real == 0:
            return f"i{self.imaginary}"
        if self.imaginary == 0:
            return f"{self.real}"
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        '''
        Addition of two complex numbers.

        Args
        ----
        other : Complex or int or float
            The number to be summed to the current complex.
        
        Returns
        -------
        Complex
            The sum of self and other.
        
        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only sum a complex to another complex, an integer or a float.")
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def _iadd__(self, other):
        '''
        Addition of two complex numbers.

        Args
        ----
        other : Complex or int or float
            The number to be summed to the current complex.
        
        Returns
        -------
        Complex
            The sum of self and other.
        
        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only sum a complex to another complex, an integer or a float.")
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __sub__(self, other):
        '''
        Subtraction of two complex numbers.

        Args
        ----
        other : Complex or int or float
            The number to be subtracted from the self.

        Returns
        -------
        Complex
            The subtraction of other from self.

        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only subtract a complex, an integer or a float" +
            "from a complex.")
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return Complex(real, imaginary)

    def __isub__(self, other):
        '''
        Subtraction of two complex numbers.

        Args
        ----
        other : Complex or int or float
            The number to be subtracted from the self.

        Returns
        -------
        Complex
            The subtraction of other from self.

        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only subtract a complex, an integer or a float" + 
            "from a complex.")
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return Complex(real, imaginary)

    def __mul__(self, other):
        '''
        Multiplication of complex numbers.

        Args
        ----
        other : complex or int or float
            The number be multiplied by self.
        
        Returns
        -------
        Complex
            The multiplication of self and other.
        
        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only multiply a complex by another complex, integer" +
            "or float.")
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        real = a * c - b * d
        imaginary = a * d + b * c
        return Complex(real, imaginary)

    def __imul__(self, other):
        '''
        Multiplication of complex numbers.

        Args
        ----
        other : complex or int or float
            The number be multiplied by self.
        
        Returns
        -------
        Complex
            The multiplication of self and other.
        
        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only multiply a complex by another complex, integer" +
            "or float.")
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        real = a * c - b * d
        imaginary = a * d + b * c
        return Complex(real, imaginary)
    
    def __truediv__(self, other):
        '''
        Division of complex numbers.

        Args
        ----
        other : Complex or int or float
            The number to divide self.

        Returns
        -------
        Complex
            The division of self by other.

        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        ZeroDivisionError
            If other is equal to zero.    
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only divide a complex by another complex, an int or a float.")
        if abs(other) == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        x, y = other.real, other.imaginary
        denominator = x**2 + y**2
        inverse_other = Complex(x/denominator, y/denominator)
        return self * inverse_other

    def __itruediv__(self, other):
        '''
        Division of complex numbers.

        Args
        ----
        other : Complex or int or float
            The number to divide self.

        Returns
        -------
        Complex
            The division of self by other.

        Raises
        ------
        TypeError
            If other is not an instance of Complex, int or float.
        ZeroDivisionError
            If other is equal to zero.    
        '''
        if isinstance(other, (int, float)):
            other = Complex(other)
        if not isinstance(other, Complex):
            raise TypeError("You can only divide a complex by another complex, an int or a float.")
        if abs(other) == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        x, y = other.real, other.imaginary
        denominator = x**2 + y**2
        inverse_other = Complex(x/denominator, y/denominator)
        return self * inverse_other

    def __abs__(self):
        '''
        The absolute value of a complex number.

        Returns
        -------
        float
            The absolute value of the complex.
        '''
        x, y = self.real, self.imaginary
        return math.sqrt(x**2 + y**2)

    def conjugate(self):
        '''
        The conjugate of a complex
        
        Returns
        -------
        Complex
            The complex conjugate.
        '''
        real = self.real
        imaginary = -self.imaginary
        return Complex(real, imaginary)
