import streamlit as st
import pandas as pd
import joblib

# Load models
models = {
    'QB': joblib.load('./models/best_model_qb.pkl'),
    'RB': joblib.load('./models/best_model_rb.pkl'),
    'WR': joblib.load('./models/best_model_wr.pkl'),
    'TE': joblib.load('./models/best_model_te.pkl')
}

# Load test datasets
test_data = {
    'QB': joblib.load('./data/processed/test_qb.pkl'),
    'RB': joblib.load('./data/processed/test_rb.pkl'),
    'WR': joblib.load('./data/processed/test_wr.pkl'),
    'TE': joblib.load('./data/processed/test_te.pkl')
}

# Define feature columns used in models
feature_cols = {
    'QB': [col for col in test_data['QB'].columns if col not in ['player_id', 'player_display_name', 'position', 'season', 'recent_team', 'fantasy_points_ppr_per_game']],
    'RB': [col for col in test_data['RB'].columns if col not in ['player_id', 'player_display_name', 'position', 'season', 'recent_team', 'fantasy_points_ppr_per_game']],
    'WR': [col for col in test_data['WR'].columns if col not in ['player_id', 'player_display_name', 'position', 'season', 'recent_team', 'fantasy_points_ppr_per_game']],
    'TE': [col for col in test_data['TE'].columns if col not in ['player_id', 'player_display_name', 'position', 'season', 'recent_team', 'fantasy_points_ppr_per_game']]
}

st.title("Fantasy Football Player PPG Predictor")

# User inputs
position = st.selectbox("Select Position", ["QB", "RB", "WR", "TE"])
mode = st.radio("Mode", ["Full Rankings Only", "Search for Player & Show Rankings"])

player = None
if mode == "Search for Player & Show Rankings":
    player = st.selectbox("Select Player", test_data[position]['player_display_name'].sort_values())

if st.button("Get Rankings"):
    df = test_data[position]
    model = models[position]

    # Generate predictions
    preds = pd.DataFrame({
        'player_display_name': df['player_display_name'],
        'predicted_fantasy_ppg': model.predict(df[feature_cols[position]])
    })

    # Round predicted PPG
    preds['predicted_fantasy_ppg'] = preds['predicted_fantasy_ppg'].round(1)

    # Rank players
    preds['rank'] = preds['predicted_fantasy_ppg'].rank(method='min', ascending=False).astype(int)

    # Sort by rank
    preds_sorted = preds.sort_values('rank').reset_index(drop=True)

    # Rename columns
    display_df = preds_sorted[['rank', 'player_display_name', 'predicted_fantasy_ppg']].copy()
    display_df.columns = ['Rank', 'Name', 'Predicted PPG (PPR)']

    if player:
        # Find player index
        player_idx = display_df[display_df['Name'] == player].index[0]

        # Slice table to show 10 rows above, 15 rows below (more scroll)
        start_idx = max(player_idx - 10, 0)
        end_idx = min(player_idx + 15, len(display_df))
        display_slice = display_df.iloc[start_idx:end_idx].copy()

        # Highlight selected player by text style instead of background
        def highlight_player(row):
            return ['font-weight: bold; color: #1155cc;' if row['Name'] == player else '' for _ in row]

        st.dataframe(display_slice.style.apply(highlight_player, axis=1))

        # Show selected player's info
        player_pred = display_df.loc[player_idx]
        st.write(f"**{player}** predicted PPG (PPR): {player_pred['Predicted PPG (PPR)']:.1f}")
        st.write(f"Predicted Rank: {player_pred['Rank']}")
    else:
        # Full rankings
        st.dataframe(display_df, height=500)











