"""""
Implementing Second-order Runge-Kutta method to solve differential equation
"""""

def dydt(y,t):
    """
    This function returns the differential equation
    """
    return y*(t**3)-1.5*y

def RK2(y,t,t0,h):
    
    n=(t-t0)/h
    i=1
    while(i<=n):
        k1=dydt(y,t0)
        k2=dydt(y+0.5*k1*h,t0+0.5*h)
        
        t0=t0+h
        y=y+(k2*h)
        i=i+1
    return y

y,t,t0,h=1,1,0,0.5
print("value of y:",RK2(y,t,t0,h))


