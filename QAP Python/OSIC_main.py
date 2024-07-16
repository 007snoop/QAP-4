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



# define functions 


# gathering user data
while True:
    custFirstName = input("Enter Customer's First Name: ")

    custLastName = input("Enter Customer's Last Name: ")

    custAdress = input("Enter Customer's Address: ")

    custCity = input("Enter Customer's City: ")

    custProv = input("Enter Customer's Province: ")
    # will set up with list validation later

    custPostalCode = input("Enter Customer's Postal Code: ")

    custPhoneNum = input("Enter Customer's Phone Number: ")


    # gathering customer data
    numCarsInsured = input("Enter number of cars to be insured: ")

    extraLiab = input("Do you want Extra Liabilities? (y/n): ")

    glassCov = input("Do you want Glass Coverage? (y/n): ")

    loanerCar = input("Do you want loaner Car? (y/n): ")

    
    break


# house keeping at the end of the program
