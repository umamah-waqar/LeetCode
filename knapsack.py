def knapsackProb(weights, values, W):
    n = len(values)
    dp = []
    for i in range(n + 1):
        row = []
        for j in range(W + 1):
           row.append(0)
        dp.append(row)

    for i in range(1, n + 1):
        for j in range(0, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]],dp[i - 1][j])

    return dp[n][W]
