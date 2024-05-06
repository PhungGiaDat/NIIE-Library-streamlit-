class MEMBER():
    def __init__(self,member_id : int,member_name : str , gender : str, email : str, phone : str) :
        self.member_id = member_id 
        self.member_name = member_name
        self.gender = gender
        self.email = email
        self.phone_number = phone
    def check_phonenumber(self):
        if len(self.phone_number) != 10:
            return False
        return True