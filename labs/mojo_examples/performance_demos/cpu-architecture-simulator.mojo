from max.tensor import Tensor, TensorSpec, TensorShape
from math import log2

# Custom Dictionary Implementation for Mojo
struct Dictionary:
    var keys: List[String]
    var int_values: List[Int]
    var float_values: List[Float32]
    var is_float_dict: Bool
    fn __init__(inout self, is_float: Bool = False):
        self.keys = List[String]()
        self.int_values = List[Int]()
        self.float_values = List[Float32]()
        self.is_float_dict = is_float
    
    fn __copyinit__(inout self, other: Self):
        self.keys = other.keys
        self.int_values = other.int_values
        self.float_values = other.float_values
        self.is_float_dict = other.is_float_dict
    
    fn set_int(inout self, key: String, value: Int):
        debug_assert(not self.is_float_dict, "Attempting to set int in float dictionary")
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.int_values[i] = value
                return
        
        self.keys.append(key)
        self.int_values.append(value)
    
    fn set_float(inout self, key: String, value: Float32):
        debug_assert(self.is_float_dict, "Attempting to set float in int dictionary")
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.float_values[i] = value
                return
        
        self.keys.append(key)
        self.float_values.append(value)
    
    fn get_int(self, key: String) -> Int:
        debug_assert(not self.is_float_dict, "Attempting to get int from float dictionary")
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.int_values[i]
        return 0
    
    fn get_float(self, key: String) -> Float32:
        debug_assert(self.is_float_dict, "Attempting to get float from int dictionary")
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.float_values[i]
        return 0.0

# CPU Architecture Simulator
struct CPUArchitectureSimulator:
    # Architectural Parameters
    var word_size: Int
    var register_count: Int
    var cache_levels: Int
    
    # Performance Metrics
    var clock_cycles: Int
    var instructions_executed: Int
    
    # Initialize CPU Architecture
    fn __init__(inout self, word_size: Int = 64, register_count: Int = 32, cache_levels: Int = 3):
        self.word_size = word_size
        self.register_count = register_count
        self.cache_levels = cache_levels
        self.clock_cycles = 0
        self.instructions_executed = 0
    
    # Instruction Encoding Simulation
    fn encode_instruction(self, opcode: String, operands: List[Int]) -> Tensor[DType.int64]:
        """
        Simulate instruction encoding process.
        
        Args:
            opcode (String): Instruction operation code.
            operands (List[Int]): List of register or immediate operands.
        
        Returns:
            Tensor[DType.int64]: Encoded instruction as a tensor.
        """
        var encoded = Tensor[DType.int64](TensorShape(1))
        
        # Basic instruction encoding simulation
        if opcode == "LOAD":
            encoded[0] = (0b0001 << 28) | (operands[0] << 20) | (operands[1] & 0xFFFFF)
        elif opcode == "STORE":
            encoded[0] = (0b0010 << 28) | (operands[0] << 20) | (operands[1] & 0xFFFFF)
        elif opcode == "ADD":
            encoded[0] = (0b0011 << 28) | (operands[0] << 20) | (operands[1] << 12) | (operands[2] & 0xFFF)
        elif opcode == "SUB":
            encoded[0] = (0b0100 << 28) | (operands[0] << 20) | (operands[1] << 12) | (operands[2] & 0xFFF)
        else:
            encoded[0] = 0  # Invalid instruction
        
        return encoded
    
    # Instruction Decoding Simulation
    fn decode_instruction(self, encoded_instruction: Tensor[DType.int64]) -> Dictionary:
        """
        Simulate instruction decoding process.
        
        Args:
            encoded_instruction (Tensor[DType.int64]): Encoded instruction tensor.
        
        Returns:
            Dictionary: Decoded instruction details.
        """
        var decoded = Dictionary(is_float=False)
        var instruction = encoded_instruction[0]
        
        # Extract opcode
        var opcode_bits = (instruction >> 28) & 0xF
        
        if opcode_bits == 0b0001:
            decoded.set_int("opcode", 1)  # LOAD
            decoded.set_int("destination_register", Int((instruction >> 20) & 0xFF))
            decoded.set_int("immediate_value", Int(instruction & 0xFFFFF))
        elif opcode_bits == 0b0010:
            decoded.set_int("opcode", 2)  # STORE
            decoded.set_int("source_register", Int((instruction >> 20) & 0xFF))
            decoded.set_int("memory_address", Int(instruction & 0xFFFFF))
        elif opcode_bits == 0b0011:
            decoded.set_int("opcode", 3)  # ADD
            decoded.set_int("destination_register", Int((instruction >> 20) & 0xFF))
            decoded.set_int("source_register1", Int((instruction >> 12) & 0xFF))
            decoded.set_int("source_register2", Int(instruction & 0xFFF))
        elif opcode_bits == 0b0100:
            decoded.set_int("opcode", 4)  # SUB
            decoded.set_int("destination_register", Int((instruction >> 20) & 0xFF))
            decoded.set_int("source_register1", Int((instruction >> 12) & 0xFF))
            decoded.set_int("source_register2", Int(instruction & 0xFFF))
        else:
            decoded.set_int("opcode", 0)  # INVALID
        
        return decoded
    
    # Performance Analysis
    fn analyze_performance(self, instructions: List[Tensor[DType.int64]]) -> Dictionary:
        """
        Analyze CPU performance for a set of instructions.
        
        Args:
            instructions (List[Tensor[DType.int64]]): List of encoded instructions.
        
        Returns:
            Dictionary: Performance metrics dictionary.
        """
        var total_instructions = len(instructions)
        var cycles_per_instruction: Float32 = 4.0  # Simplified CPI model
        
        var total_cycles = total_instructions * cycles_per_instruction
        var ipc = total_instructions / total_cycles  # Instructions per cycle
        
        var performance_metrics = Dictionary(is_float=True)
        performance_metrics.set_float("total_instructions", Float32(total_instructions))
        performance_metrics.set_float("total_cycles", Float32(total_cycles))
        performance_metrics.set_float("instructions_per_cycle", ipc)
        performance_metrics.set_float("clock_frequency", 3.5)  # GHz, example value
        
        return performance_metrics
    
    # Cache Performance Simulation
    fn simulate_cache_performance(self, memory_accesses: List[Int], cache_sizes: List[Int], associativity: List[Int]) -> Dictionary:
        """
        Simulate multi-level cache performance.
        
        Args:
            memory_accesses (List[Int]): List of memory access addresses.
        
        Returns:
            Dictionary: Cache performance metrics.
        """
        var cache_hit_rates = Tensor[DType.float32](values=[0.0 for _ in range(self.cache_levels)])
        var total_accesses = len(memory_accesses)
        
        # Enhanced cache simulation with size and associativity
        for level in range(self.cache_levels):
            var cache_size = cache_sizes[level]
            var assoc = associativity[level]
            var block_size = self.word_size  # Assuming block size equals word size
            
            # Simplified hit rate model based on cache size, associativity, and access patterns
            var hit_rate = (1.0 - (1.0 / Float32(assoc * (cache_size / block_size)))) * 100.0
            
            cache_hit_rates[level] = hit_rate
        
        var cache_metrics = Dictionary(is_float=True)
        cache_metrics.set_float("l1_hit_rate", cache_hit_rates[0])
        cache_metrics.set_float("l2_hit_rate", cache_hit_rates[1])
        cache_metrics.set_float("l3_hit_rate", cache_hit_rates[2])
        
        return cache_metrics

