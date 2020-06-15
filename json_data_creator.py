import os

path = ''
json_path = ''
borough= ''
borough_id= ''
print(f"folium.TopoJson(data=open(r'{json_path}'), name='{borough}', object_path='objects.{borough_id}', tooltip='{borough}').add_to(map2)")

for file in os.listdir(r"BoroughJSON"):
    json_file = os.path.join(r"BoroughJSON", file)
    json_id = os.listdir(json_file)[0]
    json_path = os.path.join(json_file, json_id)
    borough = file
    borough_id = json_id[5:-5]
    print(f"folium.TopoJson(data=open(r'{json_path}'), name='{borough}', object_path='objects.{borough_id}', tooltip='{borough}').add_to(map2)")