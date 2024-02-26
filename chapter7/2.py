import numpy as np

def main():
    n = int(input())
    number_list = []
    input_list = input().split(" ")

    for i in range(n):
        number_list.append(int(input_list[i]))
    dp = np.zeros((n, n),dtype=int).tolist()
    for k in range(n):
        dp[k][k]=number_list[k]

    for i in range(n):
        for j in range(i+1,n):
            dp[i][j] = dp[i][j-1]+number_list[j]

    print(np.amax(dp))


main()