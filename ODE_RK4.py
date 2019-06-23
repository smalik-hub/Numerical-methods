"""""
Implementing fourth-order Runge-Kutta method to solve differential equation
"""""
import math

def dydx(y,x):
    """
    This function returns the differential equation
    """
    return (3*(math.e**(-x))-0.4*y)     # ODE to solve

def RK4(y,x,x0,h):
    
    n=(x-x0)/h
    i=1
    while(i<=n):
        k1 = dydx(y,x0)
        k2 = dydx(y+0.5*k1*h,x0+0.5*h)
        k3 = dydx(y+0.5*k2*h,x0+0.5*h)
        k4 = dydx(y+k3*h,x0+h)
        
        x0=x0+h
        y=y+(h/6)*(k1+(2*k2)+(2*k3)+k4)
        
        i=i+1
    return y

y,x,x0,h = 5,3.0,0,1.5
print("value of y:",RK4(y,x,x0,h))


