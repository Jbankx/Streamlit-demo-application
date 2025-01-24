import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math


st.title("Credit Utlization Rate")

st.write("### Input Data")
col1, col2 = st.columns(2)
current_balance = col1.number_input("Current Balance", min_value=0, max_value=10000, value=0)
credit_limit = col2.number_input("Credit Limit", min_value=0, value=10000)



# Calculate the credit Utilization rate (%).
credit_utilization_rate = (current_balance / credit_limit) * 100
unused_credit = 100 - credit_utilization_rate



#Click Me butthon
if st.button("Calculate"):
    st.write(f"#### Utlization rate percentage: `{credit_utilization_rate:,.0f}%`")
    st.write(f"#### Unused Credit percentage is: `{unused_credit:,.0f}%`")


    # Labels and values for the pie chart
    labels = ['Current Balance', 'Credit Limit']
    values = [credit_utilization_rate, unused_credit]
    colors = ['#ff9999', '#66b3ff']  # Optional: custom colors


    # Create a pie chart using Matplotlib
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Ensures the pie chart is a circle
    # plt.title('Credit Utilization Rate')


    st.write("")  # Adds a blank line
    st.write("")  # Adds a blank line

    # Display the chart in Streamlit
    st.title("Credit Utilization Dashboard")
    st.pyplot(fig)

    # Display additional details (optional)
    # st.write(f"**Current Balance:** ${current_balance}")
    # st.write(f"**Credit Limit:** ${credit_limit}")
    # st.write(f"**Utilization Rate:** {credit_utilization_rate:.0f}%")