from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

adult_df = pd.read_csv("data/adult_clean_ehc.csv")

Y = adult_df['target'].replace({" <=50K": 0, " >50K": 1})
print(Y)

X = adult_df.drop(['target','fnlwgt','education-num','marital-status','education','workclass','relationship','occupation','sex','race','relationship','native-country'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(X,Y, random_state=909)
svc = svm.SVC(random_state=909).fit(x_train, y_train)
predict = svc.predict(x_test)
test_score = svc.score(x_test, y_test)
print(test_score)
