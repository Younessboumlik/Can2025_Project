# 🔧 API Documentation - CAN 2025 Predictor

## Overview

This document describes the internal functions and data structures of the CAN 2025 Predictor application. While this is primarily a Streamlit web application (not a REST API), understanding these functions is useful for developers who want to extend or integrate the prediction system.

## Core Functions

### 1. `load_models()`

**Purpose**: Load pre-trained machine learning models and data from pickle files.

**Returns**: Tuple of (model_home, model_away, teams_data, groups)

**Cache**: Decorated with `@st.cache_resource` for performance

**Example**:
```python
model_home, model_away, teams_data, groups = load_models()
```

**Files Loaded**:
- `model_home.pkl`: Random Forest model for home team goals
- `model_away.pkl`: Random Forest model for away team goals
- `teams_data.pkl`: Dictionary of team statistics
- `groups.pkl`: Tournament group assignments

---

### 2. `get_flag(team)`

**Purpose**: Generate HTML for displaying team flag images.

**Parameters**:
- `team` (str): Team name (e.g., "Morocco", "Egypt")

**Returns**: str - HTML image tag with flag from flagcdn.com

**Example**:
```python
flag_html = get_flag("Morocco")
# Returns: '<img src="https://flagcdn.com/16x12/ma.png" width="20">'
```

**Note**: Uses ISO country codes from `FLAG_CODES` dictionary

---

### 3. `get_distance_rabat(team_name)`

**Purpose**: Calculate geographical distance from Rabat, Morocco to a team's capital.

**Parameters**:
- `team_name` (str): Name of the team

**Returns**: float - Distance in kilometers

**Formula**: Haversine formula for great-circle distance

**Implementation**:
```python
def get_distance_rabat(team_name):
    if team_name not in capitals:
        return 2000  # Default for unknown teams
    
    lat1, lon1 = capitals['Morocco']
    lat2, lon2 = capitals[team_name]
    R = 6371  # Earth radius in km
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat/2)**2 + 
         math.cos(math.radians(lat1)) * 
         math.cos(math.radians(lat2)) * 
         math.sin(dlon/2)**2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return R * c
```

**Example**:
```python
distance = get_distance_rabat("Egypt")
# Returns: ~3200 (kilometers)
```

---

### 4. `predict_match(team1, team2)`

**Purpose**: Predict the score of a match between two teams.

**Parameters**:
- `team1` (str): First team name
- `team2` (str): Second team name

**Returns**: Tuple of (score1, score2, expected_goals_1, expected_goals_2)
- `score1` (int): Simulated score for team 1
- `score2` (int): Simulated score for team 2
- `expected_goals_1` (float): Expected goals for team 1
- `expected_goals_2` (float): Expected goals for team 2

**Process**:
1. Extract team data from `teams_data`
2. Calculate feature differences
3. Create feature DataFrame
4. Predict using ML models
5. Apply distance adjustments
6. Apply host advantage
7. Sample from Poisson distribution

**Example**:
```python
s1, s2, exp1, exp2 = predict_match("Morocco", "Egypt")
# Returns: (2, 1, 1.85, 1.23)
```

**Features Used**:
- `rank_diff`: FIFA ranking difference
- `points_diff`: FIFA points difference
- `market_value_diff`: Market value difference (millions €)
- `home_momentum`: Team 1 momentum score
- `away_momentum`: Team 2 momentum score
- `home_attack_form`: Team 1 offensive form
- `away_attack_form`: Team 2 offensive form
- `home_defense_form`: Team 1 defensive form
- `away_defense_form`: Team 2 defensive form
- `is_friendly`: Match type (0 for tournament)

**Adjustments**:
```python
# Distance penalty
exp_goals_t1 -= (distance_t1 / 1000) * 0.05
exp_goals_t2 -= (distance_t2 / 1000) * 0.05

# Host advantage
if team1 == 'Morocco':
    exp_goals_t1 += 0.4
if team2 == 'Morocco':
    exp_goals_t2 += 0.4
```

---

## Data Structures

### `teams_data` Dictionary

**Structure**:
```python
{
    'Team Name': {
        'rank': int,              # FIFA ranking
        'points': float,          # FIFA points
        'market_value': float,    # Market value in millions €
        'momentum': int,          # Recent form indicator
        'att_form': float,        # Offensive form (goals/match)
        'def_form': float,        # Defensive form (goals conceded/match)
        'is_host': bool           # True for Morocco
    }
}
```

**Example**:
```python
{
    'Morocco': {
        'rank': 13,
        'points': 1676.12,
        'market_value': 245.5,
        'momentum': 15,
        'att_form': 2.20,
        'def_form': 0.80,
        'is_host': True
    }
}
```

