 #Financials ... by Amadou

import locale


from Annuity import Annuity
from Loan import Loan

def getChoice():
    goodVal = False
    while not goodVal:
        try:
            choice = int(input("Select Operation: 1=Annuity, 2=Loan, 0=Quit): "))
            if choice < 0 or choice > 2:
                print("Unknwon operation: 1, 2 or 0 only.")

            else:
                goodVal = True
        except ValueError:
            print("Illegal input: intergers between 0 & 2 only. ")
            goodVal = False
    return choice

def getValue(prompt,vtype):
    #vType is 'i' if integer is wanted; 'f' if float is wanted
    goodVal = False
    while not goodVal:
        try:
            if vtype.lower() == "i":
                amt = int(input(prompt))
            else:
                amt = float(input(prompt))
            goodVal = True
        except ValueError as ex:
            print("Illegal value: " + str(ex))
            goodVal = False
    return amt

def doAnnuity():
    amt = getValue("Monthly Deposit: ","f")
    rate = getValue("Annual Interest Rate (6.5% = 6.5): ","f")
    term = getValue("Term (in months): ","i")
    ann = Annuity(amt, rate, term) #instantiation...
    if ann.isValid():
        print("A monthly deposit of %s" % locale.currency(ann.getAmt(),grouping=True)
              + " earning "
              + "{:.2%}".format(ann.getRate()/100)
              + " annually after "
              + str(ann.getTerm()) + " months will have a final value of %s "
                % locale.currency(ann.getFVA(),grouping=True))
        print("That include interest earned of: %s"
              % locale.currency(ann.getInterest(),grouping=True))
        sched=input("Full schedule? (Y/N): ")
        if len(sched) > 0 and sched[0].upper() == "Y":
            print ("Month      Beg.Bal.       Pmt        Int.Earned          End.Bal.")
            for i in range(1,ann.getTerm()+1):
                print("{:4} {:8,.f} {:8,.2f} {:8,.2f} {:10,.2f}".format(i, ann.getBegBal(i), ann.getAmt(), ann.getIntEarn(i), ann.getEndBal(i)))
                
            


    else:
        print("Annuity error: " + ann.getError())
               
              

def doLoan():
    amt = getValue("A loan amount of: ","f")
    rate = getValue("Annual Interest Rate (6.5% = 6.5): ","f")
    term = getValue("Term (in months): ","i")
    ln = Loan(amt,rate,term)
    if ln.isValid():
        print ("A monthly payment of %s" % locale.currency(ln.getAmt(),grouping=True)
               + " is requiredto pay back a loan of %s " % locale.currency(ln.getMoPmt(),grouping=True)
               + " over " + str(ln.getTerm()) + " at an interest rate of " + "{:.2%}".format(ln.getRate()/100)
               + " year.")
        print("That include interest earned of: %s"
              % locale.currency(ann.getInterest(),grouping=True))
        sched=input("Full schedule? (Y/N): ")
        if len(sched) > 0 and sched[0].upper() == "Y":       #zero crached 
            print("Month      Beg.Bal.     Pmt      Int.Earned    End.Bal.")
            for i in range(1,ann.getTerm()+1):
                print("{:4}   {:12,.2f}  {:12,.2f}  {:12,.2f}   {:15,.2f}".format(i, ann.getBegBal(i), ann.getAmt(), ann.getIntEarn(i), ann.getEndBal(i)))
    else:
        print("Loan Error: " + ln.getError())

     
          
def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL,'en_US')
    print("Welcome to the Financials Calculator")

    choice = getChoice()

    while choice != 0:
        if choice == 1:
            doAnnuity()
        elif choice == 2:
            doLoan()
        else:
            print("Operation unknown / not implemented")

        choice = getChoice()
        print()
    print("Thank you for Using the financials Calculator")

if __name__ == "__main__":
    main()

    
                         
