from memory import memset, memcpy
from sys import sizeof, alignof
from pathlib import Path
from time import time


struct MemorySnapshot:
    var total_allocated: Int
    var peak_memory: Int
    var allocation_count: Int
    var deallocations: Int

    fn __init__(inout self):
        self.total_allocated = 0
        self.peak_memory = 0
        self.allocation_count = 0
        self.deallocations = 0

    fn record_allocation(inout self, size: Int):
        self.total_allocated += size
        self.allocation_count += 1
        self.peak_memory = max(self.peak_memory, self.total_allocated)

    fn record_deallocation(inout self, size: Int):
        self.total_allocated -= size
        self.deallocations += 1
