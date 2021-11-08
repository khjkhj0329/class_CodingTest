name = ['First', 'Second', 'Third']
for i, num in enumerate(name):
    print('{}번호는 {}입니다.'.format(i, num))
print('-- 선생님이 하신거 --')
arr = [10, 20, 30]
for x, v in enumerate(arr): #값에 해당하는 인덱스를 알고 싶을 때 range(len)을 쓴다.
    print(x, v)
print('-- 함수를 쓰지 않고 --')
for y in range(len(arr)):
    print(i, arr[y])

