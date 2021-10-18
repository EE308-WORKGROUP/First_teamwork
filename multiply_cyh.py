import random

def multiply(grade):

    #有小数
    if grade == 5 or grade == 6:
        n1 = random.random() #随机0-1之间的一位小数
        n2 = random.random()

        num1 = random.randint(1,99)  #1-99之间整数
        num2 = random.randint(1,99)


        num_mod1 = num1 - round(n1,1)  #带小数
        num_mod2 = num2 - round(n2,1)
        res = num_mod1 * num_mod2

        print('{} * {} = ?'.format(num_mod1, num_mod2))
        print(res)

        return res

    # 没小数
    if grade == 3 or grade == 4:

        num3 = random.randint(1, 99)  # 1-99之间整数
        num4 = random.randint(1, 99)

        res = num3 * num4

        print('{} * {} = ?'.format(num3, num4))
        print(int(res))

        return res

