import datetime

user_name_greeting = input("enter your name: ")
print("Hello " + user_name_greeting + "!" + " Let's start the countdown!")
user_goals = input("Enter your top 3 goals for the countdown separated by a colon\n")
my_goals = user_goals.split(":")
goals = my_goals[0]

user_date = input("Enter your deadline for the countdown in the format dd.mm.yyyy\n")
datetime.datetime.strptime(user_date, "%d.%m.%Y")

print("Your top 3 goals are: " + goals)
print("Your deadline is: " + user_date)

#calculate how many days from now till the deadline 
print("Days left: " + str((datetime.datetime.strptime(user_date, "%d.%m.%Y") - datetime.datetime.now()).days) + " days left!") 