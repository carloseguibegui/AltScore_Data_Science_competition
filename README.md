# Dashboard de Costo de Vida (Ecuador)

## Estructura mínima para deploy en Render

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

## Instrucciones
1. Sube esta carpeta a un repositorio de GitHub.
2. En Render, crea un nuevo Web Service y conecta el repo.
3. Render detectará el `render.yaml` y hará el deploy automáticamente.
4. Si necesitas actualizar los archivos de `features_cache`, súbelos también.

## Comando de inicio
```
streamlit run dashboard.py --server.port 10000
```

## Notas
- Si usas archivos grandes o privados, considera variables de entorno o almacenamiento externo.
- Puedes personalizar el nombre del servicio y el puerto en `render.yaml`.
