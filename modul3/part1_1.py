# # if + condition
#
# var1 = int(input('Add number: '))
#
# if var1 == 1:
#     print(var1)
#
# else:
#     print('number is not 1')
#
#
#
# # true-ish
#
# print(bool(''), 'empty string')
#
# print(bool('0'), '0 string')
# print(bool(0), '0 int')
# print(bool(-1000), '-1000 int')
# print(bool(None), 'None object')


# var1 = int(input('Add number: '))
#
# if 1 + var1:
#     print(var1)
# else:
#     print('number is not x')

# elif

# var1 = int(input('Add number: '))
#
# if var1 + 1:
#     print('result first:', var1)
# elif 2 + var1:
#     print(f'result second: {2 + var1}')
# else:
#      print('number is not 1')

var1 = int(input('Add number: '))

if var1 > 10:
    print('result positive:', var1)
elif var1 < -10:
    print(f'result negative: {var1}')
elif var1 <= 10 and var1 > 0:
    print('result is in interval (0-10]')

else:
     print('number is 0')