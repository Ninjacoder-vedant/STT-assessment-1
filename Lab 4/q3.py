# def min_operations(a):
#     n = len(a)
#     res = 0
#     pref = 0
#     minPref = 0
#     for i in range(n):
#         if (i + 1) % 2 == 0:
#             d = a[i]
#         else:
#             d = -a[i]
#         pref += d
#         if pref < minPref:
#             res += minPref - pref
#             pref = minPref
#         minPref = max(minPref, pref)
#     return res

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(min_operations(a))
for i in range(10):
    print(i)