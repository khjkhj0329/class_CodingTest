# 4.Bubble Sort 구현 (버블소트가 무엇인지 말할수 있어야 함)
arr = [8, 5, 6, 3, 4]
# 첫번째
if arr[0] > arr[1]:
    arr[0], arr[1] = arr[1], arr[0] # 바꾸어주는 코드

if arr[1] > arr[2]:
    arr[1], arr[2] = arr[2], arr[1]  # 바꾸어주는 코드

if arr[2] > arr[3]:
    arr[2], arr[3] = arr[3], arr[2] # 바꾸어주는 코드

if arr[3] > arr[4]:
    arr[3], arr[4] = arr[4], arr[3] # 바꾸어주는 코드
# 2번째
if arr[0] > arr[1]:
    arr[0], arr[1] = arr[1], arr[0]  # 바꾸어주는 코드

if arr[1] > arr[2]:
    arr[1], arr[2] = arr[2], arr[1]  # 바꾸어주는 코드

if arr[2] > arr[3]:
    arr[2], arr[3] = arr[3], arr[2]  # 바꾸어주는 코드

if arr[3] > arr[4]:
    arr[3], arr[4] = arr[4], arr[3]  # 바꾸어주는 코드
# 3번째
if arr[0] > arr[1]:
    arr[0], arr[1] = arr[1], arr[0]  # 바꾸어주는 코드

if arr[1] > arr[2]:
    arr[1], arr[2] = arr[2], arr[1]  # 바꾸어주는 코드

if arr[2] > arr[3]:
    arr[2], arr[3] = arr[3], arr[2]  # 바꾸어주는 코드

if arr[3] > arr[4]:
    arr[3], arr[4] = arr[4], arr[3]  # 바꾸어주는 코드
print(arr)