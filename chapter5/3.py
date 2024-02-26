def main():
    input_list = input().split(" ")
    n = int(input_list[0])
    k = int(input_list[1])
    fruit_list = []
    for j in range(n):
        another_list = input().split(" ")
        a = int(another_list[0])
        b = int(another_list[1])

        fruit_list.append((a,b))

    print(calculate(fruit_list,k))



def calculate(listt , energy):

    listt.sort()
   
    length = len(listt)

    for k in range(length):
      
        if((listt[k][0]<=energy) and (listt[k][1]>=listt[k][0])):
            energy = energy+(listt[k][1]-listt[k][0])
            

    return energy

main()