from dual_autodiff import Dual
import numpy as np

'''
Here it is not required to define a class for our test.py file,
the reason why I am using a class, is because I want to add TestDual to __init__.py, so that the user can run tests on
Jupyter Notebook.
'''

class TestDual: 
    def test_dual(self):
        '''
        Testing if the Dual class is working correctly, here x is a dual number.
        '''
        x = Dual(2,1)
        assert x.real==2
        assert x.dual==1

    '''
    Fow all the below functions, we are going to test for x,y and n
    where x and y are dual numbers, composed of a real and dual power,
    while n is a real number.
    '''

    def test_add(self): 
        '''
        Testing addition and reverse addition 
        for all different scenarios, real and duals, duals and duals.
        '''
        x=Dual(3, 4)
        y=Dual(2, 10)
        n= -5

        x_plus_y=x+y
        y_plus_x=y+x

        n_add_x=n+x
        x_add_n=x+n

        assert x_plus_y.real==5
        assert x_plus_y.dual==14
        assert y_plus_x.real==5
        assert y_plus_x.dual==14
        assert n_add_x.real==-2
        assert n_add_x.dual==4
        assert x_add_n.real==-2
        assert x_add_n.dual==4

    def test_sub(self): 
        '''
        Testing subtraction and reverse subtraction 
        for all different scenarios, real and duals, duals and duals.
        '''
        x=Dual(0, 1)
        y=Dual(-9, 11)
        n= 10

        x_minus_y=x-y
        y_minus_x=y-x

        n_minus_x=n-x
        x_minus_n=x-n

        assert x_minus_y.real==9
        assert x_minus_y.dual==-10
        assert y_minus_x.real==-9
        assert y_minus_x.dual==10
        assert n_minus_x.real==10
        assert n_minus_x.dual==-1
        assert x_minus_n.real==-10
        assert x_minus_n.dual==1

    def test_mult(self): 
        '''
        Testing multiplication  and reverse multiplication 
        between real and dual numbers, dual and dual numbers
        '''
        x=Dual(2, 3)
        y=Dual(-1, -2)
        n= 7

        xy=x*y
        yx=y*x

        nx=n*x
        xn=x*n

        '''
        Recall multiplication between dual numbers:
        Let x = a + εb and y = c + εd, where both x and y are dual numbers, 
        then xy = ac + ε(ad + bc).

        Recall multiplication between real and dual numbers:
        Let x = a + εb be the dual number and n the real number.
        nx = an + εbn
        '''
        assert xy.real==-2
        assert xy.dual==-7
        assert yx.real==-2
        assert yx.dual==-7
        assert nx.real==14
        assert nx.dual==21
        assert xn.real==14
        assert xn.dual==21

    def test_tdiv(self): 
        '''
        Testing standard division and reverse standard division,
        for real and dual numbers, for dual and dual numbers.
        '''
        x=Dual(2, 6)
        y=Dual(4, -2)
        n= 2

        x_div_y=x/y
        y_div_x=y/x

        n_div_x=n/x
        x_div_n=x/n

        '''
        Recall division between dual numbers:
        Let x = a + εb and y = c + εd, where both x and y are dual numbers, 
        then x/y = a/c + ε(b/c - ad/c^2).

        Recall multiplication between real and dual numbers:
        Let x = a + εb be the dual number and n the real number.
        n/x = n/a - εbn/a^2
        x/n = a/n + εb/n
        '''

        assert x_div_y.real==1/2
        assert x_div_y.dual==7/4
        assert y_div_x.real==2
        assert y_div_x.dual==-7
        assert n_div_x.real==1
        assert n_div_x.dual==-3
        assert x_div_n.real==1
        assert x_div_n.dual==3

    def test_pow(self):
        '''
        Testing power and reverse power between dual numbers, real and dual numbers
        '''
        x=Dual(3,4)
        y=Dual(2,1)
        n=2

        '''
        Dual number to the power of a dual number tests
        '''
        x_pow_y=x**y
        y_pow_x=y**x
        x_nve_pow_y=x**(-y)
        y_nve_pow_x=y**(-x)

        '''
        Dual number to the power of a real number
        '''
        x_pow_n=x**n
        x_nve_pow_n=x**(-n)

        '''
        Real number to the power of a dual number
        '''
        n_pow_x=n**x
        n_nve_pow_x=n**(-x)

        '''
        Recall power with dual numbers.

        Dual number to the power of a dual number: 
        (a + εb)^(c + εd) = a^c + ε(a^c)(cb/a + log(a)d)

        Dual number to the power of a real number:
        (a + εb)^n = a^n + nεba^(n-1)

        Real number to the power of a dual number:
        n^(a + εb) = n^a + ε(n^a)log(n)b
        '''
        a,b,c,d = 3,4,2,1
        

        assert x_pow_y.real==a**(c)
        assert x_pow_y.dual==a**(c)*(c*b/a + np.log(a)*d)
        assert x_nve_pow_y.real==a**(-c)
        assert x_nve_pow_y.dual==a**(-c)*(-c*b/a + np.log(a)*(-d))

        assert y_pow_x.real==c**(a)
        assert y_pow_x.dual==c**(a)*(a*d/c + np.log(c)*b)
        assert y_nve_pow_x.real==c**(-a)
        assert y_nve_pow_x.dual==c**(-a)*(-a*d/c + np.log(c)*(-b))

        assert x_pow_n.real==a**n
        assert x_pow_n.dual==n*b*a**(n-1)
        assert x_nve_pow_n.real==a**(-n)
        assert x_nve_pow_n.dual==-n*b*a**(-n-1)

        assert n_pow_x.real==n**a
        assert n_pow_x.dual==(n**a)*np.log(n)*b
        assert n_nve_pow_x.real==n**(-a)
        assert n_nve_pow_x.dual==(n**(-a))*np.log(n)*(-b)


    def test_fdiv(self):
        '''
        Testing floor division and reverse floor division with dual and real numbers.
        The same procedure as the standard division is applyed here, with the only difference of 
        replacing / (standard division) with // (floor division)
        '''

        x=Dual(2, 6)
        y=Dual(4, -2)
        n= 2

        x_div_y=x//y
        y_div_x=y//x

        n_div_x=n//x
        x_div_n=x//n

        '''
        Recall division between dual numbers:
        Let x = a + εb and y = c + εd, where both x and y are dual numbers, 
        then x/y = a/c + ε(b/c - ad/c^2).

        Recall multiplication between real and dual numbers:
        Let x = a + εb be the dual number and n the real number.
        n/x = n/a - εbn/a^2
        x/n = a/n + εb/n
        '''
        a,b,c,d=2,6,4,-2

        assert x_div_y.real==a//c
        assert x_div_y.dual==(b*c - a*d)//c**2
        assert y_div_x.real==c//a
        assert y_div_x.dual==(d*a - c*b)//a**2
        assert n_div_x.real==n//a
        assert n_div_x.dual==-b*n//a**2
        assert x_div_n.real==a//n
        assert x_div_n.dual==b//n 

    '''
    In the next eight tests, we are going to use the following f(a + εb) = f(a) + εbf'(a), to test the functions,
    Starting with the trigonometric functions.
    '''

    def test_sin(self):
        '''
        Testing the sine function from the package (f(x)=sin(x) --> f'(x)=cos(x))
        '''
        a,b=-1,1
        x=Dual(a,b)
        sin_x = x.sin()

        assert sin_x.real==np.sin(a)
        assert sin_x.dual==b*np.cos(a)

    def test_cos(self):
        '''
        Testing the cosine function from the package (f(x)=cos(x) --> f'(x)=-sin(x))
        '''

        a,b = 5,-9
        x=Dual(a,b)
        cos_x = x.cos()

        assert cos_x.real==np.cos(a)
        assert cos_x.dual==-b*np.sin(a)

    def test_tan(self):
        '''
        Testing the tangent fucntion from the package (f(x)=tan(x) --> f'(x)=sec(x)^2)
        '''

        a,b = 10, -100
        x=Dual(a,b)
        tan_x=x.tan()

        assert tan_x.real==np.tan(a)
        assert tan_x.dual==b/np.cos(a)**2
        
    '''
    Hyperbolic funtions tests
    '''

    def test_sinh(self):
        '''
        Testing the sine function from the package (f(x)=sinh(x) --> f'(x)=cosh(x))
        '''
        a,b=-1,1
        x=Dual(a,b)
        sinh_x = x.sinh()

        assert sinh_x.real==np.sinh(a)
        assert sinh_x.dual==b*np.cosh(a)

    def test_cosh(self):
        '''
        Testing the cosine function from the package (f(x)=cosh(x) --> f'(x)=sinh(x))
        '''

        a,b = 5,-9
        x=Dual(a,b)
        cosh_x = x.cosh()

        assert cosh_x.real==np.cosh(a)
        assert cosh_x.dual==b*np.sinh(a)

    def test_tanh(self):
        '''
        Testing the tangent fucntion from the package (f(x)=tanh(x) --> f'(x)=sech(x)^2)
        '''

        a,b = 10, -100
        x=Dual(a,b)
        tanh_x=x.tanh()

        assert tanh_x.real==np.tanh(a)
        assert tanh_x.dual==b/np.cosh(a)**2


    '''
    Testing the remaining two functions, namely the logarithmic and the exponential functions.
    '''

    def test_exp(self):
        '''
        Here f(x)=f'(x), thus...
        '''
        a,b = 87,-29 
        x = Dual(a,b)
        exp_x=x.exp()

        assert exp_x.real==np.exp(a)
        assert exp_x.dual==b*np.exp(a)
    
    def test_log(self):
        '''
        For the logarithmic function, f(x)=log(x) --> f'(x)=1/x
        '''
        a,b = 1,3
        x = Dual(a,b)
        log_x=x.log()

        assert log_x.real==np.log(a)
        assert log_x.dual==b/a

    '''
    The next section of tests will verify the automatic differentiation with dual numbers. We will define some
    toy models differentiate them and compare the results obtained with the package to the analytical solution.
    For simplicity we are going to differentiate at a single point. 

    Recall, f(a + εb) = f(a) + εbf'(a), if we set b=1 then the dual part of f(a + ε) will be its derivative 
    evaluated at the point a. 
    '''

    def test_polynomial(self):
        '''
        Starting with the simplest of the examples, i.e. differentiating a polynomial

        Let us consider the following polynomial f(x) = x^2 - 1/x --> f'(x) = 2x + 1/x^2
        '''
        def analytical(x):
            return 2*x + 1/x**2
        
        x=Dual(2,1)
        f_x=x**2 - 1/x

        assert f_x.dual==analytical(2)

    def test_multvariate(self):
        '''
        Lets move to a more complicated scenario involving partial derivatives.

        Consider the multivariate function f(x,y,z) = x/(zy) + cos(x/z) + exp(y**2-xz).
        
        Multivariate functions are difficult to determine, 
        as f(a+εb, c+εd, n+εm) = f(a,c,n) + ε(bδf(a,c,n)/δa + dδf(a,c,n)/δc + mδf(a,c,n)/δn),
        i.e. the dual is the sum of all the partial derivatives at each of the real points.

        Even if the output provided is the sum of the partial derivatives, which is not useful,
        it is still interesting to test it.
        '''
        def analytical_x(x,y,z):
            '''
            Taking the derivative w.r.t x
            '''
            return 1/(z*y) - (1/z)*np.sin(x/z) - z*np.exp(y**2 - x*z)
        
        def analytical_y(x,y,z):
            '''
            Taking the derivative w.r.t y
            '''
            return -x/(z*y**2) + 2*y*np.exp(y**2 - x*z)
        
        def analytical_z(x,y,z):
            '''
            Taking the derivative w.r.t z
            '''
            return -x/((z**2)*y) + (x/z**2)*np.sin(x/z) - x*np.exp(y**2 - x*z)
        
        x=Dual(2,1)
        y=Dual(3,1)
        z=Dual(-2,1)

        f_xyz=x/(z*y) + (x/z).cos() + (y**2 - x*z).exp()

        assert f_xyz.dual==analytical_x(2,3,-2) + analytical_y(2,3,-2) + analytical_z(2,3,-2)
        
    
    def test_funtion_der(self):
        '''
        Here we are combing all the function libraries of the package dual_autodiff.

        Consider the fucntion f(x) = cosh(tanh(x))^2 + tan(exp(sin(sinh(x)))) + cos(log(x))
        '''

        def analytical(x):
            '''
            Analytical derivative
            '''
            part_1 = 2*np.cosh(np.tanh(x))*np.sinh(np.tanh(x))/(np.cosh(x)**2)
            
            sub_part_2_1 = (np.cos(np.exp(np.sin(np.sinh(x)))))**2
            sub_part_2_2 = np.exp(np.sin(np.sinh(x)))*np.cos(np.sinh(x))*np.cosh(x)
            part_2 = sub_part_2_2/sub_part_2_1

            part_3 = -np.sin(np.log(x))/x

            return part_1+part_2+part_3 
        
        x = Dual(3,1)
        f_x = (x.tanh().cosh())**2 + x.sinh().sin().exp().tan() + x.log().cos()

        '''
        Rounding the results, this is due to the complexity of the function,
        and depending on the code there could be some accuracy issues, hence
        consider 5 decimal places.
        '''

        assert round(f_x.dual,5)==round(analytical(3),5)