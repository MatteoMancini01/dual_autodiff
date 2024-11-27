
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
            >>> print(f'x*n = {x*n}')
            x*n = Dual(real=6, dual=3)

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

    This is very important to ensure consistency, symmetry and flexibility in computation!
    '''
    def __radd__(self, other):
        '''
        Implementing reverse addidion, before we had `Dual(a,b) + n`.
        Adding a daul number to a real number, e.g. `n + Dual(a,b)`.

        Follow the same procedure as before.

        '''
        if isinstance(other,(int, float)):

            '''
            Parameters:
                other: at this instance is of the form input `int` or `float` number.

            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the sum of a dual and a real number.

            Example:
                >>> from dual_autodiff import Dual
                >>> x = Dual(2,1)
                >>> n = 3
                >>> print(f'n + x = {n+x}')
                n + x = Dual(real=5, dual=1)
            '''

            real = other + self.real
            dual = self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Addition is only supported with real numbers.")
    
    
    def __rsub__(self,other):
        '''
        Implementing reverse subtraction.
        '''
        if isinstance(other,(int, float)):

            '''
            Subtracting a dual number from a real number.

            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the subtraction between a real and dual number.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 3
            >>> print(f'n - x = {n-x}')
            n - x = Dual(real=1, dual=-1)
            '''

            real = other - self.real 
            dual = -self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Subtraction is only supported with real numbers.")
    
    
    
    def __rmul__(self,other):
        '''
        Implementing reverse Multiplication.
        '''
        if isinstance(other,(int, float)):

            '''
            Parameters:
            other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the product between a dual number and a real.

            Example:
                >>> from dual_autodiff import Dual
                >>> x = Dual(2,1)
                >>> n = 3
                >>> print(f'n*x = {n*x}')
                x*n = Dual(real=6, dual=3)
            '''
            
            real = other*self.real
            dual = other*self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Multiplication is only supported with real numbers")
    
        
    def __rpow__(self,n):
        '''
        Implementing reverse power.

        Evaluating a real number to the power of a daul numner.
        One can follow a similar procedure as before.
        To evaluate $n^{(c + \epsilon d)}$ where $n$ is a real number, set $n = (a + \epsilon b)$ where $a=n$ and $b=0$, plug this into
        the previus expression for dual to the power of a dual, then $n^{(c + \epsilon d)} = n^c (1 + \epsilon log(n)d)$.

        '''
        if isinstance(n, (int, float)):
            '''
            Parameters:
                n: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the a dual number evaluated at the power of a real number.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 3
            >>> print(f'n**x = {n**x}')
            n**x = Dual(real=9, dual=9.887510598012987)
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
            Evaluation: $\frac{n}{a + \epsilon b} = \frac{n}{a}(\left 1 - \epsilon \frac{b}{a}\right)$

            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the dividing a real number by a dual numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 4
            >>> print(f'n/x = {n/x}')
            n/x = Dual(real = 2.0, dual = -1.0)

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
            
            '''
            Evaluation; $n//(a + \epsilon b) = n//a(\left 1 - \epsilon b//a\right)$
            
            Parameters:
                other: at this instance other is of the form `int` or `float`.
            
            Returns:
                str: `Dual(real=<real>, dual=<dual>)`: output is the dividing a real number by a dual numbers.

            Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> n = 4
            >>> print(f'n//x = {n//x}')
            n//x = Dual(real = 2, dual = -1)
            '''
            real = other//self.real
            dual = (-other*self.dual)//(self.real**2)
            return Dual(real, dual) 
       
        else: 
            raise TypeError("Floor division is only supported with real numbers.")


    '''
    Adding some of the esseintial functions, in particulat trigonometric, hyperbolic, exponential and logarithmic functions.
    For all the fucntions below, recall f(a + ε*b) = f(a) + ε*b*f'(a).

    Furthermore, self is the variable one wants to compute the function for, e.g. x=Dual(2,1), x.sin()
    '''

    def exp(self):
        '''
        For the exponential evaluated at $x$, where $x = a + \epsilon b$;
        real part: $f(a) = e^a$
        dual part: $bf'(a) = be^a$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,3)
            >>> exp_x = x.exp()
            >>> print(f'exp(x) = {exp_x}')
            exp(x) = Dual(real = 7.38905609893065, dual = 22.16716829679195)
        '''
        real = np.exp(self.real)
        dual = self.dual*real
        return Dual(real, dual)

    def sin(self):
        '''
        For the sine function evaluated at $x$, where $x = a + \epsilon b$;
        real part: $f(a) = \sin{a}$
        dual part: $bf'(a) = b\cos{a}$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`
        
        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> sin_x = x.sin()
            >>> print(f'sin(x) = {sin_x}')
            sin(x) = Dual(real = 0.9092974268256817, dual = -0.4161468365471424)
        '''
        real = np.sin(self.real)
        dual = self.dual*np.cos(self.real)
        return Dual(real, dual)
    
    def cos(self):
        '''
        For the cosine function evaluated $x$, where $x = a + \epsilon b$;
        real part: $f(a) = \cos{a}$
        dual part: $bf'(a) = -b\sin{a}$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,1)
            >>> cos_x = x.cos()
            >>> print(f'cos(x) = {cos_x}')
            cos(x) = Dual(real = -0.4161468365471424, dual = -0.9092974268256817)
        '''
        real = np.cos(self.real)
        dual = -self.dual*np.sin(self.real)
        return Dual(real, dual)
    
    def tan(self):
        '''
        For the tan function evaluated at $x$, where $x = a + \epsilon b$;
        real part: $f(a) = \tan{a}$
        dual part: $bf'(a) = b\sec^2{a}$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,6)
            >>> tan_x = x.tan()
            >>> print(f'tan(x) = {tan_x}')
            tan(x) = Dual(real = -2.185039863261519, dual = 34.6463952242515)
        '''
        real = np.tan(self.real)
        dual = self.dual/(np.cos(self.real))**2
        return Dual(real, dual)
    
    def log(self):
        '''
        For the logarithmic function evaluated at $x$, where $x = a + \epsilon b$;
        real part: $f(a) = \log({a})$
        dual part: $bf'(a) =\frac{b}{a}}$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,6)
            >>> log_x = x.log()
            >>> print(f'log(x) = {log_x}')
            log(x) = Dual(real = 0.6931471805599453, dual = 3.0)
        '''        
        real = np.log(self.real)
        dual = self.dual/self.real
        return Dual(real, dual)
    

    def sinh(self):
        '''
        For the sinh function evaluated at $x$, where $x = a + \epsilon b$;
        real part: $f(a) = \sinh{a}$
        dual part: $bf'(a) =b\cosh{a}}$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,6)
            >>> sinh_x = x.sinh()
            >>> print(f'sinh(x) = {sinh_x}')
            sinh(x) = Dual(real = 3.626860407847019, dual = 22.57317414650179)
        '''
        real = np.sinh(self.real)
        dual = self.dual*np.cosh(self.real)
        return Dual(real, dual)

    def cosh(self):
        '''
        For the cosh function evaluated at $x$, where $x = a + \epsilon b$;
        real part: $f(a) = \cosh{a}$
        dual part: $bf'(a) =b\sinh{a}}$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,6)
            >>> cosh_x = x.cosh()
            >>> print(f'cosh(x) = {cosh_x}')
            cosh(x) = Dual(real = 3.7621956910836314, dual = 21.761162447082114)
        '''
        real = np.cosh(self.real)
        dual = self.dual*np.sinh(self.real)
        return Dual(real, dual)
    
    def tanh(self):
        '''
        For the tanh function evaluated at $x$, where $x = a + \epsilon b$;
        real part: $f(a) = \tanh{a}$
        dual part: $bf'(a) =\frac{b}{\cosh^2{a}}$

        Returns:
            str: `Dual(real=<real>, dual=<dual>)`

        Example:
            >>> from dual_autodiff import Dual
            >>> x = Dual(2,6)
            >>> tanh_x = x.tanh()
            >>> print(f'tanh(x) = {tanh_x}')
            tanh(x) = Dual(real = 0.9640275800758169, dual = 0.4239049491189868
        '''
        real = np.tanh(self.real)
        dual = self.dual/(np.cosh(self.real))**2
        return Dual(real, dual)

    def partial_derivative(self, var_index, func, *args):
        '''
        Computes the partial derivative of a function using automatic differentiation with dual numbers.

        Parameters:
            var_index: The index of the variable to differentiate with respect to.
            func: The function to differentiate.
            *args: The values at which the function is differentiated.

        Returns:
            The partial derivative of the function with respect to the variable at `var_index`.

        Example:
        Computing first order partial derivatives of the function $f(x,y,z) = xy + x\cos{z} + \sin{y}$ at the point $(1,-1,2)$
        with respect of each variable

            >>> from dual_autodiff import Dual
            >>> def f(x,y,z):
            >>>     return x*y + x*z.cos() + y.sin() # define the function to differentiate
            >>> d = Dual(1,0) # chose any numbers for real and dual part
            >>> x,y,z = Dual(1,0),Dual(-1,0),Dual(2,0) # always set the dual part equal to zero when assining values to variables
            >>> x_partial = d.partial_derivative(0,f,x,y,z) # index 0 for x
            >>> x_partial = d.partial_derivative(1,f,x,y,z) # index 1 for y
            >>> x_partial = d.partial_derivative(2,f,x,y,z) # index 2 for z
            >>> print(f"Partial derivaive of f with respect to x, at x,y,z=1,-1,2 is {x_partial}")
            >>> print(f"Partial derivaive of f with respect to y, at x,y,z=1,-1,2 is {x_partial}")
            >>> print(f"Partial derivaive of f with respect to z, at x,y,z=1,-1,2 is {x_partial}")
            Partial derivaive of f with respect to x, at x,y,z=1,-1,2 is -1.4161468365471424
            Partial derivaive of f with respect to y, at x,y,z=1,-1,2 is 1.5403023058681398
            Partial derivaive of f with respect to z, at x,y,z=1,-1,2 is -0.9092974268256817
        '''
        variables = list(args) # convert args into a list

        # Replace the variable at var_index with a Dual number
        variables[var_index] = Dual(args[var_index].real, 1)  # Assign a dual component of 1

        # Evaluate the function with the Dual variable
        df = func(*variables)

        # Return the dual part of the result, which represents the derivative
        return df.dual

