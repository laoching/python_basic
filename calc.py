<<<<<<< HEAD
# 계산기
# 3+3, 3-3과 같이 입력하세요.
# +, -, /, *, 총 4가지 연산을 지원합니다.

# 연산을 수행하고 결과를 출력하는 calc 함수
def calc(first, user_oper, second):
    if user_oper == '+':
        return first+second
    elif user_oper == '-':
        return first-second
    elif user_oper == '*':
        return first*second
    elif user_oper == '/':
        return first/second

def main():
    # 계산을 원하는 식을 입력(ex: 3+3, 1*2...)
    formula = input()
    oper = ['+', '-', '*', '/']

    for i in formula:
        if i in oper:
            location = formula.index(i)
            user_oper = i
    first = int(formula[:location])
    second = int(formula[location+1:])
    print(calc(first, user_oper, second))

if __name__ == '__main__':
    main()
=======
# 계산기
# 3+3, 3-3과 같이 입력하세요.
# +, -, /, *, 총 4가지 연산을 지원합니다.

# 연산을 수행하고 결과를 출력하는 calc 함수
def calc(first, user_oper, second):
    if user_oper == '+':
        print(first+second)
    elif user_oper == '-':
        print(first-second)
    elif user_oper == '*':
        print(first*second)
    elif user_oper == '/':
        print(first/second)

# 계산을 원하는 식을 입력(ex: 3+3, 1*2...)
formula = input()
oper = ['+', '-', '*', '/']

for i in formula:
    if i in oper:
        location = formula.index(i)
        user_oper = i
first = int(formula[:location])
second = int(formula[location+1:])
calc(first, user_oper, second)
>>>>>>> 0f4bec57d53ba3230adac00a9a3951ab81854103
