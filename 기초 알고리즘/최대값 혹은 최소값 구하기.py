arr = [3, 6, 2, 7]
# print('최소값 : {}'.format(min(arr)))
# print('최대값 : {}'.format(max(arr)))
# 방법 1 : 범위의 최소값 혹은 이보다 작은 수를 초기화
# 최대값 = -1
# 방법 2 : 배열의 첫 원소값으로 초기화
최대값 = arr[0]
for i in arr:
    if 최대값 < i:
        최대값 = i
    print(최대값)