def match_word(list1):
    count = 0
    lst = []
    for i in list1:
        if len(i)>1 and i[0] == i[-1]:
            count =+ 1
            lst.append(i) 
    print(lst)
    return count


data = match_word(['aba','kjh','ldl','wew','345','1221'])
print(data)