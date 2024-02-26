def generate(n):

    if(n==0):
        return ["0"]
    elif(n==1):
        return ["0","1"]
    
    rec = generate(n-1)
    main_answer = []

    for j in range(len(rec)):
        strin = rec[j]
        main_answer.append("0"+strin)

    for j in range(len(rec)-1,-1,-1):
        strin = rec[j]
        main_answer.append("1"+strin)

    return main_answer

def main():
    n = int(input())
    ans  = generate(n)
    print(*ans,sep="\n")

main()

    


