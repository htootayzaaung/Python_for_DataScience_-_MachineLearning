#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:52:03 2022

@author: htootayzaaung
"""
fibonnacci_sequence = []
i = 0
pointer = 0


while (pointer <= 50):
    if (i == 0):
        fibonnacci_sequence[i] = 0
    elif (i == 1):
        fibonnacci_sequence[i] = 1
    elif (i > 1):
        fibonnacci_sequence[i] = fibonnacci_sequence[i - 1] + fibonnacci_sequence[i - 2]
    pointer = fibonnacci_sequence[i]   
    i += 1


print(fibonnacci_sequence)
