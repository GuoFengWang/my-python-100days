# -*- coding: utf-8 -*-
"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

# +
"""
Version: 1.0
Author: Andy
Date: 2019-5-10

"""
from random import randint

money=1000
while 1000 > 0:
    print('您的金钱为：%d' %money)
    go_on = False
    debt = int(input('请输入您的赌注：'))
    first_round = randint(1,6) + randint(1,6)
    if first_round == 7 or first_round == 11:
        money += debt
        print('点数为：%d 玩家获胜！您的金钱为：%d' %(first_round,money))
    elif first_round in [2,3,12]:
        money -= debt
        print('点数为: %d 庄家获胜！您的金钱为: %d' %(first_round,money))
    else:
        go_on = True
        print('点数为: %d 再摇一次骰子' %first_round)
    
    
    while go_on == True:
        second_round = randint(1,6) + randint(1,6)
        if second_round == first_round:
            money += debt
            print('点数为 %d 与第一次点数一样，玩家获胜！您的金钱为: %d' %(second_round,money))
            go_on = False
        elif second_round == 7:
                money -= debt
                print('点数为 %d 庄家获胜,您的金钱为: %d' %(second_round,money))
                go_on = False
        

print('您已输光金钱，穷逼再见')

# -

from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')

while True:
    debt=int(input('请输入金额：'))
    if debt < 0:
        break


