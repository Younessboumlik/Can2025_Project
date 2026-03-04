# ⚽ CAN 2025 Predictor - African Cup of Nations AI Prediction Tool

An interactive web application that uses machine learning to predict match outcomes for the 2025 African Cup of Nations (CAN 2025) tournament. The application features multiple prediction modes, including single match predictions, full tournament simulations, and Monte Carlo analysis.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)](https://scikit-learn.org/)

## 📑 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Technical Details](#-technical-details)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## 🌟 Features

### 1. Single Match Prediction
- Predict the outcome of any match between two teams
- View win probabilities and expected scores
- Run 100 simulations to get statistical predictions
- Visual display with team flags and detailed metrics

### 2. Group Stage Overview
- Browse all 6 groups (A-F) with their teams
- View FIFA rankings for each team
- Visual organization of the tournament structure

### 3. Full Tournament Simulation
- Simulate the entire CAN 2025 tournament
- Group stage matches with automatic qualification
- Knockout rounds (Round of 16, Quarter-finals, Semi-finals, Final)
- Penalty shootout simulation for draws
- Complete match-by-match results

### 4. Monte Carlo Analysis
- Run thousands of tournament simulations (100-10,000)
- Statistical probability of reaching each stage
- Identify favorites, outsiders, and potential surprises
- Detailed probability breakdown for top contenders

### 5. Team Statistics
- Comprehensive team profiles
- FIFA ranking and points
- Market value information
- Offensive and defensive form metrics
- Team momentum indicators

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Younessboumlik/Can2025_Project.git
cd Can2025_Project
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:8501`
   - Start exploring predictions!

### Your First Prediction (1 minute)

1. Navigate to "🎯 Match Unique" tab
2. Select two teams from the dropdowns
3. Click "🔮 Prédire"
4. View results: Win probabilities and expected score

**Example**: Morocco vs Egypt
- Result might show: Morocco 45%, Draw 25%, Egypt 30%
- Score: Morocco 1.8 - 1.4 Egypt

## 📖 Usage Guide

### Interface Overview

The application has 5 main tabs:
- 🎯 **Match Unique** - Predict single matches
- 🏆 **Groupes** - View tournament groups
- 🎲 **Simulation Unique** - Full tournament simulation
- 📊 **Monte Carlo** - Statistical analysis
- 📈 **Stats Équipes** - Team statistics

### Tab 1: Match Unique (Single Match Prediction)

**How to Use:**
1. Select Team 1 from the left dropdown
2. Select Team 2 from the right dropdown
3. Click "🔮 Prédire" button

**Results Interpretation:**
- **Win Probabilities**: Calculated from 100 simulated matches
- **Predicted Score**: Average score from all simulations
- **Team Flags**: Visual identification

**Tips:**
- Compare teams with similar rankings for closer matches
- Host nation (Morocco) gets a slight advantage (+0.4 goals)
- Consider checking team stats first in Tab 5

### Tab 2: Groupes (Tournament Groups)

View the official CAN 2025 group stage organization:

- **Group A**: Morocco (Host), Mali, Zambia, Comoros
- **Group B**: Egypt, South Africa, Angola, Zimbabwe
- **Group C**: Nigeria, Tunisia, Uganda, Tanzania
- **Group D**: Senegal, DR Congo, Benin, Botswana
- **Group E**: Algeria, Burkina Faso, Equatorial Guinea, Sudan
- **Group F**: Ivory Coast, Cameroon, Gabon, Mozambique

### Tab 3: Simulation Unique (Full Tournament Simulation)

**How to Use:**
1. Click "🚀 Simuler le Tournoi" button
2. Wait for simulation (takes 10-30 seconds)
3. Review results from top to bottom

**The app simulates:**
- Group Stage: All 36 group matches with points allocation
- Round of 16: 8 knockout matches
- Quarter-Finals: 4 matches
- Semi-Finals: 2 matches
- Final: Championship match

**Note**: Penalty shootouts (TAB) are 50/50 random for draws

### Tab 4: Monte Carlo (Statistical Analysis)

**How to Use:**
1. Set number of simulations (100-10,000)
   - 100: Quick preview
   - 1,000: Good balance (recommended)
   - 10,000: Maximum precision
2. Click "🚀 Lancer la simulation"
3. Wait for completion (1,000 sims ≈ 2-5 minutes)

**Results:**
- **Champion (%)**: Probability of winning the tournament
- **Finale (%)**: Probability of reaching the final
- **Demi (%)**: Probability of reaching semi-finals
- **Quart (%)**: Probability of reaching quarter-finals

### Tab 5: Stats Équipes (Team Statistics)

**Metrics Displayed:**
- 🏅 **Rang FIFA**: FIFA world ranking (lower = better)
- ⚡ **Points FIFA**: Numerical FIFA points
- 💰 **Valeur**: Squad market value in millions €
- 📈 **Momentum**: Recent form indicator
- 🎯 **Forme Offensive**: Goals scored per match (last 5)
- 🛡️ **Forme Défensive**: Goals conceded per match (last 5)

## 📊 How It Works

### Machine Learning Model

The prediction system uses **Random Forest** regression models trained on historical African football match data:

- **Model Architecture**: Dual model approach
  - `model_home.pkl`: Predicts home team goals
  - `model_away.pkl`: Predicts away team goals
  
- **Performance Metrics**:
  - Mean Absolute Error (MAE): 0.842 goals
  - Prediction Accuracy: 54.49%

### Features Used for Prediction

The models consider multiple factors:

1. **Team Rankings**
   - FIFA world ranking differences
   - FIFA points differences

2. **Team Form**
   - Recent performance momentum
   - Offensive form (goals scored per match)
   - Defensive form (goals conceded per match)

3. **Market Value**
   - Team market value differences (from Transfermarkt)

4. **Geographical Factors**
   - Distance from host city (Rabat, Morocco)
   - Home advantage for the host nation

5. **Match Context**
   - Tournament stage importance
   - Historical head-to-head performance

### Prediction Algorithm

1. **Feature Engineering**: Calculate differences between teams
2. **Base Prediction**: Random Forest models predict expected goals
3. **Adjustments**:
   - Distance penalty: -0.05 goals per 1000km from Rabat
   - Host advantage: +0.4 goals for Morocco
4. **Simulation**: Use Poisson distribution to generate realistic scores
5. **Aggregation**: Run multiple simulations for statistical confidence

## 🏗️ Project Structure

```
Can2025_Project/
│
├── app.py                          # Main Streamlit application
├── ai-predictor-can-2025.ipynb    # Model training notebook
├── requirements.txt                # Python dependencies
│
├── model_home.pkl                  # Trained model for home team goals
├── model_away.pkl                  # Trained model for away team goals
├── teams_data.pkl                  # Team statistics and features
├── groups.pkl                      # CAN 2025 tournament groups
│
├── README.md                       # This file
├── LICENSE                         # MIT License
└── .gitignore                      # Git configuration
```

## 🔧 Technical Details

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Machine Learning**: scikit-learn (Random Forest)
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Model Persistence**: pickle/joblib

### Data Sources

- FIFA World Rankings
- Historical match results
- Team market values (Transfermarkt)
- CAN 2025 official group draws

### Core Functions

#### `load_models()`
Load pre-trained ML models and tournament data from pickle files. Cached with `@st.cache_resource` for performance.

```python
model_home, model_away, teams_data, groups = load_models()
```

#### `predict_match(team1, team2)`
Predict the score of a match between two teams using ML models.

**Process:**
1. Extract team features and calculate differences
2. Use Random Forest models to predict expected goals
3. Apply distance penalty (travel fatigue)
4. Apply host advantage bonus
5. Sample from Poisson distribution for final scores

**Returns:** `(score1, score2, expected_goals_1, expected_goals_2)`

#### `get_distance_rabat(team_name)`
Calculate great-circle distance from Rabat, Morocco to a team's capital using the Haversine formula.

**Formula:**
```python
distance = R * 2 * atan2(sqrt(a), sqrt(1-a))
```
Where R = 6371 km (Earth's radius)

### Algorithm Details

**Poisson Distribution for Score Generation**:
```python
score = np.random.poisson(expected_goals)
```

**Distance Penalty**:
```python
exp_goals -= (distance / 1000) * 0.05  # 0.05 goals per 1000km
```

**Host Advantage**:
```python
if team == 'Morocco':
    exp_goals += 0.4  # +0.4 goals for host
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs

If you find a bug, please create an issue with:
1. Clear title describing the bug
2. Steps to reproduce the issue
3. Expected behavior vs actual behavior
4. Screenshots if applicable
5. Environment details (Python version, OS, browser)

### Suggesting Enhancements

To suggest an enhancement:
1. Check existing issues to avoid duplicates
2. Create a new issue with the `enhancement` label
3. Describe the feature clearly
4. Explain the use case and benefits
5. Provide examples if possible

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m 'Add some AmazingFeature'`
6. Push to the branch: `git push origin feature/AmazingFeature`
7. Open a Pull Request

### Code Style Guidelines

- Follow **PEP 8** style guide for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Use type hints where appropriate

**Example:**
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

### Areas for Contribution

- Improve prediction accuracy
- Add more visualization features
- Implement real-time data updates
- Add historical comparison features
- Enhance UI/UX design
- Add multi-language support
- Create mobile-responsive layout
- Add unit tests and integration tests

## 📝 Model Training

The model was trained using the Jupyter notebook `ai-predictor-can-2025.ipynb`:

1. **Data Collection**: Historical African football matches
2. **Feature Engineering**: Calculate team statistics and differentials
3. **Model Selection**: Random Forest chosen for best performance
4. **Hyperparameter Tuning**: Optimized for accuracy
5. **Validation**: Cross-validation and test set evaluation
6. **Export**: Models saved as pickle files

To retrain the models:
```bash
jupyter notebook ai-predictor-can-2025.ipynb
```

## 🎮 Usage Examples

### Example 1: Predict Host Advantage
```
Team 1: Morocco (host)
Team 2: Senegal
Expected: Morocco gets +0.4 goal advantage
```

### Example 2: Compare Rankings
```
Team 1: Nigeria (Rank 28)
Team 2: Botswana (Rank 140)
Expected: Nigeria strongly favored
```

### Example 3: Close Match
```
Team 1: Egypt (Rank 33)
Team 2: Tunisia (Rank 41)
Expected: Competitive, close percentages
```

## ❓ Troubleshooting

### Application Won't Start

**Issue**: Error when running `streamlit run app.py`

**Solutions**:
1. Check Python version: `python --version` (need 3.8+)
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check for missing pickle files
4. Try: `streamlit run app.py --server.port 8502`

### Predictions Seem Wrong

**Issue**: Results don't match expectations

**Explanation**:
- Predictions are probabilistic, not certain
- Historical data may not reflect current form
- Model has 54% accuracy - not perfect
- Upsets happen in real football too!

### Slow Performance

**Issue**: Monte Carlo simulations take too long

**Solutions**:
1. Reduce number of simulations (try 500)
2. Close other applications
3. Use faster computer if available
4. Be patient - accuracy requires time

### Teams Not Displaying

**Issue**: Missing teams or flags

**Solutions**:
1. Check internet connection (flags load from CDN)
2. Clear browser cache
3. Refresh the page
4. Check pickle files are present

## 💡 Pro Tips

1. **Run multiple simulations** for better accuracy
2. **Check team stats first** before predicting
3. **Use Monte Carlo** (1000+ sims) for tournament favorites
4. **Compare results** from different tabs
5. **Consider recent form** (momentum indicator)

## ❓ Common Questions

**Q: Why do results change each time?**
A: Predictions use probability - outcomes vary naturally.

**Q: How accurate are predictions?**
A: Model has 54.49% accuracy (better than random!).

**Q: Can I predict any match?**
A: Only teams qualified for CAN 2025.

**Q: What affects predictions most?**
A: FIFA ranking, team form, and market value.

**Q: Does Morocco always win?**
A: No, but they get home advantage (+0.4 goals).

## 🐛 Known Issues

- Predictions are probabilistic and may not reflect real outcomes
- Historical data bias may affect underdog teams
- Distance calculations assume direct routes
- Penalty shootouts are random 50/50 splits

## 🔮 Future Enhancements

- [ ] Real-time odds comparison
- [ ] Player-level statistics integration
- [ ] Live match tracking and updates
- [ ] Historical tournament comparison
- [ ] API endpoint for predictions
- [ ] Mobile application
- [ ] Multi-language support (English, Arabic, French)
- [ ] Social media integration for sharing predictions
- [ ] Export predictions to PDF/Excel

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Youness Boumlik**

- GitHub: [@Younessboumlik](https://github.com/Younessboumlik)

## 🙏 Acknowledgments

- FIFA for official rankings data
- Transfermarkt for market value data
- African Football Confederation (CAF)
- Streamlit community
- scikit-learn contributors

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Create an issue on GitHub with detailed description
3. Provide error messages and screenshots if applicable

## ⚠️ Disclaimer

This application is for entertainment and educational purposes only. Predictions are based on statistical models and historical data. Actual match outcomes depend on many unpredictable factors. Do not use for gambling or betting decisions.

---

**Enjoy predicting the CAN 2025! 🏆⚽**
