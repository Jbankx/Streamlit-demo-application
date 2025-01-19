import streamlit as st
import pandas as pd
import numpy as np

#New addition
from datetime import datetime

# Get the current date and time
latest_timestamp = datetime.now()
formatted_timestamp = latest_timestamp.strftime("%a %d %m %Y")


st.title("My first Streamlit movies app!")
st.write("Edited by Junior A.")
st.write("Latest Timestamp:", formatted_timestamp)



data = pd.read_csv("movies.csv")

# Dropdown for unique values in the 'title' column
unique_titles = data["title"].unique()
selected_title = st.selectbox("Select a title to filter:", unique_titles)

#Click Me butthon
if st.button("Click Me"):
    st.write(f"Your favorite movie is `{selected_title}`")


###################################################################
# Streamlit app
st.title("Movie Details")


# Filter the DataFrame based on the selected title
filtered_df = data[data["title"] == selected_title]

# Display the filtered table
st.dataframe(filtered_df)
###################################################################


###################################################################
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)
