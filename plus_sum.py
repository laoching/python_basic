# 10번 안에 숫자 맞추기

import random

cnt = 10
#1부터 999까지의 난수 생성
#randrange(a,b) -> a부터 b-1까지의 랜덤한 숫자
#randint(a,b) -> a부터 b까지의 랜덤한 숫자
ran = random.randrange(1, 1000)
while cnt > 0:
    n = int(input("input number: "))
    if n < 1 or n > 1000:
        print("wrong number!")
        print("chance: ",cnt)
        continue
    if n > ran:
        cnt -= 1
        print("not correct!! input smaller number")
        print("chance: ",cnt)
    elif n < ran:
        cnt -= 1
        print("not correct!! input bigger number")
        print("chance: ",cnt)
    elif n == ran:
        print("random number:", n)
        print("program End")
        break
print("answer is: ", ran)