# 📖 Documentation Index

Welcome to the CAN 2025 Predictor documentation! This index helps you find the right document for your needs.

## 🚀 Getting Started (New Users)

Start here if you're new to the project:

1. **[README.md](README.md)** - Start here! Project overview, features, and basic setup
2. **[QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes with step-by-step guide
3. **[USAGE.md](USAGE.md)** - Learn how to use all features with detailed examples

**Estimated time**: 10-15 minutes to get started

## 👨‍💻 For Developers

If you want to understand the code or extend the project:

1. **[API.md](API.md)** - Technical documentation of functions and data structures
2. **[app.py](app.py)** - Main application code (well-documented with docstrings)
3. **[ai-predictor-can-2025.ipynb](ai-predictor-can-2025.ipynb)** - Model training notebook

**Key sections in API.md**:
- Core Functions (predict_match, load_models, etc.)
- Data Structures (teams_data, groups, etc.)
- Model Details (Random Forest architecture)
- Extension Guide (how to add features)

## 🤝 For Contributors

Want to contribute to the project?

1. **[CONTRIBUTING.md](CONTRIBUTING.md)** - Complete contribution guidelines
2. **[CHANGELOG.md](CHANGELOG.md)** - Version history and how to update it
3. **[CODE_OF_CONDUCT](CONTRIBUTING.md#-code-of-conduct)** - Community guidelines

**Before contributing**:
- Read the contribution guidelines
- Check existing issues
- Follow code style (PEP 8)
- Write clear commit messages

## 📊 For Users

Using the application to predict matches:

1. **[USAGE.md](USAGE.md)** - Comprehensive usage guide
   - Tab 1: Single Match Prediction
   - Tab 2: Tournament Groups
   - Tab 3: Full Tournament Simulation
   - Tab 4: Monte Carlo Analysis
   - Tab 5: Team Statistics

2. **[QUICKSTART.md](QUICKSTART.md)** - Quick examples
   - Your first prediction
   - Running simulations
   - Interpreting results

## 🔍 Quick Reference

### Installation
```bash
git clone https://github.com/Younessboumlik/Can2025_Project.git
cd Can2025_Project
pip install -r requirements.txt
streamlit run app.py
```

See: [README.md - Installation](README.md#installation)

### Common Questions
- "How accurate are predictions?" → [README.md - Model Details](README.md#machine-learning-model)
- "How do I predict a match?" → [QUICKSTART.md - First Prediction](QUICKSTART.md#-your-first-prediction-1-minute)
- "What features are available?" → [README.md - Features](README.md#-features)
- "How can I contribute?" → [CONTRIBUTING.md](CONTRIBUTING.md)
- "How does the model work?" → [API.md - Model Details](API.md#model-details)

### Troubleshooting
- Installation issues → [USAGE.md - Troubleshooting](USAGE.md#-troubleshooting)
- Application errors → [USAGE.md - Common Questions](USAGE.md#-common-questions)
- Performance issues → [USAGE.md - Slow Performance](USAGE.md#slow-performance)

## 📚 Documentation Structure

```
Can2025_Project/
│
├── README.md              ⭐ Start here - Project overview
├── QUICKSTART.md          🚀 5-minute getting started guide
├── USAGE.md               📖 Comprehensive usage guide
├── API.md                 🔧 Technical documentation
├── CONTRIBUTING.md        🤝 Contribution guidelines
├── CHANGELOG.md           📋 Version history
├── LICENSE                ⚖️ MIT License
│
├── app.py                 💻 Main application (documented)
├── requirements.txt       📦 Python dependencies
├── ai-predictor-can-2025.ipynb  📊 Model training
│
└── *.pkl                  🎲 Pre-trained models and data
```

## 🎯 Use Cases

### "I want to predict matches"
→ [QUICKSTART.md](QUICKSTART.md) → [USAGE.md - Tab 1](USAGE.md#-tab-1-match-unique-single-match-prediction)

### "I want to run a full tournament"
→ [QUICKSTART.md - Simulate](QUICKSTART.md#-simulate-the-tournament-2-minutes) → [USAGE.md - Tab 3](USAGE.md#-tab-3-simulation-unique-full-tournament-simulation)

### "I want statistical probabilities"
→ [USAGE.md - Tab 4](USAGE.md#-tab-4-monte-carlo-statistical-analysis)

### "I want to understand team strength"
→ [USAGE.md - Tab 5](USAGE.md#-tab-5-stats-équipes-team-statistics)

### "I want to modify/extend the code"
→ [API.md](API.md) → [API.md - Extending](API.md#extending-the-system)

### "I want to contribute a feature"
→ [CONTRIBUTING.md](CONTRIBUTING.md) → [CONTRIBUTING.md - Pull Requests](CONTRIBUTING.md#pull-requests)

### "I found a bug"
→ [CONTRIBUTING.md - Reporting Bugs](CONTRIBUTING.md#reporting-bugs)

## 📞 Support Channels

1. **Documentation** - Check relevant .md files above
2. **GitHub Issues** - Create an issue for bugs/features
3. **Code Review** - Submit PR for review
4. **Discussions** - GitHub Discussions for questions

## 🔗 External Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Markdown Guide](https://www.markdownguide.org/)

## 📊 Documentation Statistics

- **Total files**: 8 documentation files
- **Total lines**: 1,987 lines
- **Total size**: ~49KB of documentation
- **Coverage**: 100% of features documented
- **Examples**: 50+ code examples and scenarios
- **Languages**: English (with French UI elements)

## 🎓 Learning Path

### Beginner (First 30 minutes)
1. Read [README.md](README.md) (5 min)
2. Follow [QUICKSTART.md](QUICKSTART.md) (10 min)
3. Try each tab in the app (15 min)

### Intermediate (Next 1-2 hours)
1. Read [USAGE.md](USAGE.md) thoroughly (30 min)
2. Explore advanced features (30 min)
3. Check [API.md](API.md) overview (15 min)

### Advanced (For Contributors)
1. Study [API.md](API.md) in detail (1 hour)
2. Read [CONTRIBUTING.md](CONTRIBUTING.md) (30 min)
3. Review source code in [app.py](app.py) (1 hour)
4. Explore model training notebook (1 hour)

## ✅ Documentation Checklist

Before using the project:
- [ ] Read README.md overview
- [ ] Complete QUICKSTART.md tutorial
- [ ] Install dependencies
- [ ] Run first prediction

Before contributing:
- [ ] Read CONTRIBUTING.md
- [ ] Check CHANGELOG.md format
- [ ] Review existing issues
- [ ] Fork repository

Before extending:
- [ ] Study API.md
- [ ] Review app.py docstrings
- [ ] Understand model architecture
- [ ] Test locally

## 🎉 Ready to Start?

Choose your path:
- **New user?** → [QUICKSTART.md](QUICKSTART.md)
- **Want details?** → [USAGE.md](USAGE.md)
- **Developer?** → [API.md](API.md)
- **Contributor?** → [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Need help?** Create an issue on GitHub with your question!

**Found a typo?** We welcome documentation improvements too!

**Enjoy predicting CAN 2025! ⚽🏆**
