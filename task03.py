n = int(input())

dict_of_negatives = {}
for _ in range(n):
    key, value = map(str, input().split())
    dict_of_negatives[key] = value

target = input()
if target in dict_of_negatives.keys():
    print(dict_of_negatives[target])
elif target in dict_of_negatives.values():
    for i in dict_of_negatives.keys():
        if dict_of_negatives[i] == target:
            print(i)
            break
else:
    print(target)
