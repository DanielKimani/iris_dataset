import numpy as np
import pandas as pd

def create_flower_species_dict(iris_pd):

    uniq_items = iris_pd['species'].unique()
    num_items = len(uniq_items)

    return dict(zip(uniq_items, range(num_items)))

def process_data():

    iris_pd = pd.read_csv("iris.csv")
    flower_species_dict = create_flower_species_dict(iris_pd)
    iris_pd['species_map'] = iris_pd['species'].map(flower_species_dict).astype(int)


    return iris_pd.drop(["species"], axis = 1)

print( process_data().head())
