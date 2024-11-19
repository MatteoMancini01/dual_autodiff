'''
The following class is designed to perform numerical differentiation.
'''
class num_diff:
    '''
    In this class there are four different functions, first order numericall differentiation with
    forward, central and backward difference and one function to compute second order derivative numerically.
    '''
    def __init__(self, f, x, h):
        '''
        Initialising input parameters;
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
            f_dash = (self.f(self.x + self.h) - self.f(self.x))/self.h
            return f_dash
    
    def first_backwards(self):
        '''
        Implementing first order numerical differentiation backward difference.
        '''
        if self.h==0:
            raise ZeroDivisionError('Division by zero is undefined')
        elif self.h<0:
            raise TypeError('Step size input must be a positive real number')
        else: 
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
            f_double_dash = (self.f(self.x + self.h) - 2*self.f(self.x) + self.f(self.x - self.h))/self.h**2 
            return f_double_dash
