def showStat(r1, r2, r3, r4, r5):
    print()
    print("\t\t", end=" ")
    for i in range(5):
        print(r1[i], " ", end=" ")
    print("\n")
    print("\t\t", end=" ")
    for i in range(5):
        print(r2[i], " ", end=" ")
    print("\n")
    print("\t\t", end=" ")
    for i in range(5):
        print(r3[i], " ", end=" ")
    print("\n")
    print("\t\t", end=" ")
    for i in range(5):
        print(r4[i], " ", end=" ")
    print("\n")
    print("\t\t", end=" ")
    for i in range(5):
        print(r5[i], " ", end=" ")
    print("\n")

def update(r1, r2, r3, r4, r5, p, j):   #Updates the matrix with appropriate entry of player's choice
    if(r5[j]==0):
        r5[j]=p
        return 5
    elif(r4[j]==0):
        r4[j]=p
        return 4
    elif(r3[j]==0):
        r3[j]=p
        return 3
    elif(r2[j]==0):
        r2[j]=p
        return 2
    elif(r1[j]==0):
        r1[j]=p
        return 1

def checkScore(r1, r2, r3, r4, r5, p, i, j):    #Returns the value for number of choice in a row at (i, n) in the matrix
    score=1
    if(i==1):
        k=j-1
        while(k>=0 and r1[k]==p):   #considering leftside
            score+=1
            k-=1
        k=j+1
        while(k<5 and r1[k]==p):    #considering right side
            score+=1
            k+=1
        if(score>=4):
            return score
        
        score=1     #considering below
        if(r2[j]==p):
            score+=1
            if(r3[j]==p):
                score+=1
                if(r4[j]==p):
                    score+=1
                    if(r5[j]==p):
                        score+=1
        if(score>=4):
            return score
        
        score=1     #considering the left diagonal
        k=j+1
        if(k<5 and r2[k]==p):
            score+=1
            k+=1
            if(k<5 and r3[k]==p):
                score+=1
                k+=1
                if(j<k and r4[k]==p):
                    score+=1
                    k+=1
                    if(k<5 and r5[k]==p):
                        score+=1
        if(score>=4):
            return score

        score=1     #considering the right diagonal
        k=j-1
        if(k>=0 and r2[k]==p):
            score+=1
            k-=1
            if(k>=0 and r3[k]==p):
                score+=1
                k-=1
                if(k>=0 and r4[k]==p):
                    score+=1
                    k-=1
                    if(k>=0 and r5[k]==p):
                        score+=1
        if(score>=4):
            return score

    elif(i==2):
        k=j-1
        while(k>=0 and r2[k]==p):   #considering leftside
            score+=1
            k-=1
        k=j+1
        while(k<5 and r2[k]==p):    #considering right side
            score+=1
            k+=1
        if(score>=4):
            return score
        
        score=1     #considering the column
        if(r3[j]==p):
            score+=1
            if(r4[j]==p):
                score+=1
                if(r5[j]==p):
                    score+=1
        if(score>=4):
            return score
        
        score=1     #considering the left diagonal
        if(j-1>=0 and r1[j-1]==p):
            score+=1
        k=j+1
        if(k<5 and r3[k]==p):
            score+=1
            k+=1
            if(k<5 and r4[k]==p):
                score+=1
                k+=1
                if(k<5 and r5[k]==p):
                    score+=1
        if(score>=4):
            return score

        score=1     #considering the right diagonal
        if(j+1<5 and r1[j+1]==p):
            score+=1
        k=j-1
        if(k>=0 and r3[k]==p):
            score+=1
            k-=1
            if(k>=0 and r4[k]==p):
                score+=1
                k-=1
                if(k>=0 and r5[k]==p):
                    score+=1
        if(score>=4):
            return score

    elif(i==3):
        k=j-1
        while(k>=0 and r3[k]==p):   #considering leftside
            score+=1
            k-=1
        k=j+1
        while(k<5 and r3[k]==p):    #considering right side
            score+=1
            k+=1
        if(score>=4):
            return score
        
