def solution(a, b):
    answer = 0
    for i in range(1, b+1):
        if (a * i) % b == 0:
            answer = b * i
            break
    return answer