import datetime
class BOOKS:
    def __init__(self,book_id,book_name,author,quantity,year_of_product,available_quantity:bool) :
        self.book_id = book_id
        self.book_name = book_name
        self.quantity = quantity
        self.year_of_product = year_of_product
        self.author = author
        self.available = available_quantity
    def add_book(self):
        self.book_id = input()
        self.book_name = input()
        self.author = input()
        self.quantity = input()
        self.year_of_product = input()
        self.book_id = input()
    def check_year(self):
        if self.year_of_product < datetime.datetime.now().year:
            return True
        else:
            return False
        
        
        