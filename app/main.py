from fastapi import FastAPI, HTTPException
from data_interactor import DatabaseService , get_connection
from scemas import *
import uvicorn

app = FastAPI()
phone  = get_connection()



@app.get("/contacts")
def get_contacts():
    return DatabaseService.get_all_contacts(phone)



@app.post("/contacts")
def create_contact_route(contact:NewContacts):

    new_id = DatabaseService.create_contact(
        contact.first_name,
        contact.last_name,
        contact.phone_number,
        phone
    )
    return {"message": "Contact created successfully", "id": str(new_id)}


@app.put("/contacts/{contact_id}")
def update_contact_route(contact_id: str, contact: NewContacts):
    updated = DatabaseService.update_contact(
        contact_id,
        contact.first_name,
        contact.last_name,
        contact.phone_number,
        phone
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact updated successfully"}



@app.delete("/contacts/{contact_id}")
def delete_contact_route(contact_id: str):
    deleted = DatabaseService.delete_contact(contact_id,phone)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)











