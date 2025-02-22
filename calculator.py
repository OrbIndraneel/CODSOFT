a=int(input("Enter 1st no.:"))
b= int(input("Enter your 2nd no.:"))
print('''For addition 1 
For  subtract 2 
For multipy 3 
For divison 4 
For percentage 5''')
c= int(input("select no."))
if (c==3):
    print(a,"*",b,"=",a*b)
elif (c==2):
    print(a,"-",b,"=",a-b)
elif(c==1):
    print(a,"+",b,"=",a+b)
elif(c==4):
    print(a,"/",b,"=",a/b)
elif(c==5):
    print(a,"/",a+b,"*","100:",a/(a+b)*100)
    print(b,"/",a+b,"*","100:",b/(a+b)*100)
else:
    print("Wrong selection")
    

        
