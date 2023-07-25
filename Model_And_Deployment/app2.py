from flask import Flask, request, render_template
import os
import numpy as np
import pandas as pd
from sklearn import tree
import math

app = Flask(__name__)

def stringToInt(string):
    integer = 0
    # check if the string is NaN
    if isinstance(string, float) and math.isnan(string):
        return 0
    try:
        # means string value given is already a int
        integer = int(string)
    except:
        string = string.lower()
        for i in string:
            integer += ord(i)
    return integer


def stringToFloat(string):
    try:
        # if the string is already a number, return the float value
        return float(string)
    except:
        # if the string contains non-numeric characters, return the sum of their ASCII values as a float
        total = 0.0
        for char in string:
            total += ord(char)
        return total


data = pd.read_csv("ultimate.csv", encoding="latin-1")

data = data.values.tolist()

X_train = []
y_train = []


for i in range(len(data)):
    X_train.append([data[i][1], data[i][4], data[i][5], data[i][6], data[i][7], data[i][8]])
    y_train.append([data[i][2], data[i][3]])

for i in range(len(X_train)):
    for x in range(len(X_train[i])):
        X_train[i][x] = stringToInt(X_train[i][x])

for i in range(len(y_train)):
    for y in range(len(y_train[i])):
        y_train[i][y] = int(stringToFloat(y_train[i][y]) * 10)


model = tree.DecisionTreeClassifier()

model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    genre = request.form['genre']
    genre = genre.lower()
    genre = stringToInt(genre)

    director = request.form['director']
    director = director.lower()
    director = stringToInt(director)

    actor1 = request.form['actor1']
    actor1 = actor1.lower()
    actor1 = stringToInt(actor1)

    actor2 = request.form['actor2']
    actor2 = actor2.lower()
    actor2 = stringToInt(actor2)

    actor3 = request.form['actor3']
    actor3 = actor3.lower()
    actor3 = stringToInt(actor3)

    actor4 = request.form['actor4']
    actor4 = actor4.lower()
    actor4 = stringToInt(actor4)

    prediction = model.predict([[genre, director, actor1, actor2, actor3, actor4]])

    rating = round(prediction[0][0]/10, 1)
    metascore = round(prediction[0][1]/10, 1)

    return render_template('result.html', rating=rating, metascore=metascore)

if __name__ == '__main__':
    app.run(debug=True)
