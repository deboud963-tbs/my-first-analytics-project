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

# Convert pickup_time and dropoff_time to datetime format
trips_merged['pickup_time'] = pd.to_datetime(trips_merged['pickup_time'])
trips_merged['dropoff_time'] = pd.to_datetime(trips_merged['dropoff_time'])

# Create a new column 'pickup_date' containing only the date from 'pickup_time'
trips_merged['pickup_date'] = trips_merged['pickup_time'].dt.date

# Sidebar filter for car brand
car_brands = trips_merged['brand'].unique()  # Get unique car brands from the DataFrame
selected_brands = st.sidebar.multiselect("Select Car Brand(s)", car_brands)

# Filter the DataFrame based on selected car brands
if selected_brands:
    trips_merged = trips_merged[trips_merged['brand'].isin(selected_brands)]

# Sidebar filter for car model (dependent on selected brands)
car_models = trips_merged['model'].unique()  # Get unique car models from the filtered DataFrame
selected_models = st.sidebar.multiselect("Select Car Model(s)", car_models)

# Filter the DataFrame based on selected car models
if selected_models:
    trips_merged = trips_merged[trips_merged['model'].isin(selected_models)]

# Compute business performance metrics
total_trips = len(trips_merged)  # Total number of trips

# Car model with the highest revenue
top_car = trips_merged.groupby('model')['revenue'].sum().idxmax()

# Total Distance across all trips
total_distance = trips_merged['distance'].sum()

# Display metrics in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Trips", value=total_trips)

with col2:
    st.metric(label="Top Car Model by Revenue", value=top_car)

with col3:
    st.metric(label="Total Distance (km)", value=f"{total_distance:,.2f}")

#Preview the contents of your dataframe
st.write("### Preview of the dataframe : ")
st.dataframe( trips_merged.head())

#Visualizations
st.title("Car Sharing Data Dashboard")
#Trips over time
st.subheader("Trips over time : ")
trips_over_time = trips_merged.groupby('pickup_date').size().reset_index(name="Number of Trips")
st.write(trips_over_time)
st.line_chart(trips_over_time, x="pickup_date", y="Number of Trips")
#Cumulative Revenue Growth Over Time
st.subheader("Cumulative Revenue Growth Over Time : ")
revenue_over_time = trips_merged.groupby('pickup_date')['revenue'].sum().cumsum()
st.write(revenue_over_time)
st.area_chart(revenue_over_time)
#Number of Trips Per Car Model
st.subheader("Number of Trips Per Car Model : ")
trips_car_model = trips_merged["model"].value_counts()
st.write(trips_car_model)
st.bar_chart(trips_car_model)
#Revenue By City
st.subheader("Revenue By City : ")
revenue_by_city = trips_merged.groupby("city_name")['revenue'].sum().sort_values(ascending=False)
st.write(revenue_by_city )
st.bar_chart(revenue_by_city )






