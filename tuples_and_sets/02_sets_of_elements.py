n, m = map(int, input().split())
set_a = set()
set_b = set()

for _ in range(n):
    set_a.add(int(input()))

for _ in range(m):
    set_b.add(int(input()))

print(*set_a.intersection(set_b), sep="\n")