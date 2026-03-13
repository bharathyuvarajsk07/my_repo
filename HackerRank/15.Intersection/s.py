n = int(input())
Eng = set(map(int, input().split()))
b = int(input())
Frn = set(map(int, input().split()))

print(len(Eng.intersection(Frn)))
