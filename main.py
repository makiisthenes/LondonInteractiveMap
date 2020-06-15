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


map2 = folium.Map(location=[51.509865, -0.118092], tiles='Stamen Toner', zoom_start=11.5)
folium.TopoJson(data=open(r'BoroughJSON\Barking and Dagenham\topo_E09000002.json'), name='Barking and Dagenham', object_path='objects.E09000002', tooltip='Barking and Dagenham').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Barnet\topo_E09000003.json'), name='Barnet', object_path='objects.E09000003', tooltip='Barnet').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Bexley\topo_E09000004.json'), name='Bexley', object_path='objects.E09000004', tooltip='Bexley').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Brent\topo_E09000005.json'), name='Brent', object_path='objects.E09000005', tooltip='Brent').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Bromley\topo_E09000006.json'), name='Bromley', object_path='objects.E09000006', tooltip='Bromley').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Camden\topo_E09000007.json'), name='Camden', object_path='objects.E09000007', tooltip='Camden').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\City of London\topo_E09000001.json'), name='City of London', object_path='objects.E09000001', tooltip='City of London').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Croydon\topo_E09000008.json'), name='Croydon', object_path='objects.E09000008', tooltip='Croydon').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Ealing\topo_E09000009.json'), name='Ealing', object_path='objects.E09000009', tooltip='Ealing').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Enfield\topo_E09000010.json'), name='Enfield', object_path='objects.E09000010', tooltip='Enfield').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Greenwich\topo_E09000011.json'), name='Greenwich', object_path='objects.E09000011', tooltip='Greenwich').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Hackney\topo_E09000012.json'), name='Hackney', object_path='objects.E09000012', tooltip='Hackney').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Hammersmith and Fulham\topo_E09000013.json'), name='Hammersmith and Fulham', object_path='objects.E09000013', tooltip='Hammersmith and Fulham').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Haringey\topo_E09000014.json'), name='Haringey', object_path='objects.E09000014', tooltip='Haringey').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Harrow\topo_E09000015.json'), name='Harrow', object_path='objects.E09000015', tooltip='Harrow').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Havering\topo_E09000016.json'), name='Havering', object_path='objects.E09000016', tooltip='Havering').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Hillingdon\topo_E09000017.json'), name='Hillingdon', object_path='objects.E09000017', tooltip='Hillingdon').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Hounslow\topo_E09000018.json'), name='Hounslow', object_path='objects.E09000018', tooltip='Hounslow').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Islington\topo_E09000019.json'), name='Islington', object_path='objects.E09000019', tooltip='Islington').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Kensington and Chelsea\topo_E09000020.json'), name='Kensington and Chelsea', object_path='objects.E09000020', tooltip='Kensington and Chelsea').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Kingston upon Thames\topo_E09000021.json'), name='Kingston upon Thames', object_path='objects.E09000021', tooltip='Kingston upon Thames').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Lambeth\topo_E09000022.json'), name='Lambeth', object_path='objects.E09000022', tooltip='Lambeth').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Lewisham\topo_E09000023.json'), name='Lewisham', object_path='objects.E09000023', tooltip='Lewisham').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Merton\topo_E09000024.json'), name='Merton', object_path='objects.E09000024', tooltip='Merton').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Newham\topo_E09000025.json'), name='Newham', object_path='objects.E09000025', tooltip='Newham').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Redbridge\topo_E09000026.json'), name='Redbridge', object_path='objects.E09000026', tooltip='Redbridge').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Richmond upon Thames\topo_E09000027.json'), name='Richmond upon Thames', object_path='objects.E09000027', tooltip='Richmond upon Thames').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Southwark\topo_E09000028.json'), name='Southwark', object_path='objects.E09000028', tooltip='Southwark').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Sutton\topo_E09000029.json'), name='Sutton', object_path='objects.E09000029', tooltip='Sutton').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Tower Hamlets\topo_E09000030.json'), name='Tower Hamlets', object_path='objects.E09000030', tooltip='Tower Hamlets').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Waltham Forest\topo_E09000031.json'), name='Waltham Forest', object_path='objects.E09000031', tooltip='Waltham Forest').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Wandsworth\topo_E09000032.json'), name='Wandsworth', object_path='objects.E09000032', tooltip='Wandsworth').add_to(map2)
folium.TopoJson(data=open(r'BoroughJSON\Westminster\topo_E09000033.json'), name='Westminster', object_path='objects.E09000033', tooltip='Westminster').add_to(map2)
folium.LayerControl().add_to(map2)
map2.save('monotone.html')
