# recurse-and-tail-recurse-examples
examples and time/stack depth test of recursive and tail-recursive function written in python and ruby.

# introdution
There are five files : one(execute_with_tco.rb) for executing ruby files with TCO, and others are codes.

Four examples available. Wrote only essential argument.

1. sum_num/tail_sum(n) : return sum from 1 to n.
2. fac/tail_fac(n) : return n!
3. fib/tail_fib(n) : return nth fibonaci number. (1, 1, 2, 3, 5...)
4. hanoi/tail_hanoi(n) : return the list that shows the way to solve hanoi tower with n disks.
5. part/tail_part(n, k) : return the list which partitioned n into k pieces.


Two tests available : 'recurse_depth_test_example' files test stack call depth, and 'recurse_speed_test_example' files test speed.

python tail call optimize code by https://chrispenner.ca/posts/python-tail-recursion here.

to execute fuby files with TCO, execute 'execute_with_tco.rb' with argument : 'depth' for test stack call depth, 'time' for test speed.
