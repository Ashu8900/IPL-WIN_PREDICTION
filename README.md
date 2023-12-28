# IPL-WIN_PREDICTION

## Overview
IPL Match Predictor is a Machine Learning-based prediction approach that utilizes various factors to predict the outcome of Indian Premier League (IPL) matches. The model is trained on comprehensive datasets, incorporating key dimensions such as Toss, Home Ground, Captains, Favourite Players, Opposition Battle, and Previous Stats. Different factors are assigned varying strengths through column transformation, Logistic Regression, and a well-structured pipeline. The web application is built using the Flask framework, and Streamlit was employed to create the user interface.

## Features
**Toss**: The model takes into account the outcome of the toss, considering its impact on match results.
**Home Ground**: Home advantage is factored in, recognizing the influence of playing on familiar turf.
**Captains**: The performance of team captains is considered, as their decisions can significantly affect match outcomes.
**Favorite Players**: The presence and performance of key players, termed "favorite players," are incorporated into the model.
**Opposition Battle**: Historical data on team matchups is used to gauge the performance against specific opponents.
**Previous Stats**: Team and player statistics from previous matches contribute to the overall prediction model.

## Model Implementation
The model implementation involves the following steps:
* **Data Collection**: Comprehensive datasets covering various dimensions are gathered to train the model.
* **Data Preprocessing**: The collected data undergoes preprocessing to clean and organize it for effective training.
* **Column Transformation**: Different factors are assigned varying strengths through column transformation, optimizing their impact on predictions.
* **Logistic Regression**: The model employs Logistic Regression, a machine-learning algorithm suitable for binary classification tasks.
* **Pipeline Creation**: A well-structured pipeline is designed to streamline the entire prediction process.

## Web Application
The model is integrated into a user-friendly web application using the Flask framework. Streamlit is utilized to create an intuitive and interactive interface for users to input match details and receive predictions.

## Getting Started
1. Clone the repository
2. Install dependencies
3. Run the streamlit file (app.py)

## Usage
1. Open the web application in your browser.
2. Input match details of Teams, stadium, Target, Current score, Overs Left, Wicket Left
3. Click the "Predict" button to receive the model's prediction for the match outcome.
