import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# loading the dataset to a Pandas DataFrame
wine_dataset = pd.read_csv('winequality-red.csv')

# number of rows & columns in the dataset
wine_dataset.shape

# first 5 rows of the dataset
wine_dataset.head()

# checking for missing values
wine_dataset.isnull().sum()

# statistical measures of the dataset
wine_dataset.describe()

# number of values for each quality
sns.catplot(x='quality', data = wine_dataset, kind = 'count')

# volatile acidity vs Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x='quality', y = 'volatile acidity', data = wine_dataset)

# citric acid vs Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x='quality', y = 'citric acid', data = wine_dataset)

correlation = wine_dataset.corr()

# constructing a heatmap to understand the correlation between the columns
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt = '.1f', annot = True, annot_kws={'size':8}, cmap = 'Blues')

# separate the data and Label
X = wine_dataset.drop('quality',axis=1)

print(X)

Y = wine_dataset['quality'].apply(lambda y_value: 1 if y_value>=7 else 0)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

print(Y.shape, Y_train.shape, Y_test.shape)

model = RandomForestClassifier()

model.fit(X_train, Y_train)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy : ', test_data_accuracy)

input_data = (7.5,0.5,0.36,6.1,0.071,17.0,102.0,0.9978,3.35,0.8,10.5)

# changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the data as we are predicting the label for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==1):
  print('Good Quality Wine')
else:
  print('Bad Quality Wine')

import streamlit as st
import pickle

with open('modelj.pkl', 'wb') as m:
    pickle.dump(model, m)

with open('modelj.pkl', 'rb') as m:
    model = pickle.load(m)

st.title('Red wine detection')
st.header('User Input')

fixed_acidity = st.number_input("Enter your fuxed_acidity:", min_value=0, max_value=100,key='s1',format="%.2f")
volatile_acidity = st.number_input("Enter your volatile_acidity:", min_value=0, max_value=100,key='s2',format="%.2f")
citric_acid = st.number_input("Enter your citric_acid:", min_value=0, max_value=100,key='s3',format="%.2f")
residual_sugars = st.number_input("Enter your residual sugars:", min_value=0, max_value=100,key='s4',format="%.2f")
chlorides = st.number_input("Enter your chlorides:", min_value=0, max_value=100,key='s5',format="%.2f")
free_sulpher = st.number_input("Enter your free sulphur:", min_value=0, max_value=100,key='s6',format="%.2f")
total_sulpher = st.number_input("Enter your total sulpher:", min_value=0, max_value=100,key='s7',format="%.2f")
density = st.number_input("Enter your desnsity:", min_value=0, max_value=100,key='s8',format="%.2f")
ph = st.number_input("Enter your ph:", min_value=0, max_value=100,key='s9',format="%.2f")
sulphates = st.number_input("Enter your sulphates:", min_value=0, max_value=100,key='s10',format="%.2f")
alcohol = st.number_input("Enter your alcohol:", min_value=0, max_value=100,key='s11',format="%.2f")

input_text=np.array([fixed_acidity,volatile_acidity,citric_acid,residual_sugars,chlorides,free_sulpher,total_sulpher,density,ph,sulphates,alcohol])
input_text= input_text.reshape(1,-1)

if st.button('Predict'):
    prediction = model.predict(input_text)
    st.write('Predicted Class:', prediction)