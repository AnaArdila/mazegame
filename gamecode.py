import random
import time
import RPi.GPIO as GPIO
import espeak
import math

beginningItem = ""
frappe = False
inventory = []
locationTracker = []
name = ""
trollWin = False

#intro stuff
def displayIntro():
    print("You wake up feeling groggy. What happened? Where are you? \n" + 
          "You survey the area and see a bag by your side. Inside the bag \n" +
          "you see a sword, a potion, and armor.")
    print()

displayIntro()

def castleOutside():
    pass

def miniGameWallAvoid():
    pass

def collectBeginningItem():
    global beginningItem
    global inventory
    
    item = input("Which item do you want to choose? ").lower()
    inventory.append(item)

    if item == "sword":
        beginningItem = "sword"
    elif item == "potion":
        beginningItem = "potion"
    elif item == "armor":
        beginningItem = "armor"
    elif item == "none":
        beginningItem = "none"
    else:
        print("That's not a valid option, please try again.")
        collectBeginningItem()
    print()

    
#gameplay - start at bottom, work up from there
def jungle():
    pass

def catMania():
    pass

def leaveSmallChild():
    print("You get back on the path.")
    choice = input("Turn [right] or [left]? ").lower()
    while choice != "right" and choice != "left":
        print("Please choose a valid option")
        choice = input("Turn [right] or [left]? ").lower()
    if choice == "right":
        catMania()
    else:
        print("You've reached a dead end :(")
        
    

def smallChild():
    global beginningItem
    global inventory
    global locationTracker
    print("As you turn right, you see that this passsage is particularly long.\n" +
          "You start going deeper and deeper into the mist that's seeping from\n" +
          "every direction, when all of a sudden you see the figure of a person\n" +
          "in the distance. You yell out to them but they don't hear you so you start\n" +
          "running towards them. Finally, you reach them. It's a little kid, but disturbinngly\n" +
          "enough he had the same off-look as the old lady.")
    choice = input("[Talk to child] or [go ahead]? ").lower()
    while choice != "talk to child" and choice!= "go ahead":
        print("Please select a valid option.")
        choice = input("[Talk to child] or [go ahead]? ").lower()
    if choice == "talk to child":
        print("You ask the child his name, but he's not answering.")
        choice = input("[Walk away] or [keep trying]? ").lower()
        while choice != "walk away" and choice != "keep trying":
            print("Please choose a valid option.")
            choice = input("[Walk away] or [keep trying]? ").lower()
        if choice == "walk away":
            leaveSmallChild()
        if choice == "keep trying":
            locationTracker.append("smallChild")
            print("You try more but nothing is working. When you decide to turn to walk away\n" +
                  "you finally hear him speak.\n" +
                  "He tells you\nthat he'll give you a puzzle piece if you can guess his name correctly.")
            print("You ask him how you could possibly guess the right name out of billions.\n" +
                  "He tells you that there's a clue at the candy house.\n"
                  "This is when you begin to doubt whether talking to that kid is really worth\n"
                  "it. There's no way you're going all the way back just to guess a name.")
            if beginningItem == "sword" or beginningItem == "potion":
                choice = input("Use " + beginningItem + " on child? ").lower()
                while choice != "yes" and choice != "no":
                    print("Please choose a valid option.")
                    choice = input("Use " + beginningItem + " on child? ").lower()
                if choice == "yes" and beginningItem == "sword":
                    print("You lift up your sword and swing at the child. The child is able to\n" +
                          "dodge it and runs away. You look at yourself and what you almost did.\n")
                    choice = input("Was that worth it? ").lower()
                    while choice != "yes" and choice != "no":
                        print("Please choose a valid option.")
                        choice = input("Was that worth it? ").lower()
                    if choice == "yes":
                        
                        print("Hm.")
                        leaveSmallChild()
                    else:
                        print("At least you show some remorse, but actions will always have consequences.")
                        leaveSmallChild()
                elif choice == "yes" and beginningItem == "potion":
                    inventory.remove("potion")
                    print("You unscrew the potion bottle and throw the liquid at the child. They get hit.\n" +
                          "He falls to the ground and struggles to breath.")
                    choice = input("[Take puzzle piece and leave] child, he'll only slow you down or \n" +
                                   "[help child]? ").lower()
                    while choice != "take puzzle piece and leave" and choice != "help child":
                        print("Please choose a valid option.")
                    choice = input("[Take puzzle piece and leave] child, he'll only slow you down or \n" +
                                   "[help child]? ").lower()
                    if choice == "take puzzle piece and leave":
                        print("Hm.")
                        leaveSmallChild()
                    else:
                        print("You try to help him but you don't know what to do. He tells you all he wanted\n" +
                              "to do was play a simple game. He hadn't gotten to play since the old lady at the\n" +
                              "candy house made his twin sister, Gretel, disappear. With his dying last breaths he asks\n" +
                              "once again, what's my name?" )
                        choice = input("You whisper [guess name] ").lower()
                        if choice == "hansel":
                            print("Little to late.")
                        else:
                            print("You still guessed wrong. It's a shame you'll never find out...perhaps if\n" +
 "                                 you had simply talked to him...You remember about the puzzle piece.")
                            choice = input("[Take puzzle piece] or [leave]? ").lower()
                            while choice != "take puzzle piece" and choice != "leave":
                                print("Please choose a valid option.")
                                choice = input("[Take puzzle piece] or [leave]? ").lower()
                            if choice == "take puzzle piece":
                                print("Puzzle piece #3 collected.")
                                leaveSmallChild()
                            else:
                                print("Very well then.")
                                leaveSmallChild()
            else:
                print("Unfortunately, it looks like going back is your option lol or \n" +
                      "you could just not collect the puzzle piece...")
                choice = input("[Go back] or [move forward]? ").lower()
                while choice != "go back" and choice != "move forward":
                    print("Please choose a valid option.")
                    choice = input("[Go back] or [move forward]? ").lower()
                if choice == "go back":
                    mansionOutside2()
                else:
                    catMania()

    else:
        leaveSmallChild()

