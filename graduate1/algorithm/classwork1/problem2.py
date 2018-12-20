def minSwap(A, B):
    dp = [[len(A), len(A)] for i in range(len(A))]
    dp[0][0] = 0
    dp[0][1] = 1
    for i in range(1, len(A)):
        if A[i] > A[i - 1] and B[i] > B[i - 1]:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1] + 1

        if A[i] > B[i - 1] and B[i] > A[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][1])
            dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)

    return min(dp[len(A) - 1][0], dp[len(A) - 1][1])


if __name__ == '__main__':
    # 测试用例个数
    t = int(input())

    output = []
    for i in range(t):
        # 元素个数
        num = int(input())
        arr = input().split()
        output.append()