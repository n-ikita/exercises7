def min_len(g, a, b):
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 0:
                g[i][j] = 999999999
    for _ in range(len(g)-2):
        for i in range(len(g)):
            for j in range(len(g)):
                for k in range(len(g)):

                    g[i][j] = min(g[i][j], g[i][k]+g[k][j])


    return g[a][b]

def min_len_Dijkstra(graph, city, city2):
    cities_list = []
    for i in range(len(graph)):
        cities_list.append([99999999, 'unseen'])

    cities_list[city][0] = 0
    while True:
        unseen_count = 0
        for i in range(len(cities_list)):
            if cities_list[i][1] == 'unseen':
                unseen_count+=1
        if unseen_count == 0:
            break

        len_list_unseen = [i[0] for i in cities_list if i[1] == 'unseen']
        for city in range(len(cities_list)):
            if cities_list[city][0] == min(len_list_unseen) and cities_list[city][1] == 'unseen':
                current_city = city
                break
        for i in range(len(cities_list)):
            if graph[current_city][i]!=0 and \
                    cities_list[current_city][0] + graph[current_city][i] < cities_list[i][0]:
                cities_list[i][0] = cities_list[current_city][0] + graph[current_city][i]
        cities_list[current_city][1] = 'seen'
    return cities_list[city2][0]

N = int(input())
m = int(input())

cities_dict = {}

road_list = []
for _ in range(N):
    road_list.append([0 for _ in range(N)])

num = 0
for _ in range(m):
    city1, city2, distance = map(str, input().split())

    if city1 not in cities_dict.keys():
        cities_dict[city1] = num
        num+=1
    if city2 not in cities_dict.keys():
        cities_dict[city2] = num
        num+=1

    road_list[cities_dict[city1]][cities_dict[city2]] = int(distance)
    road_list[cities_dict[city2]][cities_dict[city1]] = int(distance)

first_city, second_city = map(str, input().split())

print(min_len_Dijkstra(
road_list, cities_dict[first_city], cities_dict[second_city])
)