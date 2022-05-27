# def dont_give_me_five(start,end):
#     list1 = []
#     for n in range(start, end+1):
#         if '5' not in n.__str__():
#             list1.append(n.__str__())
            
#     number = list1.__len__()
#     print(list1)
            
#     return number



# test = dont_give_me_five(start=4,end=17)
# print(test)


def duplicates(arr):
    pair = 0
    for n in arr.count(n):
        if n.count % 2 == 0:
            pair += n.count / 2
        if n.count % 2 == 1:
            pair += (n.count - 1)/2
    return pair

test = duplicates([1, 2, 5, 6, 5, 2])
print(test)
        