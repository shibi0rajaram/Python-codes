# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:01:45 2019

@author: lenovo
"""

#OPTIMIZATION USING A STANDARD FUNCTION:
from scipy.optimize import minimize
#OBJECTIVE FUNCTION:
def obj(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]
#INEQUALITY CONSTRAINT:
def ineq_const(x):
    return x[0]*x[1]*x[2]*x[3]-25
#EQUALITY CONSTRAINT:
def eq_const(x):
    return (x[0]**2+x[1]**2+x[2]**2+x[3]**2)-40
#INITIAL VALUE:
x0=[1,5,5,1]
#BOUNDS:
b=(1.0,5.0)
bound=(b,b,b,b)
#DEFINING CONSTRAINTS:
con1={'type':'ineq','fun':ineq_const}
con2={'type':'eq','fun':eq_const}
constraints=[con1,con2]

#MINIMIZING THE PROBLEM:
solution=minimize(obj,x0,method='SLSQP',bounds=bound,constraints=constraints)