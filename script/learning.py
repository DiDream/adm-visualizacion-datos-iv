from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt


class LearningAlgorithm:
    def __init__(self):
        pass

# algoritmo de aprendizaje de supervisado de clasificación
# NAIVE BAYES
# https://www.youtube.com/watch?v=P930ev-eyVk&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=49
class NaiveBayesAlgorithm(LearningAlgorithm):
    def run(self):
        dataset = datasets.load_breast_cancer()

        x = dataset.data
        y = dataset.target
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        from sklearn.naive_bayes import GaussianNB

        algorithm = GaussianNB()
        algorithm.fit(x_train, y_train)

        y_pred = algorithm.predict(x_test)

        from sklearn.metrics import confusion_matrix

        matrix = confusion_matrix(y_test, y_pred)

        print('matriz confunsión')
        print(matrix)

# https://www.youtube.com/watch?v=ZeRblDJ-Jug&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=50
class DecisionTreeClassifierAlgorithm(LearningAlgorithm):
    def run(self):
        dataset = datasets.load_breast_cancer()

        x = dataset.data
        y = dataset.target
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        from sklearn.tree import DecisionTreeClassifier
        algorithm = DecisionTreeClassifier(max_depth=5, criterion='entropy')
        algorithm.fit(x_train, y_train)
        y_pred = algorithm.predict(x_test)

        from sklearn.metrics import confusion_matrix

        matrix = confusion_matrix(y_test, y_pred)

        print('matriz confunsión')
        print(matrix)

        from sklearn.metrics import precision_score
        print('presicion', precision_score(y_test, y_pred))


# un algoritmo de aprendizaje de supervisado de regresión
# https://www.youtube.com/watch?v=gP2X8a3LaTM
# ÁRBOLES DE DECISIÓN REGRESIÓN
class DecisionTreeRegressionAlgorithm(LearningAlgorithm):
    def run(self):
        dataset = datasets.load_boston()

        # Columna 6 del dataset
        print('data', dataset.data)
        x = dataset.data[:, np.newaxis, 5]
        print('x', x)
        y = dataset.target

        plt.scatter(x, y)

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        from sklearn.tree import DecisionTreeRegressor
        algorithm = DecisionTreeRegressor(max_depth=5)
        algorithm.fit(x_train, y_train)

        y_pred = algorithm.predict(x_test)
        print(algorithm.score(x_train, y_train))


# algoritmo de aprendizaje no supervisado basado en clustering
# KMeans
# https://www.youtube.com/watch?v=w2wzVg0owxU