#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Pool

def f(x):
    return x*x

p = Pool(1)
p.map(f, [1, 2, 3])