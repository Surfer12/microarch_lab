#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

// Mock function to test memory allocation
int test_memory_allocation() {
    int *test_array = malloc(5 * sizeof(int));
    
    // Check if memory allocation was successful
    assert(test_array != NULL);
    
    // Initialize and test array
    for (int i = 0; i < 5; i++) {
        test_array[i] = i * 10;
        assert(test_array[i] == i * 10);
    }
    
    free(test_array);
    return 1;
}

// Mock function to test pointer operations
int test_pointer_operations() {
    int x = 42;
    int *ptr = &x;
    
    // Test pointer dereferencing
    assert(*ptr == 42);
    
    // Test pointer arithmetic
    int array[] = {10, 20, 30, 40, 50};
    int *array_ptr = array;
    
    for (int i = 0; i < 5; i++) {
        assert(*(array_ptr + i) == array[i]);
    }
    
    return 1;
}

int main() {
    printf("Running Memory Operation Tests...\n");
    
    if (test_memory_allocation()) {
        printf("Memory Allocation Test: PASSED\n");
    } else {
        printf("Memory Allocation Test: FAILED\n");
        return 1;
    }
    
    if (test_pointer_operations()) {
        printf("Pointer Operations Test: PASSED\n");
    } else {
        printf("Pointer Operations Test: FAILED\n");
        return 1;
    }
    
    printf("All tests completed successfully!\n");
    return 0;
} 