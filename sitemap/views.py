from django.shortcuts import render
from django.http import HttpResponse
import folium
from folium.plugins import HeatMap
from shapely.geometry import Polygon
import pandas as pd
import numpy as np

# Create your views here.
def index(request):
    return render(request, 'index.html')

def map(request):
    m = folium.Map(location=[57.1522, 65.5272],
                   zoom_start=10)
    folium.Marker(location=[57.1522, 65.5272], tooltip='click for more', popup='Tyumen').add_to(m)
    df = pd.read_excel(r'D:\Работа\Наука\Карбоновые единицы\рассчеты по числу полос 13.02.24.xlsx', sheet_name='Лист2')
    for i in range(1, 11):
        HeatMap(df[['Широта', 'Долгота', i]].to_numpy(), name=f'{i} балл').add_to(m)
    m.add_child(folium.LayerControl(collapsed=False))

    m = m._repr_html_()

    # m.save('map.html')
    context = {
        'm': m
    }

    return render(request, 'map.html', context)