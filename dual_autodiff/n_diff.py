# defining a new calss numerical derivative

class num_diff:
    
    def __init__(self, f, x, h): #initialising values
        self.f = f
        self.x = x
        self.h = h

    def first_der(self): # first derivative
        # implementing numerical formula for first derivative
        return (self.f(self.x + self.h) - self.f(self.x)) / self.h
       
    
    def second_der(self): # second derivative
        # implementing numerical formula for second rerivative
        return (self.f(self.x + self.h) - 2*self.f(self.x) + self.f(self.x - self.h))/self.h**2 
       
