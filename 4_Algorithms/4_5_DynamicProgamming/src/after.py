def solution(n):
    hash = dict()
    hash[1] = 1
    hash[2] = 2

    for i in range(3, n + 1):
        val = (hash[i - 1] + hash[i - 2]) % 1000000007
        hash[i] = val

    answer = hash[n]
    return answer

print(solution(4))
print(solution(5))
print(solution(10))
print(solution(1000))
print(solution(6000))