#contact.py 
class Contacts: 
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, name: str, contact_info: str, preferred_time: str = "08:00", preferred_day: str="Monday") -> None:
        if any(contact['name'] == name for contact in self.contacts):
            raise ValueError("Contact already exists")
        contact = {"name": name, "contact_info": contact_info, "preferred_time": preferred_time, "preferred_day": preferred_day}
        self.contacts.append(contact)    
        
    def remove_contact(self, name: str) -> None:
        self.contacts = [x for x in self.contacts if x["name"] != name]
        
    def get_all_contacts_name(self, name: str) -> list:
        for contact in self.contacts:
            if contact["name"] == name:
                return contact
        raise ValueError("Contact with {name} not found")  