# Import necessary libraries

import numpy as np # type: ignore # this is handled in the pixi.toml file

# Define the Dictionary class
class Dictionary:
    def __init__(self, is_float=False):
        self.keys = []
        self.int_values = []
        self.float_values = []
        self.is_float_dict = is_float

    def set_int(self, key, value):
        assert not self.is_float_dict, "Attempting to set int in float dictionary"
        if key in self.keys:
            index = self.keys.index(key)
            self.int_values[index] = value
        else:
            self.keys.append(key)
            self.int_values.append(value)

    def set_float(self, key, value):
        assert self.is_float_dict, "Attempting to set float in int dictionary"
        if key in self.keys:
            index = self.keys.index(key)
            self.float_values[index] = value
        else:
            self.keys.append(key)
            self.float_values.append(value)

    def get_int(self, key):
        assert not self.is_float_dict, "Attempting to get int from float dictionary"
        if key in self.keys:
            index = self.keys.index(key)
            return self.int_values[index]
        return 0

    def get_float(self, key):
        assert self.is_float_dict, "Attempting to get float from int dictionary"
        if key in self.keys:
            index = self.keys.index(key)
            return self.float_values[index]
        return 0.0

# Define the CPU Architecture Simulator class
class CPUArchitectureSimulator:
    def __init__(self, word_size=64, register_count=32, cache_levels=3):
        self.word_size = word_size
        self.register_count = register_count
        self.cache_levels = cache_levels
        self.clock_cycles = 0
        self.instructions_executed = 0

    def encode_instruction(self, opcode, operands):
        encoded = np.zeros(1, dtype=np.int64)
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

    def decode_instruction(self, encoded_instruction):
        decoded = Dictionary(is_float=False)
        instruction = encoded_instruction[0]
        opcode_bits = (instruction >> 28) & 0xF

        if opcode_bits == 0b0001:
            decoded.set_int("opcode", 1)  # LOAD
            decoded.set_int("destination_register", (instruction >> 20) & 0xFF)
            decoded.set_int("immediate_value", instruction & 0xFFFFF)
        elif opcode_bits == 0b0010:
            decoded.set_int("opcode", 2)  # STORE
            decoded.set_int("source_register", (instruction >> 20) & 0xFF)
            decoded.set_int("memory_address", instruction & 0xFFFFF)
        elif opcode_bits == 0b0011:
            decoded.set_int("opcode", 3)  # ADD
            decoded.set_int("destination_register", (instruction >> 20) & 0xFF)
            decoded.set_int("source_register1", (instruction >> 12) & 0xFF)
            decoded.set_int("source_register2", instruction & 0xFFF)
        elif opcode_bits == 0b0100:
            decoded.set_int("opcode", 4)  # SUB
            decoded.set_int("destination_register", (instruction >> 20) & 0xFF)
            decoded.set_int("source_register1", (instruction >> 12) & 0xFF)
            decoded.set_int("source_register2", instruction & 0xFFF)
        else:
            decoded.set_int("opcode", 0)  # INVALID
        return decoded

    def analyze_performance(self, instructions):
        total_instructions = len(instructions)
        cycles_per_instruction = 4.0  # Simplified CPI model
        total_cycles = total_instructions * cycles_per_instruction
        ipc = total_instructions / total_cycles  # Instructions per cycle

        performance_metrics = Dictionary(is_float=True)
        performance_metrics.set_float("total_instructions", float(total_instructions))
        performance_metrics.set_float("total_cycles", float(total_cycles))
        performance_metrics.set_float("instructions_per_cycle", ipc)
        performance_metrics.set_float("clock_frequency", 3.5)  # GHz, example value
        return performance_metrics

    def simulate_cache_performance(self, memory_accesses, cache_sizes, associativity):
        cache_hit_rates = np.zeros(self.cache_levels, dtype=np.float32)
        total_accesses = len(memory_accesses)

        for level in range(self.cache_levels):
            cache_size = cache_sizes[level]
            assoc = associativity[level]
            block_size = self.word_size  # Assuming block size equals word size
            hit_rate = (1.0 - (1.0 / float(assoc * (cache_size / block_size)))) * 100.0
            cache_hit_rates[level] = hit_rate

        cache_metrics = Dictionary(is_float=True)
        cache_metrics.set_float("l1_hit_rate", cache_hit_rates[0])
        cache_metrics.set_float("l2_hit_rate", cache_hit_rates[1])
        cache_metrics.set_float("l3_hit_rate", cache_hit_rates[2])
        return cache_metrics

# Main Simulation Function
def main():
    cpu_sim = CPUArchitectureSimulator(word_size=64, register_count=32, cache_levels=3)

    instructions = []
    instructions.append(cpu_sim.encode_instruction("LOAD", [1, 100]))
    instructions.append(cpu_sim.encode_instruction("LOAD", [2, 200]))
    instructions.append(cpu_sim.encode_instruction("ADD", [3, 1, 2]))
    instructions.append(cpu_sim.encode_instruction("STORE", [3, 300]))

    for i in range(len(instructions)):
        decoded = cpu_sim.decode_instruction(instructions[i])
        print("Decoded Instruction:")
        for j in range(len(decoded.keys)):
            print(f"{decoded.keys[j]}: {decoded.get_int(decoded.keys[j])}")

    performance = cpu_sim.analyze_performance(instructions)
    print("\nPerformance Metrics:")
    for j in range(len(performance.keys)):
        print(f"{performance.keys[j]}: {performance.get_float(performance.keys[j])}")

    memory_accesses = [100, 200, 300, 400, 500]
    cache_sizes = [32768, 262144, 2097152]  # Example sizes: 32KB, 256KB, 2MB
    associativity = [8, 4, 16]  # Example associativity values

    cache_performance = cpu_sim.simulate_cache_performance(memory_accesses, cache_sizes, associativity)
    print("\nCache Performance:")
    for j in range(len(cache_performance.keys)):
        print(f"{cache_performance.keys[j]}: {cache_performance.get_float(cache_performance.keys[j])}")

if __name__ == "__main__":
    main()