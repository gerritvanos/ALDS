def getNumbers(s):
    output_list = []
    temp = ""
    for i in range(len(s)):
        if(s[i] >='0' and s[i] <='9'):
            temp += s[i]
        elif(temp != ""):
            output_list.append(int(temp))
            temp = ""
    if(temp !=""):
        output_list.append(int(temp))
    return output_list


a = 'een123zin45 6met-632meerdere+7777getallen12'
print(getNumbers(a))