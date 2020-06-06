
# coding: utf-8

# In[56]:


import folium
from folium import plugins
import json
import requests
import geopandas
import branca.colormap as cm

m = folium.Map(location=[39.78, -3.759],tiles='Cartodb Positron',  zoom_start=6, control_scale=True)

#full screen 
plugins.Fullscreen(position='topleft').add_to(m)

#Geojseon 
url = 'https://raw.githubusercontent.com/ferhd96/Folium/master'
pro = f'{url}/PROVINCIAS_ESP_FASES.json'


geo_json_data = json.loads(requests.get(pro).text)

#folium.GeoJson(geo_json_data).add_to(m)

#folium.GeoJson(us_states).add_to(m)

#Cargamos el GeoJson y establecemos el estilo 
gjson= folium.GeoJson(
   geo_json_data,
    style_function=lambda feature: {
     'fillColor': '#7AAA71' if 'tres' in feature['properties']['Fases'].lower() else '#B6DD7E',
        'color': 'black',
       'weight': 1,
       'fillOpacity': 0.9,
  }
).add_to(m)

#Establecemos la leyenda 
a=cm.linear.YlGn_03.scale(2, 3)
a.caption = 'Fases desescalada'
a.add_to(m)

#Establecemos las etiquetas 
folium.features.GeoJsonPopup(fields=['Texto'],
labels=False ).add_to(gjson)



# In[57]:


m

