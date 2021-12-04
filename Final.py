"""Creating a learning AI, who works as a personal assistant, something like
Siri."""
__author__ = "Dylan Garcia"

# First segment of code will work as an
# introduction The end works as function to add the "!" to the end of the
# print statement
import random


def main():
    """The point of this function is to work almost as table of contents,
    showing off the different functions on this project."""
    introduction()
    addition()
    subtraction()
    multiplication()
    division()
    update()
    rating()
    boolean_operators()
    loops()
    dice = int(input("What type of dice do you want to roll, 6 or 12?"))
    random_roll(dice)


def introduction():
    """The way introduction works is that it acts as the the beginning
    settings to programing this new AI to your own liking. You get to give
    it a name and let it know yours."""
    # First segment of code will work as an introduction
    print("Rebooting..." * 10)
    print("Wooooooooooooooooooooooo, just woke up from reprogramming.")
    print("Welcome to your own personal AI", end='!')
    # The end works as function to add the "!" to the end of the print
    # statement
    # The /n moves the sentence down a line
    ai_name = input("\nWhat would you like to name me? ")
    # The sep function acts as a rule for the comma, making a "-" everytime
    # there is a comma
    print("Alright, my name is", ai_name, sep=' - ')
    owner = input("Now that I know my name, what is yours?  ")
    print("Nice to meet you", owner)
    print("Think of me as your personal assistant", end='.')
    print(ai_name + " and " + owner, "will be the best team!")
    # Here the + works as a way to combine a string and a variable
    print("\nIf you have any questions, I will be happy to help", end='!')
    print("\nAs of right now I only have basic functions but I will learn as "
          "I make new progress!")
    print("\nRight now let's go over my basic functions")
    print("\nAs of right now, I can help with basic math calculations")
    print("\nThese include the ability to add, subtract, multiply, divide "
          "and use exponents")


# addition

def addition():
    """The point of this function is to show off pythons ability to do
    simple math problems."""
    print("Lets start with addition!")
    # The reason there is an int function in front of the input function is
    # so that python reads the user's input as an integer and not a string
    num_one = int(input("What's your first number: "))
    num_two = int(input("What's your second number: "))
    answer_add = (num_one + num_two)
    print("So", num_one, "+", num_two, "is", answer_add)


# subtraction

def subtraction():
    """The point of this function is to use python's subtraction ability and
    show off how it works, by doing a simple math problem. """
    print("Let's move on to subtraction")
    num_three = int(input("What do you want to subtract from: "))
    num_four = int(input("How much do you want to take off first number: "))
    answer_subtract = (num_three - num_four)
    print("So", num_three, "-", num_four, "is", answer_subtract)


# multiplication
def multiplication():
    """The point of this function to show off the two forms of multiplication
    that are able to be done. Those being simple multiplication and using
    exponents."""
    # Here simple multiplication is being done.
    print("We are gonna do two types of multiplication")
    print("The first involves basic multiplication")
    first_num = int(input("What's the first number: "))
    second_num = int(input("What's the second number: "))
    answer_multiplication = (first_num * second_num)
    print("So", first_num, "*", second_num, "is", answer_multiplication)
    print("We can now go onto the second type of multiplication, exponents.")
    base = int(input("What's your first base number: "))
    exponent = int(input("What power do you want to raise it to: "))
    # The numeric operator "**" means raising to the power
    answer_exponent = (base ** exponent)
    print("So", base, "**", exponent, "is", answer_exponent)


# division


