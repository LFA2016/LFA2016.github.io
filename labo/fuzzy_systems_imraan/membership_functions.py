import numpy as np
import matplotlib.pyplot as pl

class MembershipFunction:
    """
    This is a base class providing functionnalities which are common to all membership functions.
    """
    def plot(self, v_min, v_max, res=0.1):
        input_values = np.arange(v_min, v_max, res)
        output_values = map(self, input_values)
        pl.plot(input_values, output_values)
        pl.ylim((0, 1.1 * max(output_values)))

class TrapezoidalMF(MembershipFunction):
    """
    Trapezoidal membership function. This function implements an isosceles trapezoid.
    first_max: position of the first point where the membership function reach one (1)
    width_base: width of the base of the trapezoid
    width_top: widht of the top of the trapezoid
    """
    def __init__(self, first_max, width_base, width_top):
        self.first_max = first_max
        self.width_base = width_base
        self.width_top = width_top
        self.base_triangle = (width_base - width_top) / 2.0
        self.slope = 1.0 / self.base_triangle
    
    def __call__(self, value):
        if value < (self.first_max - self.base_triangle):
            return 0.0
        elif value < self.first_max:
            return 1.0 - ((self.first_max - value) * self.slope)
        elif value < (self.first_max + self.width_top):
            return 1.0
        elif value < (self.first_max + self.width_top + self.base_triangle):
            return 1.0 - ((value - (self.first_max + self.width_top)) * self.slope)
        else:
            return 0.0