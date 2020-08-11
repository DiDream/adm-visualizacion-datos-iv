from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt


class LearningAlgorithm:
    def __init__(self):
        pass

    def run(self):
        pass


# algoritmo de aprendizaje de supervisado de clasificación
class SupervisedLearningAlgorithm(LearningAlgorithm):
    pass


# NAIVE BAYES
# https://www.youtube.com/watch?v=P930ev-eyVk&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=49
class NaiveBayesAlgorithm(SupervisedLearningAlgorithm):
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
class DecisionTreeClassifierAlgorithm(SupervisedLearningAlgorithm):
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
class DecisionTreeRegressionAlgorithm(SupervisedLearningAlgorithm):
    def run(self):
        dataset = datasets.load_boston()

        # Columna 6 del dataset
        x = dataset.data[:, np.newaxis, 5]
        y = dataset.target

        plt.scatter(x, y)
        plt.show()

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        from sklearn.tree import DecisionTreeRegressor
        algorithm = DecisionTreeRegressor(max_depth=5)
        algorithm.fit(x_train, y_train)

        algorithm.predict(x_test)
        # score = algorithm.score(x_test, y_test)


# algoritmo de aprendizaje no supervisado basado en clustering
class NoSupervisedLearningAlgorithm(LearningAlgorithm):
    pass


# KMeans
# https://www.youtube.com/watch?v=w2wzVg0owxU
class KMeansAlgorithm(NoSupervisedLearningAlgorithm):
    def run(self):
        import pandas as pd
        from sklearn.cluster import KMeans

        dataset = pd.read_csv('moviescs.csv')
        x = dataset['cast_total_facebook_likes'].values
        y = dataset['imdb_score'].values

        X = np.array(list(zip(x, y)))
        algorithm = KMeans(n_clusters=4)
        algorithm = algorithm.fit(X)
        labels = algorithm.predict(X)
        centroids = algorithm.cluster_centers_
        colors = ['red', 'green', 'blue', 'yellow', 'fuchsia']

        assigned_colors = []
        for row in labels:
            assigned_colors.append(colors[row])

        plt.scatter(x, y, c=assigned_colors, s=5)
        plt.scatter(centroids[:, 0], centroids[:, 1], c=colors[:len(centroids)], marker='*', zorder=10)
        #plt.show()

        #sse = self.get_sse(X, labels, centroids)

    def get_sse(self, cases, labels, centroids):
        sse = 0
        for i in range(len(cases)):
            label = labels[i]
            sse += np.linalg.norm(cases[i] - centroids[label])
        return sse


learning_constructors = {
    'naive-bayes': NaiveBayesAlgorithm,
    'tree-classifier': DecisionTreeClassifierAlgorithm,
    'tree-regression': DecisionTreeRegressionAlgorithm,
    'k-means': KMeansAlgorithm
}