n = int(input("Enter the choice 1.Substitution Cipher 2.Columnar Transposition 3.Exit : "))
if n==1:
    P = str(input("Enter the plain text : "))
    Key = int(input("Enter the key : "))
    CT = ""
    PT = P.replace(" ", "")
    print(PT)
    for i in range(len(PT)):
        li = PT[i]
        if (li.isupper()): 
            CT = CT + chr((ord(li) + Key-65) % 26 + 65)
        else:
            CT = CT + chr((ord(li) + Key-97) % 26 + 97)
    print(CT)
elif n==2:
    tex=input("Enter plain text")
    tex=tex.replace(" ","")
    text=list(tex)
    for i in range(0,len(text),3):
        print(*text[i:i+3],end="\n")
        print("\n-----------\n")
        ans=[]
        for i in range(0,3):
            j=i
            while j in range(i,len(text)):
                ans.append(text[j])
                j=j+3
    print(*ans,sep="")

elif n==3:
    print("END")
else:
    print("Invalid Input")
    

