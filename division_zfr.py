import random


# 定义函数：
def div_num(grade):
    if grade == 3 or grade == 4:
        Num1 = random.randint(0, 10)
        Num2 = random.randint(1, 10)
        print('{} / {} = ?'.format(Num1, Num2))
        result = round(Num1 / Num2, 2)
        return float(result)

    if grade == 5 or grade == 6:
        Num1 = float(format(random.uniform(0, 10), '.2f'))
        Num2 = float(format(random.uniform(1, 10), '.2f'))
        print('{} / {} = ?'.format(Num1, Num2))
        result = round(Num1 / Num2, 2)
        return float(result)
