#Author: Ezra Hsieh
#Derivative Calculator

from sympy import *

def derivCalc(f, x):
    x = Symbol('x')
    d = Derivative(f, x).doit()
    print(d)
    return d

if __name__ == "__main__":
    while True:
        f = input("Enter you function: ")
        x = input("Enter the variable to differentiate with respect to: ")
        f_1 = derivCalc(f, x)
        plot(f_1)

        t = input("Do another function? (y/n) ")
        if t == 'n':
            break 
