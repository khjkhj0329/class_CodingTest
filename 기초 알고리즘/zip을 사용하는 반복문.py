human = ['김효정', '이선우', '홍해인']
number = [2308, 2311, 2319]
for i in zip(human, number):
    print(i)
print('--- 선생님이 하신거 --')
숫자 = [1, 2, 3]
알파벳 = ['a', 'b', 'c']
print('-- 리스트 O --')
for x in zip(숫자, 알파벳):
    print(x)
print('-- 리스트 X --')
for z, y in zip(숫자, 알파벳):
    print(z, y)
