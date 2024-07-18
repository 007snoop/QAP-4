# description: One Stop Insurance Company policy calulator
# author: Colin G. Yetman
# date(s): 2024-07-16 - 

# import libraries
import time
import os
import sys

# pull and set up constants from dat file(s)
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

    carQuestLst = ["Number of Cars to Insure", "Extra Liability", "Glass Coverage", "Loaner Car", "How you would like to pay"]
    return custQuestLst, carQuestLst
def provLst(VALID_PROV, custProv):
    if custProv not in VALID_PROV:
        print(f"\n Province Error -- Must be a valid province ie. {", ".join(VALID_PROV)}")


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


# screen clear outside for user input
clearScreen()
time.sleep(1)
while True:
    userName =  input("Enter your username: ").title()
    if userName == "":
        print("\n\nYou don't want to see your name pop up?\n\n")
    else:
        break
    
time.sleep(1)
print(f"\n\n       welcome, {userName:<s}, This is your One Stop Insurance Company's Program!")
time.sleep(5)
# new screen
clearScreen()

print(f"\n\n\n            Now, {userName:<s}, I will guide you through the program.")
time.sleep(3)
print(f"              Please perpare for the following questions.")
print(f"=" * 80)
time.sleep(3)
# set up lists for questions
custQuestLst, carQuestLst = progQuest()
print("\n Customer Questions: \n")
print("-" * 26)
for i in custQuestLst:
    time.sleep(0.7) 
    print(f"{i}")
print("\n Insurance Questions: \n")
print("-" * 26)
for i in carQuestLst:
    time.sleep(0.7)
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
        custFirstName = input("\nEnter Customer's First Name: ").title().strip()
        if custFirstName == "":
            blankError()
        else:
            break
    
    while True:
        custLastName = input("\nEnter Customer's Last Name: ").title().strip()
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


    # gathering sales car data and doing calculations
    
    totalCarPrem = 0
    totalExtraCost = 0

    basicPrem = float(basicPrem)
    discountAddCar = float(discountAddCar)
    totalExtraCost = float(totalExtraCost)
    totalCarPrem = float(totalCarPrem)
    extraLiabCost = float(extraLiabCost)
    glassCovCost = float(glassCovCost)
    loanerCarCov = float(loanerCarCov)
    rateHST = float(rateHST)
    validPayMethod = ["Full", "Monthly", "Down Pay"]

    numCarsInsured = int(input("\n Enter number of cars to be insured: "))

    for carNum in range(numCarsInsured):
        time.sleep(1)

        print(f"\n Car number: {carNum + 1}")

        time.sleep(1)
        if carNum == 1:
            carPrem = basicPrem
        else:
            carPrem = basicPrem * discountAddCar
        totalCarPrem += carPrem

        
        extraLiab = input("\n Do you want Extra Liabilities? (y/n): ").upper()
        if extraLiab == "Y":
            totalExtraCost += extraLiabCost

        
        glassCov = input("\n Do you want Glass Coverage? (y/n): ").upper()
        if glassCov == "Y":
            totalExtraCost += glassCovCost

        loanerCar = input("\n Do you want loaner Car? (y/n): ").upper()
        if loanerCar == "Y":
            totalExtraCost += loanerCarCov

        # do final calculation
        totalInsurPrem = totalCarPrem + totalExtraCost
        tax = totalInsurPrem * rateHST 
        totalCost = totalInsurPrem + rateHST

    while True:
        custPayMethod = input(f"\n Enter How you want to pay? {",".join(validPayMethod)}: ").title()

        if custPayMethod not in validPayMethod:
            print(f"\n Pay method not found, please enter one of the following:\n {", ".join(validPayMethod)}")

        elif custPayMethod == validPayMethod[2]:
            downPayAmt = float(input("\n How much are you paying down?: "))
            time.sleep(.7)

            if downPayAmt > 0:
                payRest = input(f"\n How are you playing the rest: \n {",".join(validPayMethod[0:2])}?: ").title()

                if payRest in validPayMethod[:1]:
                    payState = print(f"\n You selected {custPayMethod} with a down payment of ${downPayAmt:,.2f} and will pay the rest via {payRest}.")
                    break
                else:
                    print("\n \n Invalid payment method for the remaining amount. Please enter 'Full' or 'Monthly'.")
            else:
                print(f"\n Dowm payemnt must be greater than 0.")
        else:
            print(f"\n You selected {custPayMethod}.")
            downPayAmt = 0
            monthlyPayment = (totalCost + ProcFee) / 8 if custPayMethod == validPayMethod[1] else 0
            break      


        # show the user that something is happening

    # 1. Blinking message for the user
    message = ("Saving progress...")
    for _ in range(5): # sets the number of blinks
        print(message, end="\r")
        time.sleep(0.3) # sleep for the blink effect
        sys.stdout.write("\033[2K\r\033[]") # 033 not 003 you idiot
        time.sleep(0.3) # sleep for the blink effect
    print()
    print(f" -- \n Database Successfully save \n -- ")

    # Write to file

        # Generate and display receipt
    clearScreen()
    print("\n" + "="*50)
    print(f"Receipt for Policy Number: {policyNum}")
    print("="*50)
    print(f"Customer Name: {custFirstName} {custLastName}")
    print(f"Address: {custAdress}, {custCity}, {custProv}, {custPostalCode}")
    print(f"Phone Number: {custPhoneNum}")
    print(f"\nNumber of Cars Insured: {numCarsInsured}")
    print(f"Total premium: ${totalCarPrem:,.2f}")
    print(f"Total extra costs: ${totalExtraCost:,.2f}")
    print(f"Total insurance premium: ${totalInsurPrem:,.2f}")
    print(f"HST: ${tax:,.2f}")
    print(f"Total cost: ${totalCost:,.2f}")
    print(f"Down payment: ${downPayAmt:,.2f}")
    if custPayMethod == "Monthly" or (custPayMethod == "Down Pay" and payRest == "Monthly"):
        print(f"Monthly payment (with processing fee): ${monthlyPayment:,.2f}")
    print("\nPrevious Claims:")
    print("Claim #  Claim Date        Amount")
    print("---------------------------------")
    with open("QAP Python/Modules/claimsOld.dat", "r") as old:
        for data in old:
            oldLst = data.split(",")

            claimNumOld = dataLst[0].strip()
            claimDateOld = dataLst[1].strip()
            claimCostOld = dataLst[2].strip()
            print(f"{claimNumOld['claim_number']:>5}    {claimDateOld['claim_date']}    ${claimCostOld['amount']:,.2f}")

    #ending the program
    enterAnother = input("\n Would you like to process another insurance policy? (y/n): ").upper()
    if enterAnother != "Y":
        break

    



# house keeping at the end of the program
print(f"\n Thanks for using this program!\n")