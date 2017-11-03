import random
inventory=[]
position=0
invsave=[0]
window=False
rafid=False
sounds=0
patrys=0
stresslvl=0
broom=False
flooronekey=False
searcher=False
magnetman=False
nowboard=False
nowbook=False
popquiz=False
eraser=False
swordbots=False
vocabwords=False
crucible=False
difficulty=1
workout=0
gymevent=False
studentathlete=False
keyloc=random.randint(1,4)
floortwokey=False
name="default"
itemlist=[position, window, rafid, sounds, patrys, stresslvl, broom, flooronekey, searcher, magnetman, nowboard, nowbook, popquiz, eraser, swordbots, vocabwords, crucible, difficulty, floortwokey, name]
inventorysave=[]
def stress(change):
    global stresslvl
    stresslvl=stresslvl+change
    if stresslvl<0:
        stresslvl=0
    if stresslvl>=5 and stresslvl-change<5 and stresslvl<10:
        print("The school seems a little darker.")
    if stresslvl>=10 and stresslvl-change<10 and stresslvl<15:
        print("The shadows grow a little bit.")
    if stresslvl>=15 and stresslvl-change<15 and stresslvl<20:
        print("You begin to panic. The school seems hostile.")
    if stresslvl>=20 and stresslvl-change<20 and stresslvl<25:
        print("You begin to hear things around you. Whispers. Footsteps. Crying. There seems to be a constant shadow at the edge of your vision.")
    if stresslvl>=24.4 and stresslvl-change<24.4 and stresslvl<25:
        print("You are on the very brink of madness")
    if stresslvl>=25:
        dead(0)
    if stresslvl<5 and stresslvl-change>=5:
        print("The school brightens. Your resolve grows.")
    if stresslvl<10 and stresslvl-change>=10:
        print("The shadows recede slightly.")
    if stresslvl<15 and stresslvl-change>=15:
        print("You take a few deep breaths and calm yourself. You think that the school seems less angry.")
    if stresslvl<20 and stresslvl-change>=20:
        print("The noises stop suddenly. You wonder if you truly did imagine them.")
    if stresslvl<0:
        stresslvl=0

def save():
    print("SAVING...DO NOT TURN OFF THE POWER")
    global itemlist
    global invsave
    global inventorysave
    itemlist=[position, window, rafid, sounds, patrys, stresslvl, broom, flooronekey, searcher, magnetman, nowboard, nowbook, popquiz, eraser, swordbots, vocabwords, crucible, difficulty, floortwokey, name, gymevent, workout, studentathlete]
    invsave=[]
    inventorysave=[]
    for x in itemlist:
        invsave.append(x)
    for y in inventory:
        inventorysave.append(y)


def load():
    global inventory
    print("Loading...") #don't judge me for my brute force code please
    global position, window, rafid, sounds, patrys, stresslvl, broom, flooronekey, searcher, magnetman, nowboard, nowbook, popquiz, eraser, swordbots, vocabwords, crucible, difficulty, name, workout, gymevent, studentathlete, floortwokey
    position=invsave[0]
    window=invsave[1]
    rafid=invsave[2]
    sounds=invsave[3]
    patrys=invsave[4]
    stresslvl=invsave[5]
    broom=invsave[6]
    flooronekey=invsave[7]
    searcher=invsave[8]
    magnetman=invsave[9]
    nowboard=invsave[10]
    nowbook=invsave[11]
    popquiz=invsave[12]
    eraser=invsave[13]
    swordbots=invsave[14]
    vocabwords=invsave[15]
    crucible=invsave[16]
    difficulty=invsave[17]
    floortwokey=invsave[18]
    name=invsave[19]
    gymevent=invsave[20]
    workout=invsave[21]
    studentathlete=invsave[21]
    inventory=inventorysave
    whereAmI()
