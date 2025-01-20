#include <stdio.h>
#include <stdlib.h>

#define CACHE_SIZE 8
#define BLOCK_SIZE 4

struct CacheLine {
    int valid;
    int tag;
    int data[BLOCK_SIZE];
};

void visualize_cache(struct CacheLine* cache) {
    printf("\nCache Visualization:\n");
    printf("+--------+-----+---------------------+\n");
    printf("| Index  | Tag | Data                |\n");
    printf("+--------+-----+---------------------+\n");
    
    for (int i = 0; i < CACHE_SIZE; i++) {
        printf("| %6d | %3d |", i, cache[i].tag);
        if (cache[i].valid) {
            for (int j = 0; j < BLOCK_SIZE; j++) {
                printf(" %4d", cache[i].data[j]);
            }
        } else {
            printf("     Empty     ");
        }
        printf(" |\n");
    }
    printf("+--------+-----+---------------------+\n");
} 