def solution(scores):

    # 최대값과 최소값을 뺀 다른 수들을 모두 더한다
    a = sum(scores) - max(scores) - min(scores)
    # 전체갯수 -2 만큼 나눈다(나머지 제거)
    answer = a // (len(scores)-2)

    return answer