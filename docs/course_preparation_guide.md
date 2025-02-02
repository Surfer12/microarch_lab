# CIS 240: Computer Architecture and Low-Level Programming Preparation Guide

## Course Overview

This course explores the intricate relationship between software and hardware, focusing on how programs interact with computer systems at a fundamental level.

## Prerequisites and Recommended Background

- Basic programming experience (preferably in C)
- Understanding of basic computer science concepts
- Comfort with logical and computational thinking

## Language Transition Guide

### Moving from Java to C

- **Key Differences**
  - Manual memory management vs garbage collection
  - Pointers and direct memory access
  - No built-in object orientation
  - Platform-dependent behavior

- **Common Pitfalls**

  ```c
  // Java: Objects are automatically managed
  String str = new String("Hello");

  // C: Manual memory management required
  char* str = malloc(6 * sizeof(char));
  strcpy(str, "Hello");
  // Must remember to free!
  free(str);
  ```

- **Important C Concepts for Java Developers**
  - Understanding stack vs heap memory
  - Pointer arithmetic and array relationships
  - Manual string handling
  - Struct usage instead of classes

  ```c
  // Instead of Java classes, use structs
  struct Person {
      char* name;
      int age;
      void (*print)(struct Person*);  // Function pointer for methods
  };
  ```

### Transitioning from Mojo to C

- **Key Differences**
  - Lower-level memory control
  - No built-in SIMD or vectorization
  - Different approach to zero-cost abstractions
  - Manual optimization required

- **Memory Management Comparison**

  ```c
  // Mojo: Structured memory management
  fn process_data[T: DType](data: Buffer[T]):
      # Memory managed within scope
      let result = Buffer[T](data.size)
      return result

  // C: Manual memory handling
  void* process_data(void* data, size_t size) {
      void* result = malloc(size);
      if (!result) return NULL;
      // Must handle memory manually
      return result;
  }
  ```

- **Performance Optimization**
  - Understanding cache alignment
  - Manual vectorization techniques
  - Explicit memory layout control

  ```c
  // Optimize struct layout for cache
  struct OptimizedData {
      int64_t aligned_field;  // 8-byte aligned
      int32_t medium_field;   // 4-byte aligned
      int16_t small_field;    // 2-byte aligned
      int8_t tiny_field;      // 1-byte aligned
  };  // Total: 16 bytes, well-packed
  ```

### Common C Programming Gotchas

- **Memory Leaks**

  ```c
  // WRONG: Memory leak
  char* get_string() {
      char* str = malloc(10);
      return str;  // Caller must remember to free
  }

  // BETTER: Document memory ownership
  /* Caller is responsible for freeing returned string */
  char* get_string() {
      char* str = malloc(10);
      if (!str) return NULL;
      return str;
  }
  ```

- **Buffer Overflows**

  ```c
  // WRONG: Potential buffer overflow
  char buffer[5];
  strcpy(buffer, "Hello, World!");  // Writes beyond buffer

  // BETTER: Use strncpy or check sizes
  char buffer[5];
  strncpy(buffer, "Hello, World!", sizeof(buffer) - 1);
  buffer[sizeof(buffer) - 1] = '\0';  // Ensure null termination
  ```

- **Pointer Arithmetic**

  ```c
  // WRONG: Undefined behavior
  int arr[5] = {1, 2, 3, 4, 5};
  int* ptr = arr + 5;  // Points one past array
  printf("%d", *ptr);  // Undefined behavior!

  // BETTER: Stay within bounds
  int arr[5] = {1, 2, 3, 4, 5};
  for (int* ptr = arr; ptr < arr + 5; ptr++) {
      printf("%d ", *ptr);
  }
  ```

### Data Type Conversions and Transformations

#### 1. String and Number Conversions

```c
// String to Integer conversion
char str[] = "12345";
int num = atoi(str);              // Basic conversion
long lnum = strtol(str, NULL, 10); // More control, base 10

// Integer to String conversion
int num = 12345;
char str[20];
sprintf(str, "%d", num);          // Using sprintf
// or
snprintf(str, sizeof(str), "%d", num);  // Safer, prevents buffer overflow

// Floating point conversions
char float_str[] = "123.45";
float f = atof(float_str);        // String to float
double d = strtod(float_str, NULL); // String to double
```

#### 2. Base Conversions

