def generator(n):
    if(n==0):
        return [""]
    
    rec = generator(n-1)
    final_answer = []

    for j in range(len(rec)):
        s = rec[j]
        for k in range(1,n+1,1):
            final_answer.append(str(k)+s)

    return final_answer




def main():
    
    n = int(input())
    array = generator(n)
    print(*array,sep = "\n")
main()