#write a program to check whethernit is alphabet digit or special character
ch=input("enter any character=")
if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
    print("it is alphabet")
elif ch>="0" and ch<="9":
    print("it is digit")
else:
    print("it is special charcter")