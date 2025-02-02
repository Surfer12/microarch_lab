.PHONY: lint format static-analysis

lint:
	clang-format --dry-run -Werror .

format:
	clang-format -i .

static-analysis:
	cppcheck --enable=all --inconclusive --std=c99 .