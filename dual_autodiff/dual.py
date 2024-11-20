
'''
Import numpy, as it is requireded for some of the functions deinied in this class.
'''

import numpy as np 

class Dual:

    def __init__(self, a, b):
        '''
        A class designed for algebraic computation of dual numbers, and automatic differentiation with dual numbers.
        '''
        self.real = a
        self.dual = b
        
  
    def __repr__(self):
        '''
        This stands for representation, provides a string representation of the object when returned
        when fed to the elvaluation function.
        '''
        return f"Dual(real = {self.real}, dual = {self.dual})"
    
    '''
    Implementing Addition, Subtraction, Multiplication, Division and Power Operators.
    ''' 
    
    def __add__(self, other):
        '''
        Implement addition.
        '''
        if isinstance(other, Dual):
            '''
            Adding real and dual part separately, e.g. Dual(a,b) + Dual(c,d) = Dual(a+c,b+d).
            '''
            real_part = self.real + other.real
            dual_part = self.dual + other.dual
            return Dual(real_part, dual_part)
            
        elif isinstance(other,(int, float)):
            '''
            Adding the a dual number to a real number e.g. Dual(a,b) + n = Dual(a+n,b).
            '''
            real = self.real + other
            dual = self.dual
            return Dual(real, dual)
        else:
            '''
            Else raise a Type error, i.e. user's input is not a number.
            '''
            raise TypeError("Addition is only supported between Dual numbers.")

    
    def __sub__(self,other):
        '''
        Implement Subtraction.
        '''
        if isinstance(other, Dual):
            '''
            Subtract real and dual part separately, e.g. Dual(a,b) - Dual(c,d) = Dual(a-c,b-d).
            '''
            real = self.real - other.real
            dual = self.dual - other.dual
            return Dual(real, dual)
            
        elif isinstance(other,(int, float)):
            '''
            Subtracting a real number from a dual number, e.g. Dual(a,b) - m = Dual(a-m,b)
            '''
            real = self.real - other
            dual = self.dual
            return Dual(real, dual)
        else:
            '''
            Else raise TypeError
            '''
            raise TypeError("Subtraction is only supported between Dual numbers.")
    
    
    
    def __mul__(self,other):
        '''
        Implementing multiplication.
        '''
        if isinstance(other, Dual):
            '''
            Multiplication between dual numbers, in general Dual(a,b)*Dual(c,d) = Dual(a*c, a*d + b*c)
            '''
            real = self.real*other.real
            dual = self.real*other.dual + self.dual*other.real
            return Dual(real, dual)
            
        elif isinstance(other,(int, float)):
            '''
            Multiplication between a dual and real number, e.g. Dual(a,b)*n = Dual(a*n,b*n)
            '''
            real = self.real*other
            dual = self.dual*other
            return Dual(real, dual)
        else:
            '''
            Else raise TypeError
            '''
            raise TypeError("Multiplication is only supported between Dual numbers.")
    
    
    def __pow__(self,n):
        '''
        Implement power.
        '''
        if isinstance(n, (int, float)): # enabling integers and decimals as inputs
            '''
            Dual number evaluated to the power of a real number:
            This is evaluated as,
            Dual(a,b)**n = Dual(a**n, n*a(n-1)*b), compare to f(Dual(a,b)) = f(a) + Dual(0,b)*f'(a).
            '''
            real = self.real**n
            dual = n*(self.real**(n-1))*self.dual
            return Dual(real, dual)

        elif isinstance(n, Dual):
            '''
            Dual number to evaluated to the power of a dual number:
            This is evaluated as,
            Dual(a,b)**Dual(c,d) = (a**c)*Dual(1, c*b/a**2 + np.log(a)*d) see report for the full derivation.
            '''
            real = self.real**n.dual
            dual = (self.real**n.dual)*((n.real*self.dual)/self.real + np.log(self.real)*n.dual)
            return Dual(real, dual)

        else:
            '''
            Else raise TypeError
            '''
            raise TypeError("Power has to be an integer, a float or a dual number")

    
    def __truediv__(self,other):
        '''
        Implement (true) division.
        '''
        if isinstance(other, Dual):
            '''
            Division between dual numbers is defined as follows:
            Dual(a,b)/Dual(c,d) = Dual(a/c, (c*b - a*d)/c**2)
            '''
            real = (self.real)/(other.real)
            dual = (other.real*self.dual - self.real*other.dual)/(other.real**2)
            return Dual(real, dual)
            
            
        elif isinstance(other,(int, float)):
            '''
            Division of a dual number by a real number.
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
            Else raise TypeError
            '''
            raise TypeError("Dicision is only supported between dual numbers")
    
    
    def __floordiv__(self,other):
        '''
        Implementing floor division.
        '''
        if isinstance(other, Dual):
            '''
            Dual number divided by a dual number.
            Follow the same exact procedure as true division, but replace / with //.
            '''
            real = (self.real)//(other.real) 
            dual = (other.real*self.dual - self.real*other.dual)//(other.real**2) 
            return Dual(real, dual)
        
        elif isinstance(other,(int, float)):
            '''
            Dual number divided by a real number.
            '''
            if other==0:
                raise ZeroDivisionError("Division by zero is undefined")
            real = self.real//other
            dual = self.dual//other
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