# Main Simulation Function
fn main():
    # Create CPU Architecture Simulator
    var cpu_sim = CPUArchitectureSimulator(word_size=64, register_count=32, cache_levels=3)
    
    # Example Instruction Set
    var instructions = List[Tensor[DType.int64]]()
    instructions.append(cpu_sim.encode_instruction("LOAD", List[Int](1, 100)))
    instructions.append(cpu_sim.encode_instruction("LOAD", List[Int](2, 200)))
    instructions.append(cpu_sim.encode_instruction("ADD", List[Int](3, 1, 2)))
    instructions.append(cpu_sim.encode_instruction("STORE", List[Int](3, 300)))
    
    # Decode and Print Instructions
    for i in range(len(instructions)):
        var decoded = cpu_sim.decode_instruction(instructions[i])
        print("Decoded Instruction:")
        for j in range(len(decoded.keys)):
            print(decoded.keys[j] + ":", decoded.get_int(decoded.keys[j]))
    
    # Performance Analysis
    var performance = cpu_sim.analyze_performance(instructions)
    print("\nPerformance Metrics:")
    for j in range(len(performance.keys)):
        print(performance.keys[j] + ":", performance.get_float(performance.keys[j]))
    
    # Cache Performance Simulation
    var memory_accesses = List[Int](100, 200, 300, 400, 500)
    var cache_sizes = List[Int](32768, 262144, 2097152)  # Example sizes: 32KB, 256KB, 2MB
    var associativity = List[Int](8, 4, 16)  # Example associativity values
    
    var cache_performance = cpu_sim.simulate_cache_performance(memory_accesses, cache_sizes, associativity)
    print("\nCache Performance:")
    for j in range(len(cache_performance.keys)):
        print(cache_performance.keys[j] + ":", cache_performance.get_float(cache_performance.keys[j]))