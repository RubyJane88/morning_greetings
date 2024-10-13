class MessageSender:
    @staticmethod
    def send_message(email: str, message: str) -> None:
        if not email:
            raise ValueError("Email cannot be empty")
        if not message:
            raise ValueError("Message cannot be empty")
        print(f"Sending {message} to {email}")
        print("Message sent!")

      
 