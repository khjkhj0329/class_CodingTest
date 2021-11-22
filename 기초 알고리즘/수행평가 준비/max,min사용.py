arr = [3, 6, 2, 7]
# print('최소값 : {}'.format(min(arr)))
# print('최대값 : {}'.format(max(arr)))

for i in arr:
    for j in arr:
        if i > j:
            result = i
print(result)
