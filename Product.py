#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 17:01:20 2021

@author: juicy
"""
products = []
while True:
    name = input('請輸入商品名稱')
    if name == 'q':
        break
    price = input('請輸入價格')
    # p = []
    # p.append(name)
    # p.append(price)
    p = [name, price]
    products.append(p)
print(products)

print(products[0][0])