---

### `groups` Dictionary

**Structure**:
```python
{
    'Group Letter': [team1, team2, team3, team4]
}
```

**Example**:
```python
{
    'A': ['Morocco', 'Mali', 'Zambia', 'Comoros'],
    'B': ['Egypt', 'South Africa', 'Angola', 'Zimbabwe'],
    # ... more groups
}
```

---

### `FLAG_CODES` Dictionary

**Structure**:
```python
{
    'Team Name': 'ISO_COUNTRY_CODE'
}
```

**Example**:
```python
{
    'Morocco': 'MA',
    'Egypt': 'EG',
    'Nigeria': 'NG',
    # ... more teams
}
```

---

### `capitals` Dictionary

**Structure**:
```python
{
    'Team Name': (latitude, longitude)
}
```

**Example**:
```python
{
    'Morocco': (34.0209, -6.8416),
    'Egypt': (30.0444, 31.2357),
    # ... more capitals
}
```

---

## Internal Functions (Not Exposed)

### `play_knockout(t1, t2, stage_name)`

**Purpose**: Simulate a knockout match with penalty shootout for draws.

**Location**: Inside Tab 3 (Single Simulation)

**Parameters**:
- `t1` (str): First team
- `t2` (str): Second team
- `stage_name` (str): Stage description (not used, legacy)

**Returns**: str - Winning team name

**Logic**:
```python
s1, s2, _, _ = predict_match(t1, t2)
if s1 == s2:
    winner = t1 if np.random.rand() > 0.5 else t2  # Penalty shootout
else:
    winner = t1 if s1 > s2 else t2
return winner
```

---

### `simulate_group_stage()`

**Purpose**: Simulate all group stage matches.

**Location**: Inside Tab 4 (Monte Carlo)

**Returns**: Tuple of (standings, thirds)
- `standings`: Dict with qualified teams per group
- `thirds`: List of third-placed teams with stats

**Example Output**:
```python
standings = {
    'A': {'1': 'Morocco', '2': 'Mali', '3': 'Zambia'},
    'B': {'1': 'Egypt', '2': 'South Africa', '3': 'Angola'},
    # ...
}

thirds = [
    {'t': 'Zambia', 'g': 'A', 'p': 4, 'd': 2, 'f': 5},
    {'t': 'Angola', 'g': 'B', 'p': 4, 'd': 1, 'f': 4},
    # ...
]
```

---

### `simulate_knockout(standings, thirds)`

**Purpose**: Simulate knockout rounds and determine champion.

**Location**: Inside Tab 4 (Monte Carlo)

**Parameters**:
- `standings`: Group stage results
- `thirds`: Third-placed teams

**Returns**: str - Champion team name

**Side Effect**: Updates `knockout_stats` dictionary

---

## Model Details

### Random Forest Models

**Algorithm**: Random Forest Regressor (scikit-learn)

**Training Data**: Historical African football matches

**Input Features**: 10 features per match
1. rank_diff
2. points_diff
3. market_value_diff
4. home_momentum
5. away_momentum
6. home_attack_form
7. away_attack_form
8. home_defense_form
9. away_defense_form
10. is_friendly

**Output**: Continuous value (expected goals)

**Performance**:
- MAE: 0.842 goals
- Accuracy: 54.49% (predicting win/draw/loss)

**Prediction Process**:
```python
# Create feature DataFrame
X = pd.DataFrame([[...]], columns=[...])

# Predict expected goals
exp_goals_home = model_home.predict(X)[0]
exp_goals_away = model_away.predict(X)[0]

# Apply adjustments
exp_goals_home = adjust_for_distance_and_host(exp_goals_home, team_home)
exp_goals_away = adjust_for_distance_and_host(exp_goals_away, team_away)

# Generate actual score using Poisson
score_home = np.random.poisson(max(0.05, exp_goals_home))
score_away = np.random.poisson(max(0.05, exp_goals_away))
```

---

## Using the Prediction System in Your Code

### Basic Prediction

