def main():
    first_input = input().split(" ")
    n = int(first_input[0])
    x = int(first_input[1])

    input_list = input().split(" ")
    mul = []
    for i in range(n+1):
        mul.append(int(input_list[i]))
    result = mul[0]
    divider = (1000000007)

    for i in range(1,n+1):
        result = ((result*x)+mul[i])%divider
    print(result)



main()