def encounter():
    global position
    retry=True
    while retry==True:
        retry=False
        if position==13:
            print("As you enter the makerspace, bladed robotic arms whir to life around you. Apparently some senior made a sword-fighting army to defend team 1257.\nNot for the first time, you mutter curses at the seniors.\n1. Try to fight them\n2. Run\n3. Item")
            choice=eventchoose(3)
            if choice==1:
                chan=random.randint(1,3)
                if chan==3:
                    print("You call upon your gymnastic skills, and manage to dive and dodge through the whirling blades. You see a big red button labeled 'STOP' and slam it.\nThe blades keep whirling. You briefly ponder your options.")
                    chan=random.randint(1,3)
                    if chan==3:
                        print("You once again call upon your gymnastic skills, and execute a perfect escape, with not a scratch on you. You decide to never do that again, as your odds of survival are low.")
                    else:
                        print("You try to escape, but are too disheartened by faulty labeling. You barely dodge a first cut, and the rest follow too quickly to escape.")
                        dead(2)
                else:
                    print("Pondering the sheer stupidity of this decision, you dive headfirst into the blades. You last less than a second.")
                    dead(2)
            if choice==2:
                print("You back away from the swords, which slow down with your departure.")
                position=6
            if choice==3:
                ituse=eventitem()
                if ituse=="Bruce's broom":
                    print("You take out Bruce's Broom from your pocket, and hope that it really is as strong as it feels. Thankfully, Bruce is ridiculously strong, and his broom reflects this.\nYou parry the swords, which shatter upon contact. In a short time, you are victorious.")
                    stress(-4)
                    global swordbots
                    swordbots=True
                    save()
                elif ituse=="retry":
                    retry=True
                else:
                    print(f"You take out {ituse} from your pocket. You have no idea how you are going to use it against a bunch of sword-bots, but you try anyway. It doesn't work.")
                    dead(2)
        if position==99:
            print("You enter the dark closet. You immediately feel a familiar sense of dread from within, but cannot place its source. Something about the room seems overly wordy.\n1. Venture further\n2. Leave closet\n3. Item")
            choice=eventchoose(3)
            if choice==1:
                print("As you inch forward cautiously, the door closes silently behind you. By the time you realize what happened, it is too late. You see the vocabulary books on\nMrs. Pinto's desk. Semi-difficult words flood the air, some baffling you with their insuetude, others driving you mad with their simplicity. Your mind fragments.")
                dead(2)
            if choice==2:
                print("You briskly backpedal from the ominously stygian obscurity.")
                position=14
            if choice==3:
                ituse=eventitem()
                if ituse=="The Holy Book of Mr. Nowakoski":
                    print("You take the book from your pocket, and ponder how to read it in the darkness. This problem is quickly solved for you by the appearance of a halo over your head.\nAs the vocabulary books on the desk release their semi-obscure words, such as 'adventitious' and 'precept', you intone the holy syllables of 'ghoti' and 'rasterbate'\nobliterating them with the rarity of the words. As the last of the evil words fade, you flip the light switch and close the book, murmurring a thanks to the gods of\nderivational morphology.")
                    stress(-4)
                    global vocabwords
                    vocabwords=True
                    save()
                elif ituse=="retry":
                    retry=True
                else:
                    print(f"You take out {ituse} from your pocket. You don't have a chance to figure out how to use it, before you hear 'SOPORIFIC'. You fall to your knees, barely able to\nremain conscious. As your eyes close, you hear 'CURTAIL' and then nothing.")
                    dead(2)
        if position==11:
            global gymevent
            print("You enter the gym, which is less empty than you would have thought. A stereotypical jock is working out at one of the bicep curls, and looks up as you walk in. He walks towards you menacingly, looking like he is about to punch you. You notice that he has skipped leg day (and frankly looks illiterate)\n1. Try to reason with him\n2. Expeditious Retreat\n3. Item")
            if studentathlete==True:
                print("4. Stand up to him because you are a student athlete too.")
                choice=eventchoose(4)
            else:
                choice=eventchoose(3)
            if choice==1:
                print("You manage to get about four words out before you are beaten to death.")
                dead(2)
            if choice==2:
                print("You hastily back away, closing the door firmly behind you. Thankfully, the jock doesn't seem to grasp the concept of a doorknob.")
                position=10
            if choice==3:
                ituse=eventitem()
                if ituse=="The Crucible" or ituse=="The Holy Book of Mr. Nowakoski":
                    if ituse=="The Holy Book of Mr. Nowakoski":
                        print("The jock seems more confused than stunned, evidently not comprehending what he is seeing. Perhaps a different book will do the trick.")
                        ituse=eventitem()
                        if ituse!="The Crucible" and ituse!="retry":
                            print(f"You take {ituse} from your pocket, but it doesn't have any effect on the jock. You die a painful death.")
                            dead(2)
                        elif ituse=="retry":
                            print("Deciding to take nothing out of your pocket is not a great plan here.")
                            dead(2)
                        else:
                            pass
                    print("You pull the book from your pocket, and the jock is nearly stunned by the prospect of reading. He recovers fairly quickly, and is enraged at your attempt to educate him. You are now cornered by an angry jock. Only a miracle could save you now.\n1. Pray for a miracle\n2. Item")
                    choice=eventchoose(2)
                    if choice==1:
                        prayer=random.randint(1,20)
                        if prayer==20:
                            print("By some miracle, some god actually seems to hear your prayer, and intervenes. As the jock raises his fists a pile of bread and fish falls on to him from out of thin air. After a few minutes of praising the gods of magnet, you take a loaf and a fish, as proof that miracles are real.")
                            inventory.append("Loaf of Bread", "Slightly Smelly Fish (Trout?)")
                        else:
                            print("The gods are deaf to your pleas for mercy, and the jock kills you with a swift blow to the head, then goes back to working out.")
                            dead(2)
                    if choice==2:
                        ituse=eventitem()
                        if ituse=="Mr. McMenamin's Lucky Eraser":
                            print("You take out the lucky eraser, and invoke the power that once propelled that one guy's consistent billion-point slides (what was his name again?). It works far better than you could have ever hoped for. In a room full of metal equipment, lightning streaks through the window and strikes the jock in the back, affecting his magnetic polarity, in addition to other less serious effects, such as heart failure. The magnetism pulls various metal objects from across the room to him at high velocities, burying him under a pile of weights and treadmills. From beneath the pile, you hear the telltale sound of someone suffering both a stroke and a brain aneurysm simultaneously.")
                            gymevent=True
                            stress(-3)
                            save()
                        elif ituse=="The Crucible" or ituse=="The Holy Book of Mr. Nowakoski":
                            print("Congratulations! You made the angry jock even angrier. If your friends could see you, they would applaud your wisdom. You are bludgeoned to death.")
                            dead(2)
                        elif ituse=="retry":
                            print("You resign yourself to your fate.")
                            dead(2)
                        else:
                            print(f"You take {ituse} from your pocket. It doesn't do anything, and you are beaten senseless, and subsequently, lifeless.")
                            dead(2)
                elif ituse=="retry":
                    retry=True
                else:
                    print(f"You take {ituse} from your pocket. It doesn't do anything, and you are beaten senseless, and subsequently, lifeless.")
                    dead(2)
            if choice==4:
                print("You use your hard earned strength and your iron will to fight the jock. You manage to corner him, but he lashes out in one desperate attempt.\n1. Deflect with arm\n2. Item")
                choice=eventchoose(2)
                if choice==1:
                    print("You block the blow, and uppercut him with your other arm. He dies, but your arm hurts like heck")
                    stress(4)
                    gymevent=True
                    save()
                else:
                    ituse=eventitem()
                    if ituse=="Bruce's broom":
                        print("You block the blow with Bruce's (seemingly indestructible) broom. The jock's arm shatters, and he falls to the floor. After a few pokes, you determine that he is dead.")
                        gymevent=True
                        stress(-3)
                        save()
                    else:
                        print(f"You take {ituse} from your pocket, but don't have time to use it before the impact severs your student head from your athletic body.")
                        dead(2)

