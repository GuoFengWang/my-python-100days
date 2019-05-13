# -*- coding: utf-8 -*-
"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

"""
Author: Andy
Version: 1.0
Date: 2019-5-13
"""
for i in range(100,1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    if i = low ** 3 + mid ** 3 + high ** 3:
        print(i)

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
