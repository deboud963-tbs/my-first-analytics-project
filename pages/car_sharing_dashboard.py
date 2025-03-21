import streamlit as st 
import pandas as pd 

# Function to load CSV files into dataframes
@st.cache_data
def load_data():
    trips = pd.read_csv("dataset/trips.csv") 
    cars = pd.read_csv("dataset/cars.csv") 
    cities = pd.read_csv("dataset/cities.csv") 
    return trips, cars, cities 
#Load and store
trips_df, cars_df, cities_df = load_data()

# Merge trips with cars (joining on car_id)
trips_merged = trips_df.merge(cars_df, left_on='car_id', right_on='id', how='left')

# Merge trips_merged with cities_df
trips_merged = trips_merged.merge(cities_df, left_on='city_id', right_on='city_id', how='left')

# Clean up unnecessary columns
trips_merged = trips_merged.drop(columns=['id_x', 'id_y', 'car_id', 'customer_id'])


