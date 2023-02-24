score = 0
# Invite the user to the game
print("Welcome to my computer quiz")
want_to_play = input("Do you want to play my game?(yes or no) ")
#check if the user wants to play and give the correct feedback
if want_to_play.lower() == "yes":
    question1 = input("What is considered the brain of the computer? ")
    #Check if the user has the correct answer 
    if question1.lower() == "cpu":
        print("That is correct!")
        score += 1
    #If the answer is inocorrect print this
    else:
        print("That is incorrect")    
    question2 = input("what does RAM stand for? ")
    #Check if the user has the correct answer 
    if question2.lower() == ("random access memory"):
        print("That is correct!")
        score += 1
    #If the answer is inocorrect print this
    else:
        print("That is incorrect")
    question3 = input("What does GPU stand for? ")
    #Check if the user has the correct answer 
    if question3.lower() == "graphics processing unit":
        print("That is correct keep it up!")
        score += 1
    #If the answer is inocorrect print this
    else:
        print("That is incorrect")    
    question4 = input("What does PSU stand for? ")
    #Check if the user has the correct answer and calculate their score 
    if question4.lower() == "power supply":
        print("Great job!! ")
        score += 1 
        #Print the final score
        print(f'your final score is {score/4 * 100}% congragulations!')
    #If the answer is inocorrect print this
    else:
        print("That is incorrect")