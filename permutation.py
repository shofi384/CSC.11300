def anagram(n):
    if n == "":
        return [n]
    else:
        p = []
        for i in anagram(n[1:]):
            for pos in range (len(i)+1):
                p.append(i[:pos]+n[0]+i[pos:])
        return p

def main():
    n = input("Pleas enter a series of digits or word.\n\tI will print all the permutations of it: ")
    p = anagram(n)
    for j in p:
        print (j, end=" ")

main()
