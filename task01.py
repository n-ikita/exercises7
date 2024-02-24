from collections import defaultdict
list_of_words = list(map(str, input().split()))
dict_of_words = defaultdict(int)

for i in list_of_words:
    dict_of_words[i] += 1

sorted_list = sorted(dict_of_words.keys(), key=lambda x: dict_of_words[x], reverse=True)

print(*sorted_list, sep='\n')

