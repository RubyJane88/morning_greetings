import logging

class MessageSender:
    @staticmethod
    def send_message(email: str, message: str) -> bool:
        try:
            MessageSender._validate_input(email, "Email")
            MessageSender._validate_input(message, "Message")
            print(f"Sending {message} to {email}")
    
            print("Message sent!")
            return True
        except ValueError as e:
            logging.error(f"Validation error: {str(e)}")
        except Exception as e:
            logging.error(f"Unexpected error while sending message: {str(e)}")
        return False

    @staticmethod
    def _validate_input(value: str, field_name: str) -> None:
        if not value:
            raise ValueError(f"{field_name} cannot be empty")
      
 
