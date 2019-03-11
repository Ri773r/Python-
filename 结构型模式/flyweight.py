'''
享元模式 旨在于优化性能和内存使用
  *有点像单例模式
若想要享元模式有效
  *应用需要使用大量的对象
  *对象太多，存储/渲染他们的代价太大。一旦移除对象中的可变状态（因为在需要之时，应该由客户端代码显式地传递给享元），多组不同的对象可被相对更少的共享对象所替代。
  *对象ID对应应用不重要。对象共享会造成ID比较失败，所以不能依赖对象ID（那些在客户端代码看起来不同的对象，最终具有相同的ID）。
'''
import random
from enum import Enum

TreeType = Enum('TreeType','apple_tree cherry_tree peach_tree')

class Tree:
    pool = dict()

    def __new__(cls,tree_type):
        obj = cls.pool.get(tree_type,None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self,age,x,y):
        print('render a tree of type {} and age {} at ({},{})'.format(self.tree_type,age,x,y))

def main():
    rnd = random.Random()
    age_min,age_max = 1,30
    min_point,max_point = 0,100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min,age_max),
            rnd.randint(min_point,max_point),
            rnd.randint(min_point,max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min,age_max),
            rnd.randint(min_point,max_point),
            rnd.randint(min_point,max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min,age_max),
            rnd.randint(min_point,max_point),
            rnd.randint(min_point,max_point))
        tree_counter += 1

    print('tree rendered:{}'.format(tree_counter))
    print('tree actually created:{}'.format(len(Tree.pool)))

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{}=={}?{}'.format(id(t4),id(t5),id(t4)==id(t5)))
    print('{}=={}?{}'.format(id(t5),id(t6),id(t5)==id(t6)))

if __name__ == '__main__':
    main()