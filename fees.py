fees_paid=True
document_complete=True
if fees_paid:
    print("Fees are paid:")
    if document_complete:
        print("Admission confirmed:")

insert_card=True
pincode_correct=True
balance_5000=True

if insert_card:
    print("card activate")
    if pincode_correct:
        print("confirmed")
        if balance_5000:
            print("balance is 5000")
 


age=10
if age<=18:
    if age>=16:
        print("you are eligible")
    else:
        print("senior citizen:")
else:
    print("senior")

fahad="5 char"
shah="4 char"
syed="4 char"
safiullah="9 char"

if fahad=="5 char":
    if shah=="4 char":
        if syed=="4 char":
            if safiullah=="9 char":
                print("ok")
            else:
                print("kuch bhi")
    else:
        print("never") 
else:
     print("come out")


Birth_certificate=True
Id_card=True
Matric_result=True
intermediate_result=not False
Character_certificate=True
Date_of_birth=False


if Birth_certificate:
    print("okay")
    if Id_card:
        print("correct")
        if Matric_result:
            print("better")
            if intermediate_result:
                print("Admission ok")
                if Character_certificate:
                    print("confirmed")
                    if Date_of_birth:
                        print("no need")
                    else:
                     print("no need")
else:
    print("Admission closed")


fee_unit_price = 10
total_units = int(input("Total units used:"))  # <-- yahan int() lagaya
if total_units>=200:
    print(total_units* 2)
else:
    print("no tax")
result = total_units * fee_unit_price # 30 ki jaga variable bhi use kar lo
print(result)