# description: One Stop Insurance Company policy calulator
# author: Colin G. Yetman
# date(s): 2024-07-16 - 

# import libraries

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



def provLst(VALID_PROV, custProv):
    if custProv not in VALID_PROV:
        print("\n Province Error -- Must be a valid province")

    

# gathering user data
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

    custAdress = input("\nEnter Customer's Address: ")

    custCity = input("\nEnter Customer's City: ")

    while True:
        custProv = input("\nEnter Customer's Province: ").upper()
        provLst(VALID_PROV, custProv)
        if custProv in VALID_PROV:
            break
        elif custProv == "":
            blankError()
        else: 
            break




    custPostalCode = input("\nEnter Customer's Postal Code: ")

    custPhoneNum = input("\nEnter Customer's Phone Number: ")


# gathering customer data
    numCarsInsured = input("\nEnter number of cars to be insured: ")

    extraLiab = input("\nDo you want Extra Liabilities? (y/n): ")

    glassCov = input("\nDo you want Glass Coverage? (y/n): ")

    loanerCar = input("\nDo you want loaner Car? (y/n): ")



    #ending the program
    enterAnother = input("\nWould you like to process another insurance policy? (y/n): ").upper()
    if enterAnother != "Y":
        break


# house keeping at the end of the program
print(f"\n Thanks for using this program!\n")