#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Demonstrate dynamic memory allocation
void demonstrate_memory_allocation() {
    printf("Memory Allocation Demonstration:\n");

    // Allocate memory for an integer array
    int *dynamic_array = malloc(5 * sizeof(int));
    if (dynamic_array == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return;
    }

    // Initialize the array
    for (int i = 0; i < 5; i++) {
        dynamic_array[i] = i * 10;
    }

    // Print the array
    printf("Dynamic Array Contents:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", dynamic_array[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(dynamic_array);
}

// Demonstrate pointer manipulation
void demonstrate_pointer_operations() {
    printf("\nPointer Operations Demonstration:\n");

    int x = 42;
    int *ptr = &x;
    
    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", (void*)&x);
    printf("Value of ptr: %p\n", (void*)ptr);
    printf("Value pointed to by ptr: %d\n", *ptr);

    // Pointer arithmetic
    int array[] = {10, 20, 30, 40, 50};
    int *array_ptr = array;

    printf("\nArray Pointer Arithmetic:\n");
    for (int i = 0; i < 5; i++) {
        printf("*(array_ptr + %d) = %d\n", i, *(array_ptr + i));
    }
}

int main() {
    demonstrate_memory_allocation();
    demonstrate_pointer_operations();

    return 0;
} 