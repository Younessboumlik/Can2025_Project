# 📖 CAN 2025 Predictor - Usage Guide

This guide provides detailed instructions on how to use all features of the CAN 2025 Predictor application.

## 🚀 Getting Started

### Launching the Application

1. **Open your terminal/command prompt**
2. **Navigate to the project directory**:
   ```bash
   cd Can2025_Project
   ```
3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```
4. **Access the app** in your browser at `http://localhost:8501`

### Interface Overview

The application has 5 main tabs:
- 🎯 **Match Unique** - Predict single matches
- 🏆 **Groupes** - View tournament groups
- 🎲 **Simulation Unique** - Full tournament simulation
- 📊 **Monte Carlo** - Statistical analysis
- 📈 **Stats Équipes** - Team statistics

---

## 🎯 Tab 1: Match Unique (Single Match Prediction)

### Purpose
Predict the outcome of a single match between any two teams in the tournament.

### How to Use

1. **Select Team 1** from the left dropdown
2. **Select Team 2** from the right dropdown
3. **Click "🔮 Prédire"** button

### Results Interpretation

The app will show:

#### Win Probabilities
- **Team 1 Win Percentage**: Probability that Team 1 wins
- **Draw Percentage**: Probability of a draw
- **Team 2 Win Percentage**: Probability that Team 2 wins

These are calculated from 100 simulated matches.

#### Predicted Score
- Shows the average score from all simulations
- Format: `Team1 X.X - X.X Team2`
- Includes team flags for visual identification

### Example Usage

**Scenario**: Predicting Morocco vs Egypt

1. Select "Morocco" as Team 1
2. Select "Egypt" as Team 2
3. Click "🔮 Prédire"

**Sample Output**:
```
Morocco gagne: 45%
Match Nul: 25%
Egypt gagne: 30%

Score Prédit: 🇲🇦 Morocco 1.8 - 1.4 Egypt 🇪🇬
```

**Interpretation**: Morocco has a 45% chance of winning, with an expected score around 2-1.

### Tips
- Compare teams with similar rankings for closer matches
- Host nation (Morocco) gets a slight advantage
- Consider checking team stats first in Tab 5

---

## 🏆 Tab 2: Groupes (Tournament Groups)

### Purpose
View the official CAN 2025 group stage organization and team rankings.

### Information Displayed

For each of the 6 groups (A-F):
- **Team names** with country flags
- **FIFA rankings** for each team
- **Group structure** as per official draw

### Groups Overview

**Group A**: Morocco (Host), Mali, Zambia, Comoros
**Group B**: Egypt, South Africa, Angola, Zimbabwe
**Group C**: Nigeria, Tunisia, Uganda, Tanzania
**Group D**: Senegal, DR Congo, Benin, Botswana
**Group E**: Algeria, Burkina Faso, Equatorial Guinea, Sudan
**Group F**: Ivory Coast, Cameroon, Gabon, Mozambique

### How to Use

- **Simply view** the groups - no interaction needed
- **Compare rankings** within groups to identify favorites
- **Plan predictions** based on group matchups

### Use Cases

1. **Identify group favorites**: Look for lowest FIFA rankings
2. **Spot upsets**: Find potential underdogs
3. **Understand tournament structure**: See who plays whom
4. **Compare groups**: Assess "group of death" vs easier groups

---

## 🎲 Tab 3: Simulation Unique (Full Tournament Simulation)

### Purpose
Simulate the entire CAN 2025 tournament from group stage to final.

### How to Use

1. **Click "🚀 Simuler le Tournoi"** button
2. **Wait for simulation** (takes 10-30 seconds)
3. **Review results** from top to bottom

### Simulation Process

The app simulates:

#### 1. Group Stage (Phase de Groupes)
- All 36 group matches
- Points allocation (3 for win, 1 for draw)
- Goal difference calculation
- Top 2 from each group qualify
- Best 4 third-placed teams qualify