def division():
    """The point for this function is to show off the three kinds of
    division you are able to do in python.Those types of division being
    normal division,integer division and remainder division."""
    print("There are three types of division functions to work with.")
    print("The first is basic division")
    third_num = int(input("What do you want to be divided: "))
    fourth_num = int(input("What do you want it to be divided by: "))
    answer_division = (third_num / fourth_num)
    # Here the / is used as a division symbol
    print("So", third_num, "/", fourth_num, "is", answer_division)
    print("The other two division functions involve integers and giving the "
          "remainder: ")
    # The numeric operates "//" and "%" work alongside division
    # "//" gives only the integer in division and "%" gives the remainder
    print("For example, 8/3, would give you a decimal but let's say you want "
          "only the integer for your answer", end='.')
    print("Then you would use the operator '//'")
    print("8//3")
    whole_number = (8 // 3)
    print("So instead of 8/3 giving you the decimal 2.667, it gives you the "
          "integer", whole_number)
    print("The operator '%', would give you the remainder of that division "
          "problem")
    print("9%5")
    remainder = (9 % 5)
    print("So instead of 9/5 giving you the answer 1.8, it gives you the "
          "remaining value", remainder)
    print("Now that you understand the basics of the numeric operators, "
          "lets see what else I can do!")


# I want to make it as if the AI is teaching me the basic functions we have
# learned in class or explaining them to me The first part of the project is
# basically the first half of the school year This following segment is a
# way to say that I've learned a couple new things


def update():
    """The point of this update function is to make use of the if and else
    statements. You have to choice whether to install the update and
    depending on your answer you get a different output."""
    print("New Update Available! Version 2.0")
    print("Would you like to install the update?")
    # The == means that value that is the input has to equal the specific
    # value which in this case is 1
    update_answer = int(input("Enter 1 for Yes or Enter 2 for No? "))
    if update_answer == 1:
        print("Alright, the installation will commence shortly.")
        print("Installing.." * 5)
        print("Update installed!")
    else:
        print("Update will not be installed")


def rating():
    """The reasoning for this function is to further make use of the if and
    else statements, but now adding the elif function. The elif statement
    just adds more options for different outputs."""
    rating_answer = int(input("Alright before we move on, how would you rate "
                              "my services so far,on scale 1 to 5? "))
    if rating_answer == 5:
        print("WOW, thank you so much!")
    elif rating_answer == 4:
        print("Dang, almost a perfect score.")
    elif rating_answer <= 3:
        print("Hmm, must not be doing something right, will work better next "
              "time.")


def boolean_operators():
    """The point of this function os to show the three Boolean Operators,
    which are AND, OR, and NOT. Each having their owm examples."""
    print("Alright, glad to know, how about we learn some Boolean Operators.")
    print("There are three AND, OR, and NOT")
    print("AND requires two things to be met.\n OR only. \n NOT does require "
          "any.")
    print("Lets test AND. Imagine to receive an award you to have gotten a "
          "90 on the exam and have a 90 in the class. ")
    test_exam = int(input("What did you get on your last exam? "))
    test_grade = int(input("What was your grade in the class? "))
    # The >= means the input value has to be greater than or equal to 90
    if test_exam >= 90 and test_grade >= 90:
        print("You are eligible to receive the award")
    else:
        print("You are not eligible.")
    # This works because the standards are both met
    # The following operator works because at least one of the standards is met
    print("OK now OR. To ride a roller coaster you have to be 4 ft or weigh "
          "100 lbs.")
    test_weight = int(input("How much do you weigh? "))
    test_height = int(input("How tall are you? "))
    if test_weight >= 100 or test_height >= 4:
        print("You can ride the roller coaster.")
    else:
        print("You can't ride.")
    print("Lastly,there is NOT. For example, water is blue, we know that to "
          "be true.")
    water_is_blue = True
    print(water_is_blue)
    # Here the NOT function works as to complete the opposite so it turns
    # the True function to False
    water_is_not_blue = not water_is_blue
    print(water_is_not_blue)


def loops():
    """This function shows off the two different kinds of loops. The reasons
    for loops is to get ride of code that seems repetitive. """
    print("Ooooo we can get to loops now.These are fun.There are two "
          "kinds,WHILE and FOR.Lets start with WHILE.")
    # The WHILE loops works because the variable does not =0,but instead =5,
    # it subtracts one from 5 til it =0
    print("Were gonna use to while loop to countdown the start of a race.")
    race_countdown = 5
    while race_countdown != 0:
        print(race_countdown)
        race_countdown -= 1
    print("Go!")
    print("The other loop includes the FOR function")
    print("We're gonna use to FOR loop to display a range of numbers from 0 "
          "to 30")
    # The range function basically says to x ti give values ranging from 0
    # to 50 The x automatically is assigned to zero in FOR loops
    for x in range(31):
        print(x)


# The last for the second part of the integration project is def function,
# which allow you to create a function


def random_roll(dice):
    """The point of this function is to make up a function and be able to
    use that function throughout the whole project. This function rolls a
    random number depending on the dice chosen."""
    if dice == 6:
        print(random.randint(1, 6))
    elif dice == 12:
        print(random.randint(1, 12))


main()
