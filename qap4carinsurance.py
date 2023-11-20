#comment like a rank amateur. 
# create a program for car insurance company to calculate payments. 
# author. nkm
# date. november 17 -19 2023

# CONSTANTS. 
BASIC_RATE = 869.00
ADD_CAR_DISCOUNT_RATE = .75
XTRA_LIAB_RATE = 130.00
XTRA_GLASS_RATE = 86.00
XTRA_LOANER_RATE = 58.00
HST_RATE = .15
PROCESSING_FEE_RATE = 39.99
 
 #IMPORTS
import datetime


#FUNCTIONS 

def CalcBasePremium(numCarsToInsure):
    basepremium = BASIC_RATE + (numCarsToInsure - 1)*ADD_CAR_DISCOUNT_RATE*BASIC_RATE
    return basepremium


def CalcXtras(numCarsToInsure):
        xtra = 0
        if xtraLiab =="Y":
            xtra = XTRA_LIAB_RATE
        if  xtraglass =="Y":
            xtra = xtra + XTRA_GLASS_RATE
        if xtraloaner =="Y":
            xtra = xtra + XTRA_LOANER_RATE
        xtra = numCarsToInsure * xtra
        return xtra



def CalcBaseANDextras(basepremium, xtra):
    baseAndextras = 0
    baseAndextras = basepremium + xtra
    return baseAndextras

def CalcHST(baseAndextras):
    HSTtax = (baseAndextras)* HST_RATE
    return HSTtax


def CalcHSTandTotal(baseAndextras):
    totalPlusHST = (baseAndextras * HST_RATE) + baseAndextras
    return totalPlusHST

def CalcMonthlyPymts(totalPlusHST, downpaymentamount):
    monthlypymts = (totalPlusHST - downpaymentamount + PROCESSING_FEE_RATE)/8 
    return monthlypymts

def FDollar2(DollarValue):
    DollarValueStr = "${:,.2f}".format(DollarValue)
    return DollarValueStr






    


#MAIN PROGRAM

#iNPUTS - personal info
firstname =  input("Please enter customer's first name: ").title()
lastname = input("Please enter the customer's last name: ").title()
city = input("Please enter the city or nearest centre: ").title()
postalcode = input("Please enter the customer's postal code: ").upper()
postalcode = postalcode[0:3]+" "+ postalcode[3:]
phone = input("Please enter the customer's phone number (XXX XXX XXXX): ")
phone = phone[0:3]+"-"+ phone[3:6]+"-"+ phone[6:]
#policyNumber = input("Please enter policy number: ")
policyNumber = "1944"



ProvList = ["ON", "MB", "SK", "AB", "BC", "NB", "NL", "NS", "NT", "NU", "PE", "QC", "YT"]
while True:
    province = input("Please enter the two letter provincial abbreviation (XX): ").upper()

    if province =="":
        print("Provincial Code can not be blank. Please re-enter(XX): ")
    elif province not in ProvList:
        print("Invalid entry. Must be correct provincial abbreviation. Please re-enter(XX: ")
    else:
        break
#print(province)


#car information inputs 
while True:
    try:

        numCarsToInsure = int(input("Please enter how many cars will be in this policy: "))

    except:
        print("Not a valid number. Please re-enter the number of cars to be insured: ")

    else:
        break

xtraLiab = input("Does customer want extra liability insurance(Y/N): ").upper()
xtraglass = input("Does the customer want extra glass insurance(Y/N): ").upper()
xtraloaner = input("Does customer want a loaner car(Y/N): ").upper()




paymenttypeList = ["Full", "Monthly", "Downpayment"]
while True:
    paymenttype = input("Please enter your payment preference (Full/Monthly/Downpayment): ").title()


    if paymenttype =="":
        print("Can not be left blank. Please re-enter payment type: ")
    elif paymenttype not in paymenttypeList:
        print("Invalid entry. Must be Full, Monthly or Downpayment. Please re-enter: ")
    else:
        break 


