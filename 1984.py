N = int(input())
sum = 0

for i in range(1,N+1):
    List = list(map(int, input().split()))
    
    for j in range(0, len(List)):
        sum += List[j]
        
    sum = sum - max(List) - min(List)
    print('#{} {}'.format(i, round(sum/8)))
    sum = 0

