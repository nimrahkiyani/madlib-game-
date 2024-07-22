import  random
def zoo():
    noun1 = input("Enter Noun: ")
    noun2 = input("Enter Noun: ")
    verb1 = input("Enter Verb: ")
    verb2 = input("Enter Verb: ")
    adjective1 = input("Enter Adjective: ")
    adjective2 = input("Enter Adjective: ")
    adjective3 = input("Enter Adjective: ")
    noun3 = input("Enter Noun: ")
    adjective = input("Enter Adjective: ")
    body_part = input("Enter body part: ")
    noun4 = input("Enter Noun: ")

    story = f"One night, I was walking through the {noun1} when I saw a {adjective1} light in the sky.\t Suddenly, a {adjective2} alien appeared and started {verb1} towards me.\t I couldn't believe my {body_part}! The alien said, Take me to your {noun2}, and handed\t me a {adjective3} {noun3}. I quickly {verb2} and ran back to my {noun4}.\t That was the most {adjective} night of my life!"

    print(story)


def birthday():
    noun1 = input("Enter Noun: ")
    verb1 = input("Enter Verb: ")
    verb2 = input("Enter Verb: ")
    adjective1 = input("Enter Adjective: ")
    adjective2 = input("Enter Adjective: ")
    adjective = input("Enter Adjective: ")
    verb3 = input("Enter Verb: ")

    adjective3 = input("Enter Adjective: ")
    adjective4 = input("Enter Adjective: ")

    plural_noun = input("Enter plural noun: ")
    name = input("Enter person name: ")

    story1 = f"Yesterday was my birthday, and it was {adjective}!\t First, a {adjective1} clown showed up with a bag of {plural_noun}.\t He started {verb1} them everywhere! Then, my friend {name} brought\t a {adjective2} cake shaped like a {noun1}. We all {verb2} and had a {adjective3} time.\t Just when I thought it couldn't get any better,\t a {adjective4} elephant walked in and started {verb3}. Best birthday ever!"


    print(story1)


def haunted_house():
    noun1 = input("Enter Noun: ")
    noun = input("Enter Noun: ")
    verb1 = input("Enter Verb: ")
    verb2 = input("Enter Verb: ")
    adjective1 = input("Enter Adjective: ")
    adjective2 = input("Enter Adjective: ")
    adjective = input("Enter Adjective: ")
    adjective3 = input("Enter Adjective: ")
    plural_noun = input("Enter plural noun: ")
    plural_noun1 = input("Enter plural noun: ")

    story2 = (f"On Halloween night, my friends and I went to a {adjective} haunted house.\t The door creaked open, and "
              f"we saw a {adjective1} {noun} floating in the air.\t Suddenly, a {adjective2} ghost appeared and started "
              f"{verb1}.\t We all {verb2} and hid behind a {noun1}.\t The ghost said, Boo! I'm just here for the "
              f"{plural_noun}! We all laughed and gave the ghost some {plural_noun1}.\t It turned out to be a "
              f"{adjective3} night!")

    print(story2)

while True:

    story_list = [zoo , haunted_house , birthday]

    random_action = random.choice(story_list)
    random_action()

    playAgain = input("Do you want to play again? (yes/no): ")
    if playAgain == "no":
        break

