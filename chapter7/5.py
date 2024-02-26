import numpy as np

def calculate():
    arr = np.zeros(shape=(2001,2001),dtype=int)
    #for j in range(1,2001):
     #   arr[0][j-1]=j
    #for i in range(2000):
    #    arr[i][i] = 1
    for i in range(0,2001):
        for j in range(0,i+1):
            if((j==0) or (i==j)):
                arr[i][j]=1
            else:
                arr[i][j] = (arr[i-1][j-1]+arr[i-1][j])%(1e9+7)
    return arr

def main():
    n = int(input())
    liss = []
    for j in range(n):
        input_list = input().split(" ")
        liss.append((int(input_list[0]),int(input_list[1])))
    
    arra = calculate()
    for k in liss:
        if(k[1]>k[0]):
            print(0)
        else:
            print(arra[k[0]][k[1]])





main()