# Read no of units (nou) and calculate bill acc.  
# If nou>1000 then rate=10/unit, 
# if nou 1000-700 then rate=7/unit, 
# if nou 700-400 then rate=4/unit 
# else rate=2.5/unit.  
# Calculate bill = nou*rate
# and if bill>7000 then add a surcharge of 2 % to bill. 
# Display netbill


nou = int(input("Enter the number of units: "))
if nou > 1000:
    rate = 10
elif nou > 700:
    rate = 7
elif nou > 400:
    rate = 4
else:
    rate = 2.5
bill = nou * rate
if bill > 7000:
    netbill = bill + bill * 0.02
else:
    netbill = bill
print("THE NETBILL IS: ",netbill)