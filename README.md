# Dashboard de Costo de Vida (Ecuador)


# URL API:
https://altscore-data-science-competition.onrender.com/

## Estructura

- `dashboard.py`  
  Código principal de la app Streamlit.
- `requirements.txt`  
  Dependencias Python.
- `render.yaml`  
  Configuración para Render.
- `features_cache/`  
  Carpeta con los archivos de modelo y datos necesarios:
    - `model_best.pkl`
    - `features_processed.pkl`
    - `predictions_test.pkl`

## Comando de inicio
```
streamlit run dashboard.py --server.port 10000
```
