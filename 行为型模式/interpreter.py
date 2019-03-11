'''
解释器模式 为高级用户和领域专家提供一个类变成的框架，但没有暴露出编程语言那样的复杂性，这是通过实现一个DSL来达到目的的
  *DSL是一种针对特定领域、表达能力有限的计算机语言
  DSL有两类，分别是内部DSL和外部DSL
  内部DSL构建在一种宿主编程语言之上，依赖宿主编程语言
  外部DSL则是从头实现，不依赖某种已有的变成语言
  解释器模式仅与内部DSL相关
'''

from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False

class Garage:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False

class Aircondition:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_open else 'off'

    def turn_on(self):
        print('turning on the aircondition')
        self.is_on = True

    def turn_off(self):
        print('turning off the aircondition')
        self.is_on = False

class Heating:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_open else 'off'

    def turn_on(self):
        print('turning on the heating')
        self.is_on = True

    def turn_off(self):
        print('turning off the heating')
        self.is_on = False

class Boiler:
    def __init__(self):
        self.temperature = 83

    def __str__(self):
        return 'boiler temperature:{}'.format(self,temperature)

    def increase_temperature(self,amount):
        print('increase the boiler\'s temperature by {} degrees'.format(amount))
        self.temperature += amount

    def decrease_temperature(self,amount):
        print('decrease the boiler\'s temperature by {} degrees'.format(amount))
        self.temperature -= amount

class Fridge:
    def __init__(self):
        self.temperature = 2

    def __str__(self):
        return 'fridge temperature:{}'.format(self,temperature)

    def increase_temperature(self,amount):
        print('increase the fridge\'s temperature by {} degrees'.format(amount))
        self.temperature += amount

    def decrease_temperature(self,amount):
        print('decrease the fridge\'s temperature by {} degrees'.format(amount))
        self.temperature -= amount

def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress('->')
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token+argument)

    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()

    tests = ('open -> gate',
            'close -> garage',
            'turn on -> aircondition',
            'turn off -> heating',
            'increase -> boiler temperature -> 5 degrees',
            'decrease -> fridge temperature -> 2 degrees')

    open_actions = {
        'gate': gate.open,
        'garage': garage.open,
        'aircondition': airco.turn_on,
        'heating': heating.turn_on,
        'boiler temperature': boiler.increase_temperature,
        'fridge temperature': fridge.increase_temperature
    }

    close_actions = {
        'gate': gate.close,
        'garage': garage.close,
        'aircondition': airco.turn_off,
        'heating': heating.turn_off,
        'boiler temperature': boiler.decrease_temperature,
        'fridge temperature': fridge.decrease_temperature
    }

    for t in tests:
        if len(event.parseString(t)) == 2:#没有参数
            cmd, dev =  event.parseString(t)
            cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
            if 'open' in cmd_str or 'turn on' in cmd_str:
                open_actions[dev_str]()
            elif 'close' in cmd_str or 'turn off' in cmd_str:
                close_actions[dev_str]()
        elif len(event.parseString(t)) == 3:#有参数
            cmd, dev, arg = event.parseString(t)
            cmd_str, dev_str, arg_str = ' '.join(cmd), ' '.join(dev), ' '.join(arg)
            num_arg = 0
            try:
                num_arg = int(arg_str.split()[0])
            except ValueError as e:
                print('excepted number but got: "{}"'.format(arg_str[0]))

            if 'increase' in cmd_str and num_arg>0:
                open_actions[dev_str](num_arg)
            elif 'decrease' in cmd_str and num_arg>0:
                close_actions[dev_str](num_arg)

if __name__ == '__main__':
    main()