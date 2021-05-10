def 보조함수(month, day):
   month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   total = 0;
   for i in range(month -1):
       total += month_list[i]
   total += day
   return total - 1

#1단계. 시작 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
#2단계. 끝 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
#3단계. (2단계에서 구한 날짜) - (1단계에서 구한 날짜)를 구합니다.


def solution(start_month, start_day, end_month, end_day):
   start_total = 보조함수(start_month, start_day)
   end_total = 보조함수(end_month, end_day)
   return end_total - start_total

# testcase를 위한 output
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

# Run을 누르면 받게되는 output.
print("Solution: return value of the function is", ret, ".")

