import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.pipeline import make_pipeline
from sklearn import tree
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

c_df = pd.read_csv('Concrete_Data.csv')

c_df.columns = ['cement', 'BG Slag', 'Fly Ash', 'Water', 'Superplasticizer', 'Coarse Aggregate', 'Fine Aggregate', 'Age', 'Compressive Strength']

c_X = c_df.drop('Compressive Strength', axis=1)
c_Y = c_df['Compressive Strength']


X, x, Y, y = train_test_split(c_X, c_Y, test_size=0.2, random_state=894)



def concrete_settings_tester(mdi, mssi, msli):
    best_score = (0,0,0,0,0)
    all_data = []
    criterion = ['mse', 'mae']
    for i,c in enumerate(criterion):
        for md in range(1, mdi+1):
            for mss in range(2, mssi+1):
                for msl in range(1, msli+1):
                    clf = RandomForestRegressor(criterion=c, max_depth=md, min_samples_split=mss, min_samples_leaf=msl, random_state=894)
                    clf.fit(X, Y)
                    score = clf.score(x,y)
                    if score > best_score[0]:
                        best_score = (score, c, md, mss, msl)
                        all_data.append((score, c, md, mss, msl))
                    print(f"CBS: {round(best_score[0],2)} | Checking Criterion: {c}, {i+1}/2 | max_depth:{md}/{mdi}| Criterion: {c} | min_samples_split: {mss}/{mssi} | min_samples_leaf: {msl}/{msli}")
    print(f"best_score: {best_score[0]}, Criterion:{best_score[1]} max_depth: {best_score[2]}, max_samples_split: {best_score[3]},  min_samples_leaf: {best_score[4]}")

concrete_settings_tester(12, 8, 5)
