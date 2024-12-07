import numpy as np
from dual_autodiff import NumDiff

'''
Test Numerical Differentiation.

This python files allows us to test all the functions within the Dual class.

Using a class for our test python file, allows us to add TestDual to __init__.py, so that the user can run tests on
Jupyter Notebook direclty.
'''

class TestNumDiff:
    '''
    TestNumDiff contains a series of functions designed to test NumDiff.

    Testing numerical differentiation can be tricky, as the output provided is an estimate
    of the analytical solution, hence, to test all the different numerical differentiation
    methods, one can compare the numerical to the analytical results up to certain decimal places.

    For all tests, h is the step size, and x0 is the value for which the derivative is evaluated.
    '''

    def test_forward(self):
        '''
        Testing forward difference, compared to analytical up to 3 decimal places.
        '''
        h = 0.001
        x0 = 0.2

        def f(x): 
            '''
            Let us define f(x), the function we want to differentiate.
            '''
            return x + np.tan(x)
    
        def f_diff(x): 
            '''
            Let us define the analytical derivative i.e. f'(x)
            '''
            return 1 + np.cos(x)**(-2)
        
        nd = NumDiff(f,x0,h)
        num_result = nd.first_forward()
        
        assert round(num_result, 3)==round(f_diff(x0), 3)

    def test_central(self):
        '''
        Testing central difference, compared to analytical up to 5 decimal places, 
        (as this method is more accurate than the fowrward and backward differences).
        '''
        h = 0.001
        x0 = 0.2

        def f(x): 
            '''
            Let us define f(x), the function we want to differentiate.
            '''
            return x + np.tan(x)
    
        def f_diff(x): 
            '''
            Let us define the analytical derivative i.e. f'(x)
            '''
            return 1 + np.cos(x)**(-2)
        
        nd = NumDiff(f,x0,h)
        num_result = nd.first_central()
        
        assert round(num_result, 5)==round(f_diff(x0), 5)

    
    def test_backward(self):
        '''
        Testing backward difference, compared to analytical up to 3 decimal places.
        '''
        h = 0.001
        x0 = 0.2

        def f(x): 
            '''
            Let us define f(x), the function we want to differentiate.
            '''
            return x + np.tan(x)
    
        def f_diff(x): 
            '''
            Let us define the analytical derivative i.e. f'(x)
            '''
            return 1 + np.cos(x)**(-2)
        
        nd = NumDiff(f,x0,h)
        num_result = nd.first_backward()
        
        assert round(num_result, 3)==round(f_diff(x0), 3)


    def test_second_order(self):
        '''
        Testing second order numerical difference, compared to analytical up to 3 decimal places.
        '''
        h = 0.001
        x0 = 0.2

        def f(x): 
            '''
            Let us define f(x), the function we want to differentiate.
            '''
            return x + np.tan(x)
    
        def f_sec_der(x): 
            '''
            Let us also define the analytical second derivative i.e. f''(x)
            '''
            return 2*np.tan(x)*np.cos(x)**(-2)
        
        nd = NumDiff(f,x0,h)
        num_result = nd.second_order()
        
        assert round(num_result, 3)==round(f_sec_der(x0), 3)