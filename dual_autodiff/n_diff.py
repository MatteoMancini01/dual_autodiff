# defining a new calss numerative derivative

class num_diff:
    
    def __init__(self, f, x, h): #initialising values
        self.f = f
        self.x = x
        self.h = h

        

    def first_forward(self): # first derivative
        if self.h==0: # this is applied for every numerical differentiation method, we can chose h<<0 but never h=0
            raise ZeroDivisionError('Division by zero is undefined')
        # implementing numerical formula for first derivative
        else: 
            f_dash = (self.f(self.x + self.h) - self.f(self.x)) / self.h
            return f_dash
    
    def first_backwards(self): # first derivative
        if self.h==0:
            raise ZeroDivisionError('Division by zero is undefined')
        # implementing numerical formula for first derivative
        else: 
            f_dash = (self.f(self.x) - self.f(self.x-self.h)) / self.h
            return f_dash
    
    def first_central(self): # first derivative
        if self.h==0:
            raise ZeroDivisionError('Division by zero is undefined')
        # implementing numerical formula for first derivative
        else: 
            f_dash = (self.f(self.x + self.h) - self.f(self.x - self.h)) / (2*self.h)
            return f_dash
    
    def second_der(self): # second derivative
        if self.h==0:
            raise ZeroDivisionError('Division by zero is undefined')
        # implementing numerical formula for second rerivative
        else: 
            f_double_dash = (self.f(self.x + self.h) - 2*self.f(self.x) + self.f(self.x - self.h))/self.h**2 
            return f_double_dash
