import pytest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from morning_greetings.main import Application, Config


def test_send_daily_morning_greetings():
    # Mock dependencies
    contact_manager = Mock()
    message_generator = Mock()
    message_sender = Mock()

    # Set up test data
    contacts = [
        {"name": "Ruby", "email": "rubyjane@gmail.com"},
        {"name": "Kairo", "email": "kairojuan@gmail.com"}
    ]
    contact_manager.get_all_contacts.return_value = contacts
    message_generator.generate_message.return_value = "Test message"

    # Create Application instance
    config = Config(csv_path="test.csv", schedule_time="08:00")
    app = Application(config, contact_manager, message_generator, message_sender)

    # Call the method we're testing
    app.send_daily_morning_greetings()

    # Assertions
    contact_manager.load_contacts.assert_called_once_with("test.csv")
    assert message_generator.generate_message.call_count == 2
    assert message_sender.send_message.call_count == 2
    message_sender.send_message.assert_any_call("rubyjane@gmail.com", "Test message")
    message_sender.send_message.assert_any_call("kairojuan@gmail.com", "Test message")
