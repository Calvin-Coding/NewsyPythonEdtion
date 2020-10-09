import time


print("Welcome to Newsy (C) Calvin-Coding https://github.com/Calvin-Coding/NewsyPythonEdtion/blob/main/LICENSE")
name = raw_input("What is your name? ")
print("Welcome " + name)
print("LEVEL ONE")
print("Dear Editor, \n There has been disaster in our neighborhood Jonh Johnsons car has been stolen on 2/16/2020\n The one clue I have is the name Jerry Buffalo, find out who did this! \n Your Friend,\nGrant Bennet.")
print("Find Who Stole Jonh Johnsons Car!")


def newsDatabase():
    newsInput = raw_input("}- ")
    if newsInput == "--help":
        print("Commands\nSearch\nExit")
        newsDatabase()
    elif newsInput == "Search":
        searchName = raw_input("Enter Name}- ")
        if searchName == "Jerry Buffalo":
            print("SEARCHING")
            print("/")
            time.sleep(0.5)
            print("-")
            time.sleep(0.5)
            print("\\")
            time.sleep(0.5)
            print("3 ITEMS FOUND")
            print("A) POLICE RECORD INCLUDING \"JERRY BUFFALO\"\nB) MEDICAL FILE INCLUDING \"JERRY BUFFALO\"\nC) SCHOOL ENROLLMENT INCLUDING \"JERRY BUFFALO\"")
            i = 0
            while i <= 2:
            
                fileChoose = raw_input("Choose File}- ")
                if fileChoose == "A":
                    print("10:00 PM 2/16/2015\nJerry Buffalo was arrested for car jacking, turned over to hospital for\ntreatment. Later Sentinced to 4 years in prison realesed in custody with Jerry Deer")
                elif fileChoose == "B":
                    print("10:10 PM 2/16/2015\nJerry Buffalo was accepted in GHE Hospital for spinal injuies. Later turned over to Police.\n10:10 5/8/2020 Jerry Buffalo Died.")
                elif fileChoose == "C":
                    print("9:00 AM 2/15/2013\nJerry Buffalo was enrolled in a 2 year course in automotive repair. Along with Jerry Deer")
                i += 1
            
            newsDatabase()
        else:
            print("SEARCHING")
            print("/")
            time.sleep(0.5)
            print("-")
            time.sleep(0.5)
            print("\\")
            time.sleep(0.5)
            print("FILE NOT FOUND")
            newsDatabase()
    elif newsInput == "Exit":
        print("Who Stole Jonh Johnson's Car? ")
        answerWho = raw_input("Enter Name Here: ")
        if answerWho == "Jerry Deer":
            print("CONGRATS!!! YOU WON NEWSY PYTHON EDTION!")
    else:
        newsDatabase()
newsDataOpen = raw_input("Open News DataBase y/n")
if newsDataOpen == "y":
    print("type --help for help.")
    newsDatabase()

