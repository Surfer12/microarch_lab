# Error Handling and Safety in C Programming

## Defensive Programming Fundamentals

### 1. Principles of Defensive Programming
- Anticipate potential failure points
- Validate all inputs
- Implement comprehensive error checking
- Design for graceful failure

#### Defensive Input Validation Example
```c
typedef struct {
    char* data;
    size_t length;
} SafeString;

SafeString* create_safe_string(const char* input) {
    // Defensive checks
    if (!input) {
        errno = EINVAL;
        return NULL;
    }

    // Length validation
    size_t length = strlen(input);
    if (length == 0) {
        errno = ENODATA;
        return NULL;
    }

    // Maximum length protection
    const size_t MAX_STRING_LENGTH = 1024;
    if (length > MAX_STRING_LENGTH) {
        errno = E2BIG;
        return NULL;
    }

    // Safe allocation
    SafeString* safe_str = malloc(sizeof(SafeString));
    if (!safe_str) {
        errno = ENOMEM;
        return NULL;
    }

    // Copy with explicit null termination
    safe_str->data = malloc(length + 1);
    if (!safe_str->data) {
        free(safe_str);
        errno = ENOMEM;
        return NULL;
    }

    strncpy(safe_str->data, input, length);
    safe_str->data[length] = '\0';
    safe_str->length = length;

    return safe_str;
}

void destroy_safe_string(SafeString* str) {
    if (str) {
        free(str->data);
        free(str);
    }
}
```

### 2. Input Validation Strategies
- Range checking
- Type validation
- Boundary condition testing
- Sanitization techniques

#### Comprehensive Input Validation
```c
int safe_divide(int numerator, int denominator) {
    // Check for division by zero
    if (denominator == 0) {
        errno = EDOM;  // Domain error
        return -1;
    }

    // Overflow prevention
    if (numerator == INT_MIN && denominator == -1) {
        errno = ERANGE;  // Range error
        return -1;
    }

    return numerator / denominator;
}
```

## Error Detection Strategies

### 1. Error Handling Mechanisms
- Errno-based error reporting
- Return value checking
- Error logging
- Graceful error propagation

#### Robust Error Handling Pattern
```c
typedef enum {
    ERROR_NONE = 0,
    ERROR_MEMORY_ALLOCATION,
    ERROR_INVALID_INPUT,
    ERROR_FILE_OPERATION,
    ERROR_NETWORK
} ErrorCode;

typedef struct {
    ErrorCode code;
    char message[256];
} ErrorContext;

ErrorContext global_error = {0};

void set_error(ErrorContext* ctx, ErrorCode code, const char* message) {
    ctx->code = code;
    strncpy(ctx->message, message, sizeof(ctx->message) - 1);
    ctx->message[sizeof(ctx->message) - 1] = '\0';
}

void clear_error(ErrorContext* ctx) {
    ctx->code = ERROR_NONE;
    memset(ctx->message, 0, sizeof(ctx->message));
}

bool process_data(const char* input) {
    clear_error(&global_error);

    if (!input) {
        set_error(&global_error, ERROR_INVALID_INPUT, "Null input provided");
        return false;
    }

    // Simulated processing with potential failure points
    void* buffer = malloc(1024);
    if (!buffer) {
        set_error(&global_error, ERROR_MEMORY_ALLOCATION, "Failed to allocate buffer");
        return false;
    }

    // Processing logic
    bool success = true;
    // ... processing code ...

    free(buffer);
    return success;
}

// Usage example
int main() {
    if (!process_data("test")) {
        if (global_error.code != ERROR_NONE) {
            fprintf(stderr, "Error %d: %s\n", 
                    global_error.code, global_error.message);
        }
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
```

### 2. Advanced Error Tracking
- Error context preservation
- Detailed error logging
- Stack trace generation
- Error categorization

## Robust Code Design

### 1. Resource Management
- RAII-like patterns in C
- Automatic resource cleanup
- Leak prevention techniques

