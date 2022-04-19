# 계산기
# 3+3, 3-3과 같이 입력하세요.
# +, -, /, *, 총 4가지 연산을 지원합니다.
# 20220330 수정


def parse_formula(formula):
    oper = ['+', '-', '*', '/']
    user_oper = []
    user_number = []
    # 분리했던 숫자와 연산자들을 합쳐서 넣는 리스트
    combine_formula = []
    cnt = 1
    for i in formula:
        if i in oper:
            # oper 리스트에 있는 문자열을 만나면 그 앞의 문자들을 user_number에 추가
            user_number.append(formula[:formula.index(i)])
            # 숫자 추가 후 숫자와 연산자 제거
            user_oper.append(i)
            # 숫자 추가 후 숫자와 연산자 제거
            formula = formula[formula.index(i) + 1:]
    # 연산자가 없는 경우 남은 문자를 user_number에 추가
    user_number.append(formula)
    # user_number 리스트를 int형으로 변환 -> 이거 하려고 숫자랑 연산자 리스트 따로 만들었다.
    user_number = list(map(int, user_number))
    # 연산자의 개수만큼 반복문을 돌림
    for i in range(0, len(user_oper)):
        # 나눠놨던 숫자와 연산자를 합칩니다. 숫자를 먼저 넣습니다.
        combine_formula.append(user_number[i])
        combine_formula.append(user_oper[i])
        # cnt는 combine_formula 리스트에 있는 숫자+연산자의 개수를 의미함 
        cnt += 1
        # combine_formula의 길이와 사용자 입력에 있는 숫자의 개수와 비교
        if cnt == len(user_number):
            # 남은 1개의 숫자를 combine_formula 리스트에 추가
            combine_formula.append(user_number[cnt - 1])
    print(combine_formula)
    return combine_formula


def calc(combine_formula):
    for i in combine_formula:
        #if len(combine_formula) == 1:
            #continue
        if i == '*':
            # * 연산자를 만나면 연산자 기준 앞, 뒤의 숫자들을 곱해서 multiple 변수에 넣음
            multiple = combine_formula[combine_formula.index(i) - 1] * combine_formula[combine_formula.index(i) + 1]
            # 연산에 사용된 숫자, 연산자는 리스트에서 제거
            print(multiple)
            combine_formula.pop(combine_formula.index(i) - 1)
            print(combine_formula)
            combine_formula.pop(combine_formula.index(i))
            print(combine_formula)
            # 연산 결과를 다시 리스트에 삽입
            combine_formula.insert(combine_formula.index(i) - 1, multiple)
        if i == '/':
            division = combine_formula[combine_formula.index(i) - 1] // combine_formula[
                combine_formula.index(i) + 1]
            combine_formula.pop(combine_formula.index(i) - 1)
            combine_formula.pop(combine_formula.index(i))
            combine_formula.insert(combine_formula.index(i) - 1, division)

    initial_value = combine_formula[0]
    for i in range(len(combine_formula)):
        if combine_formula[i] == '/':
            initial_value /= combine_formula[i + 1]
        elif combine_formula[i] == '*':
            initial_value *= combine_formula[i + 1]
        elif combine_formula[i] == '+':
            initial_value += combine_formula[i + 1]
        elif combine_formula[i] == '-':
            initial_value -= combine_formula[i + 1]

    return initial_value


def main():
    # 계산을 원하는 식을 입력(ex: 3+3, 1*2...)
    formula = input()
    print(f'result: {calc(parse_formula(formula))}')


if __name__ == '__main__':
    main()
