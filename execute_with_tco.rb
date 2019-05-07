RubyVM::InstructionSequence.compile_option = {
  :tailcall_optimization => true,
  :trace_instruction => false
}

if ARGV[0] == "depth"
    require_relative 'recurse_depth_test_example.rb'
elsif ARGV[0] == "time"
    require_relative 'recurse_time_test_example.rb'
else
    p "Please give one argument : \'depth\' or \'time\'"
end