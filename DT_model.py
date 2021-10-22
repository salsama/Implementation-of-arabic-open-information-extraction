import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn import metrics
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
from dtreeviz.trees import dtreeviz
import graphviz

data = load_iris()
TrainPd = pd.read_excel('ChicagoDT.xls',sheet_name="Source")



Y = TrainPd['TotalCO']
X = TrainPd.drop(['TotalCO'], axis = 1)
#X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1) # 70% training and 30% test

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 5)
#model = XGBRegressor()
model = DecisionTreeRegressor(random_state = 0, max_depth=10)
model.fit(X_train, Y_train)
training_data_prediction = model.predict(X_train)
score_1 = metrics.r2_score(Y_train, training_data_prediction)

# Mean Absolute Error
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)
feature_names = [f'Feature {i+1}' for i in range(10)]
print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)
plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual CO2 Emmisions")
plt.ylabel("Predicted CO2 Emmisions")
plt.title("Actual CO2 Emmisions vs Preicted CO2 Emmisions")
plt.savefig

importances = model.feature_importances_
print (importances)

feature_importances = (importances / sum(importances)) * 100

print(feature_importances)


TrainPd.head()

TrainPd.shape

TrainPd.isnull().sum()

TrainPd.describe()
correlation = TrainPd.corr()
fig=plt.figure(figsize=(10,10))

sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

fig.savefig("ASCS.png")
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(model, filled=True)
dot_data = tree.export_graphviz(model, out_file=None,

                                filled=True)
fig1=graphviz.Source(dot_data,format="png")
fig1.save("SSSS.png")
from dtreeviz.trees import dtreeviz # remember to load the package

viz = dtreeviz(model, X_train, Y_train,
                target_name="TotalCO"

                )

viz.save("sddfs.svg")