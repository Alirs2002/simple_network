def main():
    n = int(input())
    input_list = input().split(" ")
    number_list = []
    for i in range(n):
        number_list.append(int(input_list[i]))
    for i in range(1,n):
        temp = number_list[i]
        j=i-1
        while(j>=0):
            if(number_list[j]>temp):
                number_list[j+1]=number_list[j]
                j=j-1
                if(j==-1):
                    number_list[j+1] = temp
            else:
                number_list[j+1] = temp
                break
        

    print(*number_list)



main()