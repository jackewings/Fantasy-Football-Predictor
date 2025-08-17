# Fantasy Football Player Performance Predictor

## Overview

This project builds machine learning models to predict position-specific PPR fantasy football points per game for the following season. Using historical player statistics and contextual features like team changes and experience, the model provides data-driven projections to support fantasy managers, analysts, and enthusiasts.

## Motivation

Fantasy football rankings can often rely on subjective opinions. This project applies machine learning to create a more objective framework for forecasting player performance, highlighting which factors influence future outcomes and helping guide drafting and roster decisions.

## Data

The dataset includes player-season stats from 2015–2024, covering passing, rushing, receiving, touchdowns, targets, and advanced metrics. Data is cleaned and processed to produce one observation per player per season, including features like years of experience and team switches.

## Approach

- **Data Preparation:** Cleaning, filtering low-game seasons, and feature engineering to produce relevant inputs.  
- **Modeling:** Tested multiple regression models (Linear, Ridge, Lasso, Random Forest, XGBoost) with hyperparameter tuning via randomized search.  
- **Validation:** Models evaluated using RMSE, MAE, and R² on a held-out validation set.  
- **Final Models:** Selected based on lowest cross-validated RMSE for each position.

## Results

The models produced reasonable projections given the inherent variability of fantasy football outcomes. Ridge regression performed best for QBs, RBs, and WRs, while Lasso performed best for TEs. Detailed evaluation metrics are available in the notebooks and in the `detailed_writeup` file.

## Web App

A Streamlit web app allows users to view projections by player or position, displaying predicted PPR fantasy PPG for the upcoming season.

Try it out here: [Fantasy Football Predictor App](https://fantasy-football-rankings-predictor.streamlit.app)

## Project Structure

- `data/` – Raw and cleaned NFL datasets  
- `docs/` – Project write-up  
- `models/` – Serialized models and preprocessing pipelines  
- `notebooks/` – Notebooks for EDA, feature engineering, and modeling  
- `.gitignore` – Excluded files  
- `README.md` – Project overview and usage instructions  
- `app.py` – Streamlit app script  
- `requirements.txt` – Python dependencies  

## How to Use

1. Explore the notebooks for a full walkthrough of the modeling process.  
2. Run the Streamlit app locally (`app.py`) or access the deployed version.  
3. Use the project as a foundation for fantasy football analytics and experimentation.

---

*Created by Jack Ewings*

### Connect with me

[LinkedIn](https://www.linkedin.com/in/jack-ewings-profile/) | [GitHub](https://github.com/jackewings) | [Portfolio](https://jackewings.github.io)
