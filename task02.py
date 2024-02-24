n = int(input())

dict_translate = {}
for _ in range(n):
    key, value = map(str, input().split())
    dict_translate[key] = value

target = input()
for ru, en in dict_translate.items():
    target = target.replace(ru, en)

print(target)