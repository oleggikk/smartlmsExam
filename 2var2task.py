def nullElements(lenS: int, k: int, s: list) -> list:
    for i in range(lenS):
        if (s.count(s[i]) < k):
            s[i] = 0
    return s

def findIndexesOfStrings(lenS: int, s:list) -> list:
    count = 0
    list_of_strings = []
    i = 0
    while i < lenS:
        b = []
        b.append(i)
        while (s[i] != 0):
            i += 1
            count += 1
            if (i == lenS):
                break
        if (i == lenS):
            b.append(i-1)
        else:
            b.append(i)
        b.append(count)
        count = 0
        i += 1
        list_of_strings.append(b)
    return list_of_strings

def sortStrings(list_of_strings: list, original_s: str, k: int) -> int:
    list_of_strings.sort(key=lambda list_of_strings: list_of_strings[2], reverse=True)
    for i in range(len(list_of_strings)):
        temp_elem_for_check = nullElements(list_of_strings[i][2], k, list(original_s[list_of_strings[i][0] : list_of_strings[i][1] + 1]))
        if (temp_elem_for_check.count(0) == 0):
            return list_of_strings[0][2]
        else:
            temp_list = nullElements(list_of_strings[i][2], k, list(original_s[list_of_strings[i][0] : list_of_strings[i][1] + 1]))
            temp_list = findIndexesOfStrings(list_of_strings[i][2], temp_list)
            for j in range(len(temp_list)):
                temp_list[j][0] += list_of_strings[i][0]
                temp_list[j][1] += list_of_strings[i][0]
            list_of_strings[i][2] = 0
            list_of_strings = list_of_strings + temp_list
            list_of_strings.sort(key=lambda list_of_strings: list_of_strings[2], reverse=True)




n, k = map(int, input().split())
original_s = input()
s_as_list = list(original_s)
s_as_list = nullElements(n, k, s_as_list)
list_of_strings = findIndexesOfStrings(n, s_as_list)
answer = sortStrings(list_of_strings, original_s, k)
print(answer)
# kgdflgldsfjgsfdljgljjhejhjhjksgBJFgbaiyrgybgjgflgkfglkkrokjncgndfghhbkhbfsdkfnlsdkdkgkfljgnajsdkjgfgdfgdfgagnjqoermvbshvmvlsnfhbmnzbagqwertasgfklt
