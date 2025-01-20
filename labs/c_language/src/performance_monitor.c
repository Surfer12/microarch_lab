#include <time.h>
#include <stdio.h>

struct PerformanceTimer {
    struct timespec start;
    struct timespec end;
};

void start_timer(struct PerformanceTimer* timer) {
    clock_gettime(CLOCK_MONOTONIC, &timer->start);
}

void stop_timer(struct PerformanceTimer* timer) {
    clock_gettime(CLOCK_MONOTONIC, &timer->end);
}

double get_elapsed_time(struct PerformanceTimer* timer) {
    return (timer->end.tv_sec - timer->start.tv_sec) +
           (timer->end.tv_nsec - timer->start.tv_nsec) / 1e9;
}

void print_performance_stats(const char* label, double elapsed_time) {
    printf("[Performance] %s: %.6f seconds\n", label, elapsed_time);
} 