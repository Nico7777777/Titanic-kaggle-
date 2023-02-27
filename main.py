from sklearn.linear_model import LogisticRegression
from numpy import random
import numpy as np
import pandas as pd
import csv

columns = ['Sex', 'Parch', 'Age', 'Embarked']
answerfile = "answer.csv"
train = "train.csv"
test = "test.csv"


def sex(arg):
    return 1 if arg == 'male' else 0


def age(the_age):
    avr = [0.07, 0.25, 0.47, 0.21]  # age values survive rates

    try:
        the_age = float(the_age)
    except ValueError:
        the_age = 100000
    if 0 <= the_age <= 8:
        return 1
    elif 8 < the_age <= 23:
        return 2
    elif 23 < the_age <= 41:
        return 3
    elif 41 < the_age <= 80:
        return 4
    else:
        return random.choice([1, 2, 3, 4], p=avr)


def checkpoint(arg):
    if arg == 'Q':
        return 1
    elif arg == 'S':
        return 2
    else:
        return 3


def advanced_preddiction():
    train_ds = pd.read_csv("train.csv", usecols=['Embarked', 'Age', 'Sex', 'Parch', 'Survived'])
    train_ds['Embarked'] = [checkpoint(arg) for arg in train_ds['Embarked']]
    train_ds['Age'] = [age(arg) for arg in train_ds['Age']]
    train_ds['Sex'] = [sex(arg) for arg in train_ds['Sex']]
    features = np.array([train_ds['Age'], train_ds['Parch'], train_ds['Sex'], train_ds['Embarked']]).swapaxes(0, 1)

    model = LogisticRegression()
    y = np.array(train_ds['Survived'])
    model.fit(features, y)

    test_ds = pd.read_csv("test.csv", usecols=['Embarked', 'Age', 'Sex', 'Parch', 'PassengerId'])
    test_ds['Embarked'] = [checkpoint(arg) for arg in test_ds['Embarked']]
    test_ds['Age'] = [age(arg) for arg in test_ds['Age']]
    test_ds['Sex'] = [sex(arg) for arg in test_ds['Sex']]
    features = np.array([test_ds['Age'], test_ds['Parch'], test_ds['Sex'], test_ds['Embarked']]).swapaxes(0, 1)
    pred = model.predict(features)
    print(pred[0])

    with open("answer_sheet.csv", 'w') as f:
        results = csv.writer(f, lineterminator='\n')
        results.writerow(["PassengerId", "Survived"])
        for i in range(418):
            results.writerow([test_ds['PassengerId'][i], pred[i]])


if __name__ == "__main__":
    random.seed(0)
    advanced_preddiction()
