# Our task here is to define a class containg dual and some other functions such as sin, cos, tan, log, exp and other essential functions

import numpy as np # import required package

class Dual:

    def __init__(self, a, b): # __init__ initialises the variables self.real/dual with the values a/b
        self.real = a
        self.dual = b
        
  
    def __repr__(self): # __repr__ provides a string representation of the object when printed
        return f"Dual(real = {self.real}, dual = {self.dual})"
    
    # Implementing Addition, Subtraction, Multiplication, Division and Power between dual numbers

    # Implementing Addition
    def __add__(self, other):
        if isinstance(other, Dual):
            # Adding real and dual part separately
            real_part = self.real + other.real
            dual_part = self.dual + other.dual
            return Dual(real_part, dual_part)
            # Adding a real number to a dual
        elif isinstance(other,(int, float)):
            real = self.real + other
            dual = self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Addition is only supported between Dual numbers.")

    # Implementing Subtraction
    def __sub__(self,other):
        if isinstance(other, Dual):
            # Subtracting real and dual parts separately
            real = self.real - other.real
            dual = self.dual - other.dual
            return Dual(real, dual)
            # Subtraction between dual and real numbers
        elif isinstance(other,(int, float)):
            real = self.real - other
            dual = self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Subtraction is only supported between Dual numbers.")
    
    
    # Implementing Multiplication
    def __mul__(self,other):
        if isinstance(other, Dual):
            # Multiplication between dual numbers
            real = self.real*other.real
            dual = self.real*other.dual + self.dual*other.real
            return Dual(real, dual)
            # Multiplication between dual and real numbers
        elif isinstance(other,(int, float)):
            real = self.real*other
            dual = self.dual*other
            return Dual(real, dual)
        else:
            raise TypeError("Multiplication is only supported between Dual numbers.")
    
    # Implementing Power
    def __pow__(self,n):

        if isinstance(n, (int, float)): # enabling integers and decimals as inputs
            real = self.real**n
            dual = n*(self.real**(n-1))*self.dual
            return Dual(real, dual)

        elif isinstance(n, Dual):
            real = self.real**n.dual
            dual = (self.real**n.dual)*((n.real*self.dual)/self.real + np.log(self.real)*n.dual)
            return Dual(real, dual)

        else:
            raise TypeError("Power has to be an integer or a float")

    # Implementing Standard Division
    def __truediv__(self,other):
        if isinstance(other, Dual):
            # Division between dual numbers
            real = (self.real)/(other.real) # a*c/c**2 = a/c
            dual = (other.real*self.dual - self.real*other.dual)/(other.real**2) # (c*b - a*d)/c**2
            return Dual(real, dual)
            # Dividing a dual number by a real number
        elif isinstance(other,(int, float)):
            if other==0:
                raise ZeroDivisionError("Division by zero is undefined")
            real = self.real/other
            dual = self.dual/other
            return Dual(real, dual)
        else:
            raise TypeError("Dicision is only supported between dual numbers")
    
    # Implementing Integer (Floor) Division
    def __floordiv__(self,other):
        if isinstance(other, Dual):
            # Division between dual numbers
            real = (self.real)//(other.real) # a*c//c**2 = a//c
            dual = (other.real*self.dual - self.real*other.dual)//(other.real**2) # (c*b - a*d)//c**2
            return Dual(real, dual)
        # Division betweeen dual and real numbers
        elif isinstance(other,(int, float)):
            if other==0:
                raise ZeroDivisionError("Division by zero is undefined")
            real = self.real//other
            dual = self.dual//other
        else:
            raise TypeError("Floor Division is only supported between dual numbers")

# Implementing reverse addition, subtraction, multiplication and division
    # Implementing Addition
    def __radd__(self, other):

        if isinstance(other,(int, float)):
            real = other + self.real 
            dual = self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Reversed addition is only supported with real numbers.")
    
    # Implementing Subtraction
    def __rsub__(self,other):

        # Subtraction between dual and real numbers
        if isinstance(other,(int, float)):
            real = other - self.real 
            dual = self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Reversed subtraction is only supported with real numbers.")
    
    
    # Implementing Multiplication
    def __rmul__(self,other):

        # Multiplication between real and dual numbers
        if isinstance(other,(int, float)):
            real = other*self.real
            dual = other*self.dual
            return Dual(real, dual)
        else:
            raise TypeError("Reversed multiplication is only supported with real numbers")
    
        
    def __rpow__(self,n):
        if isinstance(n, (int, float)): # enabling integers and decimals as inputs
            real = n**self.real
            dual = (n**self.real)*(np.log(n)*self.dual)
            return Dual(real, dual)


    # Implementing Standard Division
    def __rtruediv__(self, other): 
        if isinstance(other, (int, float)):
            # Division of a real number by a dual number 
            if self.real==0:
                raise ZeroDivisionError("Division by zero is undefined") 
            real = other / self.real  # n / a
            dual = (-other * self.dual) / (self.real**2)  # -n * (ε * b) / a^2
            return Dual(real, dual) 
       
        else: 
            raise TypeError("Reversed division is only supported with real numbers.")
    
    def __rfloordiv__(self, other): 
        if isinstance(other, (int, float)): 
            # Division of a real number by a dual number 
            if self.real==0:
                raise ZeroDivisionError("Division by zero is undefined") 
            real = other // self.real  # n / a
            dual = (-other * self.dual) // (self.real**2)  # -n * (ε * b) / a^2
            return Dual(real, dual) 
       
        else: 
            raise TypeError("Reversed division is only supported with real numbers.")


    # Adding some of the esseintial functions

    def exp(self): # from __init__ we have already defined our input values a and b
        real = np.exp(self.real) # f(a) = exp(a)
        dual = self.dual*real # b*f'(a) = b*exp(a)
        return Dual(real, dual)

    def sin(self):
        real = np.sin(self.real) # f(a) = sin(a) real part
        dual = self.dual*np.cos(self.real) # b*f'(a) = b*cos(a) dual part
        return Dual(real, dual)
    
    def cos(self):
        real = np.cos(self.real) # f(a) = cos(a) real part
        dual = -self.dual*np.sin(self.real) # b*f'(a) = -b*sin(a) dual part
        return Dual(real, dual)
    
    def tan(self):
        real = np.tan(self.real) # f(a) = tan(a) real part
        dual = self.dual/(np.cos(self.real))**2 # b*f'(a) = b*sec^2(a) dual part
        return Dual(real, dual)
    
    def log(self):
        real = np.log(self.real) # f(a) = log(a) real part
        dual = self.dual/self.real # b*f'(a) = b/a dual part
        return Dual(real, dual)
    
    # Adding Hyperbolic Functions and natural log

    def sinh(self):
        real = np.sinh(self.real) # f(a)
        dual = self.dual*np.cosh(self.real) # b*f'(a)
        return Dual(real, dual)

    def cosh(self):
        real = np.cosh(self.real) # f(a)
        dual = self.dual*np.sinh(self.real) # b*f'(a)
        return Dual(real, dual)
    
    def tanh(self):
        real = np.tanh(self.real) # f(a)
        dual = self.dual/(np.cosh(self.real))**2 # b*f'(a)
        return Dual(real, dual)
