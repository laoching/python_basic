a='abcdefg'
a=list(a)   # 문자열을 리스트로 변환
s = input() # 위 리스트에서 인덱스를 찾고싶은 문자열 입력
for i in range(len(a)):
    if a[i] == s:   # 리스트를 한바퀴씩 돌면서 입력한 문자열이 있는지 찾아봄
        print(a.index(s))
        break
else:
    print('없어요')