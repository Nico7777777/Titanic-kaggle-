from numpy import random
import csv

answerfile = "answer.csv"
filename = "test.csv"
new_column = "Survived"
age = 0


def sex_rate(arg):
    SVSR = [0.12, 0.26]  # sex values survive rates
    if arg == 'male':
        return SVSR[0]
    else:
        return SVSR[1]

def age_rate(arg):
    AVSR = [0.02, 0.075, 0.15, 0.059, 0.059] # age values survive rates

    try:
        age = float(line[4])
    except ValueError:
        age = 100000
    if age >= 0 and age <= 8:
       return AVSR[0]
    elif age > 8 and age <= 23:
        return AVSR[1]
    elif age > 23 and age <= 41:
        return AVSR[2]
    elif age > 41 and age <= 80:
        return AVSR[3]
    else:
        return AVSR[4]

def preddiction(sex_arg, age_arg):
    survive_percentage = (age_rate(age_arg) + sex_rate(sex_arg))/2
    return random.choice([1, 0], 1, p=[survive_percentage, 1-survive_percentage])[0]
    
if __name__ == "__main__":
    random.seed(0)
    with open(filename, 'r') as f:
        with open(answerfile, 'w') as g:
            test = csv.writer(g, lineterminator='\n')
            answer = csv.reader(f)

            all = [] # matricea cu raspunsuri
            line = next(answer)[:1] # coloana cu PassengerID-ul
            line.append(new_column) # bagam a coloana cu Survive
            all.append(line) # header-ul

            for line in answer:
                preddict = preddiction(line[3], line[4])
                line = line[:1]
                line.append(preddict) #aici trebuie sa inlocuiesc
                all.append(line)

            test.writerows(all)