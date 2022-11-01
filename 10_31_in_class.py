from re import X
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

who_data = pd.read_csv('WHO_data.csv')
st.write(who_data)

st.sidebar.header('pick two variables for your scatterplot')

xval = st.sidebar.selectbox("Pick your x-axis", who_data.select_dtypes(include=np.number).columns.tolist())
yval = st.sidebar.selectbox("Pick your y-axis", who_data.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(who_data, title = f"Correleation between {xval} and {yval} ").mark_point().encode(
    alt.X(xval, title=f"{xval}"),
    alt.Y(yval, title=f"{yval}"),
    tooltip = [xval,yval]
    )
st.altair_chart(scatter, use_container_width=True)

corr= round(who_data[xval].corr(who_data[yval]),2)
st.write(f"The correlation between {xval} and {yval} is {corr}")