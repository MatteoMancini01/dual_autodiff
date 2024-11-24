
'''
Import numpy, as it is requireded for some of the functions deinied in this class.
'''

import numpy as np 

class Dual:
    """
    A class designed for algebraic computation of dual numbers, and automatic differentiation with dual numbers.

    Dual numbers are used for algebraic computations and automatic differentiation, especially in the context of 
    optimization and numerical analysis.
    """

    def __init__(self, real, dual):
        """
        Initialises dual numbers with a real and dual part.

        A dual number is represented as `real + ε*dual`, where `ε` is an infinitesimal.
        The real part corresponds to the value of the function, and the dual part 
        corresponds to the derivative.

        Useful properties of the infinitesimal $\epsilon$:
           - $\epsilon^n = 0$ for $n \geq 2$
           - $f(a + \epsilon b) = f(a) + \epsilon bf'(a)$

        Parameters:
            real (int or float): input real part
            dual (int or float): input dual part
        """
        self.real = real
        self.dual = dual
        
  
    def __repr__(self):
        '''
        This stands for representation, provides a string representation of the object when returned
        when fed to the elvaluation function.

        The string representation is in the form `Dual(real=<real>, dual=<dual>)`,
        which makes it easy to interpret the real and dual parts of the number.

        Returns:
            str: A string representation of the dual number.

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> print(f'The dual number x = {x}') 
            The dual number x = Dual(real=2, dual=1)
            >>> print(f'The real part of x is {x.real}') 
            The real part of x is 2
            >>> print(f'The dual part of x is {x.dual}') 
            The dual part of x is 1
           
        '''
        return f"Dual(real = {self.real}, dual = {self.dual})"
    
    def __neg__(self):
        '''
        Changning the sign of a dual number to negative `-Dual(real=<real>, dual=<dual>) = Dual(real=-<real>, dual=-<dual>)`

        Parameter:
              str: `Dual(real=<real>, dual=<dual>)`: input is a dual number

        Returns:
            str: `Dual(real=<-real>, dual=<-dual>)`: output is a dual number

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> y = - x
            >>> print(f'y = {y}')
            y = Dual(real=-2, dual=-1)
        '''
        return Dual(-self.real, -self.dual)
    
    '''
    Implementing Addition, Subtraction, Multiplication, Division and Power Operators.
    ''' 
    
    def __add__(self, other):
        '''
        Implement addition.

        Computes addition between dual numbers, and real numbers.
        Addition in dual numbers is simple, like in complex numbers, where the real and imaginary parts are added separately, 
        dual numbers follow the same principle, real and dual parts of dual numbers are added separately. 
        For example, let $x = a + \epsilon b$ and $y = c + \epsilon d$ then $x + y = a + c + \epsilon (b + d)$.

        '''
        if isinstance(other, Dual):
            '''
            Adding real and dual part separately.

            Parameters:
                other: at this instance is of the form `Dual(real=<real>, dual=<dual>)`.
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the sum of the dual numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> y = Dual(5,10)
            >>> print(f'x + y = {x+y}')
            x + y = Dual(real=7, dual=11)
            '''
            real_part = self.real + other.real
            dual_part = self.dual + other.dual
            return Dual(real_part, dual_part)
            
        elif isinstance(other,(int, float)):
            '''
            Adding a dual number to a real number.

            Parameters:
                other: at this instance is of the form input `int` or `float` number.

            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the sum of a dual and a real number.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 3
            >>> print(f'x + n = {x+n}')
            x + n = Dual(real=5, dual=1)
            '''
            real = self.real + other
            dual = self.dual
            return Dual(real, dual)
        else:
            '''
            Else: 
                raise: TypeError. # If any of the above conditions are not satisfied TypeError is raised.
            '''
            raise TypeError("Addition is only supported between Dual numbers.")

    
    def __sub__(self,other):
        '''
        Implement Subtraction.

        Computing subtraction between dual numbers.

        This follows the same principle of addition, when subtracting dual numbers, the real part is subtracted from the other real part,
        and the dual part is subtracted from the other dual part. 

        For example, let $x = a + \epsilon b$ and $y = c + \epsilon d$ then $x - y = a - c + \epsilon (b - d)$.
        '''
        if isinstance(other, Dual):
            '''
            Subtract real and dual part separately.

            Parameters:
                other: at this instance other is of the form `Dual(real=<real>, dual=<dual>)`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the subtraction between dual numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> y = Dual(5,10)
            >>> print(f'x - y = {x-y}')
            x + y = Dual(real=-3, dual=-9)

            '''
            real = self.real - other.real
            dual = self.dual - other.dual
            return Dual(real, dual)
            
        elif isinstance(other,(int, float)):
            '''
            Subtracting a real number from a dual number.

            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the subtraction between a dual and real number.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 3
            >>> print(f'x - n = {x-n}')
            x - n = Dual(real=-1, dual=1)

            '''
            real = self.real - other
            dual = self.dual
            return Dual(real, dual)
        else:
            '''
            Else:
                raise: TypeError
            '''
            raise TypeError("Subtraction is only supported between Dual numbers.")
    
    
    
    def __mul__(self,other):
        '''
        Implementing multiplication.

        Multiplication between dual numbers can be expressed as follows:
        Let $x = a + \epsilon b$ and $y = c + \epsilon d$ then $xy = ac + \epsilon (ad + bc)$.
        '''
        if isinstance(other, Dual):
            '''
            Multiplication between dual numbers.
            Parameters:
                other: at this instance other is of the form `Dual(real=<real>, dual=<dual>)`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the product between dual numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> y = Dual(5, 10)
            >>> print(f'xy = {x*y}')
            xy= Dual(real=10, dual=25)

            '''
            real = self.real*other.real
            dual = self.real*other.dual + self.dual*other.real
            return Dual(real, dual)
            
        elif isinstance(other,(int, float)):
            '''
            Multiplication between a dual and real number.

            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the product between a dual number and a real.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 3
            >>> print(f'x - n = {x-n}')
            x - n = Dual(real=-1, dual=1)

            '''
            real = self.real*other
            dual = self.dual*other
            return Dual(real, dual)
        else:
            '''
            Else:
                raise: TypeError
            '''
            raise TypeError("Multiplication is only supported between Dual numbers.")
    
    
    def __pow__(self,n):
        '''
        Implement power.

        Implementing power can be quite challenging for dual numbers, there are three different possibilities one can think of, namely:
            - a dual number to the power of a real number
            - a dual number to the power of a dual number
            - a real number to the power of a dual number
        The aim is to caver all of the above cases. In particular for `__pow__` the first two are covered and in `__rpow__` the last case.
        '''
        if isinstance(n, (int, float)): 
            '''
            Dual number evaluated to the power of a real number.

            Let $x = a + \epsilon b$ be a dual number, and $n$ be a real number, also recall that $f(a + \epsilon b) = f(a) + \epsilon bf'(a)$:
            if $f(x) = x^n$ then $f'(x) = nx^{n-1}$ $\implies (a + \epsilon b)^n = a^n + \epsilon nba^{n-1}$.

            Convering the above into code.

            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the a dual number evaluated at the power of a real number.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 3
            >>> print(f'x**n = {x**n}')
            x**n = Dual(real=8, dual=12)
            '''
            real = self.real**n
            dual = n*(self.real**(n-1))*self.dual
            return Dual(real, dual)

        elif isinstance(n, Dual):
            '''
            Dual number to evaluated to the power of a dual number.
            Let $x = a + \epsilon b$, $y = c + \epsilon d$ be a dual numbers, one can follow a similar procedure as before:
            if $f(x,y) = x^y$ then $\frac{\partial f(x,y)}{\partial x} = yx^{y-1}$ and $\frac{\partial f(x,y)}{\partial y} = log(x)x^y$ 
            $\implies (a + \epsilon b)^{c + \epsilon d} = a^c + \epsilon a^c(\frac{cb}{a} + log(a)d)$.
            
            Convering the above into code.

            Parameters:
                other: at this instance other is of the form `Dual(real=<real>, dual=<dual>)`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the power of a dual number evaluated at the power of another dual number.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> y = Dual(-1,1)
            >>> print(f'x**y = {x**y}')
            x**y = Dual(real=0.5, dual=0.09657359027997264)
            '''
            real = self.real**n.real
            dual = (self.real**n.real)*((n.real*self.dual)/self.real + np.log(self.real)*n.dual)
            return Dual(real, dual)

        else:
            '''
            Else:
              raise: TypeError
            '''
            raise TypeError("Power has to be an integer, a float or a dual number")

    
    def __truediv__(self,other):
        '''
        Implement (true) division.

        Division between dual numbers is very similar to division of complex numbers, one can multiply both numerator and denominator by the 
        reciprocal of the denominator, this will allow to split the division into real and dual parts, this is illustrated below:

        $$
        \frac{a + \epsilon b}{c + \epsilon d} = \frac{a + \epsilon b}{c + \epsilon d}\frac{c - \epsilon d}{c - \epsilon d} = 
        \frac{a}{c} + \epsilon \left(\frac{b}{c} - \frac{ad}{c^2}\right) 
        $$
        '''
        if isinstance(other, Dual):
            '''
            Division between dual numbers.

            Parameters:
                other: at this instance other is of the form `Dual(real=<real>, dual=<dual>)`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the division between dual numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> y = Dual(-1,1)
            >>> print(f'x/y = {x/y}')
            x/n = Dual(real = -2.0, dual = -3.0)
            '''
            real = (self.real)/(other.real)
            dual = (other.real*self.dual - self.real*other.dual)/(other.real**2)
            return Dual(real, dual)
            
            
        elif isinstance(other,(int, float)):
            '''
            Division of a dual number by a real number.

            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the dividing a dual number by a real numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 4
            >>> print(f'x/n = {x/n}')
            x/n = Dual(real = 0.5, dual = 0.25)

            '''
            if other==0:
                '''
                If division by zero occurs, raise ZeroDivisionError.
                '''
                raise ZeroDivisionError("Division by zero is undefined")
            '''
            Compotation; Dual(a,b)/n = Dual(a/n,b/n)
            '''
            real = self.real/other
            dual = self.dual/other
            return Dual(real, dual)
        else:
            '''
            Else:
              raise: TypeError
            '''
            raise TypeError("Dicision is only supported between dual numbers")
    
    
    def __floordiv__(self,other):
        '''
        Implementing floor division, this returns integers.

        This follow exatly the same procedure as before, but instead of `x/y` we compute `x//y`.
        
        '''
        if isinstance(other, Dual):
            '''
            Division between dual numbers.

            Parameters:
                other: at this instance other is of the form `Dual(real=<real>, dual=<dual>)`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the division between dual numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> y = Dual(-1,1)
            >>> print(f'x//y = {x//y}')
            x//n = Dual(real = -2, dual = -3)
            '''
            real = (self.real)//(other.real) 
            dual = (other.real*self.dual - self.real*other.dual)//(other.real**2) 
            return Dual(real, dual)
        
        elif isinstance(other,(int, float)):
            '''
            Dual number divided by a real number.

            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the dividing a dual number by a real numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 2
            >>> print(f'x//n = {x//n}')
            x//n = Dual(real = 1, dual = 0)
            '''
            if other==0:
                raise ZeroDivisionError("Division by zero is undefined")
            real = self.real//other
            dual = self.dual//other
            return Dual(real, dual)
        else:
            raise TypeError("Floor Division is only supported between dual numbers")

    '''
    Implementing Reverse Addition, Subtraction, Multiplication and Division Operators.
    '''
    def __radd__(self, other):
        '''
        Implementing reverse addidion, before we had Dual(a,b) + n.
        Adding a daul number to a real number, e.g. n + Dual(a,b) = Dual(n+a,b).
        '''
        if isinstance(other,(int, float)):
            real = other + self.real
            dual = self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Reversed addition is only supported with real numbers.")
    
    
    def __rsub__(self,other):
        '''
        Implementing reverse subtraction
        '''
        if isinstance(other,(int, float)):
            '''
            Subtracting a dual number from a real number, e.g. n-Dual(a,b) = Dual(n-a,-b)
            '''
            real = other - self.real 
            dual = -self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Reversed subtraction is only supported with real numbers.")
    
    
    
    def __rmul__(self,other):
        '''
        Implementing reverse Multiplication
        '''
        if isinstance(other,(int, float)):
            '''
            Multipling a real number by a dual number, e.g. n*Dual(a,b) = Dual(n*a,n*b)
            '''
            real = other*self.real
            dual = other*self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Reversed multiplication is only supported with real numbers")
    
        
    def __rpow__(self,n):
        '''
        Implementing reverse power.
        '''
        if isinstance(n, (int, float)):
            '''
            Evaluating a real number to the power of a daul numner.
            One can follow a similar procedure as before.
            To evaluate n**Dual(c,d) where n is a real number, set n = Dual(a,b) where a=n and b=0, plug this into
            the previus expression for dual to the power of a dual, then n**Dual(c,d) = n**c*Dual(1, numpy.log(n)*d).
            '''
            real = n**self.real
            dual = (n**self.real)*(np.log(n)*self.dual)
            return Dual(real, dual)
        else:
            raise TypeError('Power only supports Dual or real numbers as inputs')


    
    def __rtruediv__(self, other):
        '''
        Implementing reverse standard division.
        '''
        if isinstance(other, (int, float)):
            '''
            Division of a real number by a dual number.
            '''
            if self.real==0:
                raise ZeroDivisionError("Division by zero is undefined")
            '''
            Evaluation; n/Dual(a,b) = (n/a)*Dual(1, -b/a)
            '''
            real = other/self.real
            dual = (-other*self.dual)/(self.real**2)
            return Dual(real, dual)
       
        else:
            raise TypeError("Reversed division is only supported with real numbers.")
    
    def __rfloordiv__(self, other):
        '''
        Implementing reverse floor division.
        '''
        if isinstance(other, (int, float)):
            '''
            Division of a real number by a dual number.
            This follows the same procedure as reverse standard division.
            '''
            if self.real==0:
                raise ZeroDivisionError("Division by zero is undefined") 
            real = other//self.real
            dual = (-other*self.dual)//(self.real**2)
            return Dual(real, dual) 
       
        else: 
            raise TypeError("Reversed division is only supported with real numbers.")


    '''
    Adding some of the esseintial functions, in particulat trigonometric, hyperbolic, exponential and logarithmic functions.
    For all the fucntions below, recall f(a + ε*b) = f(a) + ε*b*f'(a).

    Furthermore, self is the variable one wants to compute the function for, e.g. x=Dual(2,1), x.sin()
    '''

    def exp(self):
        '''
        For the exponential evaluated at x, where x = a + ε*b;
        real part: f(a) = exp(a)
        dual part: b*f'(a) = b*exp(a)
        '''
        real = np.exp(self.real)
        dual = self.dual*real
        return Dual(real, dual)

    def sin(self):
        '''
        For the sine function evaluated at x, where x = a + ε*b;
        real part: sin(a)
        dual part: b*cos(a)
        '''
        real = np.sin(self.real)
        dual = self.dual*np.cos(self.real)
        return Dual(real, dual)
    
    def cos(self):
        '''
        For the cosine function evaluated at x, where x = a + ε*b;
        real part: cos(a)
        dual part: - b*sin(a)
        '''
        real = np.cos(self.real)
        dual = -self.dual*np.sin(self.real)
        return Dual(real, dual)
    
    def tan(self):
        '''
        For the tan function evaluated at x, where x = a + ε*b;
        real part: tan(a)
        dual part: b*sec(a)**2
        '''
        real = np.tan(self.real)
        dual = self.dual/(np.cos(self.real))**2
        return Dual(real, dual)
    
    def log(self):
        '''
        For the logarithmic function evaluated at x, where x = a + ε*b;
        real part: log(a)
        dual part: b/a
        '''        
        real = np.log(self.real)
        dual = self.dual/self.real
        return Dual(real, dual)
    

    def sinh(self):
        '''
        For the sinh function evaluated at x, where x = a + ε*b;
        real part: sinh(a)
        dual part: b*cosh(a)
        '''
        real = np.sinh(self.real)
        dual = self.dual*np.cosh(self.real)
        return Dual(real, dual)

    def cosh(self):
        '''
        For the cosh function evaluated at x, where x = a + ε*b;
        real part: cosh(a)
        dual part: b*sinh(a)
        '''
        real = np.cosh(self.real)
        dual = self.dual*np.sinh(self.real)
        return Dual(real, dual)
    
    def tanh(self):
        '''
        For the tanh function evaluated at x, where x = a + ε*b;
        real part: tanh(a)
        dual part: b/cosh(a)**2
        '''
        real = np.tanh(self.real)
        dual = self.dual/(np.cosh(self.real))**2
        return Dual(real, dual)

    def partial_derivative(self, var_index, func, *args):
        '''
        Computes the partial derivative of a function using automatic differentiation with dual numbers.

        Arguments:
        var_index: The index of the variable to differentiate with respect to.
        func: The function to differentiate.
        *args: The values at which the function is differentiated.

        Returns:
        The partial derivative of the function with respect to the variable at `var_index`.
        '''
        # Convert the arguments to a list to allow modifications
        variables = list(args)

        # Replace the variable at var_index with a Dual number
        variables[var_index] = Dual(args[var_index].real, 1)  # Assign a dual component of 1

        # Evaluate the function with the Dual variable
        df = func(*variables)

        # Return the dual part of the result, which represents the derivative
        return df.dual

