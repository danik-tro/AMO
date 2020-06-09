import numpy as np




def hord_nuton():

    a,b = 0.1, 3.
    e = 0.0001

    f = lambda x: 2*x*np.log(x) - 1
    f1 = lambda x: 2*np.log(x) + 2
    f2 = lambda x: 2/x

    res = 0
    while  (np.abs(a-b)>2*e):
        if (f(a) * f2(a)<0):
            a += (b-a) / (f(a) - f(b)) * f(a)
        else:
            a -= f(a)/f1(a)

        if (f(b) * f2(b) < 0):
            b += (a-b) / (f(b) - f(a)) * f(b)
        else:
            b -= f(b) / f1(b)

    return (a+b)/2.0