#considering the column is un necessary since the score cannot be more than 3 from rows below 2
        
        score=1     #considering the left diagonal
        if(j-1>=0 and r2[j-1]==p):
            score+=1
            if(j-2>=0 and r1[j-2]==p):
                score+=1
        k=j+1
        if(k<5 and r4[k]==p):
            score+=1
            k+=1
            if(k<5 and r5[k]==p):
                score+=1
        if(score>=4):
            return score

        score=1     #considering the right diagonal
        if(j+1<5 and r2[j+1]==p):
            score+=1
            if(j+2<5 and r1[j+2]==p):
                score+=1
        k=j-1
        if(k>=0 and r4[k]==p):
            score+=1
            k-=1
            if(k>=0 and r5[k]==p):
                score+=1
        if(score>=4):
            return score

    elif(i==4):
        k=j-1
        while(k>=0 and r4[k]==p):   #considering leftside
            score+=1
            k-=1
        k=j+1
        while(k<5 and r4[k]==p):    #considering right side
            score+=1
            k+=1
        if(score>=4):
            return score
        
#considering the column is un necessary since the score cannot be more than 3 from rows below 2
        
        score=1     #considering the left diagonal
        if(j-1>=0 and r3[j-1]==p):
            score+=1
            if(j-2>=0 and r2[j-2]==p):
                score+=1
                if(j-3>=0 and r1[j-3]==p):
                    score+=1
        if(j+1<5 and r5[j+1]==p):
            score+=1
        if(score>=4):
            return score

        score=1     #considering the right diagonal
        if(j+1<5 and r3[j+1]==p):
            score+=1
            if(j+2<5 and r2[j+2]==p):
                score+=1
                if(j+3<5 and r1[j+3]==p):
                    score+=1
        if(j-1>=0 and r5[j-1]==p):
            score+=1
        if(score>=4):
            return score

    elif(i==5):
        k=j-1
        while(k>=0 and r5[k]==p):   #considering leftside
            score+=1
            k-=1
        k=j+1
        while(k<5 and r5[k]==p):    #considering right side
            score+=1
            k+=1
        if(score>=4):
            return score
        
#considering the column is un necessary since the score cannot be more than 3 from rows below 2
        
        score=1     #considering the left diagonal
        if(j-1>=0 and r4[j-1]==p):
            score+=1
            if(j-2>=0 and r3[j-2]==p):
                score+=1
                if(j-3>=0 and r2[j-3]==p):
                    score+=1
                    if(j-4>=0 and r1[j-4]==p):
                        score+=1
        if(score>=4):
            return score

        score=1     #considering the right diagonal
        if(j+1<5 and r4[j+1]==p):
            score+=1
            if(j+2<5 and r3[j+2]==p):
                score+=1
                if(j+3<5 and r2[j+3]==p):
                    score+=1
                    if(j+4<5 and r1[j+4]==p):
                        score+=1
        if(score>=4):
            return score

    return score

def play(r1, r2, r3, r4, r5, n):
    if(r1[0]!=0 and r1[1]!=0 and r1[2]!=0 and r1[3]!=0 and r1[4]!=0):
        print("Match over! Nobody wins!")
        return 0
    p1=int(input("Player 1: Enter your choice>> "))
    while(p1>n or r1[p1-1]!=0):
        p1=int(input("Invalid Choice! \nPlayer 1: Enter your choice>> "))
    i=update(r1, r2, r3, r4, r5, 1, p1-1)
    showStat(r1, r2, r3, r4, r5)
    score=checkScore(r1, r2, r3, r4, r5, 1, i, p1-1)
    if(score>3):
        print("Congratulations! Player 1 won!")
        return 0
    
    if(r1[0]!=0 and r1[1]!=0 and r1[2]!=0 and r1[3]!=0 and r1[4]!=0):
        print("Match over! Nobody wins!")
        return 0
    p2=int(input("Player 2: Enter your choice>> "))
    while(p2>n or r1[p2-1]!=0):
        p2=int(input("Invalid Choice! \nPlayer 2: Enter your choice>> "))
    i=update(r1, r2, r3, r4, r5, 2, p2-1)
    showStat(r1, r2, r3, r4, r5)
    score=checkScore(r1, r2, r3, r4, r5, 2, i, p2-1)
    if(score>3):
        print("Congratulations! Player 2 wins!")
        return 0
    play(r1, r2, r3, r4, r5, n)
    
def main():
    print("This will allow two players to play connect 4.\nWho connects 4 in a row is the winner!")
    answer='yes'
    while(answer[0]=='Y' or answer[0]=='y'):
        r1=[0,0,0,0,0]
        r2=[0,0,0,0,0]
        r3=[0,0,0,0,0]
        r4=[0,0,0,0,0]
        r5=[0,0,0,0,0]
        showStat(r1, r2, r3, r4, r5)

        play(r1, r2, r3, r4, r5, 5)

        answer=input("Do you want to play again?\t(yes/no)\t")
    print("\t\t\t***Thanx for playing!***")

main()
