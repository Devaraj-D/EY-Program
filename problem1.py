length=int(input("enter the lenght of the tunnel:"))
if length < 100:
    print("short tunnel")
elif length>100 and length<500:
    print("medium tunnel")
else:
    print("long tunnel")    