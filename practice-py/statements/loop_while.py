#!/usr/bin/python3

count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1


flag = 1
while flag:
    print('Given flag is really true!')
    flag -= 1
    break
else:
	print('Given flag is not true!')
