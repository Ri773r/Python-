'''
策略模式 通常用在我们希望对同一个问题透明地使用多种方案时
如果并不存在针对所有情况的完美算法，那么我们可以使用策略模式，动态地决定在每种情况下应使用哪种算法
'''

import time

SLOW = 3 # 单位妙 减缓算法速度
LIMIT = 5 #字符数
WARING = 'too bad, you picked the slow algorithm :('

def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield (seq[i], seq[(i+1)%n]) if i != n-1 else (seq[i], None)

def allUniqueSort(s):
    if len(s) > LIMIT:
        print(WARING)
        time.sleep(SLOW)
    strStr = sorted(s)
    for (c1, c2) in pairs(strStr):
        if c1 == c2:
            return False
    return True

def allUniqueSet(s):
    if len(s) <= LIMIT:
        print(WARING)
        time.sleep(SLOW)

    return True if len(set(s)) == len(s) else False

def allUnique(s,strategy):
    return strategy(s)

def main():
    while True:
        word = None
        while not word:
            word = input('Insert word(type quit to exit)> ')
            if word == 'quit':
                print('bye')
                return 

            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')
                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}):{}'.format(word,allUnique(word,strategy)))
                except KeyError as e:
                    print('Incorrect option: {}'.format(strategy_picked))
            print()

if __name__ == '__main__':
    main()