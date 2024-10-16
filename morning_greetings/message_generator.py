import logging

class MessageGenerator:
    def __init__(self, greeting: str = "Good Morning"):
        try:
            if not isinstance(greeting, str):
                raise TypeError("Greeting must be a string")
            self.greeting = greeting
            logging.info(f"MessageGenerator initialized with greeting: '{greeting}'")
        except TypeError as e:
            logging.error(f"Error initializing MessageGenerator: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in MessageGenerator initialization: {str(e)}")
            raise

    def _validate_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty")

    def generate_message(self, name: str) -> str:
        try:
            self._validate_name(name)
            message = f"{self.greeting}, {name}! I hope you have a great day!"
            logging.debug(f"Generated message for {name}: '{message}'")
            return message
        except Exception as e:
            logging.error(f"Error generating message: {str(e)}")
            raise

    def set_greeting(self, new_greeting: str) -> None:
        if not isinstance(new_greeting, str) or not new_greeting.strip():
            raise ValueError("New greeting must be a non-empty string")
        
        self.greeting = new_greeting
        logging.info(f"Greeting updated to: '{new_greeting}'")

    def generate_message(self, name: str) -> str:
        return f"{self.greeting}, {name}! I just want to say that I hope you have a great day!"


    
    