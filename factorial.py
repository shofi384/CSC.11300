def main():
    n= int(input("Please enter an integer.\nI will calculate the factorial of it: "))
    fact=1
    for factor in range(n,1,-1):
        fact=fact*factor
    print("The factorial of",n,"is",fact)

main()
