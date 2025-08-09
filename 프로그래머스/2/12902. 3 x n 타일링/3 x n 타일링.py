
def solution(n):
    MOD = 1000000007
    dp = [0] * (n + 1)
    
    #홀수 일 경우
    if n%2==1:
        return 0
    
    #짝수 일 경우
    dp[0] = 1
    dp[2] = 3
    
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2
        dp[i] %= MOD # 계속 값 갱신
    # print(dp[n])
    
    
    return dp[n]