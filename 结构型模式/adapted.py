'''
适配器模式 让两个（或多个）不兼容接口兼容 
  不要求访问他方接口源代码
  不违反开放/封闭原则（*声明一个软件的实体应该对扩展是开放的，对修改则是封闭的）
'''
class Synthesizer:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


class Computer:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'execute a program'

class Adapter:
    def __init__(self,obj,adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)

def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth,{'execute':synth.play}))
    human = Human('Bob')
    objects.append(Adapter(human,{'execute':human.speak}))

    for i in objects:
        print('{} {}'.format(str(i),i.execute()))

if __name__ == '__main__':
    main()