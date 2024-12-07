'''
The following class is designed to perform numerical differentiation.
'''
cdef class NumDiff:
    '''
    In this class there are four different functions, first order numericall differentiation with
    forward, central and backward difference and one function to compute second order derivative numerically.
    '''
    # Declare attributes for Cython optimization
    cdef object f  # Function object (can’t type explicitly in Cython)
    cdef double x, h  # Numerical input (double for optimization)

    def __init__(self, f, x, h):
        '''
        Initialising input.

        Parameters:
            f is the input function we aim to differentiate,
            x is/are the value/s at which the function is differentiated,
            h is the step size required for numerical differentiation. In general h<<0 provides accurate results, but if h is too small
              we lose rather than gaining accuracy.
        '''
        self.f = f
        self.x = x
        self.h = h

    def first_forward(self):
        '''
        Implementing first order numerical differenitaion forward difference.
        '''
        if self.h==0:
            '''
            h cannot be zero or negative, otherwise one gets an undefined answer, hence:
            '''
            raise ZeroDivisionError('Division by zero is undefined')
        elif self.h<0:
            raise TypeError('Step size input must be a positive real number')
        else:
            '''
            Returns:
                Numerical derivative, derived with forward difference
            
            Example:
                >>> import numpy as np
                >>> from dual_autodiff import NumDiff
                >>> def f(x):
                >>>     return x + np.exp(x - x**2) # define function to differentiate
                >>> x0 = 2 # point at which the derivative is computed
                >>> h = 0.01 # step size
                >>> derivative = NumDiff(f,x0,h) # call class
                >>> result = derivative.first_forward()
                >>> print(f'Forward difference of f(x) at the point x0 = {x0}, with stepsize h = {h}, is {result}')
                Forward difference of f(x) at the point x0 = 2, with stepsize h = 0.01, is 0.5987105016421079

            '''
            f_dash = (self.f(self.x + self.h) - self.f(self.x))/self.h
            return f_dash
    
    def first_backward(self):
        '''
        Implementing first order numerical differentiation backward difference.
        '''
        if self.h==0:
            raise ZeroDivisionError('Division by zero is undefined')
        elif self.h<0:
            raise TypeError('Step size input must be a positive real number')
        else: 
            '''
            Returns:
                Numerical derivative, derived with backward difference
            
            Example:
                >>> import numpy as np
                >>> from dual_autodiff import NumDiff
                >>> def f(x):
                >>>     return x + np.exp(x - x**2) # define function to differentiate
                >>> x0 = 2 # point at which the derivative is computed
                >>> h = 0.01 # step size
                >>> derivative = NumDiff(f,x0,h) # call class
                >>> result = derivative.first_backward()
                >>> print(f'Backward difference of f(x) at the point x0 = {x0}, with stepsize h = {h}, is {result}')
                Backward difference of f(x) at the point x0 = 2, with stepsize h = 0.01, is 0.5892372009922209
            '''
            f_dash = (self.f(self.x) - self.f(self.x-self.h)) / self.h
            return f_dash
    
    def first_central(self):
        '''
        Implementing fisrt order numerical differentiation central difference.
        '''
        if self.h==0:
            raise ZeroDivisionError('Division by zero is undefined')
        elif self.h<0:
            raise TypeError('Step size input must be a positive real number')
        else: 
            '''
            Returns:
                Numerical derivative, derived with central difference
            
            Example:
                >>> import numpy as np
                >>> from dual_autodiff import NumDiff
                >>> def f(x):
                >>>     return x + np.exp(x - x**2) # define function to differentiate
                >>> x0 = 2 # point at which the derivative is computed
                >>> h = 0.01 # step size
                >>> derivative = NumDiff(f,x0,h) # call class
                >>> result = derivative.first_central()
                >>> print(f'Central difference of f(x) at the point x0 = {x0}, with stepsize h = {h}, is {result}')
                Central difference of f(x) at the point x0 = 2, with stepsize h = 0.01, is 0.5939738513171644
            '''
            f_dash = (self.f(self.x + self.h) - self.f(self.x - self.h))/(2*self.h)
            return f_dash
    
    def second_order(self):
        '''
        Implementing second order numerical differentiation.
        '''
        if self.h==0:
            raise ZeroDivisionError('Division by zero is undefined')
        elif self.h<0:
            raise TypeError('Step size input must be a positive real number')
        else: 
            '''
            Returns:
                Numerical second order derivative.
            
            Example:
                >>> import numpy as np
                >>> from dual_autodiff import NumDiff
                >>> def f(x):
                >>>     return x + np.exp(x - x**2) # define function to differentiate
                >>> x0 = 2 # point at which the derivative is computed
                >>> h = 0.01 # step size
                >>> derivative = NumDiff(f,x0,h) # call class
                >>> result = derivative.second_order()
                >>> print(f'Second derivative of f(x) at the point x0 = {x0}, with stepsize h = {h}, is {result}')
                Second derivative of f(x) at the point x0 = 2, with stepsize h = 0.01, is 0.9473300649887051
            '''
            f_double_dash = (self.f(self.x + self.h) - 2*self.f(self.x) + self.f(self.x - self.h))/self.h**2 
            return f_double_dash
