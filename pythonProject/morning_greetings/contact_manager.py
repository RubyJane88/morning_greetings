import csv

class ContactManager:
    def __init__(self):
        self.contacts = []
        
    def load_contacts(self, file_path: str) -> None:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.contacts = list(csv_reader)

    def add_contact(self, name: str, email: str, preferred_time: str = "08:00"):
        contact = {
            "name": name,
            "email": email,
            "preferred_time": preferred_time
        }

        self.contacts = [x for x in self.contacts if x["name"] != name]
    
        self.contacts.append(contact)

    def remove_contact(self, name: str) -> None:
        self.contacts = [x for x in self.contacts if x["name"] != name]
    
    def get_all_contacts(self) -> list:
        return self.contacts

    def list_all_contacts(self) -> None:
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
