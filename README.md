# Morning Greetings Application

This Python application sends personalized morning greetings to a list of contacts at a scheduled time.

## Setup

1. Ensure you have Python 3.8+ and Poetry installed on your system.

2. Clone the repository and navigate to the project directory.

3. Install dependencies using Poetry:
   ```
   poetry install
   ```

4. Place your contacts in a `contacts.csv` file in the `pythonProject/morning_greetings/` directory. Format:
   ```
   name,email,preferred_time
   Ruby Jane, rubyjane@gmail.com,08:00
   Kairo Juan,kario@gmail.com,09:00
   ```

## Running the Application

1. Activate the Poetry virtual environment:
   ```
   poetry shell
   ```

2. Run the script:
   ```
   python pythonProject/morning_greetings/main.py
   ```

3. The script will:
   - Send greetings immediately (for testing)
   - Schedule daily greetings at 8:00 AM

4. Keep the script running to send scheduled greetings.

## Customization

- Modify the scheduled time in `main.py`:
  ```python
  schedule.every().day.at("08:00").do(send_daily_morning_greetings)
  ```

- Adjust the greeting message in `message_generator.py`.

## Stopping the Application

Press `Ctrl+C` in the terminal to stop the script.

## Troubleshooting

- Ensure all required files are in the correct directory structure.
- Verify that Poetry has installed all dependencies correctly.
- Check the `pyproject.toml` file for correct dependencies.
- Verify the `contacts.csv` file format and location.

### Manual Mode

To trigger the application manually:

To manually trigger the application and send greetings immediately:

```
python main.py manual
```

This command will:
1. Immediately send greetings to all contacts in the CSV file.
2. Bypass the scheduled time and run the greeting process right away.
3. Exit after sending all greetings.