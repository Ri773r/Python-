'''
模板模式 消除代码冗余
'''
################################################################ eg. 1
def bfs(graph, start, end):
    '''
    Breadth-First Search BFS 广度优先搜索
    '''
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        print('current', current)
        print('path', path)
        print('visited', visited)
        if current not in path:
            path.append(current)
            if current == end:
                print(path)
                return (True, path)
            #如果两个顶点直接没有连接，则跳过
            if current not in graph:
                continue
        #加粗
        visited = visited + graph[current]
        #加粗
    return (False,path)

def dfs(graph, start, end):
    '''
    Depth-First Search DFS 深度优先搜索
    '''
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        print('current', current)
        print('path', path)
        print('visited', visited)
        if current not in path:
            path.append(current)
            if current == end:
                print(path)
                return (True, path)
            #如果两个顶点直接没有连接，则跳过
            if current not in graph:
                continue
        #加粗     
        visited = graph[current] + visited
        #加粗
    return (False,path)

def main():
    graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Stuttgart','Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': [],
        'Munchen': []
    }
    bfs_path = bfs(graph, 'Wurzburg', 'Kassel')
    dfs_path = dfs(graph, 'Wurzburg', 'Kassel')
    print(bfs_path,dfs_path)

def traverse(graph, start, end, action):
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        print('current', current)
        print('path', path)
        print('visited', visited)
        if current not in path:
            path.append(current)
            if current == end:
                print(path)
                return (True, path)
            #如果两个顶点直接没有连接，则跳过
            if current not in graph:
                continue
        #加粗     
        visited = action(visited, graph[current])
        #加粗
    return (False,path)

def extend_bfs_path(visited, current):
    return visited + current

def extend_dfs_path(visited, current):
    return current + visited

################################################################

################################################################ eg.2
from cowpy import cow

def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg

def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)

def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg

def generate_banner(msg,style=dots_style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')

def main2():
    msg = 'happy coding'
    [generate_banner(msg,style) for style in (dots_style, admire_style, cow_style)]

################################################################


if __name__ == '__main__':
    main2()