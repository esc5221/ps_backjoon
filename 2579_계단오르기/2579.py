n = int(input())
stair = [0 for _ in range(n)]
for i in range(n):
    stair[i] = int(input())

# dp[0] : 연속되게 계단 밟았을때 최댓값 (i-1, i)
# dp[1] : 연속되지 않게 계단 밟았을때 최댓값 (i-2, i)
dp = [[0,0] for _ in range(n)]
is_twice = [False for _ in range(n)]

dp[0] = [stair[0], stair[0]]
dp[1] = [stair[0] + stair[1], stair[1]]
dp[2] = [stair[1] + stair[2], stair[0] + stair[2]]

is_twice[0] = False
is_twice[1] = True
is_twice[2] = dp[2][0] > dp[2][1]

for i in range(3, n):
    dp[i][0] = dp[i-1][1] + stair[i]
    dp[i][1] = max(dp[i-2][0] + stair[i], dp[i-2][1] + stair[i])
    is_twice[i] = dp[i][0] > dp[i][1]

answer = max(dp[n-1][0], dp[n-1][1])
print(answer)
