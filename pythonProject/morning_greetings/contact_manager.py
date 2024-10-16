import csv
import logging

class ContactManager:
    def __init__(self):
        self.contacts = []
        
    def load_contacts(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                self.contacts = list(csv_reader)
            logging.info(f"Successfully loaded {len(self.contacts)} contacts")
        except FileNotFoundError:
            logging.error(f"Contact file not found: {file_path}")
            raise
        except csv.Error as e:
            logging.error(f"Error reading CSV file: {str(e)}")
            raise

    def add_contact(self, name: str, email: str, preferred_time: str = "08:00"):
        try:
            contact = {
                "name": name,
                "email": email,
                "preferred_time": preferred_time
            }
            self.contacts = [x for x in self.contacts if x["name"] != name]
            self.contacts.append(contact)
            logging.info(f"Added contact: {name}")
        except Exception as e:
            logging.error(f"Error adding contact {name}: {str(e)}")
            raise

    def remove_contact(self, name: str) -> None:
        try:
            original_length = len(self.contacts)
            self.contacts = [x for x in self.contacts if x["name"] != name]
            if len(self.contacts) < original_length:
                logging.info(f"Removed contact: {name}")
            else:
                logging.warning(f"Contact not found for removal: {name}")
        except Exception as e:
            logging.error(f"Error removing contact {name}: {str(e)}")
            raise

    def get_all_contacts(self) -> list:
        return self.contacts

    def list_all_contacts(self) -> None:
        if not self.contacts:
            logging.info("No contacts available.")
            return
        for contact in self.contacts:
            logging.info(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
