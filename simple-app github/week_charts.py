#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio
import datetime 
from datetime import date, timedelta  
import plotly.express as px

#Modules
import database


# IMPORT dataframe from database.py
df = database.data()

# today, week, month
today = date.today()
week_prior =  today - timedelta(weeks=1)

# Filter by date
df_week = df[(df['date'].dt.date > week_prior)]  

def weekly_moodnum():
    theme1 = 'plotly_white'
    theme2 = 'plotly_dark'

    fig1 = px.line(df_week, 
                  x=df_week['date'], 
                  y=df_week['moodnum'], 
                  text="mooddesc", 
                  #title = "Mood",
                  template=theme1) #color="moodnum",

    fig1.update_traces(line_color = "black")

    fig1.add_bar(
        x=df_week['date'], 
        y=df_week['sun'],
        name='Sun',
        opacity=0.5)

    fig1.add_bar(
        x=df_week['date'], 
        y=df_week['social'],
        name='Social',
        opacity=0.5)

    fig1.add_bar(
        x=df_week['date'], 
        y=df_week['walk'],
        name='Walk',
        opacity=0.5)

    fig1.add_bar(
        x=df_week['date'], 
        y=df_week['exercise'],
        name='Exercise',
        opacity=0.5)

    fig1.update_layout(hovermode="x")
    
    return fig1

def weekly_mooddesc():
    # This creates a new dataframe. Mood descriptions are the index
    mood = pd.DataFrame(df_week['mooddesc'].value_counts())

    # Get the index and use it as a column
    mood.reset_index(inplace=True)

    # rename the column names
    mood.rename(columns = {'index':'record'}, inplace = True)
    mood.rename(columns = {'mooddesc':'count'}, inplace = True)

    fig2 = px.pie(
        mood, 
        values = mood['count'], 
        names = mood['record'],
        hole = 0.5,)

    return fig2

