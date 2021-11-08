
def solution(number):
   count = 0
   for i in range(1, number + 1):
       current = i
       temp = count
       while current != 0:
           if current%10%3 ==0 and current%10 !=0:
               count += 1
           current = current // 10
   return count