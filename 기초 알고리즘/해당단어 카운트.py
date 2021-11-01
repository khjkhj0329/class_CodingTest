# 6.어떤 문자열에 해당단어가 몇개있는지 카운팅
# ex) "ILOVKEFLOVEE"에서 "LOV"가 몇개 있는지 카운팅
text = 'ILOVKEFLOVEE'
text2 = 'LOV'
count = 0
for i in range(len(text)):
    # 첫 글자가 "L"인 경우
    if text[i] == "L":
        # 첫 글자가 "O"인 경우
        if text[i+1] == "O":
            # 첫 글자가 "V"인 경우
            if text[i+2] == "V":
                #카운팅
                count += 1
print(count)


