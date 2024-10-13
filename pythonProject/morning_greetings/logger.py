#logger.py 

import datetime

def log_message(contact: dict, message: str) -> None:
    if message:
        with open("message.log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()}:
                - Sent to {contact['name']}: {message}\n")
            