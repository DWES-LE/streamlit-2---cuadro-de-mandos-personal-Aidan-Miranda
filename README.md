# Análisis de datos de videojuegos

## Documentación de los datos
Este dataset contiene una lista de videojuegos con ventas mayores a las 100.000 copias. Y fue obtenido en la página kaggle.com.

El dataset incluye:

Rank - Ranking de ventas a nivel mundias

Name - El nombre del juego

Platform - Plataforma en la que el juego se publicó (DS,PC,PS4, etc.)

Year - Año de publicación

Genre - Genero del juego

Publisher - Compañía encargada de publicar el juego

NA_Sales - Ventas en Norteamérica (en millones)

EU_Sales - Ventas en Europa (en millones)

JP_Sales - Ventas en Japón (en millones)

Other_Sales - Ventas en el resto del mundo (en millones)

Global_Sales - Ventas a nivel mundial.

## Instrucciones

1. Clona el repositorio en tu máquina local. Puedes hacer esto descargando el repositorio como un archivo ZIP o usando Git en la línea de comandos:

        git clone https://github.com/DWES-LE/streamlit-2---cuadro-de-mandos-personal-Aidan-Miranda.git <destino>
        
2. Navega al directorio raíz del proyecto:

        cd <destino>
        
3. Crea un entorno virtual para el proyecto:

        python -m venv env
        
4. Activa el entorno virtual:

        source env/bin/activate    (En Windows es: env\Scripts\activate)
        
5. Instala Streamlit:

        pip install streamlit
        
6. Instala los requisitos:

        pip install -r requirements.txt
        
7. Ejecuta el archivo "titanic.py" usando Streamlit:

        streamlit run titanic.py

Y listo, abre tu navegador web y ve a la dirección que se te proporciona en la terminal. Por lo general, será http://localhost:8501. ¡Y eso es todo! Deberías ver la aplicación web en funcionamiento. Si deseas detener la aplicación, simplemente presiona Ctrl + C en la línea de comandos donde se está ejecutando Streamlit.
