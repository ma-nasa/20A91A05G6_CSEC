a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a<b and a<c:
    print("A is minimum")
elif b<c and b<a:
    print("b is minimum")
elif c<a and c<b:
    print("c is minimum")
else:
    print("All are equal")

output
Enter a number:10
Enter a number:20
Enter a number:30
A is minimum
