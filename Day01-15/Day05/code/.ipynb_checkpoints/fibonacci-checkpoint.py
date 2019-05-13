# -*- coding: utf-8 -*-
"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

# +
"""
output of fibonacci

Version 1.0
Author: Andy
Date: 2019-5-13
"""

a = 0
b = 1
for i in range(20):
    a , b = b , a + b
    print(a , end = ' ')
# -

a = 0
b = 1
for _ in range(20):
    (a, b) = (b, a + b)
    print(a, end=' ')
