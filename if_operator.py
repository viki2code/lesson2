def compare_str(str_first, str_second):
    if type(str_first) is not str or type(str_second) is not str:
        return 0
    elif str_first == str_second:
        return 1
    elif len(str_first) > len(str_second):
        return 2
    elif str_second == 'learn':
        return 3

res1 = compare_str(5,'123')
print(res1)
res2 = compare_str('123','123')
print(res2)
res3 = compare_str('12345','123')
print(res3)
res4 = compare_str('12345','learn')
print(res4)
res5 = compare_str('123','12345')
print(res5)
