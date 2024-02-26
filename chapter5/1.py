def calculate(n,listt):
    listt = sorted(listt)
    steps = 0
    time = 0
    for i in range(len(listt)):
        if(time<listt[i]):
            steps = steps+1
            time = time+1
        
    return steps


def main():
    n = int(input())

    inpput_list = input().split(" ")
    listt=[]
    for j in range(n):
        listt.append(int(inpput_list[j]))

    print(calculate(n,listt))

main()
