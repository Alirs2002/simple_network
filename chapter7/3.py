def calculate():
    arr = [1,1,1,2]
    
    for i in range(4,1000001):
        arr.append((arr[i-1]+arr[i-2]+arr[i-3]-arr[i-4])%(1e9+7))
    return arr


def main():
    n = int(input())
    lis = []
    for j in range(n):
        lis.append(int(input()))

    arrr = calculate()
    for k in lis:
        print(int(arrr[k]))

main()