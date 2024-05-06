import datetime
from module.books import BOOKS

class loan_ticket():
    ## This is the parent class for TICKET_DETAILS
    def __init__(self,TICKET_ID: int ,MEMBER_NAME,RECEIVING_TIME:datetime.datetime,PAYMENT_TIME :datetime.datetime ,QUANTITY_BOOKS) :
        self.TICKET_ID = TICKET_ID
        self.MEMBER_NAME = MEMBER_NAME 
        self.RECEIVING_TIME = RECEIVING_TIME
        self.PAYMENT_TIME = PAYMENT_TIME
        self.QUANTITY_BOOKS = QUANTITY_BOOKS
    ## This function checks if the receiving time is less than the payment time
    def check_time(self): 
        if self.RECEIVING_TIME < self.PAYMENT_TIME:
            return True
        else:
            return False
class ticket_details(loan_ticket,BOOKS):
    def __init__(self,TICKET_ID: int ,MEMBER_NAME,RECEIVING_TIME:datetime.datetime,
                 PAYMENT_TIME :datetime.datetime ,
                 QUANTITY_BOOKS,QUANTITY
                 ) :
        super().__init__(TICKET_ID,MEMBER_NAME,RECEIVING_TIME,PAYMENT_TIME,QUANTITY_BOOKS)
        self.QUANTITY = QUANTITY
    def check_time(self):
        if self.RECEIVING_TIME < self.PAYMENT_TIME:
            return True
        else:
            return False
        