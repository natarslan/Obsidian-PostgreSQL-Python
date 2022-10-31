#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio
import datetime 
from datetime import date, timedelta  
import plotly.express as px

# Module
import database

# IMPORT dataframe from database.py
df = database.data()

# today, week, month
today = date.today()
month_prior =  today - timedelta(weeks=4)

# Filter by date
df_month = df[(df['date'].dt.date > month_prior)]  

def monthly_moodnum():
    theme1 = 'plotly_white'
    theme2 = 'plotly_dark'

    fig3 = px.line(df_month, 
                  x=df_month['date'], 
                  y=df_month['moodnum'], 
                  text="mooddesc", 
                  #title = "Mood",
                  template=theme1) #color="moodnum",

    fig3.update_traces(line_color = "black")

    fig3.add_bar(
        x=df_month['date'], 
        y=df_month['sun'],
        name='Sun',
        opacity=0.5)

    fig3.add_bar(
        x=df_month['date'], 
        y=df_month['social'],
        name='Social',
        opacity=0.5)

    fig3.add_bar(
        x=df_month['date'], 
        y=df_month['walk'],
        name='Walk',
        opacity=0.5)

    fig3.add_bar(
        x=df_month['date'], 
        y=df_month['exercise'],
        name='Exercise',
        opacity=0.5)

    fig3.update_layout(hovermode="x")
    return fig3


def monthly_mooddesc():
    # This creates a new dataframe. Mood descriptions are the index
    mood_month = pd.DataFrame(df_month['mooddesc'].value_counts())

    # Get the index and use it as a column
    mood_month.reset_index(inplace=True)

    # rename the column names
    mood_month.rename(columns = {'index':'record'}, inplace = True)
    mood_month.rename(columns = {'mooddesc':'count'}, inplace = True)

    fig4 = px.pie(
        mood_month, 
        values = mood_month['count'], 
        names = mood_month['record'],
        hole = 0.5,)
    return fig4

