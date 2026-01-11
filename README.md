# ⚽ CAN 2025 Predictor - African Cup of Nations AI Prediction Tool

An interactive web application that uses machine learning to predict match outcomes for the 2025 African Cup of Nations (CAN 2025) tournament. The application features multiple prediction modes, including single match predictions, full tournament simulations, and Monte Carlo analysis.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)](https://scikit-learn.org/)

## 🌟 Features

### 1. **Single Match Prediction**
- Predict the outcome of any match between two teams
- View win probabilities and expected scores
- Run 100 simulations to get statistical predictions
- Visual display with team flags and detailed metrics

### 2. **Group Stage Overview**
- Browse all 6 groups (A-F) with their teams
- View FIFA rankings for each team
- Visual organization of the tournament structure

### 3. **Full Tournament Simulation**
- Simulate the entire CAN 2025 tournament
- Group stage matches with automatic qualification
- Knockout rounds (Round of 16, Quarter-finals, Semi-finals, Final)
- Penalty shootout simulation for draws
- Complete match-by-match results

### 4. **Monte Carlo Analysis**
- Run thousands of tournament simulations (100-10,000)
- Statistical probability of reaching each stage
- Identify favorites, outsiders, and potential surprises
- Detailed probability breakdown for top contenders

### 5. **Team Statistics**
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
└── .gitattributes                  # Git configuration
```

## 📱 Application Interface

### Navigation Tabs

1. **🎯 Match Unique** - Single match predictions
2. **🏆 Groupes** - View tournament groups
3. **🎲 Simulation Unique** - Full tournament simulation
4. **📊 Monte Carlo** - Statistical analysis with multiple simulations
5. **📈 Stats Équipes** - Individual team statistics

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

### Algorithm Details

**Poisson Distribution for Score Generation**:
```python
score = np.random.poisson(expected_goals)
```

**Distance Calculation** (Haversine Formula):
```python
distance = R * 2 * atan2(sqrt(a), sqrt(1-a))
```

## 🎮 Usage Examples

### Example 1: Predict a Single Match

```python
# In the "Match Unique" tab:
1. Select "Morocco" as Team 1
2. Select "Egypt" as Team 2
3. Click "🔮 Prédire"
4. View win probabilities and expected score
```

### Example 2: Run Monte Carlo Simulation

```python
# In the "Monte Carlo" tab:
1. Set number of simulations (e.g., 1000)
2. Click "🚀 Lancer la simulation"
3. Wait for completion
4. Analyze probability tables
```

### Example 3: View Team Stats

```python
# In the "Stats Équipes" tab:
1. Select a team from dropdown
2. View FIFA ranking, points, market value
3. Check offensive and defensive form
4. Review momentum indicator
```

## 🏆 Tournament Teams (CAN 2025)

The application includes all 24 qualified teams across 6 groups:

- **Group A**: Morocco (host), Mali, Zambia, Comoros
- **Group B**: Egypt, South Africa, Angola, Zimbabwe
- **Group C**: Nigeria, Tunisia, Uganda, Tanzania
- **Group D**: Senegal, DR Congo, Benin, Botswana
- **Group E**: Algeria, Burkina Faso, Equatorial Guinea, Sudan
- **Group F**: Ivory Coast, Cameroon, Gabon, Mozambique

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Areas for Contribution

- Improve prediction accuracy
- Add more visualization features
- Implement real-time data updates
- Add historical comparison features
- Enhance UI/UX design
- Add more languages support
- Create mobile-responsive layout

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

## 🐛 Known Issues

- Predictions are probabilistic and may not reflect real outcomes
- Historical data bias may affect underdog teams
- Distance calculations assume direct routes
- Penalty shootouts are random 50/50 splits

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

1. Check the [Issues](https://github.com/Younessboumlik/Can2025_Project/issues) page
2. Create a new issue with detailed description
3. Provide error messages and screenshots if applicable

## 🔮 Future Enhancements

- [ ] Real-time odds comparison
- [ ] Player-level statistics integration
- [ ] Live match tracking and updates
- [ ] Historical tournament comparison
- [ ] API endpoint for predictions
- [ ] Mobile application
- [ ] Multi-language support (English, Arabic, French)
- [ ] Social media integration for sharing predictions
- [ ] Betting odds integration
- [ ] Export predictions to PDF/Excel

## ⚠️ Disclaimer

This application is for entertainment and educational purposes only. Predictions are based on statistical models and historical data. Actual match outcomes depend on many unpredictable factors. Do not use for gambling or betting decisions.

---

**Enjoy predicting the CAN 2025! 🏆⚽**