```c
// Hexadecimal string to integer
char hex[] = "1A";
int hex_val = (int)strtol(hex, NULL, 16);  // Base 16

// Binary string to integer
char bin[] = "1010";
int bin_val = (int)strtol(bin, NULL, 2);   // Base 2

// Integer to hex string
int val = 26;
char hex_str[10];
sprintf(hex_str, "%X", val);  // Uppercase hex
sprintf(hex_str, "%x", val);  // Lowercase hex

// Working with different bases
printf("Decimal: %d\n", val);     // Base 10
printf("Hex: 0x%X\n", val);       // Base 16
printf("Octal: %o\n", val);       // Base 8
```

#### 3. Data Structure Transformations

```c
// Array to Linked List conversion
typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* array_to_list(int arr[], int size) {
    if (size == 0) return NULL;

    Node* head = malloc(sizeof(Node));
    if (!head) return NULL;

    head->data = arr[0];
    head->next = NULL;

    Node* current = head;
    for (int i = 1; i < size; i++) {
        Node* new_node = malloc(sizeof(Node));
        if (!new_node) {
            // Handle error: free allocated memory
            while (head) {
                Node* temp = head;
                head = head->next;
                free(temp);
            }
            return NULL;
        }
        new_node->data = arr[i];
        new_node->next = NULL;
        current->next = new_node;
        current = new_node;
    }
    return head;
}

// Linked List to Array conversion
int* list_to_array(Node* head, int* size) {
    // Count nodes
    int count = 0;
    Node* current = head;
    while (current) {
        count++;
        current = current->next;
    }

    // Allocate array
    int* arr = malloc(count * sizeof(int));
    if (!arr) return NULL;

    // Copy data
    current = head;
    for (int i = 0; i < count; i++) {
        arr[i] = current->data;
        current = current->next;
    }

    *size = count;
    return arr;
}
```

#### 4. File Format Conversions

```c
// Text to Binary file conversion
int text_to_binary(const char* input_file, const char* output_file) {
    FILE *in, *out;
    char ch;

    in = fopen(input_file, "r");
    if (!in) return -1;

    out = fopen(output_file, "wb");
    if (!out) {
        fclose(in);
        return -1;
    }

    while ((ch = fgetc(in)) != EOF) {
        fwrite(&ch, sizeof(char), 1, out);
    }

    fclose(in);
    fclose(out);
    return 0;
}

// Binary to Text file conversion
int binary_to_text(const char* input_file, const char* output_file) {
    FILE *in, *out;
    char ch;

    in = fopen(input_file, "rb");
    if (!in) return -1;

    out = fopen(output_file, "w");
    if (!out) {
        fclose(in);
        return -1;
    }

    while (fread(&ch, sizeof(char), 1, in) == 1) {
        fputc(ch, out);
    }

    fclose(in);
    fclose(out);
    return 0;
}
```

#### 5. Bit Manipulation and Type Punning

```c
// Float to bits visualization
void print_float_bits(float f) {
    uint32_t bits;
    memcpy(&bits, &f, sizeof(float));

    for (int i = 31; i >= 0; i--) {
        printf("%d", (bits >> i) & 1);
        if (i == 31 || i == 23) printf(" ");
    }
    printf("\n");
}

// Type punning example (note: implementation-defined behavior)
union FloatInt {
    float f;
    uint32_t i;
};

void analyze_float(float f) {
    union FloatInt fi;
    fi.f = f;
    printf("Float: %f\n", fi.f);
    printf("Bits: 0x%08X\n", fi.i);
}
```

### Conversion Pitfalls and Best Practices

#### 1. Type Conversion Safety

```c
// WRONG: Potential data loss
int large_num = 1000000;
short small_num = large_num;  // May truncate

// BETTER: Check ranges
if (large_num > SHRT_MAX || large_num < SHRT_MIN) {
    // Handle error
} else {
    short small_num = (short)large_num;
}

// WRONG: Sign extension issues
unsigned int u = 0xFFFFFFFF;
int i = u;  // Implementation-defined behavior

// BETTER: Explicit conversion with checks
if (u > INT_MAX) {
    // Handle error
} else {
    int i = (int)u;
}
```

#### 2. String Conversion Safety

```c
// WRONG: Buffer overflow risk
char small_buffer[5];
int big_number = 123456;
sprintf(small_buffer, "%d", big_number);  // Buffer overflow!

// BETTER: Use snprintf
char small_buffer[5];
int big_number = 123456;
if (snprintf(small_buffer, sizeof(small_buffer), "%d", big_number) >= sizeof(small_buffer)) {
    // Handle truncation
}

// WRONG: No error checking
char* str = "123abc";
int num = atoi(str);  // Silently returns 123

// BETTER: Use strtol for error checking
char* str = "123abc";
char* endptr;
errno = 0;
long num = strtol(str, &endptr, 10);
if (errno != 0 || endptr == str || *endptr != '\0') {
    // Handle conversion error
}
```