**Sample Output**:
```
Groupe A
🇲🇦 Morocco 2-1 Mali 🇲🇱
🇿🇲 Zambia 1-1 Comoros 🇰🇲
...
Qualifiés: Morocco, Mali
```

#### 2. Round of 16 (Huitièmes de Finale)
- 8 knockout matches
- Penalty shootouts for draws (marked as TAB)

**Sample Output**:
```
🇲🇦 Morocco 2-1 Comoros 🇰🇲 → ✅ Morocco
🇪🇬 Egypt 1-1 Angola 🇦🇴 → Angola (TAB)
```

#### 3. Quarter-Finals (Quarts de Finale)
- 4 knockout matches
- Winners advance to semi-finals

#### 4. Semi-Finals (Demi-Finales)
- 2 knockout matches
- Winners advance to final

#### 5. Final (Finale)
- Championship match
- Winner is crowned champion
- Balloons celebration! 🎈

**Sample Output**:
```
🎉 CHAMPION: MOROCCO 🏆
```

### Tips
- Run multiple simulations to see different scenarios
- Note the "best third-placed teams" - this affects knockout pairings
- Watch for upsets in knockout rounds
- (TAB) indicates penalty shootouts

### Limitations
- Penalty shootouts are 50/50 random
- No third-place playoff included
- Single simulation - results vary each time

---

## 📊 Tab 4: Monte Carlo (Statistical Analysis)

### Purpose
Run thousands of simulations to calculate statistical probabilities for each team.

### How to Use

1. **Set number of simulations** (100-10,000)
   - 100: Quick preview
   - 1,000: Good balance (recommended)
   - 5,000: High accuracy
   - 10,000: Maximum precision

2. **Click "🚀 Lancer la simulation"**

3. **Wait for completion**
   - Progress bar shows status
   - Time varies: 1,000 sims ≈ 2-5 minutes

### Results Interpretation

#### Probability Table

Shows top 10 teams with:
- **Champion (%)**: Probability of winning the tournament
- **Finale (%)**: Probability of reaching the final
- **Demi (%)**: Probability of reaching semi-finals
- **Quart (%)**: Probability of reaching quarter-finals

**Sample Output**:
```
Équipe       | Champion | Finale | Demi   | Quart
-------------|----------|--------|--------|-------
Morocco      | 18.50%   | 35.20% | 52.40% | 68.30%
Senegal      | 12.30%   | 28.40% | 45.60% | 62.10%
Egypt        | 11.80%   | 26.70% | 43.20% | 60.50%
```

#### Key Metrics

Three highlighted teams:
- **🥇 Favori**: Most likely winner
- **🥈 Outsider**: Second favorite
- **🥉 Surprise**: Third favorite

### Interpretation Guide

**High Champion Probability (>15%)**
- Clear favorite
- Strong in all stages
- Consistent performance

**Medium Champion Probability (8-15%)**
- Competitive contender
- Good chance but not dominant
- Several teams at this level

**Low Champion Probability (<8%)**
- Underdog
- May advance but unlikely to win
- Potential for surprises

### Example Analysis

**Scenario**: Morocco shows 18.5% champion probability

**Interpretation**:
- Morocco is the favorite
- But only 1 in 5 chance to win
- Tournament is highly competitive
- Other teams have realistic chances

### Use Cases

1. **Tournament Preview**: Before tournament starts
2. **Betting Insights**: Identify value picks (not recommended for gambling)
3. **Group Analysis**: Which groups have strongest teams
4. **Upset Potential**: Compare predictions to reality
5. **Strategic Planning**: Fantasy league selections

### Tips
- **More simulations = more accurate** but slower
- **Compare top teams**: Small differences suggest competitive balance
- **Check all stages**: Some teams peak early or late
- **Rerun occasionally**: As tournament progresses (if updating data)

---

## 📈 Tab 5: Stats Équipes (Team Statistics)

### Purpose
View detailed statistics and metrics for individual teams.

### How to Use

