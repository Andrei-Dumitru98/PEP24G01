# dictionary

my_dict = {'one': 1, 'two': 2, 'true': True}
print(my_dict)
print(type(my_dict))

my_dict = dict(one=1, two=2)
print(my_dict)

#iter dict
for element in my_dict:
    print('dickt key:', element)

for element in my_dict.values():
    print('dict values:', element)

for element in my_dict.items():
    print('dict values:', element)


for key, value in my_dict.items():
    print('dict values:', key, value)


# a, b =(1, 2) #same as 1, 2
# print(a)
# print(b)
# a, b = b, a
# print(a)
# print(b)

# get key /value
