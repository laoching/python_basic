import random

print('가위 바위 보 게임입니다.')
w = l = d = 0
while True:
    # 컴퓨터는 랜덤한 값으로 생성
    com_input = random.randint(1, 3)
    # 사람은 가위 바위 보 중 하나를 입력 받음
    user = input('가위(s) 바위(r) 보(p) 중 1가지를 입력하세요: ')
    user_trans = 0
    # 사람이 입력한 값을 컴퓨터와 비교하기 위해 숫자로 바꿔줌
    if user == 's' or user == 'r' or user == 'p':
        if user == 's':
            user_trans = 2
        elif user == 'r':
            user_trans = 1
        elif user == 'p':
            user_trans = 3

        # 승패 판단을 위한 공식
        judge = (user_trans - com_input + 3) % 3

        if judge == 0:
            d += 1
            print('draw!')
        elif judge == 1:
            w += 1
            print('You win!')
        elif judge == 2:
            l += 1
            print('Computer win!')
    else:
        print('가위 바위 보 중 한가지를 선택해주세요.')
    print('승리: {}\n'
          '패배: {}\n'
          '무승부: {}\n'.format(w, l, d))
