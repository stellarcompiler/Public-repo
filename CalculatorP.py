op=["Add (+)","Subtract (-)","Division (/)","Multiply (*)"]
i=0
x=eval(input("input1 :"))
y=eval(input("input2 :"))
print("Select the operator")
for i in range(len(op)):
    print (op[i])
ch=""
ch=input("Operator :")
print("Selected operation :" ,ch)
if (ch=="+"or ch=="add"or ch=="Add"):
    sum=x+y
    print("Total sum :",sum)
elif (ch=="-"or ch=="Sub"or ch=="sub"or ch=="Subtract"or ch=="subtract"):
    diff=x-y
    print("Difference :",diff)
elif (ch=="/"or ch=="Div"or ch=="div"or ch=="Division"or ch=="division"):
    div=x//y
    rem=x%y
    print("Quotient :",div)
    print("Reminder :",rem)
elif (ch=="*" or ch=="mul" or ch=="Mul"):
    m=x*y
    print("Multiplied :",m)
else:
    print("ERROR 400 BAD REQUEST")
