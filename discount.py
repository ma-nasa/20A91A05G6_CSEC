purchase=int(input("Enter the amount purchased:"))
if purchase>1000:
    dis=0.1*purchase
    finalamt=purchase-dis

elif purchase>2000:
    dis=0.2*purchase
    finalamt=purchase-dis

elif purchase>3000:
     dis=0.3*purchase
     finalamt=purchase-dis

elif purchase>5000:
     dis=0.4*purchase
     finalamt=purchase-dis

else:
    dis=0
    finalamt=purchase-dis
    print("No discount")
    
print("Discount:",dis)
print("Bill amount:",finalamt)
