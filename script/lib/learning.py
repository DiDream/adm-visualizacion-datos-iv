from sklearn.model_selection import train_test_split, cross_val_score, ShuffleSplit
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston


class LearningAlgorithm:
    def __init__(self, data, x, y, args):
        self.data = data
        self.x = x
        self.y = y
        self.args = args

    def run(self):
        pass


# algoritmo de aprendizaje de supervisado de clasificación
class SupervisedLearningAlgorithm(LearningAlgorithm):
    name = 'Supervised Learning Algorithm'

    def __init__(self, data, x, y, args):
        if x is None:
            x = data.columns.tolist()
        super().__init__(data, x, y, args)
        self.test_size = args.test_size

    def object_to_int(self, column_name):
        values = self.data[column_name].unique().tolist()
        self.data[column_name].replace(values, range(len(values)), inplace=True)

    def process_data(self):
        for column in self.x:
            if self.data.dtypes[column] == 'object':
                self.object_to_int(column)

        x = self.data[self.x]
        if self.y in x:
            x = x.drop([self.y], 1)
        x = np.array(x)

        y = np.array(self.data[self.y])
        return x, y

    def show_model_accuracy(self, model, X_train, X_test, y_train, y_test):
        y_pred = model.predict(X_test)

        # Representación de la precisión del modelo
        from sklearn.metrics import confusion_matrix
        matrix = confusion_matrix(y_test, y_pred)

        print('Matriz confusión')
        print(matrix)

        from sklearn.metrics import precision_score
        print('precision_score', precision_score(y_test, y_pred))

        # https://www.youtube.com/watch?v=L_dQrZZjGDg&ab_channel=DataTalks
        cv = ShuffleSplit(n_splits=7, test_size=self.test_size, random_state=0)
        scores = cross_val_score(model, X_train, y_train, cv=cv)
        print('cross_val_score', scores.mean())

        fig = plt.figure()
        fig.suptitle('{} score {:.3f}'.format(self.name, scores.mean()))
        ax = sns.boxplot(x=scores)
        ax.set_xlabel('scores')
        plt.show()


# NAIVE BAYES
# https://www.youtube.com/watch?v=P930ev-eyVk&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=49
class NaiveBayesAlgorithm(SupervisedLearningAlgorithm):
    name = 'Naive Bayes'

    def run(self):
        x, y = self.process_data()

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=self.test_size)

        from sklearn.naive_bayes import GaussianNB

        algorithm = GaussianNB()
        algorithm.fit(X_train, y_train)

        self.show_model_accuracy(algorithm, X_train, X_test, y_train, y_test)


# https://www.youtube.com/watch?v=ZeRblDJ-Jug&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=50
class DecisionTreeClassifierAlgorithm(SupervisedLearningAlgorithm):
    name = 'Decision Tree Classifier'

    def run(self):
        x, y = self.process_data()
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=self.test_size)

        from sklearn.tree import DecisionTreeClassifier
        algorithm = DecisionTreeClassifier(max_depth=self.args.max_depth, criterion='entropy')
        algorithm.fit(X_train, y_train)

        self.show_model_accuracy(algorithm, X_train, X_test, y_train, y_test)


# un algoritmo de aprendizaje de supervisado de regresión
# https://www.youtube.com/watch?v=gP2X8a3LaTM
# ÁRBOLES DE DECISIÓN REGRESIÓN
class DecisionTreeRegressionAlgorithm(SupervisedLearningAlgorithm):
    name = 'Decision Tree Regression'

    def run(self):
        # boston = load_boston()
        # x, y = boston.data, boston.target

        x, y = self.process_data()
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=self.test_size)

        from sklearn.tree import DecisionTreeRegressor
        algorithm = DecisionTreeRegressor(max_depth=self.args.max_depth)
        algorithm.fit(X_train, y_train)

        self.show_model_accuracy(algorithm,X_train, X_test, y_train, y_test)

    def show_model_accuracy(self, model, X_train, X_test, y_train, y_test):
        y_pred = model.predict(X_test)
        score = model.score(X_test, y_test)
        print('model score', score)

        cv = ShuffleSplit(n_splits=7, test_size=self.test_size, random_state=0)
        scores = cross_val_score(model, X_train, y_train, cv=cv)
        print('cross_val_score', scores.mean())

        fig, (axPred, axScore) = plt.subplots(ncols=2)
        fig.suptitle('{} prediction'.format(self.name))

        axPred.scatter(y_test, y_pred)
        axPred.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
        axPred.set_title('Predictions')
        axPred.set_xlabel('correct values')
        axPred.set_ylabel('predictions')

        axScore.set_xlabel('scores')
        axScore.set_title('Score {:.3f}'.format(scores.mean()))
        sns.boxplot(x=scores, ax=axScore)

        plt.show()


# algoritmo de aprendizaje no supervisado basado en clustering
class NoSupervisedLearningAlgorithm(LearningAlgorithm):
    pass


# KMeans
# https://www.youtube.com/watch?v=w2wzVg0owxU
class KMeansAlgorithm(NoSupervisedLearningAlgorithm):
    def __init__(self, data, x, y, args):
        super().__init__(data, x[0], y, args)
        self.n_clusters = args.n_clusters

    def run(self):
        from sklearn.cluster import KMeans

        x = self.data[self.x].values
        y = self.data[self.y].values
        X = np.array(list(zip(x, y)))

        algorithm = KMeans(n_clusters=self.n_clusters)
        algorithm = algorithm.fit(X)
        labels = algorithm.predict(X)
        centroids = algorithm.cluster_centers_
        colors = ['red', 'green', 'blue', 'yellow', 'fuchsia']

        assigned_colors = []
        for row in labels:
            assigned_colors.append(colors[row])

        plt.scatter(x, y, c=assigned_colors, s=5)
        plt.scatter(centroids[:, 0], centroids[:, 1], c=colors[:len(centroids)], marker='*', zorder=10)
        plt.show()

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