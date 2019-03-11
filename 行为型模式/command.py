'''
命令模式 使用这种设计模式，可以将一个操作（比如，复制/粘贴）封装为一个对象 这样能提供很多好处
  *我们可以在任何时候执行一个命令，而并不一定是在命令创建时
  *执行一个命令的客户端代码并不需要知道命令的任何实现细节
  *可以对命令进行分组，并按一定的顺序执行
'''

import os

verbose = True

class RenameFile:
    def __init__(self,path_src,path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print('[renaming "{}" to "{}"]'.format(self.src,self.dest))
        os.rename(self.src,self.dest)

    def undo(self):
        if verbose:
            print('[renaing "{}" back to "{}"]'.format(self.dest,self.src))
            os.rename(self.dest,self.src)

def delete_file(path):
    if verbose:
        print('deleting file "{}"'.format(path))

    os.remove(path)

class CreateFile:
    def __init__(self,path,txt='hello world\n'):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print('[creating file "{}"]'.format(self.path))
        with open(self.path,'w',encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)

class ReadFile:
    def __init__(self,path):
        self.path = path

    def execute(self):
        if verbose:
            print('[reading file "{}"]'.format(self.path))
        with open(self.path,'r',encoding='utf-8') as in_file:
            print(in_file.read(),end='')

def main():
    orig_name, new_name = 'file1', 'file2'

    commands = []
    for cmd in CreateFile(orig_name),ReadFile(orig_name),RenameFile(orig_name,new_name):
        commands.append(cmd)

    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')

    if answer not in 'yY':
        print('the result is {}'.format(new_name))
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass

if __name__ == '__main__':
    main()