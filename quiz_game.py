print("Welcome to the computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does BCD stand for? ")
if answer.lower() == "binary coded decimal":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does BIU stand for? ")
if answer.lower() == "bus interface unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GUI stand for? ")
if answer.lower() == "graphical user interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")