# Dollars to Euros
# Created by Jonathan Kessler
# Version 1.0
# 10/21/2024



dollar_amount=float(input("Enter dollar amount to be converted : $"))

euros = dollar_amount * .94540
print("----------------------")
print("Amount of euros : €" +str(euros))
print("----------------------")
again= input("Would you like convert again : ")
if again == "Yes":
    x=1

elif again == "No":
    x=2
    


while x == 1:
    dollar_amount=float(input("Enter dollar amount to be converted : $"))
    euros = dollar_amount * .94540
    print("----------------------")
    print("Amount of euros : €" + str(euros) )
    print("-----------------------")
    again= input("Would you like convert again : ")
    if again == "Yes":
        x=1

    elif again == "No":
        x=2


    print("-------------------------")
print("program finished")
