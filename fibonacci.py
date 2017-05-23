def main():
    n= int(input("Please enter an integer.\nI will print the Fibonacce of it: "))
    f1=0
    f2=1
    nextterm=f1+f2
    for i in range(n+1):
        if i<1:
            print(f1)
        elif i==1:
            print(f2)
        else:
            print(nextterm)
            f1=f2
            f2=nextterm
            nextterm=f1+f2

main()