def leaveMansion():
    print("You get on the path and see you can either go back or continue ahead to where\n" +
          "there's a right turn.")
    choice = input("[Right] or [back]? ").lower()
    while choice != "right" and choice != "back":
        print("Please choose a valid option.")
        choice = input("[Right] or [back]? ").lower()
    if choice == "right":
        smallChild()
    else:
        towerOutside2()
    

def mansionBoxCombo():
    pass

def mansionInside():
    global locationTracker
    locationTracker.append(mansionInside)
    print("Although this mansion looks huge on the outside, curiously enough it’s completely empty except\n" +
          "for a box in the middle of the floor. The box has four buttons on it: red, yellow, blue, and \n" +
          "green. By it, there’s a note.")
    choice = input("[Read note] or try to [open box]? ").lower()
    while choice != "read note" and choice != "open box":
        print("Please select a valid option.")
        choice = input("[Read note] or try to [open box]? ").lower()
    if choice == "read note":
        print("The box will open if you press the buttons a certain way.\n" +
              "'Helpful,' you think to yourself.")
        choice = input("Enter [button combination]? [Quit]? ").lower()
        while choice != "button combination" and choice != "quit":
            print("Please select a valid choice.")
            choice = input("Enter [button combination]? [Quit]? ").lower()
        if choice == "button combination":
            mansionBoxCombo()
        else:
            leaveMansion()
    else:
        while choice != "button combination" and choice != "quit":
            print("Please select a valid choice.")
            choice = input("Enter [button combination]? [Quit]? ").lower()
        if choice == "button combination":
            mansionBoxCombo()
        else:
            leaveMansion()

def mansionOutside2():
    pass

def mansionOutside():
    global locationTracker
    locationTracker.append("mansionOutside")
    print("You don't what it is about this weird place, but there seems\n" +
          "to be abadoned buildings everywhere. The most recent one being\n" +
          "the mansion you have now walked upon.")
    choice = input("[Go inside] or [keep walking]? ").lower()
    while choice != "go inside" and choice != "keep walking":
        print("Please enter a valid choice.")
        choice = input("[Go inside] or [keep walking]? ").lower()
    if choice == "go inside":
        mansionInside()
    else:
        leaveMansion()

