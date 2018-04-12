# importamos las librerías necesarias
import urllib
from bs4 import BeautifulSoup
import pandas as pd
# Guardamos en la variable la url de Wikipedia sobre la que vamos a extraer los datos
wikipage = "https://es.wikipedia.org/wiki/Liga_de_Campeones_de_la_UEFA"

# Utilizamos urlopen para conectarnos a la web y guardar la conexión en la variable page
page = urllib.request.urlopen(wikipage)

# Utilizamos el parser de html para formatear el resultado que está en la tabla
soup = BeautifulSoup(page, "html.parser")

# Guardamos en la variable el contenido de la tabla localizada
tabla_campeones = soup.find("table", class_ = "sortable")
# Creamos una lista por cada columna que existe en la tabla
A=[]
B=[]
C=[]
D=[]
E=[]

# Recorremos las diferentes listas para obtener los datos necesarios
for row in tabla_campeones.findAll("tr"):
    cells = row.findAll('td') # Filtramos por td para algunas columnas
    equipos=row.findAll('b') # Filtramos por b (negrita) para equipos campeones
    equipos2=row.findAll('td') # Filtramos por td para subcampeones
    if len(cells)==5: # Extraemos el contenido de la tabla
        A.append(cells[0].find(text=True))
        B.append(equipos[0].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(equipos2[3].findAll(text=True))
        E.append(cells[4].find(text=True))
      
# Con la librería importada de pandas convertimos la tabla en un dataframe
df=pd.DataFrame(A,columns=['Temporada'])
df['Campeon']=B
df['Resultado']=C
df['Subcampeon']=D
df['Notas']=E

# Mostramos por pantalla el dataset creado
#print(df)
#print df.to_html()
# Guardamos el dataframe en un csv utilizando la coma como separador
df.to_csv('campeones.csv', sep=',', encoding='utf-8')