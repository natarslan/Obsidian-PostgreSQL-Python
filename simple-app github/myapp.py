#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio #sql
import psycopg2 #sql
import folium #map
from streamlit_folium import st_folium #map

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

# Modules
import database
import journal_map
import week_charts
import month_charts


# MAP
m = journal_map.mymap()
folium.LayerControl().add_to(m)

# WEEKLY CHARTS
week_figure1 = week_charts.weekly_moodnum()
week_figure2 = week_charts.weekly_mooddesc()

# MONTHLY CHARTS
month_figure1 = month_charts.monthly_moodnum()
month_figure2 = month_charts.monthly_mooddesc()


# LAYOUT
# Source: https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/

st.header("Weekly Analysis")

# ADD THE MAP
col1 = st.columns(1)
st_data = st_folium(m, width=1500, height=250)

# ADD THE PLOTS IN COLUMNS
col2, col3 = st.columns(2)

with col2:
    st.plotly_chart(week_figure1, use_container_width=True)

with col3:
    st.plotly_chart(week_figure2, use_container_width=True)
    