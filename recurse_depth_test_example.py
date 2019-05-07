import functools
import sys
import inspect

accm = 0
stack_depth = 0

class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)
        
def tail_recursive(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated

def sum_num(n):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if n == 1:
        return 1
    return n + sum_num(n - 1)

@tail_recursive
def tail_sum(n, k = 1):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if n == 1:
        return k
    return recurse(n - 1, k + n)

def fac(n):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if n == 1:
        return 1
    return n * fac(n - 1)

@tail_recursive
def tail_fac(n, k = 1):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if n == 1:
        return k
    return recurse(n - 1, k * n)

def fib(n):
    memory = {}
    return fib_(n)

memory = {}
def fib_(n):
    global accm, memory, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if n in memory:
        return memory[n]
    elif n <= 2:
        return 1
    else:
        a = fib_(n - 1) + fib_(n - 2)
        memory[n] = a
        return a

@tail_recursive
def tail_fib(n, curr = 1, back = 0, dbback = 0):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if n <= 1:
        return curr
    return recurse(n - 1, curr + back, curr, back)

def hanoi(n, start = 1, temp = 2, finish = 3):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if n == 1:
        return [[start, finish]]
    to_return = []
    to_return += hanoi(n - 1, start, finish, temp)
    to_return += hanoi(1, start, temp, finish)
    to_return += hanoi(n - 1, temp, start, finish)
    return to_return

class Hanoi_args:
    def __init__(self, n, start = 1, temp = 2, finish = 3):
        self.n = n
        self.start = start
        self.temp = temp
        self.finish = finish
        
def tail_hanoi(a):
    return tail_hanoi_process(Hanoi_args(a))

@tail_recursive
def tail_hanoi_process(args : Hanoi_args, to_return = None, stack = None):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if to_return is None:
        to_return = []
    if stack is None:
        stack = []
    if args.n == 1:
        to_return.append([args.start, args.finish])
    else:
        to_merge = []
        to_merge.append(Hanoi_args(args.n - 1, args.start, args.finish, args.temp))
        to_merge.append(Hanoi_args(1, args.start, args.temp, args.finish))
        to_merge.append(Hanoi_args(args.n - 1, args.temp, args.start, args.finish))
        stack = to_merge + stack
    if stack == [] and to_return != []:
        return to_return
    return recurse(stack[0], to_return, stack[1:])

def part(n, k):
    return pprime(n, n, k)

def pprime(m, n, k, to_append = None, to_return = None):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if to_return is None:
        to_return = []
    if to_append is None:
        to_append = []
    if k < 1:
        to_return.append(to_append)
    else:
        for i in range(n - k + 1, 0, -1):
            if i * k >= n and m >= i:
                a = to_append[:]
                a.append(i)
                pprime(i, n - i, k - 1, a, to_return)
        return to_return[:]

class Part_args:
    def __init__(self, m, n, k, to_append = None):
        self.m = m
        self.n = n
        self.k = k
        if to_append is not None:
            self.to_append = to_append
        else:
            self.to_append = []

def tail_part(n, k):
    return tail_pprime(Part_args(n, n, k))

@tail_recursive
def tail_pprime(args : Part_args, to_return = None, queue = None):
    global accm, stack_depth
    if stack_depth < len(inspect.stack()):
        stack_depth = len(inspect.stack())
    accm += 1
    if to_return is None:
        to_return = []
    if queue is None:
        queue = []
    if args.k >= 1:
        for i in range(args.n - args.k + 1, 0, -1):
            if i * args.k >= args.n and args.m >= i:
                new_to_append = args.to_append[:]
                new_to_append.append(i)
                new_args = Part_args(i, args.n - i, args.k - 1, new_to_append)
                queue.append(new_args)
    else:
        to_return.append(args.to_append)
    if queue == []:
        return to_return
    return recurse(queue[0], to_return, queue[1:])

sys.setrecursionlimit(10000)    

one_num_funcs = [sum_num, tail_sum, fac, tail_fac, fib, tail_fib]
hanois = [hanoi, tail_hanoi]
parts = [part, tail_part]

for next_func in one_num_funcs:
    accm = 0
    stack_depth = 0
    print(next_func.__name__)
    print("length :", len(str(next_func(60))))
    print("called :", accm)
    print("depth :", stack_depth - len(inspect.stack()))
    print("----------")
for next_func in hanois:
    accm = 0
    stack_depth = 0
    print(next_func.__name__)
    print("length :", len(next_func(10)))
    print("called :", accm)
    print("depth :", stack_depth - len(inspect.stack()))
    print("----------")
for next_func in parts:
    accm = 0
    stack_depth = 0
    print(next_func.__name__)
    print("length :", len(next_func(20, 8)))
    print("called :", accm)
    print("depth :", stack_depth - len(inspect.stack()))
    print("----------")

