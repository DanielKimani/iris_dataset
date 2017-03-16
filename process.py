from csv import reader
import numpy as np
import pandas as pd



def create_flower_species_dict(iris_pd):

    uniq_items = iris_pd['species'].unique()
    num_items = len(uniq_items)

    return dict(zip(uniq_items, num_items))

def process_data():

    iris_pd = pd.read_csv("iris.csv")
    flower_species_dict = create_flower_species_dict(iris_pd)
    iris_pid = iris['species_as_num'].map(flower_species_dict).astype(int)


# lol take a break here to do rainbow push project


