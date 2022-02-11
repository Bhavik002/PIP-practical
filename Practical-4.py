# Find runner-up from given list
# 20CS002
# BHAVIK AMBASANA

n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])
