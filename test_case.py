# 계산기
# 3+3, 3-3과 같이 입력하세요.
# +, -, /, *, 총 4가지 연산을 지원합니다.

from unittest import *

def number_separate(formula):
    oper = ['+', '-', '*', '/']
    user_number = []
    for i in formula:
        if i in oper:
            # oper 리스트에 있는 문자열을 만나면 그 앞의 문자들을 user_number에 추가
            user_number.append(formula[:formula.index(i)])
            # 숫자 추가 후 숫자와 연산자 제거
            formula = formula[formula.index(i) + 1:]
    # 연산자가 없는 경우 남은 문자를 user_number에 추가
    user_number.append(formula)
    # user_number 리스트를 int형으로 변환
    user_number = list(map(int, user_number))
    return user_number

def oper_separate(formula):
    oper = ['+', '-', '*', '/']
    user_oper = []
    for i in formula:
        if i in oper:
            user_oper.append(i)
            # 숫자 추가 후 숫자와 연산자 제거
            formula = formula[formula.index(i) + 1:]
    return user_oper

# 연산을 수행하고 결과를 출력하는 calc 함수
def calc(user_oper, user_number):
    initial_value = user_number[0]
    for i in user_oper:
        operator = user_oper.index(i)
        if i == '*':
            # * 연산자를 만나면 연산자 기준 앞, 뒤의 숫자들을 곱해서 multiple 변수에 넣음
            multiple = user_number[operator] * user_number[operator+1]
            # 연산에 사용된 숫자들은 리스트에서 제거
            user_number.pop(operator)
            user_number.pop(operator)
            # 연산 결과를 숫자 리스트에 삽입
            user_number.append(multiple)
            # 연산에 사용된 연산자 제거
            user_oper.pop(operator)
            if len(user_number) == 1:
                return user_number[0]
        elif i == '/':
            division = user_number[operator] // user_number[operator+1]
            user_number.pop(operator)
            user_number.pop(operator)
            user_number.insert(0,division)
            user_oper.remove(i)
            if len(user_number) == 1:
                return user_number[0]
    if user_oper[0] == '*':
        multiple = user_number[operator] * user_number[operator + 1]
        return multiple
    elif user_oper[0] == '/':
        division = user_number[operator] // user_number[operator + 1]
        return division
    for i in range(len(user_oper)):
        if user_oper[i] == '+':
            initial_value += user_number[i + 1]
        elif user_oper[i] == '-':
            initial_value -= user_number[i + 1]
    return initial_value

def main():
    # 계산을 원하는 식을 입력(ex: 3+3, 1*2...)
    formula = input()
    number_separate(formula)
    oper_separate(formula)
    print(f'result: {calc(oper_separate(formula), number_separate(formula))}')

class customtest(TestCase):
    def test_sum_units_digit(self):
        self.assertEqual(calc(['+', '+'],[1, 2, 3]), 6)
    def test_sub_units_digit(self):
        self.assertEqual(calc(['+', '-', '+'], [1, 2, 3, 4]), 4)
    def test_mul_tenth_digit(self):
        self.assertEqual(calc(['+', '*'],[12, 2, 3]), 18)

if __name__ == '__main__':
    main()