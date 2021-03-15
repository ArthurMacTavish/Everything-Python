#Ask for Name
print("Hello, What is your name?")
name = input()

#No name check
if name == "":
    print("You don't have name? Haha")
    input("Press any key to Exit!")
    exit()

#Asking for Age
print("How old are you?")
age = int(input())

#Age Checker and Conditioning
if age < 0:
    print("No way, That's Illegal! No one is under 0 Years old!")
    input("Press any key to Exit!")
    exit()
elif age == 0:
    print("Are you even sure you are 0 years old?")
    input("Press any key to exit")
    exit()
elif age <= 12:
    ageCondition = "under"
elif age == 13:
    ageCondition = "exactly"
elif age >= 100:
    print("Give us a second to thinking... How?")
    print("You're " + str(age) + " years old!?")
    input("Jokes over, You're dead, " + name + ". So, Press any key to Exit!")
    exit()
elif age > 13:
    ageCondition = "over"

#Output
print ("So your name is " + name + ". You're " + str(age) + " years old, So you're " + ageCondition + " 13 years old")
input("Press any key to Exit!")
exit()