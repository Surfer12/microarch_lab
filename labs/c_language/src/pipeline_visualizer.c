#include <stdio.h>

#define STAGES 5
#define INSTRUCTIONS 10

void visualize_pipeline() {
    char* stages[] = {"Fetch", "Decode", "Execute", "Memory", "Writeback"};
    
    printf("\nPipeline Visualization:\n");
    printf("Time-> ");
    for (int t = 0; t < INSTRUCTIONS + STAGES - 1; t++) {
        printf("%2d ", t);
    }
    printf("\n");
    
    for (int s = 0; s < STAGES; s++) {
        printf("%-8s ", stages[s]);
        for (int t = 0; t < INSTRUCTIONS + STAGES - 1; t++) {
            if (t >= s && t < INSTRUCTIONS + s) {
                printf(" I%d ", t - s + 1);
            } else {
                printf("    ");
            }
        }
        printf("\n");
    }
    
    printf("\nKey:\n");
    printf("I1-I%d: Instruction sequence\n", INSTRUCTIONS);
    printf("Empty spaces: Pipeline bubbles\n");
} 