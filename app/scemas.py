from pydantic import BaseModel

class NewContacts(BaseModel):
    first_name: str
    last_name: str
    phone_number: str