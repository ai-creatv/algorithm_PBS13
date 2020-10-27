def solution(genres, plays):
    map1 = dict()
    map2 = dict()
    
    for i, elem in enumerate(zip(genres, plays)):
        g, p = elem
        if g not in map1:
            map1[g] = 0
            map2[g] = []

        map1[g] += p
        map2[g].append((i, p))
    
    sort_map1 = sorted(list(map1.items()), key=lambda x: -x[1])

    answer = []

    for g, p in sort_map1:
        sort_map2 = sorted(map2[g], key=lambda x: -x[1])
        answer += list(map(lambda x: x[0], sort_map2))[:2]
    
    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))