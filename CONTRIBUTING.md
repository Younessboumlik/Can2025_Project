# Contributing to CAN 2025 Predictor

Thank you for your interest in contributing to the CAN 2025 Predictor project! We welcome contributions from the community.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Clear title** describing the bug
2. **Steps to reproduce** the issue
3. **Expected behavior** vs actual behavior
4. **Screenshots** if applicable
5. **Environment details**:
   - Python version
   - Operating system
   - Browser (if applicable)
   - Dependencies versions

### Suggesting Enhancements

We love new ideas! To suggest an enhancement:

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with the `enhancement` label
3. **Describe the feature** clearly
4. **Explain the use case** and benefits
5. **Provide examples** if possible

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**:
   ```bash
   git commit -m "Add: descriptive commit message"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**

## 📋 Development Guidelines

### Code Style

- Follow **PEP 8** style guide for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Use type hints where appropriate

Example:
```python
def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate distance between two coordinates using Haversine formula.
    
    Args:
        lat1: Latitude of first point
        lon1: Longitude of first point
        lat2: Latitude of second point
        lon2: Longitude of second point
    
    Returns:
        Distance in kilometers
    """
    # Implementation here
    pass
```

### Testing

Before submitting a pull request:

1. **Test your changes** manually
2. **Run the application** locally
3. **Test edge cases**
4. **Check for console errors**
5. **Verify all features still work**

### Documentation

- Update **README.md** if you add new features
- Add **docstrings** to new functions
- Update **comments** for modified code
- Include **usage examples** for new features

### Commit Message Format

Use clear, descriptive commit messages:

```
Add: Brief description of what was added
Fix: Brief description of what was fixed
Update: Brief description of what was updated
Remove: Brief description of what was removed
Refactor: Brief description of refactoring
Docs: Brief description of documentation changes
```

Examples:
- `Add: Monte Carlo simulation feature`
- `Fix: Incorrect distance calculation for Comoros`
- `Update: FIFA rankings for January 2025`
- `Docs: Add installation instructions for Windows`

## 🔍 Areas We Need Help

### High Priority

1. **Model Improvements**
   - Better feature engineering
   - Alternative ML algorithms
   - Hyperparameter optimization
   - Cross-validation strategies

2. **Data Quality**
   - Update team statistics
   - Add more historical matches
   - Validate current rankings
   - Fix incorrect data points

3. **UI/UX Enhancements**
   - Mobile responsive design
   - Better visualizations
   - Interactive charts
   - Improved color schemes

### Medium Priority

4. **Performance Optimization**
   - Faster simulation times
   - Efficient data loading
   - Caching strategies
   - Code optimization

5. **New Features**
   - Export predictions to PDF
   - API endpoints
   - Historical comparison
   - Live match updates

6. **Internationalization**
   - English translation
   - Arabic translation
   - Spanish translation
   - Other languages

### Low Priority

7. **Testing**
   - Unit tests
   - Integration tests
   - Performance tests
   - UI tests

8. **Documentation**
   - Video tutorials
   - API documentation
   - Architecture diagrams
   - Best practices guide

## 🚀 Setting Up Development Environment

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/Can2025_Project.git
cd Can2025_Project
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

### 5. Make Changes

- Create a feature branch
- Make your changes
- Test thoroughly
- Commit and push

## 📦 Dependencies Management

When adding new dependencies:

1. **Check if necessary** - avoid bloat
2. **Choose stable versions** - prefer established packages
3. **Update requirements.txt**:
   ```bash
   pip freeze > requirements.txt
   ```
4. **Document the reason** in your PR

## 🧪 Testing Guidelines

### Manual Testing Checklist

- [ ] Application starts without errors
- [ ] All tabs are accessible
- [ ] Single match prediction works
- [ ] Group display is correct
- [ ] Tournament simulation completes
- [ ] Monte Carlo simulation runs
- [ ] Team stats display correctly
- [ ] Flags display properly
- [ ] No console errors
- [ ] Responsive on different screen sizes

### Test Cases to Consider

1. **Edge Cases**:
   - Same team selected twice
   - Missing team data
   - Very high/low rankings
   - Extreme scores

2. **Performance**:
   - Large number of simulations
   - Multiple rapid predictions
   - Memory usage
   - Load times

3. **Data Validation**:
   - Invalid team names
   - Missing pickle files
   - Corrupted data
   - Version compatibility

## 🎯 Code Review Process

All pull requests will be reviewed for:

1. **Functionality**: Does it work as intended?
2. **Code Quality**: Is it clean and maintainable?
3. **Documentation**: Is it well documented?
4. **Testing**: Has it been tested?
5. **Style**: Does it follow guidelines?
6. **Impact**: Does it break existing features?

## ❓ Questions?

If you have questions:

1. **Check the README** first
2. **Search existing issues**
3. **Create a new issue** with the `question` label
4. **Be specific** about your question

## 🏆 Recognition

Contributors will be:

- Listed in the **README.md** acknowledgments
- Mentioned in release notes
- Credited for their contributions

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of:

- Age
- Body size
- Disability
- Ethnicity
- Gender identity
- Level of experience
- Nationality
- Personal appearance
- Race
- Religion
- Sexual identity and orientation

### Our Standards

**Positive behavior includes**:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards others

**Unacceptable behavior includes**:
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by creating an issue or contacting the project maintainer. All complaints will be reviewed and investigated promptly and fairly.

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to CAN 2025 Predictor! 🎉⚽

