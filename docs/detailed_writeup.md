# Fantasy Football Player Performance Predictor: Project Write-up

## Introduction  
Predicting fantasy football performance is inherently noisy due to factors like team changes, role adjustments, injuries, and competition from teammates. This project uses machine learning to provide data-driven projections for player fantasy points per game (PPG), helping fantasy managers, analysts, and enthusiasts make more informed decisions. By combining historical performance data with contextual features, the model forecasts each player’s PPR fantasy output for the following season.

---

## Project Motivation  
Fantasy football rankings can often rely on subjective opinions or simplified projections. A predictive model provides a more objective, quantitative framework, identifying which stats and features truly correlate with future performance. This can guide player drafting, roster decisions, and overall strategy.

---

## Data Collection and Preparation  

## Data Collection
The data for this project was obtained from publicly available NFL datasets, which provide comprehensive player and season-level statistics. The datasets can be accessed [here](https://github.com/nflverse/nflverse-data/releases/tag/stats_player) and they included:  
- **Player information:** Name, position, rookie season  
- **Season summary stats:** Season, team, Games played, passing/rushing/receiving stats, touchdowns, targets/receptions, and advanced metrics

### Dataset Scope  
- The combined dataset includes 5,815 player-season records spanning 2015–2024.  
- Separate position-specific datasets were created (# of observations and columns are after cleaning and filtering):  
  - **Quarterbacks (QB):** 291 observations, 27 columns  
  - **Running Backs (RB):** 727 observations, 29 columns  
  - **Wide Receivers (WR):** 1,199 observations, 28 columns  
  - **Tight Ends (TE):** 610 observations, 23 columns  

### Data Cleaning  
- Filtered to only include skill positions (QB, RB, WR, TE)  
- Removed rows for players with fewer than 8 games in a season  
- Addressed players retiring by dropping rows where the next season’s fantasy points were unavailable  
- Merged player info from multiple CSVs to create a complete dataset with consistent features

### Feature Engineering  
- Converted season stats to per-game stats (e.g., rushing yards per game)  
- Added `years_of_experience` based on draft season  
- Added a binary feature `new_team_next_year` for team switches  
- Created target variable: `fantasy_points_ppr_per_game_next_year`  

---

## Modeling Approach  

### Data Preprocessing  
- Split the data into train (2015–2023), test (2024), and validation sets (20% of training set)  
- Scaled features for models that required it  

### Baseline Models  
- Tested multiple machine learning models, including Linear Regression, Ridge, Lasso, XGBoost, and Random Forest Regressor  
- Randomized search with cross-validation (50 iterations, 5-fold CV) was used for hyperparameter tuning

### Handling Edge Cases  
- Players who played fewer than 8 games in a season were excluded  
- Predictions are only made for consecutive seasons where the target variable exists  

### Model Selection  
Final models were chosen for each position based on lowest cross-validated RMSE:  

| Position | Model | CV RMSE |
|----------|-------|---------|
| QB       | Ridge | 3.690   |
| RB       | Ridge | 3.963   |
| WR       | Ridge | 3.291   |
| TE       | Lasso | 2.650   |

Once models were selected, preprocessing and feature scaling were finalized for evaluation.

---

## Evaluation and Results  

### Metrics  
Models were evaluated on the validation set using:  
- RMSE (Root Mean Squared Error)  
- MAE (Mean Absolute Error)  
- R²  

### Validation Set Performance  

**Quarterbacks (QB):**  
- **Model:** Ridge Regression  
- **RMSE:** 3.53  
- **MAE:** 2.51  
- **R²:** 0.112  

**Running Backs (RB):**  
- **Model:** Ridge Regression  
- **RMSE:** 3.85  
- **MAE:** 3.08  
- **R²:** 0.517  

**Wide Receivers (WR):**  
- **Model:** Ridge Regression  
- **RMSE:** 3.31  
- **MAE:** 2.66  
- **R²:** 0.614  

**Tight Ends (TE):**  
- **Model:** Lasso Regression  
- **RMSE:** 2.74  
- **MAE:** 2.01  
- **R²:** 0.521  

---

## Deployment: Streamlit Web Application  

### App Overview  
A Streamlit app was built to allow users to view fantasy projections and interact with the models. Users can search for a player or view full position rankings for the upcoming season.

### User Experience  
The interface is intuitive, displaying predicted PPR fantasy points per game along with player ranking for the selected position. 

### Technical Details  
- Models and preprocessing pipelines were serialized for use in the app  
- App deployed via Streamlit Cloud: [Fantasy Football Predictor App](https://fantasy-football-rankings-predictor.streamlit.app)  

---

## Challenges and Lessons Learned  

- **Noisy outcomes:** Fantasy football performance is influenced by unpredictable factors; modeling consecutive seasons helps mitigate noise.  
- **Data preprocessing:** Filtering low-game seasons and merging multiple sources ensured a cleaner dataset.  
- **Feature selection:** Adding years of experience and team switch indicators improved predictions modestly, while future teammate average PPG features did not enhance model performance.  
- **Deployment experience:** Building a Streamlit app provided experience in presenting models to end users.

---

## Future Directions  

- Incorporate injury histories and projected playing time  
- Explore deep learning models to capture nonlinear relationships  
- Automate live data pulls during the NFL season for dynamic predictions  
- Add model explainability tools (SHAP, LIME) for transparency

---

## Tools & Technologies  
- **Python:** pandas, scikit-learn, matplotlib, seaborn  
- **Modeling:** Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting  
- **Deployment:** Streamlit  
- **Version Control:** GitHub  

---

## How to Use This Project  

1. Explore the Jupyter notebooks to follow the full data pipeline  
2. Run the Streamlit app locally (`app.py`) or access the deployed version  
3. Use as a foundation for further experimentation or integration into fantasy analytics workflows

---

## Author  
**Jack Ewings**

### Connect with me
[LinkedIn](https://www.linkedin.com/in/jack-ewings-profile/) | [GitHub](https://github.com/jackewings) | [Portfolio](https://jackewings.github.io)


