T = int(input())
for t in range(1, T+1):
    N = int(input())
    Len = ''
    for N in range(0, N):
        List = list(input().split())
        a = List[0]
        b = int(List[1])
        Len += a*b

    print('#{}'.format(t))

    for i in range(0, len(Len), 10):
        print(Len[i:i+10])
