import random


def addition(x):
    if 0 < x < 5:
        firstNum = random.randint(0, 100)
        secondNum = random.randint(0, 100)
        print(firstNum, "+", secondNum, '=?')
        return float((firstNum + secondNum))
    elif 4 < x < 7:
        firstNum = round(random.uniform(0, 100), 2)
        secondNum = round(random.uniform(0, 100), 2)
        print(firstNum, "+", secondNum, '=?')
        return float((firstNum + secondNum))
