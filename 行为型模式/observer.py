'''
观察者模式 描述单个对象（发布者，又称主持者或可观察者）与一个或多个对象（订阅者，又称为观察者）之间的发布-订阅关系
  *若希望在一个对象的状态变化时能够通知/提醒所有相关者（一个对象或者一组对象），则可以使用观察者模式
  *观察者模式的一个重要特性是，在运行时，订阅者/观察者的数量以及观察者是谁都可能会变化，也可以改变
'''

class Publisher:
    def __init__(self):
        self.observers = []

    def add(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add:{}'.format(observer))

    def remove(self,observer):
        try:
            self.observers.remove(observer)
        except ValueError as e:
            print('Failed to remove:{}'.format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers]

class DefaultFormatter(Publisher):
    def __init__(self,name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}:'{}' has data = {}".format(type(self).__name__,self.name,self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,new_value):
        try:
                self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()

class HexFomatter:
    def notify(self,publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,publisher.name,hex(publisher.data)))

class BinaryFomatter:
    def notify(self,publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__,publisher.name,bin(publisher.data)))

def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFomatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFomatter()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print()
    df.remove(hf)
    df.add(bf)

    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)

if __name__ == '__main__':
    main()

