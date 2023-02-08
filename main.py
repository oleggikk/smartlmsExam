def stringSearch(n: int, k: int, s: list) -> int:
    if (k == 1):
        return n
    count = 0
    max_count = 0
    for i in range(0, n):
        while (s[i] != 0):
            count += 1
            i += 1
            if (i == n):
                break;
        if (max_count < count):
            max_count = count
        count = 0
    return max_count




n, k = map(int, input().split())
s = list(input())
for i in range(0, n):
    if (s.count(s[i]) < k):
        s[i] = 0
print(s)
print(stringSearch(n, k, s))

