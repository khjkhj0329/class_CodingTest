# 6.어떤 문자열에 해당단어가 몇개있는지 카운팅
# ex) "ILOVKEFLOVEE"에서 "LOV"가 몇개 있는지 카운팅
text = "ILOVKEFLOVEE"
text2 = "LOV"

print(text.count(text2))
count = 0
for i in range(len(text)):
    # 첫 글자가 "L"인 경우 and 찾아야 하는 끝 글자의 범위체크
    if text[i] == text2[0] and i + len(text2) <= len(text):
        # 두번째 글자가 "O"인 경우
        if text[i+1] == text2[1]:
            # 세번째 글자가 "V"인 경우
            if text[i+2] == text2[2]:
                count += 1
print(count)
    # # 첫 글자가 "L"인 경우
    # if text[i] == "L":
    #     # 첫 글자가 "O"인 경우
    #     if text[i+1] == "O":
    #         # 첫 글자가 "V"인 경우
    #         if text[i+2] == "V":
    #             #카운팅
    #             count += 1


