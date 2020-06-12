# https://alysivji.github.io/getting-started-with-folium.html  - Folium Get Started
# https://martinjc.github.io/UK-GeoJSON/  - GeoJSON Data
import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import requests


#  Stamen Terrain, Stamen Toner, Mapbox Bright, and Mapbox Control Roo  - Map Options
map1 = folium.Map(location=[51.509865, -0.118092], tiles='Stamen Terrain', zoom_start=11.5)
# When adding Json data, insert into Properties --> "scalerank": 5, "featurecla": "Name of Boundary"
with open("outer_london.geojson", 'rb') as f:
    read = json.load(f)
folium.GeoJson(
    data=read,
    name='Outer London Outline').add_to(map1)
map1.save('colored.html')
folium.LayerControl().add_to(map1)

map2 = folium.Map(location=[51.509865, -0.118092], tiles='Stamen Toner', zoom_start=11.5)
map2.save('monotone.html')
