T = int(input())


for i in range(1, T+1):
    N = int(input())
    List = list(map(int, input().split()))
    List.sort()

    print('#{}'.format(i), end=' ')
    for i in range(N):
        print(List[i], end=' ')
    print()
