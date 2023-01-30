# -*- coding: utf-8 -*-
"""Fvs_mapCalor_Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wCZyDjruSKhfJmYVdNTnN3AGFTDjFHoA
"""

import folium
import branca.colormap
import numpy as np
from folium.plugins import HeatMap

# geo_json_arquivo = ""
geo_json_arquivo = "geojson_es.json"
dados = np.genfromtxt('export_chamados_mapa.csv',delimiter=",")

# print(dados)

mapa_es = folium.Map([-19.4666,-40.9845], zoom_start=8 , tiles=None)

folium.TileLayer("cartodbpositron").add_to(mapa_es)

#Adicionando a fronteira dos municipios
estilo = lambda x: {"color" : "gray",
                   "fillOpacity": 0,
                   "weight": 0.3}

folium.GeoJson(geo_json_arquivo, style_function = estilo,name = "Municipios").add_to(mapa_es)

#Paleta de cores
indices = [0, 0.3, 0.7, 1]

colormap = branca.colormap.StepColormap(["green", "yellow", "red"], index = indices,
                                       caption = "Força dos chamados na região !")

dicionario_cores = {0: "green",
                   0.3: "green",
                   0.301: "yellow",
                   0.7: "yellow",
                   0.701: "red",
                   1: "red"}


colormap.scale(0, 100).add_to(mapa_es)

#Mapa de Calor
HeatMap(data = dados,
       gradient = dicionario_cores,
       min_opacity = 0.8,
       radius = 18,
       blur = 20,
       name = "Dados Calor").add_to(mapa_es)


#Controle de camadas
folium.LayerControl(position = "topleft").add_to(mapa_es)

mapa_es.save("regional_vitoria.html")

mapa_es