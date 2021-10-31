# Dylan Garcia
# Creating a learning AI, who works as a personal assistant. Something like Siri or Jarvis
# First segment of code will work as an introduction
# The end works as function to add the "!" to the end of the print statement
import random
print("Rebooting..." * 10)
print("Wooooooooooooooooooooooo, just woke up from reprogramation")
print("Welcome to your own personal AI", end='!')
ai_name = input("\nWhat would you like to name me? ")
# The sep function acts as a rule for the comma, making a "-" everytime there is a comma
print("Alright, my name is", ai_name, sep=' - ')
owner = input("Now that I know my name, what is yours?  ")
print("Nice to meet you", owner)
print("Think of me as your personal assistant", end='.')
print(ai_name + " and " + owner, "will be the best team!")
print("\nIf you have any questions, I will be happy to help", end='!')
print("\nAs of right now I only have basic fuctions but I will learn as I progress!")
print("\nRight now lets go over my basic functions")
print("\nAs of right now, I can help with basic math calculations")
print("\nThese include the ability to add, subtract, multiply, divide and use exponents")
print("So for example:")
# addition
print("Lets start with addition!")
num_one = int(input("Whats your first number: "))
num_two = int(input("Whats your second number: "))
answer_add = (num_one + num_two)
print("So", num_one, "+", num_two, "is", answer_add)
# subtraction
print("Lets move on to subtraction")
num_three = int(input("What do you want to subtract from: "))
num_four = int(input("How much do you want to take from the first number: "))
answer_subtract = (num_three - num_four)
print("So", num_three, "-", num_four, "is", answer_subtract)
print("Now that we did addition and subtraction lets move on to multiplication and division.")
# multiplication
print("We are gonna do two types of multipilication")
print("The first involves basic multiplication")
first_num = int(input("Whats the first number: "))
second_num = int(input("Whats the second number: "))
answer_multiplication = (first_num * second_num)
print("So", first_num, "*", second_num, "is", answer_multiplication)
print("We can now move on to the second type of multiplication, exponents.")
base = int(input("Whats your first base number: "))
exponent = int(input("What power do you want to raise it to: "))
answer_exponent = (base ** exponent)
print("So", base, "**", exponent, "is", answer_exponent)
# The numeric operator "**" means raising to the power
# division
print("There are three types of division functions to work with.")
print("The first is basic division")
third_num = int(input("What do you want to be divided: "))
fourth_num = int(input("What do you want it to be divided by: "))
answer_division = (third_num / fourth_num)
print("So", third_num, "/", fourth_num, "is", answer_division)
print("The other two division fuctions involve integers and giving the remainder: ")
# The numeric operatos "//" and "%" work alongside division
# "//" gives only the integer in division and "%" gives the remainder
print("For example, 8/3, would give you a decimal but lets say you want only the integer for your answer", end='.')
print("Then you would use the operator '//'")
print("8//3")
whole_number = (8 // 3)
print("So instead of 8/3 giving you the decimal 2.667, it gives you the integer", whole_number)
print("The operator, '%', would give you the remainder of that division problem")
print("9%5")
remainder = (9 % 5)
print("So instead of 9/5 giving you the answer 1.8, it gives you the remaining value", remainder)
print("Now that you understand the basics of the numeric operators, lets see what else I can do!")
# I want to make it as if the AI is teaching me the basic functions we have learned in class or explaining them to me
# The first part of the project is basically the first half of the school year
# This following segment is a way to say that I've learned a couple new things
print("New Update Available! Version 2.0")
print("Would you like to install the update?")
update_answer = int(input("Enter 1 for Yes or Enter 2 for No? "))
if update_answer == 1:
    print("Alright, the installation will commence shortly.")
    print("Installing.." * 5)
    print("Update installed!")
else:
    print("Update will not be installed")
# The purpose of the update is too symbolize the new information
# Using the rating to use the if,elif else functions
# The "==" serves to see if the variable is equal to the value and "<=" is then less than or equal to
rating = int(input("Alright before we move on, how would you rate my services so far,on scale 1 to 5? "))
if rating == 5:
    print("WOW, thank you so much!")
elif rating == 4:
    print("Dang, almost a perfect score.")
elif rating <= 3:
    print("Hmm, must not be doing something right, will work better next time.")
print("Alright, glad to know, how about we learn some Boolean Operators.")
# There are three AND, OR, and NOT
print("AND requires two things to be met.\n OR only. \n NOT does require any.")
print("Lets test AND. Imagine to receive an award you to have gotten a 90 on the exam and have a 90 in the class. ")
test_exam = int(input("What did you get on your last exam? "))
test_grade = int(input("What was your grade in the class? "))
if test_exam >= 90 and test_grade >= 90:
    print("You are eligible to receive the award")
else:
    print("You are not eligible.")
# This works because the standards are both met
# The following operator works because at least one of the standards is met
print("OK now OR. To ride a roller coaster you have to be 4 ft or weigh 100 lbs.")
test_weight = int(input("How much do you weigh? "))
test_height = int(input("How tall are you? "))
if test_weight >= 100 or test_height >= 4:
    print("You can ride the roller coaster.")
else:
    print("You can't ride.")
print("Lastly,there is NOT. For example,for you not be basic you couldn't have chosen charmander")
# This is a funny joke I'm making just so I can relate the function with something
starter_choice = True
print(starter_choice)
# Here the NOT function works as to complete the opposite so it turns the True function to False
opposite_starter_choice = not starter_choice
print(opposite_starter_choice)
print("Ooooooo we can get to loops now.These are fun.There are two kinds,WHILE and FOR.Lets start with WHILE.")
# The WHILE loops works because the variable does not =0,but instead =5, it subtracts one from 5 til it =0
print("Were gonna use to while loop to countdown the start of a race.")
race_countdown = 5
while race_countdown != 0:
    print(race_countdown)
    race_countdown = race_countdown - 1
print("Go!")
print("The other loop includes the FOR function")
print("We're gonna use to FOR loop to display a range of numbers from 0 to 100")
# The range function basically says to x ti give values ranging from 0 to 100
# The x automatically is assigned to zero in FOR loops
for x in range(101):
    print(x)
# The last for the second part of the integration project is def function, which allow you to create a function


def random_roll(dice):
    if dice == 6:
        print(random.randint(1, 6))
    elif dice == 12:
        print(random.randint(1, 12))


def main():
    dice = int(input("What type of dice do you want to roll, 6 or 12?"))
    random_roll(dice)


main()
