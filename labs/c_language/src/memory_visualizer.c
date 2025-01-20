#include <stdio.h>
#include <stdlib.h>

#define MEMORY_SIZE 64
#define BLOCK_SIZE 8

void visualize_memory(char* memory, size_t size) {
    printf("\nMemory Layout:\n");
    printf("+");
    for (int i = 0; i < size/BLOCK_SIZE; i++) {
        printf("--------+");
    }
    printf("\n|");
    
    for (int i = 0; i < size; i++) {
        if (memory[i] == 0) {
            printf(" FREE  |");
        } else {
            printf(" ALLOC |");
        }
        if ((i+1) % BLOCK_SIZE == 0 && i != size-1) {
            printf("\n+");
            for (int j = 0; j < size/BLOCK_SIZE; j++) {
                printf("--------+");
            }
            printf("\n|");
        }
    }
    
    printf("\n+");
    for (int i = 0; i < size/BLOCK_SIZE; i++) {
        printf("--------+");
    }
    printf("\n");
}

void visualize_fragmentation(char* memory, size_t size) {
    int free_blocks = 0;
    int total_free = 0;
    
    for (int i = 0; i < size; i++) {
        if (memory[i] == 0) {
            total_free++;
            if (i == 0 || memory[i-1] != 0) {
                free_blocks++;
            }
        }
    }
    
    printf("\nFragmentation Analysis:\n");
    printf("Total free space: %d bytes\n", total_free);
    printf("Free blocks: %d\n", free_blocks);
    printf("Average block size: %.2f bytes\n", 
           (float)total_free/free_blocks);
} 