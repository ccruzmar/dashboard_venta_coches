import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Leer el archivo CSV dentro de la carpeta 'data'
df = pd.read_csv('data/vehicles_us.csv')

# 2. Encabezado de la aplicación
st.header("🚗 Dashboard: Análisis de Anuncios de Venta de Coches")

# 3. Mostrar una tabla con las primeras filas para que el usuario vea qué datos tenemos
st.write("Vista previa de los primeros datos:")
st.write(df.head())

# 4. Checkbox para mostrar el histograma
show_histogram = st.checkbox('📊 Mostrar Histograma de Kilometraje')

if show_histogram:
    st.write('Creación de un histograma para la columna "odometer"')
    fig = px.histogram(
        df, x="odometer", title="Distribución de Kilometraje (odometer)")
    st.plotly_chart(fig, use_container_width=True)

# 5. Checkbox para mostrar gráfico de dispersión
show_scatter = st.checkbox('📉 Mostrar Gráfico de Dispersión Precio vs Año')

if show_scatter:
    st.write('Creación de un gráfico de dispersión: Precio vs Año del Modelo')
    fig = px.scatter(df, x="model_year", y="price",
                     title="Relación entre Precio y Año del Modelo")
    st.plotly_chart(fig, use_container_width=True)

# 6. Mensaje final de interacción
st.write("✅ Puedes activar o desactivar las casillas de verificación para mostrar/ocultar cada gráfico.")
