import numpy as np
import cv2 as cv
import skimage.measure
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
import warnings
import glob


if not sys.warnoptions:
    warnings.simplefilter("ignore")

def gaussian_f(x, a1, b1, c1, a2, b2, c2):
    """Fit function y=f(x,p) . """
    return a1 * np.exp(-((x-b1)/c1)**2) + a2 * np.exp(-((x-b2)/c2)**2)

def first_derivative_f(x, a1, b1, c1, a2, b2, c2):
    """Compute firs derivative of function f. """
    result=(((2*a1*(x-b1))*np.exp(-((x-b1)/c1)**2))/(c1**2)) - (((2*a2*(x-b2))*np.exp(-((x-b2)/c2)**2))/(c2**2))
    return result
    
def second_derivative_f(x, a1, b1, c1, a2, b2, c2):
    """Compute second derivative of function f. """
    result=a1*((((4*(x-b1)**2)*np.exp(-((x-b1)/c1)**2))/(c1**4))-((2*np.exp(-((x-b1)/c1)**2))/(c1**2))) +a2*((((4*(x-b2)**2)*np.exp(-((x-b2)/c2)**2))/(c2**4))-((2*np.exp(-((x-b2)/c2)**2))/(c2**2)))
    return result

def curvature_f(axis_x, entropy):
    curvature=[]
    """Compute curvature of function point by point. """ 
    popt, pcov = curve_fit(gaussian_f, axis_x, entropy,  maxfev=5000000)
    a1, b1, c1, a2, b2, c2 = popt
    
    for x in axis_x:
        y_I = first_derivative_f(np.float64(x), np.float64(a1),  np.float64(b1), np.float64(c1), np.float64(a2), np.float64(b2), np.float64(c2))
        y_II = second_derivative_f(np.float64(x), np.float64(a1),  np.float64(b1), np.float64(c1), np.float64(a2), np.float64(b2), np.float64(c2))
        curvature.append(y_II/[(1 + (y_I**2) )**(3/2)])       
    return curvature        




