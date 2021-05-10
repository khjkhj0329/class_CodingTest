# 펠린드롬 간단하게 만들어보기
# [0] 과 [4]를 비교
# [1] 과 [3]을 비교
# 둘 다 참이어야만 하죠
# [2]는 비교x

a = "neven"
b = "abcba"
# 5글자인 경우
# 하나라도 만족하지 못하면, 펠린드롬이 아니다.

# if a[0] != a[4]:
#     print("펜린드롬이 아니다.")
# elif a[1] != a[3]:
#     print("펠린드롬이 아니다")
# else:
#     print("펠린드롬이다.")

# i값이 0, 1
# for i in range(2):
#     if a[i] != a[4-i]:
#         print("펠린드롬이 아니다")
# print("펠린드롬이다.")


for i in range(len(a)//2):
    if a[i] != a[len(a)-1 -i]:
        print("펠린드롬이 아니다")
print("펠린드롬이다")






