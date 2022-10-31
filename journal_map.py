#!/usr/bin/env python
# coding: utf-8


from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import geopandas
import database

# IMPORT dataframe from database.py
df = database.data()

# CONVERT to geodataframe
gdf = geopandas.GeoDataFrame(
    df, 
    geometry=geopandas.points_from_xy(df.lon, df.lat))


# MAP

def mymap():


    center = [59.31373922932743, 18.068295014789005]
    zoom = 6

    m = folium.Map(location=center, zoom_start=zoom, tiles="Stamen Toner")

    marker_cluster = MarkerCluster(
        name="clustered name",
    ).add_to(m)

    for row in gdf.itertuples():
        folium.Marker(location=[row.lat,row.lon],popup=row.mooddesc).add_to(marker_cluster)

    folium.LayerControl().add_to(m)
    
    return m


