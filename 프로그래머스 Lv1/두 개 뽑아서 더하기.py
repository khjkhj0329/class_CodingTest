def solution(absolutes, signs):
    answer = 0
    # 넘겨받는 배열(list)읠 길이를 일반화 시킴 len(absolutes)
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


if __name__ == "__main__":
    abs = [4, 7, 12]
    s = [True, False, True]
    print(solution(abs, s))