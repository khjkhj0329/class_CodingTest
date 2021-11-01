# 4.Bubble Sort 구현 (버블소트가 무엇인지 말할수 있어야 함)
arr = [8, 5, 6, 3, 4]

# 0, 1, 2, 3
# 0, 1, 2
# 0, 1
# 0

for i in range(0, len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

# len(arr) : 5
# len(arr) - i - 2:
# i:0 #j: 0, 1, 2, 3
# i:1 #j: 0, 1, 2
# i:2 #j: 0, 1
# i:3 #j: 0

# len(arr) : 4
# i:0 #j: 0, 1, 2
# i:1 #j: 0, 1
# i:2 #j: 0

# 첫번째  0,1,2,3
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0] # 바꾸어주는 코드
#
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]  # 바꾸어주는 코드
#
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2] # 바꾸어주는 코드
#
# if arr[3] > arr[4]:
#     arr[3], arr[4] = arr[4], arr[3] # 바꾸어주는 코드
# # 2번째 0,1,2
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]  # 바꾸어주는 코드
#
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]  # 바꾸어주는 코드
#
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2]  # 바꾸어주는 코드
#
# if arr[3] > arr[4]:
#     arr[3], arr[4] = arr[4], arr[3]  # 바꾸어주는 코드
# # 3번째 0,1
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]  # 바꾸어주는 코드
#
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]  # 바꾸어주는 코드
#
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2]  # 바꾸어주는 코드
#
# if arr[3] > arr[4]:
#     arr[3], arr[4] = arr[4], arr[3]  # 바꾸어주는 코드
# print(arr)
# # 네번째 0
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]  # 바꾸어주는 코드
#
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]  # 바꾸어주는 코드
#
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2]  # 바꾸어주는 코드
#
# if arr[3] > arr[4]:
#     arr[3], arr[4] = arr[4], arr[3]  # 바꾸어주는 코드
# print(arr)