def eventitem():
    global inventory
    number=0
    for x in inventory:
        number+=1
        number=str(number)
        print (number+". "+str(x))
        number=int(number)
    print(f"{number+1}. Cancel")
    while True:
        global flooronekey
        use=input("What do you do? ")
        try:
            int(use)
        except ValueError:
            use=input("Invalid command. Try again: ")
        use=int(use)
        if use<=number and use>=1:
            return inventory[use-1]
        elif use==number+1:
            return "retry"
        else:
            print("You don't have that. Try again.")
def eventchoose(number):
    choice=input("Choose: ")
    itsok=False
    while itsok==False:
        itsok=True
        isanint=True
        try:
            int(choice)
        except ValueError:
            choice=input("Invalid command. Try again: ")
            itsok=False
            isanint=False
        if isanint==True:
            choice=int(choice)
            if choice>number or choice<1:
                choice=input("Invalid command. Try again: ")
                itsok=False
    return choice

def dead(death):
    if death==0:
        print("The voices in your head grow to be unbearable. You sit down in a corner, and glance at the clock. Your glance meets the red 12:00 just as it begins to flash 'BELL'.\nHow did it get that late? Your mind is still reeling as the lights go out. The noises are drowned out by one sinister laugh. A shadow that is somehow darker than\nthe night appears in front of you. You scream, and the shadow grabs you. The last thing that you see is the red 'HELL' on the clock.")
    if death==1:
        print("The last thing you see is Mr. Rafalowski's face on his ID. His smile seems too wide, as if he finds you humorous. You see nothing after that.")
    print("YOU HAVE DIED")
    if invsave[0]==0:
        jack=input()
        while True:
            x=random.randint(1,5)
            if x==1:
                print("ALL WORK AND NO PLAY MAKES JACK A DULL BOY")
            if x==2:
                print("A LLWO RK ANDNO PLAYMA KESJA CKAD U LLBO Y")
            if x==3:
                print("ALLWORKANDNOPLAYMAKESJACKADULLBOYALLWORKAN")
                print("DNOPLAYMAKESJACKADULLBOYALLWORKANDNOPLAYMA")
            if x==4:
                print("ALL WORK  AND NO PLAY MIGHT JUST KILL  YOU")
            if x==5:
                print("DEAR MAGNET: STRESS LESS MORE STRESS DEATH")
    else:
        jack=input("Reload last save? Y/N: ")
        if jack=="n" or jack=="N":
            while True:
                x=random.randint(1,5)
                if x==1:
                    print("ALL WORK AND NO PLAY MAKES JACK A DULL BOY")
                if x==2:
                    print("A LLWO RK ANDNO PLAYMA KESJA CKAD U LLBO Y")
                if x==3:
                    print("ALLWORKANDNOPLAYMAKESJACKADULLBOYALLWORKAN")
                    print("DNOPLAYMAKESJACKADULLBOYALLWORKANDNOPLAYMA")
                if x==4:
                    print("ALL WORK  AND NO PLAY MIGHT JUST KILL  YOU")
                if x==5:
                    print("DEAR MAGNET: STRESS LESS MORE STRESS DEATH")
        else:
            load()
def things(room):
    if room==2 and rafid==False:
        print("You see the ID card of Mr. Rafalowski. It glints with undiscovered secrets.")
    if room==3 and broom==False:
        print("You see the Broom of Bruce. It seems to be the only object in the room that is perfectly clean.")
    if room==6 and searcher==False:
        print("You see Mrs. Gerstein's latest invention. It looks to be far more advanced than you could ever hope to understand.")
    if room==7 and popquiz==False:
        print("You see a stack of papers on the desk. You feel a sense of dread from just looking at them.")
        stress(0.5)
    if room==15 and eraser==False:
        print("You see the eraser on the board. You recall someone getting 2 billion points in one class.")
    if room==99 and crucible==False:
        print("You see 'The Crucible' on the desk.")
    if room==26 and yearbook==False:
        print("You see a yearbook in the corner")
    if room==21 and terrycad==False:
        print("You see a flash drive on Theresa 'Terry' OConnor's desk")
    if room==31 and kippcad==False:
        print("You see a flash drive on Mrs. Kipp's desk")



def item():
    global inventory
    number=0
    for x in inventory:
        number+=1
        number=str(number)
        print (number+". "+str(x))
        number=int(number)
    print(f"{number+1}. Cancel")
    while True:
        global flooronekey
        use=input("Which item do you use? ")
        try:
            int(use)
        except ValueError:
            use=input("Invalid command. Try again: ")
        use=int(use)
        if use<=number and use>=1:
            itemused=inventory[use-1]
            if itemused=="Mrs. Gerstein's Searcher of Seeking":
                print("You take the searcher from your pocket and scan the area.")
                if stresslvl>15 and random.randint(15,30)-stresslvl<=0:
                    print("Your palms are sweating. Your knees are weak and your arms are heavy. You fumble with the device, but only succeed in playing a rap playlist.")
                    stress(random.randint(-1,1))
                    return "retry"
                if (position==1 and keyloc==3) or (position==5 and keyloc==2) or (position==12 and keyloc==4) or (position==10 and keyloc==1) and flooronekey==False:
                    print("You find a set of keys! They seem to be from the cleaners, but they're usually good about not leaving things lying around...")
                    inventory.append("Floor one keys")
                    flooronekey=True
                    return "retry"
                else:
                    print("You find nothing")
                    return "retry"
            if itemused=="Mr. Sanservino's Test":
                if stresslvl<20:
                    print("You aren't insane enough to use that yet. You do not fully understand the powers that you are toying with.")
                    return "retry"
                elif stresslvl>=20:
                    areyousure=input("As scared as you are, this seems like it could go very badly for you. Just looking at the test makes your mind throb. Are you sure? Y/N: ")
                    if areyousure=="y" or areyousure=="Y":
                        if stresslvl>=24:
                            print("Your mind is on the very edge of collapsing as you take the test from your pocket. The benign words that you see by daytime tell an entirely different story by\nnight. You don't have enough resolve left to stop yourself, and with what may be your last sane thought, you read the paper. Incredibly, you don't die. Your mind is at the same\nlevel of insanity as that of Mr. Sanservino, and in the moment that your mind fragments, you discover the power of the madness; the strength of those with nothing to\nlose and no one to fear. Whoever finds you in the morning will be in for quite a surprise. In the distance, you hear an italian laugh.")
                            victory(1)
                        else:
                            print("In your state of insanity, you determine that reading Mr. Sanservino's test is a good choice. You are horribly wrong. As you read it, the shadows reach from\nevery corner towards you, and the voices in your head begin to scream. After that, there is only darkness.")
                            dead(2)
            else:
                print(f"Dr. Fang's words echoed... {name}, there is a time and place for everything, but not now.")
                return "retry"
        elif use==number+1:
            return "retry"
        else:
            print("Invalid Command. Try again.")