def towerClimb():
    return 51

def leaveTower():
    choice = input("[Go forward] or [turn right]? ").lower()
    if choice == "go forward":
        mansionOutside()
    elif choice == "turn right":
        jungle()
    else:
        print("Please choose a valid option.")
        leaveTower()

def towerOutside2():
    global inventory
    
    if puzzlePiece1 in inventory == False:
        towerOutside()
    else:
        print("You reached the tower")
        choice = input("Go back to [troll bridge], forward to [mansion], or turn [right]? ").lower()
        while choice != "troll bridge" and choice != "mansion" and choice != "right":
            print("Please choose a valid option.")
            choice = input("Go back to [troll bridge], forward to [mansion], or turn [right]? ").lower()
        if choice == "troll bridge":
            trollBridge2()
        elif choice == "mansion":
            mansionOutside2()
        else:
            jungle()
        


def towerOutside():
    global inventory
    global locationTracker
    
    print("You keep walking forward and begin to see a tower in the distance.\n" +
          "When you get close enough, you see that there is a light on top, but\n" +
          "You can't really tell what it is.")
    choice = input("[Climb to top] to reach the light or [continue walking]? ").lower()
    if choice == "climb to top":
        locationTracker.append("tower")
        if towerClimb() > 50:
            print("Congratulations, you got to the top! Right underneath the bright\n" +
                  "light you see a puzzle piece.")
            choice = input("[Take it] or [leave it]? ").lower()
            while( choice != "take it" and choice != "leave it"):
                print("Please choose a valid option.")
                choice = input("[Take it] or [leave it]? ").lower()
            
            if choice == "take it" or "take":
                print("Puzzle piece #1 collected.")
                inventory.append("puzzlePiece1")
                print("You decide to leave the tower and continue exploring.")
                leaveTower()
            else:
                print("You do you. You decide not to take the puzzle piece and\n" +
                      "continue exploring.")
                leaveTower()
        else:
            print("You failed to climb the tower, better luck next time.")
            towerOutside()
    else:
        leaveTower()
                
                    
def cave():
    pass


def leaveTroll():
    global name
    print("Before you leave the troll has one last question for you.")
    name = input("What is your name? ")
          
    choice = input("Continue [forward], [turn right], or go [back]? ").lower()
    if choice == "forward":
        towerOutside()
    elif choice == "right":
        cave()
    elif choice == "back":
        abadonedStarbucks()
    else:
        print("That's not a valid option, please try again.")
        leaveTroll()
    print()

def postTrollFight():
    global trollWin
    if trollWin == True:
        leaveTroll()
    else:
        choice = input("[Try again], [go back], [give gift], or [solve riddle]? ").lower()
        while choice != "try again" and "go back" and "give gift" and "solve riddle":
            print("Please enter a valid choice.")
            choice = input("[Try again], [go back], [give gift], or [solve riddle]? ").lower()
        if choice == "try again":
            trollFight()
        elif choice == "go back":
            abadonedStarbucks()
        elif choice == "give gift":
            trollGift()
        else:
            trollRiddle()
            

