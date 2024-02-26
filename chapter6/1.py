def shift_list(listt):
    temp = listt[0]
    for i in range(0,3):
        listt[i] = listt[i+1]

    listt[3] = temp
    return listt

def calculate(chocolate_list):
    if(chocolate_list[0]==0):
        return [0,0,0,0]
    people_list = [1,0,0,0]
    chocolate_list[0] = chocolate_list[0]-1
    i = 0
    while(True):
        chocolate_list = shift_list(chocolate_list)
        i = i+1
        if(i==4):
            i=0
        if(chocolate_list[i]>0):
            chocolate_list[i] = chocolate_list[i]-1
            people_list[i] = people_list[i]+1
            if(chocolate_list[i]==0):
                break
        

    return people_list


def main():
    input_list = input().split(" ")
    for k in range(3):
        input_list[k] = int(input_list[k])

    listtt = calculate(input_list)
    print(*listtt)

main()


