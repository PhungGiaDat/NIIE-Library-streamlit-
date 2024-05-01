class member():
    def __init__(self,member_id : int,member_name : str , gender : str, email : str, phone : str) :
        self.member_id = member_id 
        self.member_name = member_name
        self.gender = gender
        self.email = email
        self.phone_number = phone  
    def input(self):
        self.member_id = input()
        self.member_name = input()
        self.gender = input()
        self.email = input()
        self.phone = input()
    def check_phonenumber(self):
        if len(self.phone_number) != 10:
            return False
        return True