import random

def subtraction ( x ):
    if (0 < x < 5):
        firstNum = random.randint(0,100)
        secondNum = random.randint(0,100)
    elif(6 >= x >=5):
        firstNum = round(random.uniform(0,100),2)
        secondNum = round(random.uniform(0,100),2)
    print(firstNum, "-", secondNum)
    return (firstNum - secondNum)
dskdksf