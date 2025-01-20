# Contributing to Microarchitecture Learning Lab

## Welcome Contributors!

We're thrilled that you're interested in contributing to the Microarchitecture Learning Lab. This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Be patient and understanding
- Provide constructive feedback
- Collaborate openly and transparently

## How to Contribute

### Reporting Issues

1. Check existing issues to avoid duplicates
2. Use the issue template provided
3. Provide detailed information:
   - Detailed description
   - Steps to reproduce
   - Expected vs. actual behavior
   - Environment details

### Suggesting Enhancements

1. Open a new issue
2. Clearly describe the enhancement
3. Provide context and rationale
4. Include potential implementation ideas

### Pull Request Process

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
   - Follow coding standards
   - Add/update tests
   - Update documentation

4. Commit your changes
   - Use clear, descriptive commit messages
   - Reference issue numbers if applicable

5. Push to your fork
   ```bash
   git push origin feature/your-feature-name
   ```

6. Open a Pull Request
   - Use the PR template
   - Describe changes in detail
   - Link related issues

### Contribution Areas

We welcome contributions in:
- Documentation improvements
- Code examples
- Performance optimizations
- Simulation tools
- Jupyter notebook enhancements
- Bug fixes
- New language examples

### Development Setup

1. Clone the repository
2. Install dependencies
   ```bash
   pip install -r requirements/vscode/python-requirements.txt
   pip install -r requirements/vscode/jupyter-requirements.txt
   ```
3. Set up development environment
   - Use VSCode recommended extensions
   - Follow language-specific setup guides

### Coding Standards

#### Python
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings
- Use black for formatting
- Use pylint for linting

#### Mojo
- Follow Mojo style guidelines
- Add comments and documentation
- Optimize for performance
- Use built-in safety features

#### C
- Follow MISRA C guidelines
- Use const and static appropriately
- Minimize dynamic memory allocation
- Add comprehensive error handling

### Testing

- Write unit tests for new functionality
- Ensure 80%+ test coverage
- Run tests before submitting PR
  ```bash
  pytest
  ```

### Documentation

- Update README if needed
- Add comments to complex code
- Create/update Jupyter notebooks
- Maintain clear, concise documentation

## Review Process

- PRs require review from maintainers
- Automated checks must pass
- Constructive feedback will be provided
- Be open to suggested improvements

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Project documentation
- Potential future acknowledgments

## Questions?

If you have questions, please:
- Check documentation
- Open an issue
- Ask in discussions

Thank you for contributing to the Microarchitecture Learning Lab! 