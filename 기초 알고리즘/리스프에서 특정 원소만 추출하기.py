# ex) [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2를 제외한 나머지만 추출하기
list = [1, 2, 2, 2, 3, 1, 1, 3, 2]
answer = []
for i in list:
    if i != 2:
        print(i)