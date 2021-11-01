# 원소의 갯수를 카운터하기
# ex) [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2의 갯수를 카운팅
num = [1, 2, 2, 2, 3, 1, 1, 3, 2]
answer = 0
for n in num:
    if n == 2:
        answer += 1
print(answer)
# print(f'2의 개수 {answer}개')
