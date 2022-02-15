# 계산기
# 3+3, 3-3과 같이 입력하세요.
# +, -, /, *, 총 4가지 연산을 지원합니다.

import re

# 연산을 수행하고 결과를 출력하는 calc 함수
def calc(user_oper, user_number):
    sum = user_number[0]
    for i in range(len(user_oper)):
        if user_oper[i] == '+':
            sum += user_number[i + 1]
        elif user_oper == '-':
            sum -= user_number[i + 1]
        elif user_oper == '*':
            sum *= user_number[i + 1]
        elif user_oper == '/':
            sum /= user_number[i + 1]
    return sum

def main():
    # 계산을 원하는 식을 입력(ex: 3+3, 1*2...)
    formula = input()
    oper = ['+', '-', '*', '/']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    user_oper = []
    user_number = []
    num_loca = []
    oper_loca = []
    for i in formula:
        if i in oper:
            user_oper.append(i)
            oper_loca.append(formula.index(i))
        elif i in num:
            user_number.append(i)
            num_loca.append(formula.index(i))
            user_number = list(map(int, user_number))

    print("num_loca:",num_loca)
    print("oper_loca:",oper_loca)
    #print(user_oper)
    print(user_number)
    #print(calc(user_oper, user_number))

if __name__ == '__main__':
    main()
