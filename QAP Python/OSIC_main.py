# description: One Stop Insurance Company policy calulator
# author: Colin G. Yetman
# date(s): 2024-07-16 - 

# import libraries
import time
import os


# pull and set up constants from dat file
with open("QAP Python/Modules/const.dat", "r") as f:
    for data in f:
        dataLst = data.split(",")

        policyNum = dataLst[0].strip() # 1944
        basicPrem = dataLst[1].strip() # 869.00
        discountAddCar = dataLst[2].strip() # .25
        extraLiabCost = dataLst[3].strip() # 130.00
        glassCovCost = dataLst[4].strip() # 86.00
        loanerCarCov = dataLst[5].strip() # 58.00
        rateHST = dataLst[6].strip() # .15
        ProcFee = dataLst[7].strip() # 39.99

# define constants 
VALID_PROV = ["BC", "AB", "NL", "ON", "QC", "MB", "SK", "PE", "NB"]


# define functions 
def blankError():
    print("\n blank Error -- cannot be blank \n")

def progQuest():
    custQuestLst = ["Customer First Name", "Customer Last Name", "Customer Street address", "Customer City", "Customer Province", "Customer Postal Code", "Customer Phone Number"]

    carQuestLst = ["Number of Cars to Insure", "Extra Liability", "Glass Coverage", "Loaner Car"]
    return custQuestLst, carQuestLst
def provLst(VALID_PROV, custProv):
    if custProv not in VALID_PROV:
        print(f"\n Province Error -- Must be a valid province ie. {", ".join(VALID_PROV)}")

def payMethod():
    validPayMethod = ["Full", "Monthly", "Down Pay"]
    return validPayMethod


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


clearScreen()
time.sleep(1)
while True:
    userName =  input("Enter your username: ").title()
    if userName == "":
        print("\n\nYou dont want to see your name pop up?\n\n")
    else:
        break
    
time.sleep(1)
print(f"       welcome, {userName:<s}, This is your One Stop Insurance Company's Program!")
time.sleep(5)
# new screen
clearScreen()

print(f"            Now, {userName:<s}, I will guide you through the program.")
time.sleep(1)
print(f"              Please perpare for the following questions.")
print(f"================================================================")
time.sleep(1)
# set up lists for questions
custQuestLst, carQuestLst = progQuest()
print("\nCustomer Questions: \n")
for i in custQuestLst: 
    print(f"{i}")
print("\nInsurance Questions: \n")
for i in carQuestLst:
    print(f"{i}")

print(f"\n\n{userName}, Please let me know when you are done reading and would like to continue.")
time.sleep(1)
while True:
    doneReading = input("Are you done (Y)? ").upper().strip()
    if doneReading == "Y": 
        break

clearScreen()
# gathering customer data
while True:
    while True:
        custFirstName = input("\nEnter Customer's First Name: ")
        if custFirstName == "":
            blankError()
        else:
            break
    
    while True:
        custLastName = input("\nEnter Customer's Last Name: ")
        if custLastName == "":
            blankError()
        else:
            break
    while True:
        custAdress = input("\nEnter Customer's Street Address: ")
        if custAdress == "":
            blankError()
        else:
            break
    
    while True:
        custCity = input("\nEnter Customer's City: ")
        if custCity == "":
            blankError()
        else:
            break

    while True:
        custProv = input("\nEnter Customer's Province: ").upper()
        provLst(VALID_PROV, custProv)
        if custProv in VALID_PROV:
            break

    
    while True:
        custPostalCode = input("\nEnter Customer's Postal Code: ")
        if custPostalCode == "":
            blankError()
        else:
            break
    
    while True:
        custPhoneNum = input("\nEnter Customer's Phone Number: ")
        if custPhoneNum == "":
            blankError()
        else:
            break


    # gathering sales car data
    numCarsInsured = input("\nEnter number of cars to be insured: ")

    extraLiab = input("\nDo you want Extra Liabilities? (y/n): ")

    glassCov = input("\nDo you want Glass Coverage? (y/n): ")

    loanerCar = input("\nDo you want loaner Car? (y/n): ")

    while True:
        custPayMethod = input(f"\nEnter How you want to pay? ").title()
        if custPayMethod not in payMethod():
            print(f"\nPay method not found, please enter one of the following:\n {", ".join(payMethod())}")
        elif custPayMethod == payMethod([2]):
            downPayAmt = input("\n How much are you paying down?: ")
        else:
            break




    #ending the program
    enterAnother = input("\nWould you like to process another insurance policy? (y/n): ").upper()
    if enterAnother != "Y":
        break


# house keeping at the end of the program
print(f"\n Thanks for using this program!\n")