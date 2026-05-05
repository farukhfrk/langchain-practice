# Contributing to LangChain Practice Repository

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 📋 Code of Conduct

Be respectful, inclusive, and constructive in all interactions.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- Virtual environment (venv, conda, etc.)

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/langchain-practice.git
cd langchain

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 📝 Code Style Guidelines

### Docstrings

All modules and functions must have comprehensive docstrings:

```python
"""
Module-level docstring explaining the purpose of this module.

This module demonstrates [concept] and includes examples of [feature].
It's useful for [use case].

Example:
    python filename.py
"""

def function_name(param1: str, param2: int) -> str:
    """
    Brief description of what the function does.
    
    Longer explanation if needed, describing the algorithm or approach.
    
    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2
        
    Returns:
        str: Description of return value
        
    Raises:
        ValueError: When [specific condition]
        
    Example:
        >>> result = function_name("input", 42)
        >>> print(result)
        output
    """
```

### Comments

- Add inline comments for non-obvious logic
- Use comments to explain "why", not "what"
- Keep comments up-to-date with code

```python
# Good comment explaining why
# Query embeddings are cached to avoid redundant API calls
cached_embedding = cache.get(query_key)

# Avoid obvious comments
# Increment counter
counter += 1
```

### Naming Conventions

- Use descriptive variable names: `user_embeddings` not `ue`
- Use snake_case for functions and variables
- Use PascalCase for classes
- Use UPPER_CASE for constants

### Formatting

- Follow PEP 8 style guide
- Max line length: 100 characters
- Use 4 spaces for indentation
- Add blank lines between functions (2 lines at module level, 1 line in classes)

## 🔧 Types of Contributions

### Bug Reports

When reporting bugs, please include:
1. Python version
2. LangChain version
3. Relevant environment (API provider being used)
4. Steps to reproduce
5. Expected vs actual behavior
6. Error traceback

### Feature Additions

1. **New Examples**: Add examples that clearly demonstrate LangChain concepts
2. **Improvements**: Enhance existing code with better documentation or efficiency
3. **Output Parsers**: Add examples of new output parsing techniques
4. **Integrations**: Add integrations with new LLM providers

### Documentation Improvements

- Fix typos or unclear explanations
- Add missing examples
- Improve README or inline comments
- Add new learning resources

## ✅ Submission Guidelines

### Before Submitting

1. **Test your code**
   ```bash
   # Ensure your script runs without errors
   python your_script.py
   ```

2. **Check your code style**
   ```bash
   # Run formatter (optional but recommended)
   python -m black your_file.py
   ```

3. **Add comments and docstrings**
   - Module-level docstring
   - Function/class docstrings
   - Inline comments for complex logic

4. **Update documentation**
   - Update README if adding new modules
   - Add examples to module docstrings

5. **Test all examples**
   - Ensure all examples are runnable
   - Verify output is meaningful

### Submission Process

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/langchain-practice.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   # Use descriptive branch names like:
   # - feature/add-claude-example
   # - fix/typo-in-readme
   # - docs/improve-chain-explanation
   ```

3. **Make your changes**
   ```bash
   # Edit files and add new examples
   git add .
   ```

4. **Write a good commit message**
   ```bash
   git commit -m "Add brief description of changes
   
   More detailed explanation if needed. Explain:
   - What changed
   - Why it changed
   - How it works
   "
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**
   - Title: Clear description of changes
   - Description: Explain what, why, and how
   - Reference any related issues

### PR Description Template

```markdown
## Description
Brief description of what this PR adds or fixes.

## Type of Change
- [ ] Bug fix
- [ ] New example
- [ ] Documentation update
- [ ] Code improvement
- [ ] New feature

## Related Issues
Fixes #issue_number (if applicable)

## Changes Made
- Bullet point 1
- Bullet point 2
- Bullet point 3

## Testing
Describe how you tested your changes.

## Checklist
- [ ] Code follows style guidelines
- [ ] Added comments and docstrings
- [ ] Updated README (if needed)
- [ ] Tested the code
- [ ] No new warnings generated
```

## 📦 Dependency Guidelines

### Adding New Dependencies

Before adding new dependencies:
1. Consider using built-in Python libraries
2. Check if LangChain already provides the functionality
3. Verify the package is actively maintained
4. Update `requirements.txt` with version pinning

```bash
# Format for requirements.txt
package-name==1.0.0
```

## 🐛 Debugging Tips

### Common Issues

**Issue: API Key not found**
```bash
# Solution: Check .env file
cat .env
# Make sure OPENAI_API_KEY, etc. are set
```

**Issue: Import errors**
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Issue: Rate limiting**
```python
# Solution: Add delays between API calls
import time
time.sleep(1)  # Add 1 second delay
```

## 🎓 Learning Resources for Contributors

- [LangChain Documentation](https://python.langchain.com/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Workflow Guide](https://guides.github.com/introduction/flow/)

## ❓ Questions or Need Help?

1. Check existing issues and discussions
2. Create a new issue with detailed information
3. Start a discussion in the repository

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT).

## 🎉 Thank You!

Thank you for contributing to make this project better! Your efforts help the community learn and grow.

---

**Happy Contributing! 🚀**