def victory(win):
    if win==1:
        print("You have survived the night, but at the cost of your sanity. Despite your appearance, you are unrecognizable as the person who was trapped inside Magnet for the night.")
        print("Victory?")
        jack=input()
        print("With your new powers, and freedom to use them, the only question is:")
        while True:
            choice=input("What do you do? ")
def chose(number):
    while True:
        choice=input("What do you do? ")
        itsok=False
        while itsok==False:
            itsok=True
            isanint=True
            try:
                int(choice)
            except ValueError:
                choice=input("Invalid command. Try again: ")
                itsok=False
                isanint=False
            if isanint==True:
                choice=int(choice)
                if choice>number or choice<1:
                    choice=input("Invalid command. Try again: ")
                    itsok=False
        choice=int(choice)
        go=option(choice)
        if go=="retry":
            pass
        else:
            stress(difficulty)
            return go
def whereAmI():
    global position
    while True:
        if position==0:
            print("\nYou are in the main lobby of the dark school. You see hallways leading north and east, and stairs leading up.\n1. North Hallway\n2. East Hallway\n3. Stairs Up\n4. Main Office\n5. Item")
            position=chose(5)
        if position==1:
            print("\nYou are in the southern hallway of the first floor.\n1. Go east\n2. Go west\n3. Broom Closet\n4. Auditorium\n5. Item")
            position=chose(6)
        if position==2:
            print("\nYou are in the main office of the school. You see the announcement system.")
            things(2)
            if rafid==False:
                print("1. Leave office\n2. Use announcement system\n3. Item\n4. Take ID")
                position=chose(4)
            else:
                print("1. Leave office\n2. Use announcement system\n3. Item")
                position=chose(3)
        if position==3:
            print("\nYou are in the small broom closet.")
            things(3)
            print("1. Leave broom closet\n2. Item")
            if broom==False:
                print("3. Take Broom")
                position=chose(3)
            else:
                position=chose(2)
        if position==4:
            print("\nYou are in the dark auditorium. You see a light switch and a podium. There is a closet in the corner.\n1. Leave auditorium\n2. Flip light switch\n3. Give a speech\n4. Open closet\n5. Item")
            position=chose(5)
        if position==5:
            print("\nYou are in the eastern hallway of the first floor. The hallway continues to the north and south. You see Mr. Nowakoski's, Mr. Sanservino's and Mrs. Gerstein's rooms.\n1. Go north\n2. Go south\n3. Enter Mr. Nowakoski's room\n4. Enter Mr. Sanservino's room\n5. Enter Mrs. Gerstein's room\n6. Item")
            position=chose(6)
        if position==10:
            print("\nYou are in the northern hallway of the first floor. The hallway continues to the east and west. You see the fitness center.\n1. Go east\n2. Go west\n3. Enter fitness center\n4. Item")
            position=chose(4)
        if position==6:
            print("\nYou are in Mrs. Gerstein's room. You see a door leading to the Maker Space.")
            things(6)
            print("1. Leave room\n2. Enter Maker Space\n3. Item")
            if searcher==False:
                print("4. Take Invention")
                position=chose(4)
            else:
                position=chose(3)
        if position==12:
            print("You are in the eastern hallway of the first floor. The hallway continues to the north and south. You see Mr. McMenamin's and Ms. Arnold's rooms. There is a window in the eastern wall.\n1. Go north\n2. Go south\n3. Enter Mr. McMenamin's room\n4. Enter Ms. Arnold's room\n5. Look out the window\n6. Item")
            position=chose(6)
        if position==8:
            print("You are in the room of Mr. Nowakoski. You can feel the holiness of the place around you. You see his board of sayings in the back of the room, and his collection of books in the front.\n1. Leave room\n2. Look at the wall\n3. Look at the books\n4. Item")
            position=chose(4)
        if position==7:
            print("You have gained entry to the room of Mr. Sanservino. Just being in here chills your blood. You see the presentation podium at the front of the room.")
            things(7)
            stress(0.5)
            print("1. Leave classroom\n2. Practice a presentation\n3. Item")
            if popquiz==False:
                print("4. Take papers")
                position=chose(4)
            else:
                position=chose(3)
        if position==14:
            print("You enter Ms. Arnold's room. You see a door leading to Mrs. Pinto's office. There is writing on the whiteboard.\n1. Leave room\n2. Enter office\n3. Look at whiteboard\n4. Item")
            position=chose(4)
        if position==13:
            if swordbots==True:
                print("You enter the makerspace. You see several manufacturing machines. \n1. Leave the makerspace\n2. Item")
                position=chose(2)
            else:
                encounter()
        if position==15:
            print("You enter Mr. McMenamin's room. You reminisce briefly.")
            things(15)
            print("1. Leave room\n2. Reminisce some more\n3. Item")
            if eraser==True:
                position=chose(3)
            else:
                print("4. Take eraser")
                position=chose(4)
        if position==99:
            if vocabwords==False:
                encounter()
            else:
                print("You stand in Mrs. Pinto's office. It's not very large, but it is very cluttered.")
                things(99)
                print("1. Leave office\n2. Item")
                if crucible==False:
                    print("3. Take 'The Crucible'")
                    position=chose(3)
                else:
                    position=chose(2)
        if position==11:
            if gymevent==False:
                encounter()
            else:
                print("You stand in the gym, surrounded by workout equipment and the smell of sweat.\n1. Leave gym\n2. Item\n3. Get swoll")
                position=chose(3)
        if position==17:
            print("You stand outside the senior lounge. You see hallways leading to the north and to the east.\n1. Go north\n2. Go east\n3. Enter senior lounge\n4. Item")
            position=chose(4)
        if position==18:
            print("You are in the southern hallway of the second floor. The hallway continues to the east and west. You see Mr. Liu's, Mr. Straut's and Mrs. OConnor's rooms.\n1. Go east\n2. Go west\n3. Enter Mr. Liu's room\n4. Enter Mr. Straut's room\n5. Enter Mrs. OConnor's room\n6. Item")
            position=chose(6)
        if position==22:
            print("You are in the eastern hallway of the second floor. The hallway continues to the north and south. You see Dr. Fang's and Dr. Jiderian's rooms.\n1. Go north\n2. Go south\n3. Enter Dr. Fang's room\n4. Dr. Jiderian's room\n5. Item")
            position=chose(5)
        if position==27:
            print("You are in the northern hallway of the second floor. The hallway continues to the east and west. You see Senora Mejia's and Mrs. Mansfield-Smith's rooms.\n1. Go east\n2. Go west\n3. Enter Senora Mejia's room\n4. Enter Mrs. Mansfield-Smith's room\n5. Item")
            position=chose(5)
        if position==29:
            print("You are in the western hallway of the second floor. The hallway continues to the north and south. You see Mr. Raite's, Mrs. Kipp's and Mr. Merkl's room\n1. Go north\n2. Go south\n3. Enter Mr. Raite's room\n4. Enter Mrs. Kipp's room\n5. Enter Mr. Merkl's room\n6. Item")
            position=chose(6)
        if position==26:
            print("You are in Senora Mejia's room")
            things(26)
            print("1. Leave room\n2. Item")
            if yearbook==False:
                print("3. Take yearbook")
                position=chose(3)
            else:
                position=chose(2)
        if position==21:
            print("You are in Mrs. OConnor's room. Banks of computers light the room, each with a 'spinny' chair in front of it.")
            things(21)
            print("1. Leave room\n2. Spin in a chair\n3. Item")
            if terrycad==False:
                print("4. Take flash drive")
                position=chose(4)
            else:
                position=chose(3)
        if position==20:
            print("You are in Mr. Liu's room. You reminisce about his old room, and the daily Rukkus games.")
            things(20)
            print("1. Leave room\n2. Item")
            if table==False:
                print("3. Investigate Table")
                position=chose(3)
            else:
                position=chose(2)
        if position==32:
            print("You are in Mr. Raite's room. You see a door leading to a closet with a sign labeled 'DANGER'.")
            things(32)
            print("1. Leave room\n2. Enter chemical storage\n3. Item")
            if lighter==False:
                print("4. Take lighter")
                position=chose(4)
            else:
                position=chose(3)
        if position==19:
            print("You are in Mr. Straut's room. While some people liked him, you kind of hated him.")
            things(19)
            print("1. Leave room\n2. Item")
            position=chose(2)








