#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2

# Source: https://www.dataquest.io/blog/tutorial-connect-install-and-query-postgresql-in-python/
connection = psycopg2.connect(database="MY-DATABASE",
                        host="localhost",
                        user="MY-USERNAME",
                        password="MY-PASSWORD",
                        port="MY-PORT-NUMBER")

query = '''
SELECT 
    dataview_data -> 'date' as date,
    dataview_data -> 'tags' as tags,
    dataview_data -> 'mood-no' as moodnum,
    dataview_data -> 'mood-desc' as mooddesc,
    dataview_data -> 'social' as social,
    dataview_data -> 'walk' as walk,
    dataview_data -> 'exercise' as exercise,
    dataview_data -> 'physical-no' as physical,
    dataview_data -> 'menstrual-cycle' as mens,
    dataview_data -> 'geom' as geom,
    dataview_data -> 'sun' as sun
FROM obsidian.file;
'''

# From  sql database to pandas dataframe:https://stackoverflow.com/questions/70892143/psycopg2-connection-sql-database-to-pandas-dataframe
df = sqlio.read_sql_query(query, connection)

# SPLIT: Split the column geom with delimeter
df[['lat','lon']] = df['geom'].str.split(',',expand=True)

# FLOAT: Convert pandas.core.series to float
df['lat'] = df['lat'].astype(float)
df['lon'] = df['lon'].astype(float)

# NULL: Drop rows where specific column (geom) values are null
df = df.dropna(subset=["geom"])

# Make the sun/social/walk/exercise values 5 or 0 to match the mood (easier when you plot them together)
df['sun'] = df['sun'] * 5
df['social'] = df['social'] * 5
df['walk'] = df['walk'] * 5
df['exercise'] = df['exercise'] * 5

# JOURNAL: Keep only the rows that contain a specific string
# If this was ==False then it would have dropped all The Rows that Contain a Specific String
df = df[df["tags"].str.contains("journal")==True]

# SORT by date
df = df.sort_values('date')

st.header("Obsidian Journal to PostgreSQL & Streamlit")

import datetime 
from datetime import date, timedelta   

# Convert date column & Set Index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date')

def data():
    df_all = df 
    return df_all

