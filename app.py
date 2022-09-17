import streamlit as st
import pickle
import pandas as pd

teams = {'Chennai Super Kings',
         'Delhi Capitals',
         'Gujarat Titans',
         'Kolkata Knight Riders',
         'Lucknow Super Giants',
         'Mumbai Indians',
         'Punjab Kings',
         'Rajasthan Royals',
         'Royal Challengers Bangalore',
         'Sunrisers Hyderabad'}

cities = ['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
          'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
          'Visakhapatnam', 'Bengaluru', 'Jaipur', 'Bangalore', 'Raipur',
          'Ranchi', 'Cuttack', 'Nagpur', 'Johannesburg', 'Centurion',
          'Durban', 'Bloemfontein', 'Port Elizabeth', 'Kimberley',
          'East London', 'Cape Town']

st.title("IPL Win Predictor")

col1, col2 = st.columns(2)

pipe = pickle.load(open('pipe.pkl', 'rb'))

with col1:
    batting_team = st.selectbox("Select The Batting team", sorted(teams))

with col2:
    bowling_team = st.selectbox("Select The Bowling team", sorted(teams))

if batting_team != bowling_team:
    selected_city = st.selectbox("Select City ", sorted(cities))

    target = st.number_input('Tagret')

    col3, col4, col5 = st.columns(3)

    with col3:
        score = st.number_input('score')

    with col4:
        overs = st.number_input('overs')

    with col5:
        wickets = st.number_input('wickets out')

    if st.button('Predict Probability'):
        runs_left = target - score
        ball_left = 120 - (overs * 6)
        wickets = 10 - wickets
        crr = score / overs
        rrr = (runs_left * 6) / ball_left

        input_df = pd.DataFrame({'Team1': [batting_team], 'Team2': [bowling_team], 'City': [selected_city], 'runs_left': [runs_left],
                                 'ball_left': [ball_left], 'wickets': [wickets], 'total_run_x': [score], 'crr': [crr], 'rrr': [rrr]})

        st.table(input_df)
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]
        st.header(batting_team + "-" + str(round(win*100)) + "%")
        st.header(bowling_team + "-" + str(round(loss*100)) + "%")
