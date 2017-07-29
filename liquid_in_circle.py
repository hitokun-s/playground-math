# -*- coding: utf-8 -*-

# 緩やかにしたsin関数と円で囲まれる領域の、円に対する割合を、sin関数の高さを変えながら、計算する。

import matplotlib.pyplot as plt
from scipy import optimize, exp, sqrt, integrate, sin, pi
import numpy as np

diff = 0 # 0.01刻みで[-1,1]を動かす

def f(x):
    # return (x**3 - x)/2 - 0.1
    return  sin(pi * x) / 8 + diff
def g(x):
    return - sqrt(1 - x**2)
def h(x):
    return f(x) - g(x)

def BinarySearch(upper,lower,err):
    up=upper
    low=lower
    count=0
    while True:
        count=count+1
        mid=(up+low)/2
        y=h(mid)
        if abs(y)<err: #解が発見された
            break
        elif h(low)*y<0: #解は下限と中間点の間にある
            up=mid
        else:                     #解は上限と中間点の間にある
            low=mid
    # print "x: %s" % mid
    # print "y: %s" % y
    # print "calc count: %d" % count
    return mid

def calc():
    b = BinarySearch(1.0,0.0, 0.001)
    a = BinarySearch(0.0,-1.0, 0.001)
    area = integrate.quad(h, a, b)[0]
    ratio = area / pi
    return ratio

def test():
    ratio = calc()
    print "h: %s, ratio: %s" % (diff, ratio)
    x = np.arange(-1.0, 1.0, 0.001)
    y = f(x)
    plt.plot(x, y)

    y = g(x)
    plt.plot(x, y)
    
    plt.title("wave in circle")
    plt.ylim(-1.0, 1.0)  # yの範囲を指定
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':    
    res = []
    diffs = np.arange(-0.99,0,0.01)
    for d in diffs:
        diff = round(d, 2)
        ratio = calc()
        print "h: %s, ratio: %s" % (diff, ratio)
        res.append([diff, ratio])
        res.append([-diff, 1 - ratio])
    res.append([1, 1])
    res.append([-1, 0])
    res.append([0, 0.5])
    res = sorted(res, key=lambda x: x[0])
    print res