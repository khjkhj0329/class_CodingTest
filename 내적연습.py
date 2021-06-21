a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

# a[0]*b[0] + a[1]*b[1] + a[2]*a[2] + a[3]*b[3]

answer = 0
for i in range(len(a)):
    answer += (a[i]*b[i])

print(answer)