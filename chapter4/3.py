step = 1

def main():
    n = int(input())
    han(n,"A","B","C")


def han(n,src,dst,help):
    global step
    if(n==1):
        print(step,src,dst)
        step = step+1
    else:
        han(n-1,src,help,dst)
        print(step,src,dst)
        step = step+1
        han(n-1,help,dst,src)





main()