#### 3. Memory Management in Conversions

```c
// WRONG: Memory leak in error case
char* convert_to_uppercase(const char* input) {
    char* result = malloc(strlen(input) + 1);
    for (int i = 0; input[i]; i++) {
        result[i] = toupper(input[i]);
        if (some_error_condition) return NULL;  // Memory leak!
    }
    result[strlen(input)] = '\0';
    return result;
}

// BETTER: Clean up on error
char* convert_to_uppercase(const char* input) {
    char* result = malloc(strlen(input) + 1);
    if (!result) return NULL;

    for (int i = 0; input[i]; i++) {
        result[i] = toupper(input[i]);
        if (some_error_condition) {
            free(result);
            return NULL;
        }
    }
    result[strlen(input)] = '\0';
    return result;
}
```

#### 4. Platform-Dependent Conversions

```c
// WRONG: Assumes sizeof(int) == 4
uint32_t convert_to_network_order(int value) {
    return htonl(value);
}

// BETTER: Explicit about size
uint32_t convert_to_network_order(int32_t value) {
    return htonl((uint32_t)value);
}

// WRONG: Assumes endianness
float bits_to_float(uint32_t bits) {
    return *(float*)&bits;  // Type-punning, undefined behavior

// BETTER: Use memcpy
float bits_to_float(uint32_t bits) {
    float result;
    memcpy(&result, &bits, sizeof(float));
    return result;
}
```

#### 5. Best Practices Summary

- Always check for conversion errors
- Use appropriate buffer sizes
- Clean up resources on error paths
- Be explicit about types and sizes
- Consider platform differences
- Document assumptions and requirements
- Use safe alternatives to dangerous functions
- Validate input before conversion
- Handle edge cases gracefully

### Practical C Examples

- **Dynamic Array Implementation**

  ```c
  typedef struct {
      int* data;
      size_t size;
      size_t capacity;
  } DynamicArray;

  DynamicArray* create_array(size_t initial_capacity) {
      DynamicArray* arr = malloc(sizeof(DynamicArray));
      if (!arr) return NULL;

      arr->data = malloc(initial_capacity * sizeof(int));
      if (!arr->data) {
          free(arr);
          return NULL;
      }

      arr->size = 0;
      arr->capacity = initial_capacity;
      return arr;
  }

  void destroy_array(DynamicArray* arr) {
      if (arr) {
          free(arr->data);
          free(arr);
      }
  }
  ```

- **Function Pointers for Callbacks**

  ```c
  typedef void (*EventHandler)(const char* event);

  void register_callback(EventHandler handler) {
      // Store handler for later use
      handler("Event occurred!");
  }

  void my_handler(const char* event) {
      printf("Handling event: %s\n", event);
  }

  // Usage
  register_callback(my_handler);
  ```

### Debugging Tips

- Use tools like Valgrind for memory leak detection
- GDB for step-by-step debugging
- Address Sanitizer for memory error detection

  ```bash
  # Compile with sanitizer
  gcc -fsanitize=address -g program.c
  ```

### Recommended Practice Exercises

#### 1. Memory Management Exercises

- Implement a simple string class with proper memory management
- Create a generic linked list implementation
- Build a memory pool allocator

```c
// Example string class implementation
typedef struct {
    char* data;
    size_t length;
} String;

String* string_create(const char* initial) {
    String* str = malloc(sizeof(String));
    if (!str) return NULL;

    str->length = strlen(initial);
    str->data = malloc(str->length + 1);
    if (!str->data) {
        free(str);
        return NULL;
    }

    strcpy(str->data, initial);
    return str;
}

void string_destroy(String* str) {
    if (str) {
        free(str->data);
        free(str);
    }
}
```

#### 2. Data Structure Conversion

- Convert Java ArrayList to C dynamic array
- Implement a binary search tree without classes
- Create a hash table using C structs

```c
// Example hash table entry
typedef struct Entry {
    char* key;
    void* value;
    struct Entry* next;
} Entry;

typedef struct {
    Entry** buckets;
    size_t size;
    size_t capacity;
} HashMap;
```

#### 3. Algorithm Implementation

- Implement sorting algorithms using pointers
- Create a simple memory allocator
- Build a basic garbage collector

```c
// Example quicksort implementation
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}
```

#### 4. Low-Level Operations

- Bit manipulation exercises
- Implement basic compression algorithms
- Create a simple serialization format

```c
// Example bit manipulation
uint32_t set_bit(uint32_t num, int pos) {
    return num | (1u << pos);
}

uint32_t clear_bit(uint32_t num, int pos) {
    return num & ~(1u << pos);
}

uint32_t toggle_bit(uint32_t num, int pos) {
    return num ^ (1u << pos);
}
```