def option (instruct):
    global difficulty
    global itemlist
    global position
    global rafid
    global searcher
    global popquiz
    global eraser
    if position==0:
        if instruct==1:
            print("You enter the hallway to the north.")
            return 12
        if instruct==2:
            print("You enter the hallway to the east.")
            return 1
        if instruct==3:
            print("You climb the stairs")
            return 17
        if instruct==4:
            if flooronekey==True:
                print("You enter the main office")
                return 2
            else:
                print("The door is locked.")
                return "retry"
        if instruct==5:
            return item()
    if position==2:
        global searcher
        global inventory
        if instruct==1:
            print("You leave the office.")
            return 0
        if instruct==2:
            print("You use the announcement system. You always wanted to do that.")
            stress(-1)
            global patrys
            global sounds
            if random.randint(1,10)<=patrys:
                if sounds==0:
                    print("You hear sounds from somewhere in the school. They are too loud to be accidental.")
                    stress(6)
                    sounds=1
                    patrys-=1
                elif sounds==1:
                    print("Your blood chills. Something is watching you.")
                    stress(9)
                    sounds=2
                elif sounds==2:
                    print("You only get a glimpse of the figure bearing down on you. It is too large to be human and too fast to stop.")
                    dead(1)
            patrys+=1
            return "retry"
        if instruct==4 and rafid==False:
            print("You take Mr. Rafalowski's ID. You can feel its power flow through you.")
            rafid=True
            inventory.append("Mr. Rafalowski's ID Card")
            return "retry"
        if instruct==3:
            return item()
        else:
            print("You already picked that up")
            return "retry"
    if position==1:
        if instruct==1:
            print("You go east.")
            return 5
        if instruct==2:
            print("You go west.")
            return 0
        if instruct==3 and flooronekey==True:
            print("You enter the broom closet.")
            return 3
        elif instruct==3:
            print("The door is locked")
            return "retry"
        if instruct==4:
            print("You enter the auditorium.")
            return 4
        if instruct==5:
            return item()
    if position==3:
        global broom
        if instruct==1:
            print("You leave the broom closet.")
            return 1
        if instruct==2:
            return item()
        if instruct==3 and broom==False:
            print("You pick up the broom. Your legs nearly buckling from its surprising weight.")
            broom=True
            inventory.append("Bruce's broom")
            return "retry"
        else:
            print("You already picked up the broom")
            return "retry"
    if position==4:
        if instruct==1:
            print("You leave the auditorium")
            return 1
        elif instruct==2:
            print("You flip the switch. Nothing happens.")
            return "retry"
        elif instruct==3:
            print ("You give a speech to the empty room. You hear nothing, but sense that something is listening to you.")
            stress(2)
            return "retry"
        elif instruct==4:
            if flooronekey==True:
                print("You open the closet. You see only water bottles and stacks of paper.")
                global magnetman
                if searcher==True and magnetman==False:
                    print("Mrs. Gerstein's invention lights up in your pocket and emits a loud tone. A suit of armor materializes from the shadows, as if it had been invisible. It's Magnet Man!")
                    magnetman=True
                    inventory.append("The Magnet Man")
                    stress(-3)
                    return "retry"
                else:
                    print("You can't see anything important, so you close the closet")
                    return "retry"
            else:
                print("The door is locked")
                return "retry"
        elif instruct==5:
            return item()
    if position==5:
        if instruct==1:
            print("You walk north")
            return 10
        if instruct==2:
            print("You walk south")
            return 1
        if instruct==3:
            if flooronekey==True:
                print("You enter Mr. Nowakoski's room")
                return 8
            else:
                print("The door is locked")
                return "retry"
        if instruct==4:
            if flooronekey==True:
                print("You enter Mr. Sanservino's room")
                return 7
            else:
                print("The door is locked")
                return "retry"
        if instruct==5:
            print("You enter Mrs. Gerstein's room")
            return 6
        if instruct==6:
            return item()
    if position==6:
        if instruct==1:
            print("You leave the room")
            return 5
        if instruct==2:
            if flooronekey==True:
                print("You enter the Maker Space")
                return 13
            else:
                print("The door is locked")
                return "retry"
        if instruct==3:
            return item()
        if instruct==4 and searcher==False:
            print("You take the invention. Upon closer inspection, you discern that it can be used to locate hidden things")
            inventory.append("Mrs. Gerstein's Searcher of Seeking")
            searcher=True
            return "retry"
        else:
            print("You already picked up the invention")
            return "retry"
    if position==10:
        if instruct==1:
            print("You go east")
            return 5
        if instruct==2:
            print("You go west")
            return 12
        if instruct==3:
            if flooronekey==True:
                print("You enter the fitness center")
                return 11
            else:
                print("The door is locked")
                return "retry"
        if instruct==4:
            return item()
    if position==12:
        if instruct==1:
            print("You go north")
            return 10
        if instruct==2:
            print("You go south")
            return 0
        if instruct==3:
            if flooronekey==True:
                print("You enter Mr. McMenamin's room")
                return 15
            else:
                print("The door is locked")
                return "retry"
        if instruct==4:
            print("You enter Ms. Arnold's room")
            return 14
        if instruct==5:
            global window
            if stresslvl<5 or window==False:
                print("You look out the window at the empty parking lot. You resolve to get out of this school to avoid the embarassment you will face in the morning.")
                if stresslvl<5 and window==False:
                    stress(-1)
                window=True
            elif stresslvl<10:
                print("You look out the window at the empty parking lot. It has gotten too dark to see clearly, but you can't quite see all of the parking spaces. There seems to be a shadow\nbeing cast from just out of sight.")
                stress(1)
            elif stresslvl<15:
                print("You look out the window at the dark parking lot. It should be far too dark to see anything, but you can clearly see a black car in one of the spaces. When did that\nget here? You don't see a license plate.")
                stress(3)
            else:
                print("You look out the window at the dark walkway. Something hits the window hard. You jolt back, terrified. The window shudders a few more times, before stopping.")
                stress(5)
            return "retry"
        if instruct==6:
            return item()
    if position==8:
        if instruct==1:
            print("You leave the room")
            return 5
        if instruct==2:
            global nowboard
            if nowboard==False:
                print("You walk toward the board. Your vision begins to swim as you get closer.")
                boardchoice=input("Back away? Y/N: ")
                if boardchoice=="n" or boardchoice=="N":
                    print("You touch the board and immediately fall to the floor, in a daze.")
                    nowboard=True
                    dead(0)
                    return 100
                else:
                    print("You back away quickly from the board, and your vision clears. What was that?")
                    stress(1)
                    return "retry"
            else:
                print("You walk to the board and look at it. You see nothing but hilarious pictures and jokes.")
                return "retry"
        if instruct==3:
            global nowbook
            if nowbook==False:
                print("You look over the books, recognizing several of the titles, when your finger passes over a familiar name. Mr. Nowakoski wrote a book! You pick it up and feel a rush of knowledge.")
                nowbook=True
                inventory.append("The Holy Book of Mr. Nowakoski")
                return "retry"
            else:
                print("You look over the books remembering when you read some of them. None of the books look even remotely bad, of couse.")
                return "retry"
        if instruct==4:
            return item()
    if position==7:
        if instruct==1:
            print("You leave the room")
            return 5
        if instruct==2:
            print("You practice for a presentation")
            stress(0.5)
            present=random.randint(1,8)
            if present<=3:
                print("You have flashbacks to last month.")
                stress(2)
            elif present==4:
                print("You remember the taste of cultural food and sweet drinks.")
                stress(-6)
            elif present==8:
                print("A shadow appears at the desk. It laughs Italianly, and writes a zero on a piece of paper. You nearly faint.")
                stress(7)
            else:
                print("You hear distant laughter. Whether it is long ago or far away, you can't tell.")
                stress(3)
            return "retry"
        if instruct==3:
            return item()
        if instruct==4 and popquiz==False:
            print("You approach the papers. The shadows wrap around you as you do so, but you persevere and pick up the papers.")
            popquiz=True
            difficulty+=0.2
            inventory.append("Mr. Sanservino's Test")
            return "retry"
        else:
            print("For whatever reason, you are compelled to pick up some more papers. This seems like a pretty bad idea.")
            difficulty+=0.3
            stress(1)
            inventory.append("Miscellaneous Malign Papers")
            return "retry"
    if position==14:
        if instruct==1:
            print("You leave the room")
            return 12
        if instruct==2:
            if flooronekey==True:
                print("You open the door and enter Mrs. Pinto's office")
                return 99
            else:
                print("The door is locked")
                return "retry"
        if instruct==3:
            print("You look at the board. All of the writing seems to be in varying shades of red and brown.")
            if keyloc==3:
                print("You read 'She SellS SeaShellS on the firSt floor'")
            elif keyloc==1:
                print("You read 'Nora Nelly Needs Nice New Nuggets'")
            elif keyloc==2:
                print("You read 'EliE Eats Eggs with Elk chEEsE'")
            else:
                print("You read 'We Want Worse Weather With Wild Winds'")
            return "retry"
        if instruct==4:
            return item()
    if position==13:
        if instruct==1:
            print("You leave the makerspace")
            return 6
        if instruct==2:
            return item()
    if position==15:
        if instruct==1:
            print("You leave the classroom")
            return 12
        if instruct==2:
            chance=random.randint(1,20)
            if chance<19:
                print("You think back on the good old days, and relax a little.")
                stress(-0.3)
                return "retry"
            elif chance==19:
                print("You remember the war. Specifically the World War 1 game, in which your team bought 3 cavalry for $3000. You wince at the memory.")
                stress(3)
                return "retry"
            else:
                print("You remember the stress of the DBQ, which hurt even more when it didn't count for anything. Your mind hurts.")
                stress(5)
                return "retry"
        if instruct==3:
            return item()
        if instruct==4 and eraser==False:
            eraser=True
            inventory.append("Mr. McMenamin's Lucky Eraser")
            print("You pick up the eraser, and feel the luck of a billion billions in your hand.")
            return "retry"
        else:
            print("You already picked up the eraser")
            return "retry"
    if position==99:
        if instruct==1:
            print("You leave the office.")
            return 14
        if instruct==2:
            return item()
        if instruct==3:
            global crucible
            crucible=True
            inventory.append("The Crucible")
            print("You take 'The Crucible' and note the lack of italics in the book's title.")
            return "retry"
    if position==11:
        global workout
        if instruct==1:
            print("You leave the gym")
            return 10
        if instruct==2:
            return item()
        if instruct==3 and workout==0:
            print("You pump iron for several minutes, and thereby become 'swoll' as Mr. Stanko")
            inventory.append("Strength of Stanko")
            workout=1
            return "retry"
        elif instruct==3 and workout==1:
            print("You continue to work out, and eventually become as strong as Mrs. Lebrun")
            inventory.append("Legs of LeBrun")
            inventory.remove("Strength of Stanko")
            workout=2
            return "retry"
        elif instruct==3 and workout<100:
            print("You go around the machines, doing various exercises, in the hopes that you may one day become truly powerful.")
            workout+=1
            return "retry"
        elif instruct==3 and workout==100:
            print("All that training, all that dedication, has culminated in this one beautiful moment. You have become as strong as Mrs. Valley. You briefly ponder pulverizing a mountain.")
            inventory.append("Mrs. Valley's Raw Power")
            inventory.remove("Legs of LeBrun")
            stress(-2)
            workout+=1
            return "retry"
        elif instruct==3 and workout<200:
            print("You lift a few machines and the weight rack, but you don't feel much benefit.")
            workout+=1
            return "retry"
        else:
            print("For god's sake, you literally cannot be stronger than Mrs. Valley, no matter how many push-ups you do or buildings you lift. Just stop. Please. Do something better with your life.")
            return "retry"
    if position==17:
        if instruct==1:
            print("You go north")
            return 29
        if instruct==2:
            print("You go east")
            return 18
        if instruct==3:
            if floortwokey==True:
                print("You enter the senior lounge.")
                return 98
            else:
                print("The door is locked")
                return "retry"
    if position==18:
        if instruct==1:
            print("You go east")
            return 22
        if instruct==2:
            print("You go west")
            return 17
        if instruct==3:
            if floortwokey==True:
                print("You enter Mr. Liu's room")
                return 20
            else:
                print("THe door is locked")
                return "retry"
        if instruct==4:
            print("You enter Mr. Straut's room")
            return 19
        if instruct==5:
            if floortwokey==True:
                print("You enter Mrs. OConnor's room")
                return 21
            else:
                print("The door is locked")
                return "retry"
        if instruct==6:
            return item()
    if position==22:
        if instruct==1:
            print("You go north")
            return 27
        if instruct==2:
            print("You go south")
            return 18
        if instruct==3:
            if floortwokey==True and fangevent==True:
                print("You enter Dr. Fang's room")
                return 23
            elif fangevent==False:
                print("You put your hand on the handle")
                return 23
            else:
                print("The door is locked")
                return "retry"
        if instruct==4:
            print("You enter Dr. Jiderian's room")
            return 24
        if instruct==5:
            return item()
    if position==27:
        if instruct==1:
            print("You go east")
            return 22
        if instruct==2:
            print("You go west")
            return 29
        if instruct==3:
            print("You enter Senora Mejia's classroom")
            return 26
        if instruct==4:
            if floortwokey==True:
                print("You enter Mrs. Mansfield-Smith's Office")
                return 101
            else:
                print("The door is locked")
                return "retry"
        if instruct==5:
            return item()

    if position==29:
        if instruct==1:
            print("You go north")
            return 27
        if instruct==2:
            print("You go south")
            return 18
        if instruct==3:
            print("You enter Mr. Raite's room")
            return 32
        if instruct==4:
            if flooronekey==True:
                print("You enter Mrs. Kipp's room")
                return 31
            else:
                print("THe door is locked")
                return "retry"
        if instruct==5:
            if flooronekey==True:
                print("You enter Mr. Merkl's room")
                return 30
            else:
                print("The door is locked")
                return "retry"
        if instruct==6:
            return item()
    if position==21:
        if instruct==1:
            print("You leave the room")
            return 18
        if instruct==2:
            spinner=random.randint(1,10)
            for x in spinner:
                print("You spin in the chair")
                stress(-0.1)
            if spinner==9:
                print("You fall out of the chair, and hit your head. You get up, fairly dizzy, and quite disoriented.")
                stress(1)
            if spinner==10:
                print("You spin too fast and knock a computer on to the floor. It shatters, spraying shards of plastic and glass everywhere. Your legs are now bleeding, and you are going to have to pay some hefty fines.")
                stress(3)
                global difficulty
                difficulty+=0.2
            return "retry"
        if instruct==3:
            return item()
        if instruct==4:
            if terrycad==False:
                print("You pick up Mrs. OConnor's flash drive, wondering what designs she might have worked on while you were doing busywork.")
                inventory.append("Mrs. OConnor's flash drive")
                return "retry"
            else:
                print("You try to pick up the flash drive, but realize that it is already in your pocket. What an idiot!")
                return "retry"
    if position==20:
        if instruct==1:
            print("You leave the room")
            return 18
        if instruct==2:
            return item()
        if instruct==3:
            if table==False:
                if workout>=2:
                    print("You wrench the leg cover free from the table. You get Table, the Table Leg.")
                    inventory.append("Table, the Table Leg")
                    table=True
                    return "retry"
                else:
                    print("You try to remove the leg, but can't manage to wrench it free.")
                    return "retry"
            else:
                print("You see the broken table. You feel kind of badly to be honest.")
                stress(0.1)
                return "retry"
    if position==32:
        if instruct==1:
            print("You leave the room")
            return 29
        if instruct==2:
            if lockpick==True:
                print("You open the door, and enter the hazardous chemical storage.")
                return 33
            else:
                print("The door has a lock on it that doesn't match any key that you've seen so far.")
                return "retry"
        if instruct==3:
            return item()
        if instruct==4:
            if lighter==False:
                print("You take the lighter, and give it a few good twirls before putting it in your pocket. You slightly burn yourself in the process.")
                inventory.append("Lighter")
                stress(0.2)
                return "retry"
    if position==19:
        global papers
        global mathprobs
        if instruct==1:
            print("You leave the room.")
            return 18
        if instruct==2:
            ituse=eventitem()
            if ituse=="Lighter" and papers==False:
                print("You take out your lighter and touch it to Mr. Straut's papers, laughing maniacally as they go up in smoke. You feel much better")
                stress(-4)
            if ituse=="Mr. McMenamin's Lucky Eraser" and mathprobs==False:
                print("You wipe away the problems and homework clearly labeled 'DNE'. You feel satisfied.")
                stress(-2.5)
            else:
                print("You don't know how to use that right now")
            return "retry"


