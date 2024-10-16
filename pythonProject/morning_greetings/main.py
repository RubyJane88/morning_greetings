import logging
import os
import time
import sys
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

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("application.log"),
            logging.StreamHandler()
        ]
    )

def run_scheduled_task(app):
    logging.info("Running scheduled task")
    try:
        app.send_daily_morning_greetings()
        logging.info("Scheduled task completed successfully")
    except Exception as e:
        logging.error(f"Error in scheduled task: {str(e)}")

def setup_application():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "contacts.csv")
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Contacts file not found: {csv_path}")
    
    config = Config(csv_path=csv_path, schedule_time="08:00")
    return Application(config, ContactManager(), MessageGenerator("Good Morning"), MessageSender())

def run_application(app):
    if len(sys.argv) > 1 and sys.argv[1] == "manual":
        logging.info("Manual trigger activated. Sending greetings now...")
        run_scheduled_task(app)
    else:
        logging.info(f"Automatic mode. Scheduled to run daily at {app.config.schedule_time}")
        schedule.every().day.at(app.config.schedule_time).do(run_scheduled_task, app)
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            logging.info("Program terminated by user.")

def main():
    setup_logging()
    
    try:
        app = setup_application()
        run_application(app)
    except FileNotFoundError as e:
        logging.error(f"File error: {str(e)}")
    except ConnectionError as e:
        logging.error(f"Network error: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
    finally:
        logging.info("Application shutting down.")

if __name__ == "__main__":
    main()