#### Resource Management Example
```c
typedef struct {
    FILE* file;
    char* buffer;
} ResourceManager;

ResourceManager* create_resource_manager(const char* filename) {
    ResourceManager* manager = malloc(sizeof(ResourceManager));
    if (!manager) return NULL;

    manager->file = fopen(filename, "r");
    if (!manager->file) {
        free(manager);
        return NULL;
    }

    manager->buffer = malloc(1024);
    if (!manager->buffer) {
        fclose(manager->file);
        free(manager);
        return NULL;
    }

    return manager;
}

void destroy_resource_manager(ResourceManager* manager) {
    if (manager) {
        if (manager->file) {
            fclose(manager->file);
        }
        if (manager->buffer) {
            free(manager->buffer);
        }
        free(manager);
    }
}
```

### 2. Fail-Safe Design Patterns
- Implement fallback mechanisms
- Design for partial failure
- Implement circuit breaker patterns

## Debugging Techniques

### 1. Debugging Strategies
- Compile-time assertions
- Runtime checks
- Logging frameworks
- Memory debugging tools

#### Compile-Time Assertions
```c
#define STATIC_ASSERT(condition, message) \
    typedef char static_assertion_##message[(condition) ? 1 : -1]

// Usage examples
STATIC_ASSERT(sizeof(int) == 4, integer_size_must_be_4_bytes);
STATIC_ASSERT(sizeof(void*) == 8, pointer_size_must_be_8_bytes);
```

### 2. Memory Debugging
- Valgrind usage
- Address Sanitizer
- Memory leak detection
- Undefined behavior tracking

#### Memory Debugging Example
```c
// Compile with: gcc -fsanitize=address -g memory_debug_example.c
void memory_debug_demo() {
    // Intentional memory errors for demonstration
    int* leak = malloc(sizeof(int));  // Memory leak
    
    int* buffer = malloc(10 * sizeof(int));
    buffer[10] = 42;  // Buffer overflow
    
    free(buffer);
    free(buffer);  // Double free
}
```

### 3. Logging and Tracing
- Structured logging
- Log levels
- Performance-aware logging

#### Logging Framework
```c
typedef enum {
    LOG_DEBUG,
    LOG_INFO,
    LOG_WARNING,
    LOG_ERROR,
    LOG_CRITICAL
} LogLevel;

void log_message(LogLevel level, const char* file, 
                 int line, const char* format, ...) {
    const char* level_strings[] = {
        "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
    };

    va_list args;
    va_start(args, format);

    fprintf(stderr, "[%s] %s:%d - ", 
            level_strings[level], file, line);
    vfprintf(stderr, format, args);
    fprintf(stderr, "\n");

    va_end(args);

    // Optional: Additional handling for critical errors
    if (level == LOG_CRITICAL) {
        abort();
    }
}

// Macro for easier logging
#define LOG(level, ...) \
    log_message(level, __FILE__, __LINE__, __VA_ARGS__)
```

## Learning Objectives
- Master defensive programming techniques
- Develop comprehensive error handling skills
- Understand memory safety principles
- Learn advanced debugging strategies

## Practical Exercises
1. Implement a robust string handling library
2. Create a resource management framework
3. Develop a logging system with multiple verbosity levels
4. Write memory-safe data structures

## Recommended Resources
- "Defensive Programming" by James Whittaker
- Valgrind documentation
- CERT C Coding Standard
- AddressSanitizer guides

## Assessment
- Defensive programming challenge
- Error handling implementation project
- Memory safety analysis
- Debugging technique demonstration

## Best Practices Checklist
- [ ] Always validate inputs
- [ ] Use comprehensive error checking
- [ ] Implement graceful error handling
- [ ] Prevent resource leaks
- [ ] Use logging for diagnostics
- [ ] Employ memory debugging tools
- [ ] Design for failure scenarios 