'''
模型-视图-控制器模式 MVC模式 每个部分都有明确的职责 
模型负责访问数据，管理应用的状态 视图是模型的外在表现 控制器是模型与视图之间的连接
高效mvc模式应当遵守 
智能模型
  *包含所有的校验/业务规则/逻辑
  *处理应用的状态
  *访问应用数据（数据库、云或其他）
  *不依赖UI
瘦控制器
  *在用户与视图交互时，更新模型
  *在模型改变时，更新视图
  *如果需要，在数据传递给模型/视图之前进行处理
  *不展示数据
  *不直接访问应用数据
  *不包含校验/业务规则/逻辑
傻瓜视图
  *展示数据
  *允许用户与其交互
  *仅做最小的数据处理，通常由一种模板语言提供处理能力（例如，使用简单的变量和循环控制）
  *不存储任何数据
  *不直接访问应用数据
  *不包含校验/业务规则/逻辑

如果你正在从头实现MVC，并且想弄清自己做的对不对，可以尝试回答以下两个关键的问题：
  *如果你的应用有GUI，那么他可以换肤吗？易于改变他的皮肤/外观以及给人的感受吗？可以为用户提供运行期间改变应用皮肤的能力吗？
  如果这做起来并不简单，那就意味着你的MVC实现在某些地方存在问题。
  *如果你的应用没有GUI（例如，是一个终端应用）,为其添加GUI支持有多难？或者，如果添加GUI没什么用，那么是否易于添加视图从而
  以图表（饼图、柱状图等）或文档（PDF、电子表格等）形式展示结果？如果因此而作出的变更不小（小的变更是，在不变更模型的情况下，
  创建控制器并绑定到视图），那么你的MVC实现就有些不对了。
'''

quotes = ('A man is not complete until he is married.Then he is finished.',
        'As I said before,I never repeat myself.',
        'Behind a successful man is an exhausted woman.',
        'Black holes really suck...',
        'Facts are stubborn things.')

class QuoteModel:
    def get_quote(self,n):
        try:
            value = quotes[n]
        except IndexError as e:
            value = 'Not found!'
        return value

class QuoteTerminalView:
    def show(self,quote):
        print('And the quote is:"{}"'.format(quote))

    def error(self,msg):
        print('Error:{}'.format(msg))

    def select_quote(self):
        return input('Which quote number would u like to see?')


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as e:
                self.view.error('Incorrect index "{}"'.format(n))
        quote = self.model.get_quote(n)
        self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()