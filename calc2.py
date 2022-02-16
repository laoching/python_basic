# 계산기
# 3+3, 3-3과 같이 입력하세요.
# +, -, /, *, 총 4가지 연산을 지원합니다.

# 연산을 수행하고 결과를 출력하는 calc 함수
def calc(user_oper, user_number):
    hap = user_number[0]
    for i in user_oper:
        if i == '*':
            gop = user_number[user_oper.index(i)] * user_number[user_oper.index(i)+1]
            user_number.pop(user_oper.index(i))
            user_number.pop(user_oper.index(i))
            user_number.append(gop)
            user_oper.pop(user_oper.index(i))
            if len(user_number) == 1:
                return user_number[0]
        elif i == '/':
            na = user_number[user_oper.index(i)] // user_number[user_oper.index(i)+1]
            user_number.pop(user_oper.index(i))
            user_number.pop(user_oper.index(i))
            user_number.insert(0,na)
            user_oper.remove(i)
            if len(user_number) == 1:
                return user_number[0]
    if user_oper[0] == '*':
        gop = user_number[user_oper.index(i)] * user_number[user_oper.index(i) + 1]
        return gop
    elif user_oper[0] == '/':
        na = user_number[user_oper.index(i)] // user_number[user_oper.index(i) + 1]
        return na
    for i in range(len(user_oper)):
        if user_oper[i] == '+':
            hap += user_number[i + 1]
        elif user_oper[i] == '-':
            hap -= user_number[i + 1]
    return hap

def main():
    # 계산을 원하는 식을 입력(ex: 3+3, 1*2...)
    formula = input()
    oper = ['+', '-', '*', '/']
    #num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    user_oper = []
    user_number = []
    for i in formula:
        if i in oper:
            user_oper.append(i)
            # oper 리스트에 있는 문자열을 만나면 그 앞의 문자들을 user_number에 추가
            user_number.append(formula[:formula.index(i)])
            # 숫자 추가 후 숫자와 연산자 제거
            formula = formula[formula.index(i) + 1:]
    # 연산자가 없는 경우 남은 문자를 user_number에 추가
    user_number.append(formula)
    # user_number 리스트를 int형으로 변환
    user_number = list(map(int, user_number))
    print('result: {}'.format(calc(user_oper, user_number)))


if __name__ == '__main__':
    main()
