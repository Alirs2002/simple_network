def calculate(listt):
    
    tup = Sort_Tuple(listt)
    counter = 0
    max = 0
    for j in range(len(tup)):
        if(tup[j][0]>=max):
            counter = counter+1
            max = tup[j][1]

    return counter




def main():
    n = int(input())
    tup_list = []
    for k in range(n):
        input_list = input().split(" ")
        l = int(input_list[0])
        r = int(input_list[1])
        tup_list.append((l,r))

    print(calculate(tup_list))

def Sort_Tuple(tup): 
 
  
    tup.sort(key = lambda x: x[1]) 
    return tup 

main()