N,K = map(int, input().split()245)
count =0
while(N != 1):
    if N % K == 0: 
        N = N // K
    else: N = N-1
    count += 1
    
print(count)