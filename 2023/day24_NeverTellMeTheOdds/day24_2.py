#!/opt/anaconda3/bin/python
#Jake Feiler

import numpy as np
import sys
from scipy.optimize import fsolve

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    lines = []
    for line in input_file:
        next_line = line.strip().replace('@', '').replace(',', '').split(' ')
        lines.append(list(filter(None, next_line)))
    return lines

def equations(variables,  X1, Y1, Z1, VX1, VY1, VZ1, X2, Y2, Z2, VX2, VY2, VZ2, X3, Y3, Z3, VX3, VY3, VZ3):
    t1, t2, t3 = variables
    eq1 = X1 + VX1 * t1 + (X2 + VX2 * t2 - X1 - VX1 * t1)/(t2 - t1) * (t3 - t1) - X3 - VX3 * t3
    eq2 = Y1 + VY1 * t1 + (Y2 + VY2 * t2 - Y1 - VY1 * t1)/(t2 - t1) * (t3 - t1) - Y3 - VY3 * t3
    eq3 = Z1 + VZ1 * t1 + (Z2 + VZ2 * t2 - Z1 - VZ1 * t1)/(t2 - t1) * (t3 - t1) - Z3 - VZ3 * t3

    return [eq1, eq2, eq3]

def main():
    s = get_input('input.txt')
    x1, y1, z1, vx1, vy1, vz1 = int(s[0][0]), int(s[0][1]), int(s[0][2]), int(s[0][3]), int(s[0][4]), int(s[0][5])
    x2, y2, z2, vx2, vy2, vz2 = int(s[1][0]), int(s[1][1]), int(s[1][2]), int(s[1][3]), int(s[1][4]), int(s[1][5])
    x3, y3, z3, vx3, vy3, vz3 = int(s[2][0]), int(s[2][1]), int(s[2][2]), int(s[2][3]), int(s[2][4]), int(s[2][5])


    #Trial and error to find the right starting estimate for fsolve
    #See work.txt for math derivation of 3 equations to use in fsolve
    
    t1, t2, t3 = fsolve(equations, args=(x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2, x3, y3, z3, vx3, vy3, vz3),x0=[5_000_000_000, 60_5000_000, 176_500_000], maxfev = 50000, factor = 0.000001)
    #t1, t2, t3 = fsolve(equations, args=(x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2, x3, y3, z3, vx3, vy3, vz3),x0=[500_000_000_000, 300_000_000_000, 100_000_000_000])    

    VX0 = (x2 + vx2 * t2 - x1 - vx1 * t1)/(t2 - t1)
    VY0 = (y2 + vy2 * t2 - y1 - vy1 * t1)/(t2 - t1)
    VZ0 = (z2 + vz2 * t2 - z1 - vz1 * t1)/(t2 - t1)

    X0 = round(x1 + vx1 * t1 - VX0 * t1)
    Y0 = round(y1 + vy1 * t1 - VY0 * t1)
    Z0 = round(z1 + vz1 * t1 - VZ0 * t1)

    print(X0 + Y0 + Z0)
    
main()


"""
1008195171795.9987 177443247580.00003 403663893514.99945
-77.99999999999997 269.00000000000045 71.00000000000013
318090941338468.0 124187623124112.9 231363386790707.97
673641951253288.9
"""
