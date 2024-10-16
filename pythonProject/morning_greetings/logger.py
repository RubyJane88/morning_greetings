#logger.py 

import logging
import os
from datetime import datetime

def setup_logging(log_file="application.log"):
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
     
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        logging.info("Logging setup completed successfully.")
    except PermissionError:
        print(f"ERROR: Permission denied when trying to create log file: {log_file}")
        print("The application will continue, but logs will only be printed to the console.")
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler()]
        )
    except Exception as e:
        print(f"ERROR: Failed to set up logging: {str(e)}")
        print("The application will continue without logging.")

def log_message(contact: dict, message: str) -> None:
    try:
        if message:
            logging.info(f"Sent to {contact['name']}: {message}")
    except Exception as e:
        print(f"ERROR: Failed to log message: {str(e)}")

