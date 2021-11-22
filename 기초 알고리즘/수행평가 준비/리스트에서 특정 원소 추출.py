arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]

result = list()
for i in arr:
    if i != 2:
        #print(i)
        # 새로운 공간에 i를 넣는다.
        result.append(i)
print(result)