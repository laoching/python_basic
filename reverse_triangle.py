# 삼각형 출력

for i in range(5):
    # 공백을 넣어주는 역할, 카운터 변수가 사용되지 않아서 _을 사용
    for _ in range(5-i-1):
        print(' ',end=' ')
    # 실제로 삼각형을 만들어 주는 부분
    for j in range(i+1):
        print('*', end=' ')
    for k in range(i):
        print('*', end=' ')
    print()