import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from CSV files
commodity_data = pd.read_csv('data\data_commodity.csv', encoding='latin1')
index_data = pd.read_csv('data\index.csv', encoding='latin1')

# Set the Date column as the index for time series plotting
commodity_data['Date'] = pd.to_datetime(commodity_data['Date'])
commodity_data.set_index('Date', inplace=True)
index_data['Date'] = pd.to_datetime(index_data['Date'])
index_data.set_index('Date', inplace=True)

# Streamlit App
st.title('Global Commodity Data Visualization App')

# Sidebar Navigation
page = st.sidebar.radio("Navigate to", ('Home', 'Commodities', 'Index'))

# Home Page
if page == 'Home':
    st.subheader('Home')
    st.image('img/globe.png')
    st.write("""
    Welcome to the Global Commodity Data Visualization App!
    
    This app allows you to explore and visualize global commodity data and index information.
    Navigate to the "Commodities" or "Index" pages using the sidebar to explore specific data sets.
    
    """)
    
    # Plot four graphs in two columns
    col1, col2 = st.columns(2)
    
    # Column 1: Plot for column 2
    col1.subheader('Energy')
    fig_col2 = px.line(index_data.iloc[:, 1])
    col1.plotly_chart(fig_col2)
       
    # Column 3: Plot for column 14
    col1.subheader('Metals & Minerals')
    fig_col14 = px.line(index_data.iloc[:, 13])
    col1.plotly_chart(fig_col14)
    

# Commodities Page
elif page == 'Commodities':
    st.subheader('Commodities')
    st.image('img/globe.png')
    commodity_options = st.multiselect('Select Commodities:', commodity_data.columns)
    visualize_button_commodities = st.button('Visualize')
    
    if visualize_button_commodities and commodity_options:
        st.subheader('Commodities Data Visualization')
        
        # Plot commodity data using Plotly Express
        fig_commodities = px.line(commodity_data[commodity_options], labels={'value': 'Commodity Value'})
        st.plotly_chart(fig_commodities)

# Index Page
elif page == 'Index':
    st.subheader('Index')
    st.image('img/globe.png')
    index_options = st.multiselect('Select Index Variables:', index_data.columns)
    visualize_button_index = st.button('Visualize')
    
    if visualize_button_index and index_options:
        st.subheader('Index Data Visualization')
        
        # Plot index data using Plotly Express
        fig_index = px.line(index_data[index_options], labels={'value': 'Index Value'})
        st.plotly_chart(fig_index)
