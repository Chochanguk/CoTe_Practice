'''
dp[1]=0
dp[2]=1
dp[3]=dp[1]+dp[2]
'''
    
def solution(n):
    answer = 0
    MOD = 1000000007
    if n<=1:
        return 0
    if n==2:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]