```python
import pickle
import pandas as pd
import numpy as np

# Load models
with open('model_home.pkl', 'rb') as f:
    model_home = pickle.load(f)
with open('model_away.pkl', 'rb') as f:
    model_away = pickle.load(f)
with open('teams_data.pkl', 'rb') as f:
    teams_data = pickle.load(f)

# Predict a match
def predict(team1, team2):
    t1 = teams_data[team1]
    t2 = teams_data[team2]
    
    # Create features
    X = pd.DataFrame([[
        t1['rank'] - t2['rank'],
        t1['points'] - t2['points'],
        t1['market_value'] - t2['market_value'],
        t1['momentum'], t2['momentum'],
        t1['att_form'], t2['att_form'],
        t1['def_form'], t2['def_form'],
        0
    ]], columns=['rank_diff', 'points_diff', 'market_value_diff',
                 'home_momentum', 'away_momentum',
                 'home_attack_form', 'away_attack_form',
                 'home_defense_form', 'away_defense_form', 'is_friendly'])
    
    # Predict
    exp1 = model_home.predict(X)[0]
    exp2 = model_away.predict(X)[0]
    
    # Generate score
    s1 = np.random.poisson(max(0.05, exp1))
    s2 = np.random.poisson(max(0.05, exp2))
    
    return s1, s2

# Example
score1, score2 = predict("Morocco", "Egypt")
print(f"Morocco {score1} - {score2} Egypt")
```

---

### Monte Carlo Analysis

```python
def monte_carlo(n_simulations=1000):
    win_count = {team: 0 for team in teams_data.keys()}
    
    for _ in range(n_simulations):
        # Simulate tournament
        champion = simulate_tournament()
        win_count[champion] += 1
    
    # Calculate probabilities
    probabilities = {
        team: (count / n_simulations) * 100
        for team, count in win_count.items()
    }
    
    return probabilities

# Run analysis
probs = monte_carlo(1000)
print(f"Morocco: {probs['Morocco']:.2f}%")
```

---

## Extending the System

### Adding New Features

To add a new feature to predictions:

1. **Update data collection** in notebook
2. **Add feature to `teams_data`**
3. **Retrain models** with new feature
4. **Update `predict_match()` function**
5. **Test thoroughly**

### Example: Adding "Home Support" Feature

```python
# In predict_match()
support_diff = t1.get('home_support', 0) - t2.get('home_support', 0)

X_input = pd.DataFrame([[
    # ... existing features ...
    support_diff  # New feature
]], columns=[
    # ... existing columns ...
    'support_diff'  # New column
])
```

---

### Creating a REST API

To expose predictions as a REST API:

```python
from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

# Load models at startup
model_home = pickle.load(open('model_home.pkl', 'rb'))
model_away = pickle.load(open('model_away.pkl', 'rb'))
teams_data = pickle.load(open('teams_data.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.json
    team1 = data['team1']
    team2 = data['team2']
    
    s1, s2, exp1, exp2 = predict_match(team1, team2)
    
    return jsonify({
        'team1': team1,
        'team2': team2,
        'score1': int(s1),
        'score2': int(s2),
        'expected1': float(exp1),
        'expected2': float(exp2)
    })

if __name__ == '__main__':
    app.run(debug=True)
```

**Usage**:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"team1": "Morocco", "team2": "Egypt"}'
```

---

## Performance Considerations

### Optimization Tips

1. **Cache model loading**: Use `@st.cache_resource`
2. **Vectorize predictions**: Batch multiple predictions
3. **Reduce simulations**: Use 100-1000 for development
4. **Profile code**: Identify bottlenecks
5. **Use NumPy**: Replace Python loops

### Benchmark

**Single prediction**: ~1ms
**100 simulations**: ~100ms
**Full tournament**: ~500ms
**Monte Carlo (1000)**: ~5 minutes

---

## Error Handling

### Common Errors

**Missing team data**:
```python
t1 = teams_data.get(team1)
if t1 is None:
    raise ValueError(f"Team {team1} not found")
```

**Invalid inputs**:
```python
if team1 == team2:
    raise ValueError("Teams must be different")
```

**Model file missing**:
```python
try:
    with open('model_home.pkl', 'rb') as f:
        model_home = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found!")
```

---

## Testing

### Unit Tests

```python
def test_predict_match():
    s1, s2, exp1, exp2 = predict_match("Morocco", "Egypt")
    
    assert isinstance(s1, (int, np.integer))
    assert isinstance(s2, (int, np.integer))
    assert s1 >= 0 and s2 >= 0
    assert exp1 > 0 and exp2 > 0

def test_get_distance():
    d = get_distance_rabat("Morocco")
    assert d == 0  # Same city
    
    d = get_distance_rabat("Egypt")
    assert 3000 < d < 3500  # Approximate distance
```

---

## Future API Enhancements

### Planned Features

1. **Batch predictions**: Predict multiple matches at once
2. **Historical data**: Query past predictions
3. **Live updates**: Real-time odds
4. **WebSocket**: Streaming predictions
5. **Authentication**: API key management
6. **Rate limiting**: Prevent abuse
7. **Caching**: Store frequent predictions
8. **Versioning**: Multiple model versions

---

## Support

For API-related questions:
- Check this documentation
- Review example code
- Create GitHub issue
- Contact maintainers

---

**Happy coding! ⚽🔧**
