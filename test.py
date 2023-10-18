import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Basic Streamlit')
st.write("TEST")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

choice = st.radio(
     "What's your favorite animal",
     ('Cat', 'Dog', 'Rabbit'))
st.write(f"You selected {choice}")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
data = pd.read_csv(url)

# df2 = df.groupby('species')['body_mass_g'].mean()
# st.bar_chart(df2)

url = st.text_input("Enter the data URL")
if url:
    data = pd.read_csv(url)
    group_data = data.groupby(['species', 'sex'])['flipper_length_mm'].mean().unstack()
    fig, ax = plt.subplots()
    group_data.plot(kind='bar', ax=ax)
    ax.set_title("Flipper Length for 3 Penguin Species by Sex", size=10) #, color="red")
    st.pyplot(fig)
else:
    st.write("Please enter a data URL to load the data.")

# Seaborn barplot
# fig, ax = plt.subplots()
# sns.barplot(x="species", y="flipper_length_mm", data=data, hue="sex", ax=ax)
# ax.set_title("Flipper Length for 3 Penguin Species by Sex", size=20, color="red")
# st.pyplot(fig)

# data = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 22, 35]
# })
# df2 = df.groupby('species')['body_mass_g'].mean()

# st.title("Dynamic Data Display Example")
age_range = st.slider("Select Body Mass Range", min_value=2300, max_value=6500, value=(2300, 6500))
filtered_data = data[(data['body_mass_g'] >= age_range[0]) & (data['body_mass_g'] <= age_range[1])]

# fig, ax = plt.subplots()
# filtered_data.groupby('species')['body_mass_g'].mean().plot(kind='bar', ax=ax)
# ax.set_xlabel('Species')
# ax.set_ylabel('Mean Body_Mass_g')
# ax.set_title('Mean Body Mass by Species')
# st.pyplot(fig)

df2 = filtered_data.groupby('species')['body_mass_g'].mean()
st.bar_chart(df2)

st.dataframe(filtered_data[['species','body_mass_g']])
