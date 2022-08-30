from sympy import *
def lag_weights_roots(n):
    x = Symbol('x')
    roots = Poly(laguerre(n, x)).all_roots()
    x_i = [rt.evalf(20) for rt in roots]
    w_i = [(rt/((n+1)*laguerre(n+1, rt))**2).evalf(20) for rt in roots]
    return x_i, w_i
print(lag_weights_roots(20))
