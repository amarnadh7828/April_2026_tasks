result = lambda a,b,c:a+b+c
print(result(10,5,5))


# Syntax:
# filter(function, iterable)


list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
empty_list = []
for i in list_1:
    if i%2==0:
        empty_list.append(i)
print(empty_list)