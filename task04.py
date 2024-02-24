n = int(input())

dict_of_shapes = {}
for _ in range(n):
    item = list(map(str, input().split()))
    dict_of_shapes[item.pop(0)] = item

target = input()
for key in dict_of_shapes.keys():
    if target in dict_of_shapes[key]:
        print(key)
        break