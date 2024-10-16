class MessageSender:
    @staticmethod
    def send_message(email: str, message: str) -> None:
        MessageSender._validate_input(email, "Email")
        MessageSender._validate_input(message, "Message")
        print(f"Sending {message} to {email}")
        print("Message sent!")

    @staticmethod
    def _validate_input(value: str, field_name: str) -> None:
        if not value:
            raise ValueError(f"{field_name} cannot be empty")
      
 
