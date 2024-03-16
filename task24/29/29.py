s = open('24.txt').readline().strip() + '+'
num = ''
max_num = '0'
alp = '0123456789ABCDEFGHIJ'
for el in s:
    if el in alp:
        num += el
    else:
        if num and num[0] != '0' and int(num, 20) % 2 == 0 and int(num, 20) > int(max_num, 20):
            max_num = num
        num = ''
print(max_num)

