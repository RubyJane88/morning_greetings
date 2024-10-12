import datetime

user_greeting = input("enter a greeting for the countdown: ")
user_goal_deadline = input("enter your goal before the countdown separated by a colon\n")
print(user_greeting)
input_goals = user_goal_deadline.split(":")

greetings = user_greeting[0]
goals = user_goal_deadline[1]

deadline_date = datetime.datetime.strptime(goals, "%d.%m.%Y")
print(input_goals)