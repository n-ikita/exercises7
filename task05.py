def children_count(name, dict_names):
    if name not in dict_names.keys():
        return 0
    count = 0
    for i in dict_names[name]:
        count+=children_count(i, dict_names)
    return len(dict_names[name])+count

n = int(input())

dict_of_names = {}
for _ in range(n):
    key, value = map(str, input().split())
    if key not in dict_of_names.keys():
        dict_of_names[key] = [value]
    else:
        dict_of_names[key].append(value)

target = input()

print(children_count(target, dict_of_names))