def trollFight():
    global inventory
    global beginningItem
    global trollWin


    playerLife = 100
    trollLife = 100
    print("Your total life points equals 100. If you let it reach 0 or below, you die.\n" +
          "The troll has 100 life points as well, get it to go below 0 and he won't die because\n" +
          "he's magical but you'll have earned his respect and he'll let you through.")
    print("You will hear a command go through at a random given time. If you respond under a \n" +
          "certain amount of time to the command then you will damage the enemy. If not, the \n" +
          "enemy will damage you. The blue button corresponds to hit\n" +
          "and the red button to kick. Press each button now to see the colors. Then hold down\n" +
          "both at the same time to start. Press third button to quit before game ends.")

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP) #set up pin 23 as an input.
    GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP) #set up pin 24 as an input.

    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)

    #use these lists to keep track of measured response times
    delays =[]

    es = espeak.ESpeak()
    es.speed=250

    GPIO.output(17,0)
    GPIO.output(4,0)
    if (GPIO.input(23) and GPIO.input(24)) == True:
        es.say("The fight will begin in five seconds. Be ready.")
        time.sleep(5)
        while playerLife > 0 and trollLife > 0:
            word = ""
            timing = 0
            #Your code here!
            #---listen for button
            #---randomly pick time to present light/sound stimulus (1<5 seconds)
            #---time how long it takes!

                
            ran_num = random.random()*5
            if ran_num < 2.5:
                word = "hit"
                time.sleep(ran_num)
                GPIO.output(4,1)
                start_time = time.time()
            else:
                word = "kick"
                time.sleep(ran_num)
                GPIO.output(17,1)
                start_time = time.time()

            if ran_num <2.5:
                while GPIO.input(23)!=0:
                    pass

            else:
                while GPIO.input(24)!=0:
                    pass

            timing = time.time() - start_time

            if timing > 0.4 and word == "hit":
                playerLife -= 20
                es.say("The troll hit you and you lost 20 life points!")
                es.say("You're now at {} life points".format(playerLife))
            elif timing > 0.4 and word == "kick":
                playerLife -= 20
                es.say("The troll kicked you and you lost 20 life points!")
                es.say("You're now at {} life points".format(playerLife))
            elif timing <= 0.4 and word == "hit":
                trollLife -= 20
                es.say("You hit the troll and the troll lost 20 life points!")
                es.say("The troll is now at {} life points".format(trollLife))
            else:
                trollLife -= 20
                es.say("You kicked the troll and the troll lost 20 life points!")
                es.say("The troll is now at {} life points".format(trollLife))

            delays.append(timing)
                
            #When done kill/reset stimuli:
            GPIO.output(4,0)
            GPIO.output(17,0)

    GPIO.cleanup()

    if playerLife <= 0:
        es.say("Unfortunately you lost, better luck next time.")
        postTrollFight()
          
    else:
        es.say("You won! You have earned the troll's respect and blessing to cross.")
        trollWin = True
        postTrollFight()

def trollRiddle():
    print("A woman had two sons who were born on the same hour of the same day of the same year.\n" +
              "But they were not twins.")
    choice = input("How could this be so? ").lower()
    if "triplets" in choice:
        print("Correct! The troll is satisfied and lets you go through.")
        leaveTroll()
    else:
        print("That is incorrect. Try again.")
        trollRiddle()
    print()

def trollGift():
    if "frappe" in inventory:
        print("You decide to give him the caramel frappe you got from the abadoned Starbucks.\n" +
              "He looks pleased with this gift and lets you through.")
        leaveTroll()
    else:
        print("You reach in your pocket and pull out a big old hand of nothing.\n" +
              "This does not impress the troll.")
        choice = input("Seems like you will either have to [fight] or solve the [riddle]. ").lower()
        if choice == "fight":
            trollFight()
        elif choice == "riddle":
            trollRiddle()

def trollBridge2():
    pass

def trollBridge():
    print("You enter a passageway that is filled with water. Luckily, there's a bridge.\n" +
          "You begin crossing it when a troll suddently pops out from underneath.\n" +
          "He says he won't let you pass unless you either [fight] him, give him a [gift], \n" +
          "or solve a [riddle].")
    choice = input("Which will it be? ").lower()
    if choice == "fight":
        trollFight()
    elif choice == "gift":
        trollGift()
    elif choice == "riddle":
        trollRiddle()
    
    else:
        print("That is not a valid choice. Please try again.")
        trollBridge()
    print()

def leaveStarbucks1():
    print("You walk down for a little but once again are forced to choose [left] or [right].")
    choice = input("What do you pick? ").lower()
    if choice == "left":
        print("Lol dead end. Try again.")
        leaveStarbucks1()
    elif choice == "right":
        trollBridge()
    else:
        print("That's not a valid option, please try again.")
        leaveStarbucks1()
    