if paymenttype == "Downpayment":
        while True:
            try:
                downpaymentamount = float(input("Enter downpayment: "))
            except:
                print("Not a valid amount. Please re-enter dowmpayment amount: ")
            else:
                break

if paymenttype != "Downpayment":
    downpaymentamount = 0

    
xtra = CalcXtras(numCarsToInsure)
#print(numCarsToInsure)
#print(xtra)


basepremium = CalcBasePremium(numCarsToInsure)
#print(basepremium)


baseAndextras = CalcBaseANDextras(basepremium, xtra)
#print(baseAndextras)

HSTtax = CalcHST(baseAndextras)
#print(f"this is the hst tax alone: {HSTtax}")


totalPlusHST = CalcHSTandTotal(baseAndextras)
#print(f" the total plus hst:  {totalPlusHST}")

monthlypayments = CalcMonthlyPymts(totalPlusHST, downpaymentamount)
#print(f"the montly payments are {monthlypayments}")


thedatetoday = datetime.datetime.now()
thedatetodayDISPLAY = datetime.datetime.strftime(thedatetoday, "%Y-%m-%d")

firstpaymentdate = thedatetoday + datetime.timedelta(days=32)
#print(firstpaymentdate)
firstpaymentdateDSP = datetime.datetime.strftime(firstpaymentdate,"%Y-%m-%d")

firstpaymentdateDay = firstpaymentdate.day
firstpaymentdateDay = 1
#print(firstpaymentdateDay)

firstpaymentdateMonth = firstpaymentdate.month
firstpaymentdateYear = firstpaymentdate.year

paymentdate = datetime.date(firstpaymentdateYear, firstpaymentdateMonth, firstpaymentdateDay)
#print(f"the date of the first payment is: {paymentdate}")

'''paymentdateDay = paymentdate.day
paymentdateMonth = paymentdate.month
paymentdateYear = paymentdate.year

#print(f"this is the payment month {paymentdateMonth}")'''




"""
nextpaymentDates = paymentdate + datetime.timedelta(days = 32)
#print(f"the is the second payment ..ie..the first pymt after the first one: {nextpaymentDates}")


#for x in range (9, 1):
nextpaymentDates = nextpaymentDates + datetime.timedelta(days = 32)
nextpaymentDay = nextpaymentDates.day
nextpaymentDay = 1
nextpaymentDatesMonth = nextpaymentDates.month

for month in range(nextpaymentDatesMonth,7):
    
    if month > 12:
        month = 1
    
    
    # print(month)
    

    monthList = ["January", "February", "March","April","May","June","July", "August", "September", "October", "November", "December"]
    print(f"Payment schedule is the 1, {monthList[month]}.")
    
    #print(monthList[month])



nextpaymentDatesYear = nextpaymentDates.year
print(f"this is the next payment date that hasn't been fixed yet {nextpaymentDates}")
print(f"second payment date: {nextpaymentDatesYear}-{nextpaymentDatesMonth}-{nextpaymentDay}")"""

#FORMATTING DOLLAR VALUES TO BE PRINTED OUT 
basepremiumDSP = FDollar2(basepremium)
xtraDSP = FDollar2(xtra)
baseAndextrasDSP = FDollar2(baseAndextras)
totalPlusHSTDSP = FDollar2(totalPlusHST)
#costofClaimlistDSP = "${:,.2f}".format(costofClaim)
downpaymentamountDSP = FDollar2(downpaymentamount)
HSTtaxDSP = FDollar2(HSTtax)
monthlypaymentsDSP = FDollar2(monthlypayments)

#PREVIOUS CLAIMS
numberofclaimsList= []
previousClaimslist = []
costofClaimlist = []
dateofClaimsList = []

numberofclaims = 1

