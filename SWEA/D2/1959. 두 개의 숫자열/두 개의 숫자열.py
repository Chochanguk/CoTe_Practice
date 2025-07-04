T=int(input())
for tc in range(1,T+1):
    answer=0
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    # print(A,B)
    # A가 더 길면
    if N<M:
        for i in range(0,M-N+1):
            result=0
            for j in range(N):
                result+=A[j]*B[i+j]
            answer=max(answer,result)
    else:
        for i in range(N-M+1):
            result = 0
            for j in range(M):
                result += A[i+j] * B[j]
            answer = max(answer, result)
    print(f'#{tc} {answer}')