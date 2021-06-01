number = int(input("Enter a number "))
print("The factors of {} are,".format(number))

for i in range(1,number+1):
    if number % i == 0:
        print(i)
        
output:        
Enter a number 77
The factors of 77 are,
1
7
11
77
