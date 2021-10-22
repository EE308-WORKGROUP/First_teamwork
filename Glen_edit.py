import random
import addition
import multiply_cyh
import subtraction
import division_zfr

flag = True


# 加减乘除函数选择器（type1等于加减乘除分别对应1 2 3 4，grade对应年级1-6）返回答案
def calculationtypeselect(type1, grade):
    if type1 == 1:
        res = addition.addition(grade)

    elif type1 == 2:
        res = subtraction.subtraction(grade)

    elif type1 == 3:
        res = multiply_cyh.multiply(grade)

    elif type1 == 4:
        res = division_zfr.div_num(grade)

    return res


correctNumber = 0
# 过滤年级输入和问题数量中的非数字输入
while True:
    yourGrade = input("Please enter your grade?")
    yourGrade = yourGrade.replace(" ", "")  #
    if yourGrade in ['1', '2', '3', '4', '5', '6']:
        break
    else:
        print("Please enter correct grade from 1 to 6")

while True:
    yourNumberOfQuestion = input("Please enter the number of questions(1-10)")
    yourNumberOfQuestion = yourNumberOfQuestion.replace(" ", "")
    if yourNumberOfQuestion in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        break
    else:
        print("Please enter correct number of the question from 1 to 10")

yourGrade = int(yourGrade)
yourNumberOfQuestion = int(yourNumberOfQuestion)

for i in range(yourNumberOfQuestion):

    if yourGrade == 1 or yourGrade == 2:

        yourType = random.randint(1, 2)

    elif yourGrade == 3 or yourGrade == 4 or yourGrade == 5 or yourGrade == 6:

        yourType = random.randint(3, 4)

    result = calculationtypeselect(yourType, yourGrade)
    print("result is:", result)
    # 过滤答案输入中的不合理输入，即非数字（可使用空格）
    while True:
        answer = input()
        if (answer.count(".") == 1 and not answer.startswith(".") and not answer.endswith(".")) or (
                answer.count(".") == 0):
            answerDotAndSpaceFilter = answer.replace(".", "")
            answerDotAndSpaceFilter = answerDotAndSpaceFilter.replace(" ", "")
            if answerDotAndSpaceFilter.isdigit():
                answer = answer.replace(" ", "")
                break
            else:
                print("Please input a valid number:")
                continue
        else:
            print("Please input a valid number:")

    print("your answer is:", answer)
    answer = float(answer)
    if result == answer:
        correctNumber = correctNumber + 1

if correctNumber == yourNumberOfQuestion:
    print("End! All right, that's great! Your score is 100")
elif correctNumber < yourNumberOfQuestion:
    print("End! Wrong question, your score is ", 100 / yourNumberOfQuestion * correctNumber)
