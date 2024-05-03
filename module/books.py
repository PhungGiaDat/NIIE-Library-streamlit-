import datetime
class BOOKS:
    def __init__(self,book_id,book_name,author,quantity,year_of_product,available_quantity:bool) :
        self.book_id = book_id
        self.book_name = book_name
        self.quantity = quantity
        self.year_of_product = year_of_product
        self.author = author
        self.available = available_quantity
    def check_year(self):
        if self.year_of_product < datetime.datetime.now().year:
            return True
        else:
            return False
class TYPE_BOOKS(BOOKS):
    def __init__(self,book_id,book_name,author,quantity,year_of_product,available_quantity:bool,book_typeID,GENRE,SUBGENRE,TYPE_FORMAT,TYPE_LANGUAGE,EDITTION,PUBLICATION_DATE:datetime.date):
        super().__init__(book_id,book_name,author,quantity,year_of_product,available_quantity)
        self.book_typeID = book_typeID
        self.genre= GENRE
        self.subgenre = SUBGENRE
        self.type_format = TYPE_FORMAT
        self.type_language = TYPE_LANGUAGE
        self.edittion = EDITTION
        self.publication_date = PUBLICATION_DATE
    def check_year(self):
        if self.year_of_product < datetime.datetime.now().year:
            return True
        else:
            return False
        
        
        