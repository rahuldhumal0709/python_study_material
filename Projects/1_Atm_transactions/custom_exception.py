class InvalidPinError(Exception):

    def __str__(self):
        return "InvalidPinError : INCORRECT PIN"
    
class InvalidAmountError(Exception):
    
    def __str__(self):
        return "AmountError : INVALID AMOUNT"

class MaximumAmountError(Exception):
    
    def __str__(self):
        return "AmountError : ENTERED AMOUNT IS MORE THAN 25000"

class LessAmountError(Exception):
    
    def __str__(self):
        return "AmountError : CURRENT BALANCE IS LESS THAN ENTERED AMOUNT"