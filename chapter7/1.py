def main():
    n = int(input())
    listt = [1,1]
    for i in range(2,n+1):
        listt.append((listt[i-1]+listt[i-2]) % (1e9+7))

    result = listt[n]


    print(int(result))

main()