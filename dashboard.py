import streamlit as st
import pandas as pd
import pickle
import pydeck as pdk
import numpy as np

# --- Cargar artefactos guardados ---
@st.cache_resource
def load_artifacts():
    with open('features_cache/model_best.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('features_cache/features_processed.pkl', 'rb') as f:
        features = pickle.load(f)
    with open('features_cache/predictions_test.pkl', 'rb') as f:
        predictions = pickle.load(f)
    return model, features, predictions

model, features, predictions = load_artifacts()
features_with_preds = features.merge(predictions, on='hex_id', how='inner')

# --- UI del Dashboard ---
st.title('Dashboard de Análisis de Costo de Vida de distintas regiones de Ecuador')

st.write("Explora las predicciones del costo de vida y entiende los factores que influyen en cada zona.")
st.markdown("""
<b>Colores del mapa:</b><br>
<span style='color:green;'>● Verde</span>: Bajo costo de vida<br>
<span style='color:orange;'>● Amarillo</span>: Costo de vida medio<br>
<span style='color:red;'>● Rojo</span>: Alto costo de vida<br>
""", unsafe_allow_html=True)

# --- Mapa con pydeck: color según costo de vida ---
map_data = features_with_preds[['lat', 'lon', 'cost_of_living']].copy()
# Normalizar costo de vida a [0, 1] para el color
min_col = map_data['cost_of_living'].min()
max_col = map_data['cost_of_living'].max()
map_data['color_scale'] = (map_data['cost_of_living'] - min_col) / (max_col - min_col + 1e-9)
# Verde (bajo) a rojo (alto)
map_data['color'] = map_data['color_scale'].apply(lambda x: [int(255*x), int(255*(1-x)), 0, 180])
layer = pdk.Layer(
    "ScatterplotLayer",
    map_data,
    get_position='[lon, lat]',
    get_fill_color='color',
    get_radius=350,
    pickable=True,
)
view_state = pdk.ViewState(
    latitude=-1.5,
    longitude=-78.0,
    zoom=6,
    pitch=0,
)
tooltip = {"html": "<b>Costo de vida:</b> {cost_of_living}"}
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))
# st.map(map_data, latitude='lat', longitude='lon')
