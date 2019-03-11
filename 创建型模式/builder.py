'''
建造者模式 
  想要创建一个复杂的对象（对象由多个部分构成，且对象的创建要经过多个不同的步骤，这些步骤也许还遵从特定的顺序）
  要求一个对象能有不同的表现，并希望将对象的构造与表现解耦
  想要在某个时间点创建对象，但在稍后的时间点再访问
'''
from enum import Enum 
import time 

#🍕进度
PizzaProgress = Enum('PizzaProgress','queued preparation baking ready')
#生面团类型
PizzaDough = Enum('PizzaDough','thin thick')
#调味料类型
PizzaSauce = Enum('PizzaSauce','tomato creme_fraiche')
#装饰类型
PizzaTopping = Enum('PizzaTopping','mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3

class Pizza:
    def __init__(self,name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self,dough):
        self.dough = dough
        print('preparing the {} dough of your {} ...'.format(self.dough.name,self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))

class MargaritaBuidler:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella,oregano) to your margarita...')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella,PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarella,oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')

class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the creme fraiche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the crene fraiche sauce')

    def add_topping(self):
        print('adding the topping (mozzarella,bacon,ham,musgrooms,red onion,oregano) to your creamy bacon')
        self.pizza.topping.append([i for i in (PizzaTopping.mozzarella,PizzaTopping.bacon,PizzaTopping.ham,PizzaTopping.mushrooms,PizzaTopping.red_onion,PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella,bacon,ham,musgrooms,red onion,oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creany bacon is ready')

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self,builder):
        self.builder = builder
        for step in (builder.prepare_dough,builder.add_sauce,builder.add_topping,builder.bake):
            step()

    @property
    def pizza(self):
        return self.builder.pizza
    
def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like,[m]argarita or [c]reamy bacon?')
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry,only margarita (key m) and creamy bacon (key c) are available')
        return (False,None)
    return (True,builder)

def main():
    builders = dict(m=MargaritaBuidler,c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input,builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy your {}'.format(pizza))

if __name__ == '__main__':
    main()