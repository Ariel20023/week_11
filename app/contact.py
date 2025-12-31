class Contact:
    def __init__(self,id:str,first_name:str,last_name:str,phone_number:str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def to_dict(self):
        return {
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "phone_number":self.phone_number
        }
