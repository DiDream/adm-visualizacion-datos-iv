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

### Algoritmos supervisados de clasificación
Es importante, para la ejecución de estos algoritmos, que las etiquetas tengan valores binarios, discretos. El fichero usado como ejemplo es [script/assets/titanic.csv](script/assets/titanic.csv), en el que cada fila almacena los datos de un pasajero del Titanic (nombre, sexo, edad, clase, etc) y su supervivencia en el accidente.

#### Naive Bayes
Para obtener el modelo a partir del algoritmo `Naive Bayes`, ejecutamos:
```bash
> ./iochart.py learn -a naive-bayes --data assets/titanic.csv -x Sex Pclass Fare Embarked -y Survived
```
Nótese que con `-a` o `--algorithm` especificamos el algoritmo a ejecutar, en este caso `naive-bayes`.

Cuya ejecución dará como resultado algo similar a:
```bash
> ./iochart.py learn -a naive-bayes --data titanic.csv -x Sex Pclass Fare Embarked -y Survived
Matriz confusión
[[91 19]
 [18 51]]
precision_score 0.7285714285714285
cross_val_score 0.8101898101898101
```

De igual forma, se mostrará una gráfica de cajas y bigotes a partir de las diferentes precisiones del modelo obtenidas.

| Precisión de Naive Bayes |
| --- |
| ![Precisión de Naive Bayes](assets/naive-bayes-score.png) |


#### Árboles de Decisión Clasificación
De forma similar que con el algoritmo `Naive Bayes`, para obtener el modelo a partir del algoritmo de árboles de decisión, ejecutamos:

```bash
> ./iochart.py learn -a tree-classifier --data assets/titanic.csv -x Sex Pclass Fare Embarked -y Survived
```

Lo cual, dará como resultado, algo similar a:
```bash
> ./iochart.py learn -a tree-classifier --data assets/titanic.csv -x Sex Pclass Fare Embarked -y Survived
Matriz confusión
[[101   6]
 [ 33  39]]
precision_score 0.8666666666666667
cross_val_score 0.8051948051948051
```

Y se mostrará la gráfica de cajas y bigotes con las precisiones obtenidas.

| Precisión de Árboles de Decisión Clasificación |
| --- |
| ![Precisión de Árboles de Decisión Clasificación](assets/decision-tree-classifier-score.png) |

### Algoritmos de regresión

#### Árboles de Decisión Regresión
Para obtener el modelo de aprendizaje a partir del algoritmo `Árboles de Decisión Regresión`, ejecutamos, por ejemplo:

```bash
> ./iochart.py learn -a tree-regression --data ./assets/winequality-red.csv -y quality
```
Nótese que al no especificar el campo `-x` se toman todos los campos, excepto el asignado a `y`.

Como se puede ver, la predicción obtenida es mala (pasa lo mismo con los datos de [`script/assets/winequality-white.csv`](script/assets/winequality-white.csv)):
```bash
> ./iochart.py learn -a tree-regression --data ./assets/winequality-red.csv  -y quality
model score 0.2692830829129489
cross_val_score 0.31480678505264087
```

Lo cual se puede ver también en las gráficas mostradas:
| Precisión de Algoritmos de regresión |
| --- |
| ![Precisión de Algoritmos de regresión](assets/winequality-red-score.png) |

Por otro lado para demostrar la correcta implementación del algoritmo, he utilizando el dataset de boston de `sklearn`, obteniendo resultados más aceptables.
```
model score 0.809496091404841
cross_val_score 0.7420437247991698
```

| Precisión de Algoritmos de regresión (Boston) |
| --- |
| ![Precisión de Algoritmos de regresión (Boston)](assets/boston-score.png) |

### Algoritmos de aprendizaje no supervisado basado en clustering
#### K-Means
Para ejecutar el algoritmo, podemos ejecutar el comando:
```bash
> ./iochart.py learn --data moviescs.csv -x cast_total_facebook_likes -y imdb_score --algorithm k-means
```
Mediante el argumento `--n-clusters` podemos especificar los clusters que queremos obtener, por defecto es 2.

El comando mostrará como resultado una gráfica con los clústeres coloreados y su centroide como `*`.

| K-Means con 2 clusters | k-Means con 3 clusters |
| --- | --- |
| ![K-Means con 2 clusters](assets/k-means-clusters-2.png) | ![k-Means con 3 clusters](assets/k-means-clusters-3.png) |