n, k = map(int, input().split())
val = []
dp = [0 for i in range(k+1)]
dp[0] = 1
for _ in range(n):
    val.append(int(input()))
for i in val:
    for j in range(i, k+1):
        dp[j] = dp[j] + dp[j-i]
print(dp[k])

'''
가치가 1,2,5인 코인으로 10만들기
초기 dp[0]값만 1로 설정, 초기 테이블에서 금액을 못만드는 경우는 0으로 하게끔 유도해야 한다
val = 1 : 1 1 1 1 1 1 1 1 1 1 1
이러다 경우의 수를 세어가다 보면 규칙성이 존재한다.
현재 값(dp[j])에 현재 값의 val만큼 앞의 dp값을 더해주면 된다. (dp[j-val[i]])
이 규칙이면 위에 초기 테이블에서 금액 못만드는 경우 = 0도 만족시켜줄 수 있다
말로 풀어 쓰자면,
val이 2일때, dp[2]값은, 1원을 쓰고 2원 만드는 경우의수(기존 dp[2]) + 2원을 쓰고 0원 만드는 경우의수(dp[0])
val이 2일때, dp[6]값은, 1원을 쓰고 6원 만드는 경우의수(기존 dp[6]) + 2원을 쓰고 4원 만드는 경우의수(dp[4])
val = 2 : 1 1 2 2 3 3 4 4 5 5 6
val = 5 : 1 1 2 2 3 4 5 6 7 8 10
'''