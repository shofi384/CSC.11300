def main():
    n= int(input("Please enter an integer.\nI will print the sum of all cubes up to the integer: "))
    SumTotal=0
    for i in range(n+1):
        SumTotal+=i*i*i
    print(SumTotal)

main()
