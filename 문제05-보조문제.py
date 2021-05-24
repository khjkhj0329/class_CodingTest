
# 1부터 해당하는 숫자까지
# 박수를 총 몇 번 쳐야 하는가?

a = 7

카운터 = 0

for num in range(1, a+1):
# 해당하는 숫자는 박수를 몇 번 쳐야 하는가?
    while num:
        if num % 10 == 3 or num % 10 == 6 or num % 10 ==9:
            카운터 += 1
        num = num // 10  # 몫 구하기

print(카운터)
