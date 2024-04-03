qty=float (input ("Enter the qty of item sold:\n"))
val=float(input("Enter the value of item:\n"))
discount=float(input("Enter the discount percentage:\n"))
tax=float(input("enter your tax%:\n"))
amt= qty*val
discount_amt=(amt*discount)/100
sub_total=amt-discount_amt
tax_amt=(sub_total*tax)/100
total_amt=sub_total+tax_amt
print("********Bill***********")
print("Quantity of Item sold: \t ",qty)
print("Price per item: \t", val)
print("\n\t\t ------------")
print("Amount: \t\t",amt)
print("Discount total: \t",discount_amt)
print("   \t\t--------------")
print("Tax%:+",tax_amt)
print("   \t\t--------------")
print("total amount to be paid",total_amt)

