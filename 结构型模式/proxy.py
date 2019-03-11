'''
代理模式 
  *远程代理，代表一个活跃于远程位置（例如，我们自己的远程服务器或云服务）的对象
  *虚拟代理，将一个对象的初始化延迟到真正需要使用时进行
  *保护/防护代理，用于对处理敏感信息的对象进行访问控制
  *当我们希望通过添加帮助信息（比如，引用计数）来扩展一个对象的行为时，可以使用智能（引用）代理
'''

##################虚拟代理 用于懒初始化 用到的时候才初始化##################
class LazyPropetry:
    '''
    懒加载描述符类
    '''
    def __init__(self,method):
        #记录方法引用（指针）
        self.method = method
        #记录方法名字
        self.method_name = method.__name__

    def __get__(self,obj,cls):
        '''
        obj 调用方对象
        cls 调用方对象类 type(obj)
        '''
        print(obj)
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj,self.method_name,value)
        return value

class Test:
    '''
    测试类
    '''
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        #假设_resource变量为一个初始化缓慢/代价大的变量
        #不在创建的时候初始化 等到真正用到的时候初始化
        self._resource = None

    #相当于创建了一个类的描述符对象 Test.resoure
    #resource = LazyPropetry(resource)
    @LazyPropetry
    def resource(self):
        '''
        初始化过程
        '''
        print('initializing self._resource which is:{}'.format(self._resource))
        self._resource = tuple(range(5))
        return self._resource

def main():
    print(Test.__dict__)
    t = Test()
    print(t.x)
    print(t.y)
    print(t._resource)
    print(t.__dict__)
    print(t.resource)
    print(t.__dict__)
    print(Test.__dict__)

########################################################################

##################保护/防护代理 控制对敏感对象的访问#######################
class SensitiveInfo:
    def __init__(self):
        self.users = ['nick','tom','ben','mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users),' '.join(self.users)))

    def add(self,user):
        self.users.append(user)
        print('Add user {}'.format(user))

class Info:
    '''SensitiveInfo的保护代理'''
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self,user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")

def main2():
    info = Info()

    while True:
        print('1.read list 2.add user 3.quit')
        key = input('choose option ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknow option:{}'.format(key))

########################################################################


if __name__ == '__main__':
    main2()