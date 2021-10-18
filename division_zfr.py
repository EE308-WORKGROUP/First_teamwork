import random

#定义函数：
def div_num(grade):
    print('当前等级：',grade)
    if grade == 3 or grade == 4:
        Num1 = random.randint(0, 10)
        Num2 = random.randint(1, 10)


    if grade == 5 or grade == 6:
        Num1 = float(format(random.uniform(0, 10), '.2f'))
        Num2 = float(format(random.uniform(1, 10), '.2f'))

    print(Num1, '/', Num2, '=?')
    result = float(format((Num1 / Num2), '.2f'))

    return result

#输入等级
while(True):
    in_num = int(input('Please enter a grade(1~6):'))
    if in_num not in range(1,7):
        print('Wrong!')
    else:
        grade = in_num
        print(grade)
        break
#输出结果
print(div_num(grade))





