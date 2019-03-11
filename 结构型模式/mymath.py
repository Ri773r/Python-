'''
修饰器模式 允许我们无需使用继承或组合就能扩展任意可调用对象（函数、方法之类）的行为
  *Python装饰器实现
'''

import functools

def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer

@memoize
def nsum(n):
    '''返回前N个数的和'''
    assert (n>=0),'n must be >= 0'
    return 0 if n==0 else n + nsum(n-1)

@memoize
def fibonacci(n):
    '''返回斐波那契数列的第N个数'''
    assert (n>=0),'n must be >= 0'
    return n if n in (0,1) else fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec':'fibonacci(100)','import':'fibonacci','func':fibonacci},{'exec':'nsum(200)','import':'nsum','func':nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']),'from __main__ import {}'.format(m['import']))
        print('name:{},doc:{},executing:{},time:{}'.format(m['func'].__name__,m['func'].__doc__,m['exec'],t.timeit()))