#to the left of Candy House
def abadonedStarbucks():
    global inventory
    print("You go farther down the path and come across an abandoned StarBucks, no old ladies in sight.")
    choice = input("Go inside? ").lower()
    if choice == "yes":
        print("You never did get a bite of that candy house. Lucky for you, there happens to be a free\n" +
              "caramel frappe sitting on the counter.")
        choice = input("Take it? ").lower()
        if choice == "yes":
              inventory.append("frappe")
        print("You exit the abadoned Starbucks. You can either turn [left] or [head back] to the candy house.")
        choice = input("Which will it be? ").lower()
        if choice.casefold() == "left":
            leaveStarbucks1()
        else:
            candyHouseOutside2()
              
    elif choice == "no":
        choice = input("[Continue] the direction you were heading or [turn back]? ").lower()
        if choice == "continue":
            leaveStarbucks1()
        else:
            candyHouseOutside2()

def leaveCandyHouse():
    print()
    choice = input("You get back on the path. [Left] or [right]? ").lower()
    if choice == "left":
        abadonedStarbucks()
    elif choice == "right":
        
        startingPoint2()

def basementWithKey():
    print("You see a chest, it’s locked. Luckily, you have a key and a second later it's wide open.\n" +
                  "In it is a picture book. the picture book contains pictures of various kids looking \n" +
                  "over a chest….in a basement…almost exactly like what you’re doing right now…you get a strange \n" +
                  "feeling and decide to close the photo album. As you turn around, you see a flash go off. You \n" +
                  "start to run. When you get outside the old lady is no longer there. You look towards the door \n" +
                  "again and she’s sitting there staring at you with a vacant look in her eye. \n"
                  "Right above her head are three blue circles.")
    leaveCandyHouse()
    print()
    


def exploreCandyHouse():
    global locationTracker
    locationTracker.append("candyHouseInside")
    key = False
    print("You enter into her living room. There’s stairs leading both to the [attic] and \n" +
           "to the [basement].")
    choice = input("Which do you choose? ").lower()
    if choice == "attic":
        print("You go up the attic and see a chest wide open. Inside the chest contains a key.\n" +
              "You put it in your bag.Then go back down stairs.")
        key = True
        choice = input("Go to [basement] or [leave]? ").lower()
        if choice == "basement":
            basementWithKey()
        elif choice == "leave":
            leaveCandyHouse()
        else:
            print("That is not a valid option. Please try again.")
            
        
    elif choice == "basement":
        print("You see a chest, but unfortunately it's locked so you head back up stairs.")
        exploreCandyHouse()
            
              
    else:
        print("That is not a valid option. Please try again.")
        exploreCandyHouse()
    print()

def candyHouseOutside():
    global locationTracker
    locationTracker.append("candyHouseOutside")
    global beginningItem
    print("You make a left turn and see a trail of breadcrumbs on the road.\n" +
          "You begin following it and it leads you to a house made out of candy.\n" +
          "Perfect, you were beginning to feel a little hungry.")
    print()
    choice = input("[Eat house] or [knock on door] like a normal human being? ").lower()
    print()
    if choice == "eat house":
        print("Right as you were about to take a huge bite out of the chocolate \n"
              + "chip cookie walls, an old lady comes out and starts hitting you on \n"
              + "the head. Wow this lady really packs a punch.")
        print()

        if beginningItem != "none":
            choice = input("Use " + beginningItem + "? " ).lower()
            if choice == "yes":
                if beginningItem == "sword":
                    print("You frightened the old lady with the sword and she passed out.\n")
                    choice = input("[Explore] her house or [run away] in shame at what you just did? ").lower()
                    if choice == "explore":
                        exploreCandyHouse()
                    else:
                        leaveCandyHouse()
                elif beginningItem == "potion":
                    print("Ah so the old lady sees you're a fellow witch (which you do not/n" +
                          "obect to because you're terrified right now. She invites you, but/n" +
                          "then disappears all of a sudden.")
                    choice = input("[Explore] her house or [leave] because you're too shook to explore? ").lower()
                    if choice == "explore":
                        exploreCandyHouse()
                    else:
                        leaveCandyHouse()
                else:
                    print("The old lady eventually gets tired because you're armor is too strong so\n"+
                          "she passes out.")
                    choice = input("[Explore] her house or [leave] because what could she possible have of value.").lower()
                    if choice == "explore":
                        exploreCandyHouse()
                    else:
                        leaveCandyHouse()
                          
                          
        else:
            print("You need to run away before this old lady gives you a concussion.")
            choice = input("[Left] or [right]? ").lower()
            if choice == "right":
                startingPoint2()
            else:
                abadonedStarbucks()
            
                           
    elif choice == "knock on door":
        print("A nice old lady answers the door and invites you in. She gives you a bowl\n" +
              "of warm chocolate chip cookies and then proceeds to pass out on the couch.\n")                  
        print("Chocalate chip cookie +1")
        inventory.append("cookie")
        print()

        choice = input("Explore house? ").lower()
        if choice == "yes":
            exploreCandyHouse()
        elif choice == "no":
            leaveCandyHouse()
    elif choice == "Leave without exploring":
        leaveCandyHouse()
    else:
        print("Please choose a valid option.")
        candyHouseOutside()

