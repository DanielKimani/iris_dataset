import numpy as np
import pandas as pd
from sklearn import svm

def create_flower_species_dict(iris_pd):

    uniq_items = iris_pd['species'].unique()
    num_items = len(uniq_items)

    return dict(zip(uniq_items, range(num_items)))

def process_data():

    iris_pd = pd.read_csv("iris.csv")
    flower_species_dict = create_flower_species_dict(iris_pd)
    iris_pd['species_map'] = iris_pd['species'].map(flower_species_dict).astype(int)

    matrix_dropped = iris_pd.drop(["species"], axis = 1)
    matrix_prime = matrix_dropped.sample(frac = 1).reset_index(drop = True)

    return matrix_prime

def svm_predict():
    d = process.process_data()

    X = d.ix[:,:-1]
    y = d.ix[:,-1]

    X_train, X_test = X[:-20], X[-20:]
    y_train, y_test = y[:-20], y[-20:]

    clf = svm.SVC()
    clf.fit(X_train, y_train)
    return clf.predict(X_test, y_test)
    #np.mean(clf.predict(X_test) == y_test)
