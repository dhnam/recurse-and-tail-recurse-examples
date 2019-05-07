$accm = 0

def sum_num(n)
    $accm += 1
    if n == 1
        return 1
    end
    return n + sum_num(n - 1)
end


def tail_sum(n, k = 1)
    $accm += 1
    if n == 1
        return k
    end
    return tail_sum(n - 1, k + n)
end

def fac(n)
    $accm += 1
    if n == 1
        return 1
    end
    return n * fac(n - 1)
end


def tail_fac(n, k = 1)
    $accm += 1
    if n == 1
        return k
    end
    return tail_fac(n - 1, k * n)
end

def fib(n)
    $memory = {}
    fib_(n)
end

$memory = {}
def fib_(n)
    $accm += 1
    if $memory.key?(n)
        return $memory[n]
    elsif n <= 2
        return 1
    else
        a = fib_(n - 1) + fib_(n - 2)
        $memory[n] = a
        return a
    end
end

def tail_fib(n, curr = 1, back = 0, dbback = 0)
    $accm += 1
    if n <= 1
        return curr
    end
    return tail_fib(n - 1, curr + back, curr, back)
end

def hanoi(n, start = 1, temp = 2, finish = 3)
    $accm += 1
    if n == 1
        return [[start, finish]]
    end
    to_return = []
    to_return += hanoi(n - 1, start, finish, temp)
    to_return += hanoi(1, start, temp, finish)
    to_return += hanoi(n - 1, temp, start, finish)
    return to_return
end

class Hanoi_args
    def initialize(n, start = 1, temp = 2, finish = 3)
        @n = n
        @start = start
        @temp = temp
        @finish = finish
    end
    attr_accessor :n
    attr_accessor :start
    attr_accessor :temp
    attr_accessor :finish
end
        
def tail_hanoi(a)
    return tail_hanoi_process(Hanoi_args.new(a))
end


def tail_hanoi_process(args, to_return = [], stack = [])
    $accm += 1
    if args.n == 1
        to_return.push([args.start, args.finish])
    else
        to_merge = []
        to_merge.push(Hanoi_args.new(args.n - 1, args.start, args.finish, args.temp))
        to_merge.push(Hanoi_args.new(1, args.start, args.temp, args.finish))
        to_merge.push(Hanoi_args.new(args.n - 1, args.temp, args.start, args.finish))
        stack = to_merge + stack
    end
    if stack == [] and to_return != []
        return to_return
    end
    return tail_hanoi_process(stack[0], to_return, stack[1..-1])
end

def part(n, k)
    return pprime(n, n, k)
end

def pprime(m, n, k, to_push = [], to_return = [])
    $accm += 1
    if k < 1
        to_return.push(to_push)
    else
        for i in (n - k + 1).downto(1)
            if i * k >= n and m >= i
                a = to_return[0..-1]
                a.push(i)
                pprime(i, n - i, k - 1, a, to_return)
            end
        end
        return to_return[0..-1]
    end
end

class Part_args
    def initialize(m, n, k, to_push = [])
        @m = m
        @n = n
        @k = k
        @to_push = to_push
    end
    attr_accessor :m
    attr_accessor :n
    attr_accessor :k
    attr_accessor :to_push
end

def tail_part(n, k)
    return tail_pprime(Part_args.new(n, n, k))
end

def tail_pprime(args, to_return = [], queue = [])
    $accm += 1
    if args.k >= 1
        for i in (args.n - args.k + 1).downto(1)
            if i * args.k >= args.n and args.m >= i
                new_to_push = args.to_push[0..-1]
                new_to_push.push(i)
                new_args = Part_args.new(i, args.n - i, args.k - 1, new_to_push)
                queue.push(new_args)
            end
        end
    else
        to_return.push(args.to_push)
    end
    if queue == []
        return to_return
    end
    return tail_pprime(queue[0], to_return, queue[1..-1])
end

one_num_funcs = [method(:sum_num), method(:tail_sum), method(:fac), method(:tail_fac),  method(:fib), method(:tail_fib)]
hanois = [method(:hanoi), method(:tail_hanoi)]
parts = [method(:part), method(:tail_part)]

for next_func in one_num_funcs
    $accm = 0
    puts next_func.name
    start = Time.now
    puts "length : " + next_func.call(6000).to_s.length.to_s
    puts "time : " + (Time.now - start).to_s
    puts "called : " + $accm.to_s
    puts "----------"
end
for next_func in hanois
    $accm = 0
    puts next_func.name
    start = Time.now
    puts "length :" + next_func.call(20).length.to_s
    puts "time :" + (Time.now - start).to_s
    puts "called :" + $accm.to_s
    puts "----------"
end
for next_func in parts
    $accm = 0
    puts next_func.name
    start = Time.now
    puts "length :" + next_func.call(50, 10).length.to_s
    puts "time :" + (Time.now - start).to_s
    puts "called :" + $accm.to_s
    puts "----------"
end