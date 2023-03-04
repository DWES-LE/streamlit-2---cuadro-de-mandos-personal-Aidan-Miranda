# Imports
import streamlit as st
import pandas as pd
import altair as alt

# Cargar datos
data = pd.read_csv('datos/vgsales.csv')


# Crear sidebar para la selección de género y plataforma
with st.sidebar:
    # Crear menú desplegable para seleccionar género
    genre = st.selectbox('Selecciona el género', data['Genre'].unique())

# Ventas globales por género y plataforma
with st.container():
    st.header('Ventas globales por género y plataforma')
    # Filtrar datos según las selecciones del usuario
    # Crear menú desplegable para seleccionar plataforma
    platform = st.selectbox('Selecciona la plataforma', data['Platform'].unique())

    filtered_data = data[(data['Genre'] == genre) & (data['Platform'] == platform)]
    # Calcular las ventas globales aproximadas
    global_sales = filtered_data['Global_Sales'].sum()
    # Mostrar el resultado al usuario
    st.write(f"Las ventas globales aproximadas para {genre} en {platform} son: {global_sales.round(2)} millones")

st.write('---')

# Porcentaje de ventas por plataforma para cada género
with st.container():
    st.header('Porcentaje de ventas por plataforma para cada género')
    # Filtrar datos según el género seleccionado por el usuario
    filtered_data = data[data['Genre'] == genre]

    # Agrupar los datos por plataforma y sumar las ventas globales
    sales_by_platform = filtered_data.groupby('Platform')['Global_Sales'].sum()

    # Calcular el total de ventas globales para el género seleccionado
    total_sales = sales_by_platform.sum()

    # Calcular el porcentaje de ventas de cada plataforma
    platform_percentages = (sales_by_platform / total_sales) * 100
    # Ordenar los porcentajes de mayor a menor
    sorted_percentages = platform_percentages.sort_values(ascending=False)
    # Crear un gráfico de barras que muestre los porcentajes de ventas por plataforma
    st.write(f"Porcentaje de ventas por plataforma para {genre}")
    st.bar_chart(sorted_percentages.round(2))

    # Mostrar un checkbox para controlar si se muestran todos los porcentajes o no
    show_all_percentages = st.checkbox('Mostrar todos los porcentajes')

    # Dividir la pantalla en tres columnas
    col1, col2, col3, col4, col5 = st.columns(5)

    # Mostrar los porcentajes de ventas de cada plataforma en la columna correspondiente si el checkbox está seleccionado
    if show_all_percentages:
        for i, (platform, percentage) in enumerate(platform_percentages.iteritems()):
            if i % 5 == 0:
                column = col1
            elif i % 5 == 1:
                column = col2
            elif i % 5 == 2:
                column = col3
            elif i % 5 == 3:
                column = col4
            else:
                column = col5
            column.write(f"{platform.center(15)}: {percentage:.2f}%")


st.write('---')

with st.container():
    st.header('Cuota de mercado por publisher para cada género')

    # Crear multiselect para que el usuario pueda seleccionar varios publishers
    publishers = st.multiselect('Publisher', data['Publisher'].unique())

    # Filtrar datos según las selecciones del usuario
    filtered_data = data[(data['Genre'] == genre) & (data['Publisher'].isin(publishers))]

    # Agrupar datos por publisher y sumar las ventas globales
    publisher_sales = filtered_data.groupby('Publisher')['Global_Sales'].sum()

    # Sacar también el número de juegos publicados por cada publisher
    publisher_games = filtered_data.groupby('Publisher')['Name'].count()

    # Gráfica de ventas globales por publisher
    sales_chart = alt.Chart(filtered_data).mark_bar().encode(
        x=alt.X('Publisher', sort=alt.EncodingSortField(field='Global_Sales', op='sum', order='descending')),
        y='sum(Global_Sales)',
        color='Publisher'
    ).properties(
        title=f'Ventas globales por publisher'
    )

    # Gráfica de número de juegos publicados por publisher
    games_chart = alt.Chart(filtered_data).mark_bar().encode(
        x=alt.X('Publisher', sort=alt.EncodingSortField(field='Name', op='count', order='descending')),
        y='count(Name)',
        color='Publisher'
    ).properties(
        title=f'Número de juegos por publisher'
    )

    col1, col2 = st.columns(2)
    col1.altair_chart(sales_chart)
    col2.altair_chart(games_chart)

st.write('---')

with st.container():

    st.header('Cuota de mercado por género')
    
    # Calcular el porcentaje de ventas por género
    genre_sales_pct = data.groupby('Genre')['Global_Sales'].sum() / data['Global_Sales'].sum() * 100

    st.bar_chart(genre_sales_pct.round(2))
