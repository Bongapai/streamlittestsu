import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a Streamlit app
st.title("-Chart-")

# Sidebar to upload a CSV file
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded data into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Sidebar for chart customization
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])
    x_axis = st.sidebar.selectbox("Select X-Axis Column", data.columns)
    y_axis = st.sidebar.selectbox("Select Y-Axis Column", data.columns)
    # p_color = st.sidebar.color_picker("Select Chart Color", "#FF5733")

    # Main content area
    st.header("Chart Preview")

    if chart_type == "Line Chart":
        st.line_chart(data[[x_axis, y_axis]])
    elif chart_type == "Bar Chart":
        st.bar_chart(data[[x_axis, y_axis]])
    elif chart_type == "Scatter Plot":
        st.write("This is a scatter plot:")
        # fig, ax = plt.subplots()
        st.scatter_chart(data[[x_axis, y_axis]])
        # fig, ax = st.pyplot()
        # ax.scatter(data[x_axis], data[y_axis], c=p_color)
        # st.write(ax.scatter(data[x_axis], data[y_axis])
else:
    st.sidebar.write("Please upload a CSV file to get started.")
