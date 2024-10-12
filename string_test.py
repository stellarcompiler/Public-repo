ch=""
str1=""
ch=input("Enter any string :\n")
str1=input("Enter any string :\n")

out1=ch.upper()
out2=ch.lower()
str2=ch+" "+str1
print("Extract substring")
x=int(input("From :"))
y=int(input("To :"))
char=ch[x:(y+1)]

print("Uppercase :",out1)
print("Lowercase :",out2)
print("Concatenation Operation :",str2)
print("Extracted Substring :",char)