1. **Select a team** from the dropdown menu
2. **View comprehensive statistics**

### Metrics Explained

#### Top Row Metrics

**🏅 Rang FIFA (FIFA Ranking)**
- Lower = better (e.g., rank 10 > rank 50)
- Updated from FIFA official rankings
- Major factor in predictions

**⚡ Points FIFA (FIFA Points)**
- Numerical points assigned by FIFA
- Accumulated from recent matches
- Higher = stronger team

**💰 Valeur (Market Value)**
- Total squad value in millions of euros
- From Transfermarkt database
- Indicates team quality and investment

**📈 Momentum**
- Recent form indicator
- Positive = improving, Negative = declining
- Based on last 5-10 matches

#### Form Metrics

**🎯 Forme Offensive (Offensive Form)**
- Average goals scored per match
- Based on recent 5 matches
- Progress bar visualization
- Higher = more attacking threat

**🛡️ Forme Défensive (Defensive Form)**
- Average goals conceded per match
- Based on recent 5 matches
- Progress bar visualization
- Lower = better defense

### Example Analysis

**Morocco Statistics**:
```
Rang FIFA: 13
Points FIFA: 1676
Valeur: 245.5 M€
Momentum: +15

Forme Offensive: 2.20 buts/match
Forme Défensive: 0.80 buts/match
```

**Interpretation**:
- **Strong team**: Top 15 FIFA ranking
- **High value**: Expensive, quality players
- **Positive momentum**: Recently improving
- **Good offense**: Scoring 2+ goals per match
- **Solid defense**: Conceding less than 1 goal per match
- **Prediction**: Likely to perform well in tournament

### Comparison Strategy

To compare two teams:
1. **Check rankings**: Lower rank usually favored
2. **Compare momentum**: Positive trend is advantage
3. **Assess forms**: Balance of offense/defense
4. **Consider value**: Higher usually means better squad
5. **Make prediction**: Use Tab 1 for simulation

### Tips
- **Use before predictions**: Understand team strength
- **Compare opponents**: Check both teams' stats
- **Track momentum**: Recent form matters
- **Consider balance**: Strong offense + defense = best teams

---

## 🎓 Advanced Usage

### Scenario Analysis

**Question**: "Who would win: Morocco vs Senegal?"

**Process**:
1. **Tab 5**: Check both teams' stats
   - Morocco: Rank 13, Momentum +15
   - Senegal: Rank 20, Momentum +8
2. **Tab 1**: Run prediction
   - Result: Morocco 45%, Draw 25%, Senegal 30%
3. **Tab 4**: Check long-term probabilities
   - Morocco: 18% to win tournament
   - Senegal: 12% to win tournament
4. **Conclusion**: Morocco favored but competitive match

### Tournament Strategy

**For Fantasy Leagues**:
1. **Tab 4**: Identify teams likely to advance far
2. **Tab 5**: Select players from high-scoring teams
3. **Tab 2**: Pick from weaker groups for easier paths
4. **Tab 3**: Run simulations to spot consistent performers

### Data Analysis

**Understanding the Model**:
- Predictions combine multiple factors
- Not deterministic - includes randomness
- Based on historical patterns
- More accurate for favorites than underdogs

---

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

---

## 💡 Best Practices

### For Accurate Predictions
- Use Monte Carlo with 1,000+ simulations
- Check team stats before predicting
- Run multiple single simulations
- Consider recent news/injuries (not in model)

### For Fast Results
- Use single match predictions
- Keep Monte Carlo simulations under 1,000
- Close unused tabs
- Run one prediction at a time

### For Entertainment
- Try impossible matchups
- Run multiple tournament simulations
- Compare with friends' predictions
- Track accuracy during real tournament

---

## 📞 Support

Need help?
- Check README.md for setup issues
- Review this guide for usage questions
- Create an issue on GitHub for bugs
- Refer to CONTRIBUTING.md for development

---

**Enjoy using CAN 2025 Predictor! ⚽🏆**
