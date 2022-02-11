# 1부터 n까지의 합 구하기(n>0)

while True:
    n = int(input("n을 입력하세요: "))
    if n > 0:
        break
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print('1부터 n까지의 합: ',sum)