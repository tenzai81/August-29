total = float(input("Please provide the total amount for you bill. "))
print('How was the level of service?')
service = input('Please select good, ok, or bad  ')
if service == "good": 
    tips= (total * .2)
    total_bill = tips + total
    print(f'Your tip amount is {tips}$') 
    print(f'Your total amount is {total_bill}$')
elif service == "ok": 
    tips= (total * .15)
    total_bill = tips + total
    print(f'Your tip amount is {tips}$') 
    print(f'Your total amount is {total_bill}$')   
elif service == "bad": 
    tips= (total * .1)
    total_bill = tips + total
    print(f'Your tip amount is {tips}$') 
    print(f'Your total amount is {total_bill}$')