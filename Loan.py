#Loan
class Loan:
    """ Loan Calculator"""

    def __init__(self,a=0.0,r=0.0,t=0):
        # create 'private' variables for the class
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error = ""
        if self.isValid():
            self.buildLoan()

    def setAmt(self,value):
        self._amt = value
    def getAmt(self):
        return self._amt

    def setRate(self,value):
        self._rate = value
    def getRate(self,value):
        return self._rate

    def setTerm(self,value):
        self._term = value
    def getTerm(self,value):
        self._term


    def isValid(self):
        valid = True
        if self.getAmt() <= 0:
            self._error  = "Amount must be positive."
            valid = False
        elif self.getRate() <= 1 or self.getRate() > 25:
            self._error = "Rate is out of bounds: 1 to 25 only "
            valid = False
        elif self.getTerm() <= 0:
            self._error = "Term must be positive."
            valid = False
        return self._error

    def getError(self):
        return self._error

    def buildLoan(self):
        self._bbal = [0] * self._term
        self._intchg = [0] * self._term
        self._ebal = [0] * self._term

        morate = self._rate /12 / 100
        denom = ((1+morate)* self._term) - 1
        self._mopmt = (morate + morate / denom) * self._amt

        self._bbal[0] = self._amt
        for i in range(0, self._term):
            if i > 0:
                self._bbal[i] = self._ebal[i-1]
            self._intchg[i] = self._bbal[i] * morate
            self._ebal[i] = self._bbal[i] + self._intchg[i] - self._mopmt

        def getMoPmt(self):
            return self._mopmt

        def getInterest(self):
            return (self._mopmt * self._term) - self._amt

        def getBbal(self,mo):
            return self._bbal[mo-1]

        def getIntchg(self,mo):
            return self.intchg[mo-1]
        def getEbal(self,mo):
            return self_ebal[mo-1]

                
            

        
            
