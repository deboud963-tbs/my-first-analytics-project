import streamlit as st

st.title("My Streamlit Web App")
st.write("This is a content to start with")

#Contents in a sidebar
with st.sidebar:
    st.header("This is a sidebar Section")
    user_input = st.text_input("Enter your name")
    option = st.selectbox("Choose an option", ["Choice A", "Choice B", "Choice C"])

#Contents in the main window
st.header("This is the main section")
#Display user input
st.write(f"Hello, {user_input}! You selected option {option}.")

#Adding Contents in multiple columns
col1, col2 = st.columns(2)
with col1:
    st.subheader("Column 1")
    st.button("Click me!")
    st.write("This is some text in column 1")
with col2:
    st.subheader("Column 2")
    st.line_chart({"data":[1,5,2,6,2,1]})

#Expandable section
with st.expander("See explanation"):
    st.write("This is an expandable section with additional information.")


import streamlit as st
import pandas as pd
import numpy as np

st.title("Manipulate Streamlit Chart")

#Generate random data
bar_data = pd.DataFrame(np.random.randn(20,3), columns = ["a", "b", "c"])
st.bar_chart(bar_data)

#Generate random data for line chart
line_data = pd.DataFrame(np.random.randn(20,3), columns=["a","b","c"])
st.line_chart(line_data)

#Generate random data for scatter chart
chart_data = pd.DataFrame(np.random.randn(20,3), columns = ["a","b","c"])
st.scatter_chart(chart_data)


import streamlit as st
import pandas as pd

st.title("CSV File Uploader")



df1000 = pd.read_csv("dataset/trips_data_1000.csv")
df100 = pd.read_csv("dataset/trips_data_100.csv")
st.write("### Preview of First File:")
st.dataframe(df1000.head()) #Show first few rows
st.write("### Preview of Second File:")
st.dataframe(df100.head()) #Show first few rows


# Chart 1 File 1: Bar chart of customers by country
st.subheader("Customers by City")
country_counts = df1000["customer_city"].value_counts()
st.write(country_counts)
st.bar_chart(country_counts)

# Chart 2 File 1: Line chart of Tripvcs over time
st.subheader("Subscriptions Over Time")
df1000['Trips Date'] = pd.to_datetime(df1000['pickup_time']).dt.date
subscriptions_by_date = df1000.groupby('Trips Date').size().reset_index(name='Count')
st.write(subscriptions_by_date)
st.line_chart(subscriptions_by_date, x="Trips Date", y="Count")


