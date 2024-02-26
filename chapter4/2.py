def main():
    input_list = input().split(" ")
    x = int(input_list[0])
    y = int(input_list[1])

    if(x>y):
        print(gcd(x,y))
    else:
        print(gcd(y,x))
    


def gcd(m,n):
    if(n==0):
        return m
    else:
        return gcd(n,m%n)




main()