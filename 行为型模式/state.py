'''
状态模式 状态模式是一个或多个有限状态机（简称状态机）的实现，用于解决一个特定的软件工程问题
  *状态机是一个抽象机器，具有两个主要部分：状态和转换。
  状态是指一个系统的当前状况。一个状态机在任意时间点只会有一个激活状态。
  转换是指从当前状态到一个新状态的切换。
  在一个转换发生之前或之后通常会执行一个或多个动作。
  状态机可以使用状态图进行视觉上的展现。
'''

# 已创建       ↗→终止
#   |     运行
#   ↓  ↗↙    ↘
#  等待    ←   阻塞
#   ↓↑         ↓↑
# 换出并等待  换出并阻塞
# 

from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition

@acts_as_state_machine
class Process:
    #定义状态机状态
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    #定义状态转换 一个状态转换就是一个Event
    wait = Event(from_states=(created, running, blocked, swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting,to_state=running)
    terminate = Event(from_states=running,to_state=terminated)
    block = Event(from_states=(running,swapped_out_blocked),to_state=blocked)
    swap_wait = Event(from_states=waiting,to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked,to_state=swapped_out_blocked)

    def __init__(self,name):
        self.name = name

    @after('wait')
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate')
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swappped out and blocked'.format(self.name))

def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as e:
        print('Error： transition of {} from {} to {} failed'.format(process.name, process.current_state, event_name))

def state_info(process):
    print('state of {}:{}'.format(process.name, process.current_state))

def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'

    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1,p2)]

    print()
    transition(p1,p1.wait,WAITING)
    transition(p2,p2.terminate,TERMINATED)
    [state_info(p) for p in (p1,p2)]

    print()
    transition(p1,p1.run,RUNNING)
    transition(p2,p2.wait,WAITING)
    [state_info(p) for p in (p1,p2)]

    print()
    transition(p2,p2.run,RUNNING)
    [state_info(p) for p in (p1,p2)]

    print()
    [transition(p,p.block,BLOCKED) for p in (p1,p2)]
    [state_info(p) for p in (p1,p2)]

    print()
    [transition(p,p.terminate,TERMINATED) for p in (p1,p2)]
    [state_info(p) for p in (p1,p2)]



if __name__ == '__main__':
    main()