while True: 
    previousClaim = input("Enter a one word description of previous claim (Press Enter/Return to Quit): ").upper()
    #previousClaimslist.append(previousClaim)
    if previousClaim =="":
        break 
    costofClaim = float(input("Enter the cost of the claim: "))
    dateofClaim = input("Enter the date of the previous claim(YYYY-MM-DD): ")
    #dateofClaimParsed = datetime. datetime.strptime(dateofClaim,"%Y-%m-%d")
    
    previousClaimslist.append(previousClaim)  
    costofClaimlist.append(costofClaim)
    dateofClaimsList.append(dateofClaim)
    numberofclaimsList.append(numberofclaims)
    numberofclaims +=1 

    costofClaimlistDSP = "${:,.2f}".format(costofClaim)

"""
    #FORMATTING DOLLAR VALUES TO BE PRINTED OUT 
    basepremiumDSP = FDollar2(basepremium)
    xtraDSP = FDollar2(xtra)
    baseAndextrasDSP = FDollar2(baseAndextras)
    totalPlusHSTDSP = FDollar2(totalPlusHST)
    costofClaimlistDSP = "${:,.2f}".format(costofClaim)
    downpaymentamountDSP = FDollar2(downpaymentamount)
    HSTtaxDSP = FDollar2(HSTtax)
    monthlypaymentsDSP = FDollar2(monthlypayments)"""

    

          



print()
print()
print("---------------------------------------------------------------")
print("                   ONE STOP INSURANCE COMPANY")
print("                         123 Jump Street")
print("                          Corner Brook")
print("                       Newfoundland A1A 2A1")
print("                            1-800-CARS")
print()
print()
print(f"POLICY NUMBER: {policyNumber:<4s}")
print(f"INVOICE DATE:  {thedatetodayDISPLAY:<10}")
print()
print()
print(f'{firstname:<10s}{lastname:<15}')
print(f'{city:<12s}')
print(f"{province:<2} CANADA")
print(f"{postalcode:<7s}")
print(f"{phone:<12s}")
print()
print()
print("----------------------------------------------------------------")
print("INSURANCE DETAILS")
print()
print(f"Number of cars to insure: {numCarsToInsure}")
print(f"Extra Coverage(Optional) ")
print(f"               Liability: {xtraLiab}")
print(f"                   Glass: {xtraglass}")
print(f"              Loaner Car: {xtraloaner}")
print()
print(f"            Payment Type: {paymenttype}")
#print(f"  Downpayment(if chosen): {downpaymentamountDSP}")
print()
print("-----------------------------------------------------------------")
print('BREAKDOWN OF CHARGES')
print()
print(f"                                   Base premium: {basepremiumDSP:>10s}")
print(f"                         Extra coverage charges: {xtraDSP:>10s}")
print(f"                                    Downpayment: {downpaymentamountDSP:>10s}")
print()
print(f"                                       SubTotal: {baseAndextrasDSP:>10s}")
print(f"                                            HST: {HSTtaxDSP:>10s}")
print(f"                                     Total Cost: {totalPlusHSTDSP:>10s}")
print()
print("----------------------------------------------------------------")
print(f"PAYMENT SCHEDULE")
print()
print(f"                           First payment is due: {paymentdate}")
print(f"                               Full payment due: {totalPlusHSTDSP:>10s}")
print(f"           If paying monthly, 8 intallments due: {monthlypaymentsDSP:>10s}")
#print(f'The second payment date is: {nextpaymentDatesYear}-{nextpaymentDatesMonth}-{nextpaymentDay}')
print()
print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
print(f"PREVIOUS CLAIMS")
print()






print("                       Claim #   Claim Date       Amount")
print("------------------------------------------------------------------")

for z in range (0,len(numberofclaimsList)): 

    print(f"                        {numberofclaimsList[z]:<1d}.        {dateofClaimsList[z]}     {costofClaimlistDSP:>10s}")

print("------------------------------------------------------------------")
print()
print()

   

        


    




    
    

    
    
    