#### 5. System Integration

- Create a simple file I/O library
- Implement basic network operations
- Build a command-line argument parser

```c
// Example command line parser
typedef struct {
    int verbose;
    char* input_file;
    char* output_file;
} Options;

Options parse_args(int argc, char* argv[]) {
    Options opts = {0};  // Initialize to 0
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0) {
            opts.verbose = 1;
        } else if (strcmp(argv[i], "-i") == 0 && i + 1 < argc) {
            opts.input_file = argv[++i];
        } else if (strcmp(argv[i], "-o") == 0 && i + 1 < argc) {
            opts.output_file = argv[++i];
        }
    }
    return opts;
}
```

## Key Learning Objectives

1. Understand digital hardware design
2. Learn how high-level programs translate to machine instructions
3. Explore computer architecture principles
4. Develop low-level programming skills

## Technical Preparation

### 1. Programming Skills

- **C Language Fundamentals**
  - Pointers and memory management
  - Bit-level operations
  - Struct and memory layout
  - Compilation process

- **Recommended C Practice Areas**

  ```c
  // Example areas to practice
  int *ptr = malloc(sizeof(int) * 10);  // Dynamic memory allocation
  unsigned int bitwise_ops = 0x0F & 0xF0;  // Bitwise operations
  struct SystemState {
      int cpu_state;
      char* memory_ptr;
  };  // Struct design
  ```

### 2. Hardware Concepts

- Binary and hexadecimal number systems
- Boolean logic
- Basic digital circuit understanding
- CPU instruction set basics

### 3. Development Environment Setup

- **Recommended Tools**
  - GCC or Clang compiler
  - Make build system
  - Git for version control
  - Text editor or IDE (VSCode, Vim, etc.)

### 4. Recommended Learning Resources

- **Books**
  - "Computer Systems: A Programmer's Perspective"
  - "Digital Design and Computer Architecture"

- **Online Resources**
  - MIT OpenCourseWare: Computer Architecture lectures
  - Coursera: Nand to Tetris
  - RISC-V educational resources

## Practical Preparation Checklist

### Technical Skills

- [ ] Review C programming fundamentals
- [ ] Practice memory management
- [ ] Understand compilation process
- [ ] Learn basic assembly language concepts

### Hardware Understanding

- [ ] Study basic digital logic
- [ ] Understand how instructions are executed
- [ ] Learn about CPU registers and memory hierarchy

## Lab and Project Expectations

- Hands-on hardware simulation
- Low-level programming assignments
- Potential FPGA or simulation-based projects

## Instructor's Perspective

Drawing from Tina Smilkstein's background in digital systems and medical technology, expect a course that bridges theoretical concepts with practical applications.

## Additional Tips

1. Start early with C programming practice
2. Build small projects to reinforce concepts
3. Don't be afraid to experiment and make mistakes
4. Collaborate with classmates
5. Ask questions and seek clarification

## Sample Preparation Project

Try implementing a simple memory allocator or simulate a basic CPU instruction decoder to get hands-on experience.

## Contact and Support

- Instructor Office Hours: [To be announced]
- Course Communication Platform: [To be specified]

**Remember**: This course is about understanding the fundamental relationship between software and hardware. Stay curious and enjoy the journey!

## Advanced Topics and Applications

### Integrated Circuits (ICs)

- **Fundamentals**
  - Overview of integrated circuits and their evolution
  - Systems-on-chip (SoC) architecture
  - Design and fabrication processes

- **Design Process**
  - Schematic capture and layout
  - Simulation and verification
  - Power management considerations

- **Medical Applications**
  - Signal processing for diagnostics (ECG, EEG)
  - Microcontrollers in medical devices
  - Power optimization for battery-operated devices

### Medical Device Technology

- **Design Considerations**
  - Regulatory compliance (ISO 13485, FDA)
  - Biocompatibility and reliability
  - Miniaturization challenges

- **Practical Applications**
  - Case studies of medical devices
  - Integration of ICs in medical systems
  - Power management solutions

### Interactive Learning Resources

- **Visual Aids and Simulations**
  - Circuit design simulations
  - Hardware interaction demonstrations
  - Medical device anatomy diagrams

- **Hands-on Exercises**
  - IC design exercises using SPICE
  - CAD tutorials for device design
  - Interactive code examples via Jupyter Notebooks

- **Assessment and Feedback**
  - End-of-section quizzes
  - Project-based assessments
  - Continuous feedback mechanisms

## Industry Connection

- Guest lectures from medical device professionals
- Mentorship opportunities
- Career pathways in electronics and medical devices
