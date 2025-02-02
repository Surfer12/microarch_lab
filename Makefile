.PHONY: build cmake lint format static-analysis

cmake:
	mkdir -p build && cd build && cmake ..

build: cmake
	cd build && cmake --build .

lint:
	@echo "Lint target deprecated. Please use CMake build tools."

format:
	@echo "Format target deprecated. Please use CMake build tools or install clang-format."

static-analysis:
	cppcheck --enable=all --inconclusive --std=c99 .