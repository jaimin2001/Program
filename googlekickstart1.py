n = int(input())
cnt = 0
c = 0
for _ in range(n):
    t1 = list(map(int, input().split()))
    num = t1[0]
    k = t1[1]
    temp = list(map(int, input().split()))
    for i in range(num):
        if temp[i] == k:
            for j in range(k, 0, -1):
                for it in range(k):
                    if temp[i+it] == j:
                        cnt+=1
            if cnt == k:
                c += 1
            cnt = 0
    print(c)
    c = 0