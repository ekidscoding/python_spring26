from collections import Counter

list_binary = [1, 0, 1, 1, 1, 0]

# def count_ones(my_list) -> int:
#     result = 0
#     for i in my_list:
#         if i == 1:
#             result += 1
#     return result

# print(count_ones(list_binary))

print(Counter(list_binary)[1])