def startup():
    global difficulty
    global studentathlete
    print("Let's play a game")
    print("Are you a boy or a girl?\n1. Yes\n2. Dog-person\n3. Cat-person\n4. Lycanthrope-american")
    eventchoose(4)
    print("Hm. Interesting.")
    print("What kind of person are you? Be honest.\n1. Total Wuss\n2. Amateur\n3. Student Athlete\n4. The Creator Himself")
    answer=eventchoose(4)
    if answer==4:
        password=input("Oh, really? What's the magic number then? ")
        password=str(password)
        numbo=0
        for x in password:
            numbo=numbo+(int(x)+13745)**2
        numbo=numbo*8573146
        if numbo==9719740776207578:  #if you use this password, then shame on you. This is for me.
            for x in range(100):
                print()
            difficulty=float(input("Great to see you then, sir. Set the difficulty as you see fit: "))
            give=True
            stuath=input("Are you a student athlete sir? Y/N: ")
            if stuath=="y" or stuath=="Y":
                print("Of course you are sir.")
                global studentathlete
                studentathlete==True
            else:
                print("Probably for the best sir.")
            while give<13:
                print("Would you like some items sir?\n1. Searcher\n2. Floor one keys\n3. Rafalowski's ID\n4. Eraser\n5. Bruce's broom\n6. Holy Book\n7. Mr. Sanservino's Test\n8. The Crucible\n9. Magnet Man\n10. Strength of Stanko\n11. Legs of LeBrun\n12. Mrs. Valley's Raw Power\n13. All\n14. Nope")
                give=eventchoose(14)
                if give==1 or give==13:
                    inventory.append("Mrs. Gerstein's Searcher of Seeking")
                    global searcher
                    searcher=True
                if give==2 or give==13:
                    inventory.append("Floor one keys")
                    global flooronekey
                    flooronekey=True
                if give==3 or give==13:
                    inventory.append("Mr. Rafalowski's ID Card")
                if give==4 or give==13:
                    inventory.append("Mr. McMenamin's Lucky Eraser")
                if give==5 or give==13:
                    inventory.append("Bruce's broom")
                if give==6 or give==13:
                    inventory.append("The Holy Book of Mr. Nowakoski")
                if give==7 or give==13:
                    inventory.append("Mr. Sanservino's Test")
                if give==8 or give==13:
                    inventory.append("The Crucible")
                if give==9 or give==13:
                    inventory.append("The Magnet Man")
                if give==10 or give==13:
                    inventory.append("Strength of Stanko")
                if give==11 or give==13:
                    inventory.append("Legs of LeBrun")
                if give==12 or give==13:
                    inventory.append("Mrs. Valley's Raw Power")
                    global workout
                    workout=101
        else:
            print("Liars have no place in this game. You hadn't even gotten past your character creation, and now you're dead.")
            dead(2)
    elif answer==1:
        difficulty=0.15
        print("Hm. I see...wimp.")
    elif answer==2:
        difficulty=0.25
        print("Hm. I see.")
    elif answer==3:
        difficulty=0.4
        studentathlete=True
        jack=input("Hm. How do you have time to play this game then? ")
        print("I really don't care.")
    global name
    name=input("And what is your name? ")
    print(f"Well best of luck to you, {name}. You will need it.")
    print("There is a pretty good chance that you are laughing at the previous line, but I'll let it go.")
    whereAmI()

startup()





















