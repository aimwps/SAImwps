from sklearn.model_selection import train_test_split
from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
adult_df = pd.read_csv("data/adult_clean_ehc.csv")

Y = adult_df['target'].replace({" <=50K": 0, " >50K": 1})
print(Y)


X = adult_df.drop(['target','fnlwgt','education-num','marital-status','education','workclass','relationship','occupation','sex','race','relationship','native-country'], axis=1)

x_train, x_test, y_train, y_test = train_test_split(X,Y, random_state=909)
#svc = svm.SVC(random_state=909).fit(x_train, y_train)
def SVM_on_ehc():
    print("")
    params = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
    svc = svm.SVC(random_state=0)
    grid_clf = GridSearchCV(svc, params).fit(x_train, y_train)
    ordered_params = sorted(list(grid_clf.cv_results_))
    best_params = grid_clf.best_params_
    print(f"Ordered params are: {ordered_params}")
    print(f"The best parameters were: {best_params}")
    predict = svc.predict(x_test)
    test_score = svc.score(x_test, y_test)
    print(test_score.shape)
    print(f"the model scored: {test_score}")



def RFC_on_ehc():
    rfc = RandomForestClassifier(random_state=894)
    rfc.fit(x_train, y_train)
    predict = rfc.predict(x_test)
    score = rfc.score(x_test, y_test)
    print(predict)
    print(score)

RFC_on_ehc()