def exploreCandyHouse3():
    global name
    print("As you head towards the basement, you look around for the old lady but she's\n" +
          "no where in sight. I wonder if she ever got in communication with that other kid...\n" +
          "Regardless you open the chest that contained the picture book. You flip to the first\n" +
          "page and notice a list of names...Hansel, Peter, Jack...but then you see something.\n" +
          "Is that? No it couldn't be...at the bottom of the page is your name: " + name)
    print("All of a sudden you hear the door shut. What do you do?")


def candyHouseOutside3():         
    print("You see the candy house and know straight where to go. You enter the house.")
    exploreCandyHouse3()

def candyHouseOutside2():
    print("You're back to the ever so familiar candy house. I wonder where the old lady went?...\n" +
          "Guess you'll find out sooner or later.")
    if "candyHouseInside" in locationTracker:
        print("You've already explored the house. You notice the three blue circles that were above the old\n" +
              "lady's head are painted crudely on the wall as well. You decide to leave as there's nothing\n" +
              "here for you.")
        leaveCandyHouse()
    else:
        choice = input("Would you like to [explore] the house or [get back] on path? ").lower()
        if choice == "explore":
            exploreCandyHouse()
        elif choice == "get back":
            leaveCandyHouse()
        else:
            print("Please choose a valid option.")
            candyHouseOutside2()
        

def startingPoint():
    print("You look down and see two yellow circles\n" +
          "I wonder what that could mean? Regardless, you decide to begin finding a way\n" +
          "out of your current predicament. You see a path leading in two directions.")
    choice = input("[Left] or [right]? ").lower()
    if choice == "left":
        candyHouseOutside()
    elif choice == "right":
        castleOutside()
    print()

def startingPoint2():
    global beginningItem
    global locationTracker
    if beginningItem == "none":
        choice = input("Would you like to [collect an item] now, [go left], or [go right]? ").lower()
        if choice == "collect an item":
            collectBeginningItem()
            startingPoint2()
        elif choice == "go left":
            if "candyHouseOutside" in locationTracker:
                candyHouseOutside2()
            else:
                candyHouseOutside()
        elif choice == "go right":
            castleOutside()
        else:
             print("That's not a valid option, please try again.")
             startingPoint2()
    else:
        print("You're back to the spot with two yellow circles.")
        choice = input("Would you like to [go left] or [go right]? ").lower()
        if choice == "go left":
            if "candyHouseOutside" in locationTracker:
                candyHouseOutside2()
            else:
                candyHouseOutside()
        elif choice == "go right":
            castleOutside()
        else:
             print("That's not a valid option, please try again.")
             startingPoint2()


collectBeginningItem()
startingPoint()

def childrenLaughter():
    print("All of a sudden you hear children's laughter.")
    choice = input("Head [towards] or [away] from it? ").lower()
    print()
    if choice == "towards":
        candyHouseOutside()
    elif choice == "away":
        print("welp")
    else:
        print("That's not a valid option, please try again.")
        childrenLaughter()
    print()

