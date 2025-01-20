# Makefile for C Language Microarchitecture Lab

# Add cross-platform support
ifeq ($(OS),Windows_NT)
    CC = gcc
    RM = del /Q
    MKDIR = mkdir
    EXE_EXT = .exe
else
    CC = gcc
    RM = rm -rf
    MKDIR = mkdir -p
    EXE_EXT =
endif

# Add platform-specific flags
ifeq ($(OS),Windows_NT)
    CFLAGS += -D_WIN32
else
    CFLAGS += -D_UNIX
endif

# Compiler flags
CFLAGS += -Wall -Wextra -std=c11 -g
OPTIMIZE_FLAGS = -O2

# Directories
SRC_DIR = src
BUILD_DIR = build
TEST_DIR = tests

# Source files
SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(SRCS))

# Targets
.PHONY: all clean test

# Default target
all: $(BUILD_DIR) $(BUILD_DIR)/microarch_lab

# Create build directory
$(BUILD_DIR):
	$(MKDIR) $(BUILD_DIR)

# Compile main executable
$(BUILD_DIR)/microarch_lab: $(OBJS)
	$(CC) $(CFLAGS) $(OPTIMIZE_FLAGS) -o $@ $^

# Compile source files to object files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) $(OPTIMIZE_FLAGS) -c $< -o $@

# Run tests
test:
	@echo "Running tests..."
	$(MAKE) -C $(TEST_DIR)

# Clean build artifacts
clean:
	$(RM) $(BUILD_DIR)
	$(MAKE) -C $(TEST_DIR) clean

# Help target
help:
	@echo "Makefile for Microarchitecture Lab"
	@echo "Targets:"
	@echo "  all     - Build the main executable"
	@echo "  test    - Run test suite"
	@echo "  clean   - Remove build artifacts"
	@echo "  help    - Display this help message" 