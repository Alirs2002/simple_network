import sys
sys.setrecursionlimit(10000000)

def main():
    
    n = int(input())
    result = func(n)
    print(result)


def func(n):
    
    if(n==0):
        return 5
    elif(n%2==0):
        return (func(n-2)**2)-21
    else:
        return (func(n-1)**2)



main()