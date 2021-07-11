#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:01:20 2021

@author: juicy
"""

import os

products = []
if os.path.isfile('products.csv'):
    print('Check file OK!')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])

    for p in products:
        print(p)
else:
    print('File not found!')

while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入價格')
    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]
    products.append([name, price])
    
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
        
for p in products:
    print(p)