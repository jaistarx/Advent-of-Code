def calculateScore():
    total=0
    h = open('input.txt', 'r')
    content = h.read()
    a=content.splitlines()  
    # print(a)

    for i in a:
        if(i[0]=="A"):
            if(i[2]=="X"):
                total=total+1+3
            elif(i[2]=="Y"):
                total=total+2+6
            else:
                total=total+3+0
        elif(i[0]=="B"):
            if(i[2]=="X"):
                total=total+1+0
            elif(i[2]=="Y"):
                total=total+2+3
            else:
                total=total+3+6
        elif(i[0]=="C"):
            if(i[2]=="X"):
                total=total+1+6
            elif(i[2]=="Y"):
                total=total+2+0
            else:
                total=total+3+3
    print(total)

# calculateScore()

def calculateScorePart2():
    total=0
    h = open('input.txt', 'r')
    content = h.read()
    a=content.splitlines()  
    # print(a)

    for i in a:
        if(i[0]=="A"):
            if(i[2]=="X"):
                total=total+3+0
            elif(i[2]=="Y"):
                total=total+1+3
            else:
                total=total+2+6
        elif(i[0]=="B"):
            if(i[2]=="X"):
                total=total+1+0
            elif(i[2]=="Y"):
                total=total+2+3
            else:
                total=total+3+6
        elif(i[0]=="C"):
            if(i[2]=="X"):
                total=total+2+0
            elif(i[2]=="Y"):
                total=total+3+3
            else:
                total=total+1+6
    print(total)
calculateScorePart2()