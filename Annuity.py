#Annuity

class Annuity:
    """Annuity Calculator"""
    

    def __init__(self,a=0.0,r=0.0,t=0):
        #create 'private" variables for the class values
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error= ""
        if self.isValid():
            self.buildAnnuity()
    #set and get methods 'encapsulate' data values

    def setAmt(self,value):
        self._amt = value
    def getAmt(self):
        return self._amt

    def setRate(self,value):
        self._rate = value
    def getRate(self):
        return self._rate

    def setTerm(self,value):
        self._term = value
    def getTerm(self):
        return self._term

    def isValid(self):
        valid = True
        if self._amt <= 0:
            self._error = "Amount must be positive."
            valid = False
        elif self._rate <= 1 or self._rate > 25:
            self._error = " Rate out of bounds: 1 to 25 only."
            valid = False
        elif self._term <= 0:
            self._error = "Term must be positive."
            valid = False
        return valid

    def getError(self):
        return self._error

    def buildAnnuity(self):
         self._begbal = [0.0] * self._term
         self._intearn = [0.0] * self._term
         self._endbal = [0.0] * self._term

         morate = self._rate/ 12.0/ 100.0
         for i in range(0,self._term):
             if i > 0:
                 self._begbal[i] = self._endbal[i-1] #begbal starts at 0
             self._intearn[i] = (self._begbal[i] + self._amt) * morate
             self._endbal[i] = self._begbal[i] + self._amt + self._intearn[i] # i = 1 month

    def getFVA(self):
        return self._endbal[self._term-1] # -1 because [0.0]

    def getInterest(self):
        return self._endbal[self._term -1] - (self._amt  * self._term)
    def getBegBal(self,mo):
        return self._begbal[mo-1] # 0 - 12 = 13         >>> -1 = 12 
    def getIntEarn(self,mo):
        return self._intearn[mo-1]
    def getEndBal(self,mo):
        return self._endbal[mo-1]

    
             
            
        
