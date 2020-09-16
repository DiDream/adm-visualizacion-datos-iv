# Visualización de Datos IV
![Build and deploy server to GKE](https://github.com/DiDream/adm-visualizacion-datos-iv/workflows/Build%20and%20deploy%20server%20to%20GKE/badge.svg)
![Build and deploy client to GKE](https://github.com/DiDream/adm-visualizacion-datos-iv/workflows/Build%20and%20deploy%20client%20to%20GKE/badge.svg)

Puede acceder a la demo de la aplicación en **[https://edu.ajmonfue.me/adm-4/](https://edu.ajmonfue.me/adm-4/)**

## Enunciados
### 1. Extiende el framework anterior para que permita, con los conjuntos de datos que has estado considerando hasta este momento, representar esos datos utilizando mapas geográficos.
Para implementar la representación de mapas geográficos, se ha seguido el tutorial http://www.geomapik.com/desarrollo-programacion-gis/mapas-con-python-geopandas-matplotlib/. Dicha implementación se ha realizado sólo en script de python.

Se puede comprobar su funcionamiento ejecutando:
```bash
> ./iochart.py chart --x-axis total_2008 --chart-type map --data assets/us-elections.geojson --chart-file-name us-elections
```
El cual dará como resultado la gráfica en el fichero con nombre [`us-elections.png`](assets/us-elections.png).

| us-elections |
| --- |
| ![us-elections](assets/us-elections.png) |

O bien:
```bash
> ./iochart.py chart --x-axis NAT2018 --chart-type map --data assets/natalidad.geojson --chart-file-name natalidad
```
Que dará como resultado [`natalidad.png`](assets/natalidad.png)

| natalidad |
| --- |
| ![natalidad](assets/natalidad.png) |


### 2. Utiliza la librería scikit-learn para desarrollar algoritmos de aprendizaje sobre los conjunto de datos que has venido utilizando hasta este momento. El estudio debe considerar, al menos, un algoritmo de aprendizaje de supervisado de clasificación, uno de regresión y un algoritmo de aprendizaje no supervisado basado en clustering. Utiliza alguna herramienta que permita representar gráficamente el resultado que has obtenido.