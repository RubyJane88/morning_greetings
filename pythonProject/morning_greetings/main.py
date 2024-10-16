import logging
import os
import time
import sys
import datetime
from typing import List
from dataclasses import dataclass

import schedule

from contact_manager import ContactManager
from message_generator import MessageGenerator
from message_sender import MessageSender

@dataclass
class Config:
    csv_path: str
    schedule_time: str

class Application:
    def __init__(self, config: Config, contact_manager: ContactManager, 
                 message_generator: MessageGenerator, message_sender: MessageSender):
        self.config = config
        self.contact_manager = contact_manager
        self.message_generator = message_generator
        self.message_sender = message_sender
        self.logger = logging.getLogger(__name__)

    def send_daily_morning_greetings(self) -> None:
        try:
            self.contact_manager.load_contacts(self.config.csv_path)
            contacts = self.contact_manager.get_all_contacts()
            self._send_greetings(contacts)
        except Exception as e:
            self.logger.error(f"Error sending greetings: {str(e)}")

    def _send_greetings(self, contacts: List[dict]) -> None:
        for contact in contacts:
            try:
                message = self.message_generator.generate_message(contact["name"])
                self.message_sender.send_message(contact["email"], message)
                self.logger.info(f"Sent greeting to {contact['name']}")
            except Exception as e:
                self.logger.error(f"Error sending to {contact['name']}: {str(e)}")

def run_scheduled_task():
    print(f"Running scheduled task at {datetime.datetime.now()}")
    app.send_daily_morning_greetings()
    print("Scheduled task completed")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    csv_path = os.path.join(current_dir, "contacts.csv")
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Full path to CSV file: {csv_path}")
    print(f"Does file exist? {os.path.exists(csv_path)}")
    
    config = Config(csv_path=csv_path, schedule_time="08:00")  # Changed to a time a few minutes from now for testing
    app = Application(config, ContactManager(), MessageGenerator("Good Morning"), MessageSender())
    
    if len(sys.argv) > 1 and sys.argv[1] == "manual":
        print("Manual trigger activated. Sending greetings now...")
        app.send_daily_morning_greetings()
    else:
        print(f"Automatic mode. Scheduled to run daily at {config.schedule_time}")
        schedule.every().day.at(config.schedule_time).do(run_scheduled_task)
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
                print(f"Waiting for scheduled time. Current time: {datetime.datetime.now().strftime('%H:%M')}")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
