import random
import sys
import time
global burned
global poisoned
global pcrit
burned=False
poisoned=False
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
fangevent=False
yearbook=False
terrycad=False
kippcad=False
kippevent=False
table=False
lockpick=False
lighter=False
papers=False
mathprobs=False
mathevent=False
table=False
name="default"
password=0
hairspray=False
physbook=False
itemdic={1: "Mrs. Gerstein's Searcher of Seeking", 2: "Floor one keys",3: "Mr. Rafalowski's ID Card",4: "Mr. McMenamin's Lucky Eraser", 5: "Bruce's broom",6: "The Holy Book of Mr. Nowakoski",7: "Mr. Sanservino's Test",8: "The Crucible",9: "Magnet Man",10: "Strength of Stanko",11: "Legs of LeBrun",12: "Mrs. Valley's Raw Power",13: "Floor two keys",14: "Lighter",15: "Hair spray",16: "Table, the Table Leg",17: "Loaf of bread",18: "Slightly Smelly Fish (Trout?)",19: "Yearbook",20: "Mrs. OConnor's Flash Drive",21:"The Physics Textbook"}
itemlist=[position, window, rafid, sounds, patrys, stresslvl, broom, flooronekey, searcher, magnetman, nowboard, nowbook, popquiz, eraser, swordbots, vocabwords, crucible, difficulty, floortwokey, name, fangevent, yearbook, terrycad, kippcad, kippevent, table, lockpick, lighter, papers, mathprobs]
inventorysave=[]
def stress(change):
    global stresslvl
    stresslvl+=change
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
    global password
    password=str(int(password)+42)

def save():
    print("SAVING...DO NOT TURN OFF THE POWER")
    global itemlist
    global invsave
    global inventorysave
    itemlist=[position, window, rafid, sounds, patrys, stresslvl, broom, flooronekey, searcher, magnetman, nowboard, nowbook, popquiz, eraser, swordbots, vocabwords, crucible, difficulty, floortwokey, name, gymevent, workout, studentathlete, fangevent, yearbook, terrycad, kippcad, kippevent, table, lockpick, lighter, papers, mathprobs, floortwokey, hairspray, physbook]
    invsave=[]
    inventorysave=[]
    for x in itemlist:
        invsave.append(x)
    for y in inventory:
        inventorysave.append(y)


def load():
    global inventory, itemlist, invsave, inventorysave
    print("Loading...")
    global position, window, rafid, sounds, patrys, stresslvl, broom, flooronekey, searcher, magnetman, nowboard, nowbook, popquiz, eraser, swordbots, vocabwords, crucible, difficulty, floortwokey, name, gymevent, workout, studentathlete, fangevent, yearbook, terrycad, kippcad, kippevent, table, lockpick, lighter, papers, mathprobs, floortwokey, hairspray, physbook
    for it in itemlist:
        pos=itemlist.index(it)
        it=invsave[pos]
    inventory=inventorysave
    whereAmI()

def encounter():
    global position
    retry=True
    while retry==True:
        global position
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
                        prayer=random.randint(1,10)
                        if prayer==10:
                            print("By some miracle, q god actually seems to hear your prayer, and intervenes. As the jock raises his fists a pile of bread and fish falls on to him from out of thin air. After a few minutes of praising the gods of magnet, you take a loaf and a fish, as proof that miracles are real.")
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
        if position==24:
            global mathevent
            a=random.randint(2,10)
            b=random.randint(2,10)
            b=random.randint(2,10)
            c=random.randint(2,10)
            d=random.randint(2,10)
            e=random.randint(2,7)
            print("You enter the classroom, and immediately see a table in front of the door. There is a piece of paper with a single math problem on it. You could try to climb over the table, but that seems like a bad idea.")
            print("1. Climb over the desk\n2. Look at the problem")
            choice=eventchoose(2)
            if choice==1:
                print("You try to climb over the desk. Before you can, Dr. Jiderian materializes in front of you. 'SHOW YOUR WORK!' he yells, and throws a marker at you. It knocks you out cold, and the fall to the ground kills you.")
                dead(2)
            if choice==2:
                print(f"You read the problem. It says {a}*{b}+({c}*{d})^{e}. What is your answer? (Pencil and paper only, no calculator!)")
                answer=eventchoose(10000000000000000000000000000000000000000000000)
                rightans=(a*b)+((c*d)**e)
                if answer==rightans:
                    print("With a flurry of brilliance, you solve the 'calculus' problem. You feel very intelligent.")
                    mathevent=True
                    stress(-5)
                    save()
                else:
                    print("You put the wrong answer, and know it immediately after you write it. Dr. J appears in front of you, but instead of killing you, he just fails you and judo flips you. Instead of dying, you wake up outside of his door, with the ignominy of your failure still stinging.")
                    stress(5)
                    position=22
                    whereAmI()
        if position==31:
            global kippevent
            print("""You enter Mrs. Kipp's classroom,and immediately feel a chill run down your spine. A laser specter looms from the shadows and whispers "Swipe in...now..." """)
            stress(2)
            print("1. Explain yourself\n2. Run\n3. Item")
            choice=eventchoose(3)
            if choice==1:
                explanation=input("You take a deep breath and try to recall the magic words: ")
                if explanation=="XYZZY":
                    print("You use a cheat code, and destroy the laser specter in a torrent of magic. You feel powerful. Is this how the creator always feels?")
                    stress(-5)
                    kippevent=True
                else:
                    print("Those were not the magic words. Those were just regular words. Those don't work on specters, much less ones made of lasers. The laser specter takes the remnants of your soul.")
                    dead(2)
            if choice==2:
                print("You manage to outrun the laser specter, and shut the door behind you.")
                position=31
            if choice==3:
                ituse=eventitem()
                if ituse=="Mr. Rafalowski's ID Card":
                    print("You swipe Mr. Rafalowski's ID across the laser specter, which screams in anguish. Somewhere in the scream, you hear a faint beep. You are victorious.")
                    stress(-4)
                    kippevent=True
                else:
                    print("You really don't know how to use that against a laser specter. You die. Painfully. With lasers. And ghosts. You should have just swiped in.")
                    dead(2)
        if position==23:
            print("With your hand on the handle, you feel a presence just beyond it. This could be a difficult fight, and will require all your skill and ingenuity.\n1. Back away\n2. Press onward")
            choice=eventchoose(2)
            if choice==1:
                print("You back away. Wisely.")
                position=22
            if choice==2:
                print("""You enter the room\n\nYou see before you Mr. Capodice himself. Upon seeing you, he laughs. "You cannot possibly defeat me," he laughs. The door slams behind you, and from somewhere, POKeMON music starts to play.""")
                tho=input("Fight!")
                if bossbattle()==False:
                    position=22
                else:
                    global fangevent
                    fangevent=True
                    save()


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
    if room==24 and floortwokey==False:
        print("You see a set of keys on Dr. J's desk.")
    if room==19:
        if papers==False:
            print("You see a stack of flammable papers on the desk")
        if mathprobs==False:
            print("You see problems on the board, clearly labeled 'DNE'")
    if room==23 and physbook==False:
        print("You see, one textbook that seems to stand out from the rest.")

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
            print("You are in the western hallway of the first floor. The hallway continues to the north and south. You see Mr. McMenamin's and Ms. Arnold's rooms. There is a window in the eastern wall.\n1. Go north\n2. Go south\n3. Enter Mr. McMenamin's room\n4. Enter Ms. Arnold's room\n5. Look out the window\n6. Item")
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
            print("You stand outside the senior lounge. You see hallways leading to the north and to the east.\n1. Go north\n2. Go east\n3. Descend Stairs\n4. Enter senior lounge\n5. Item")
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
        if position==24:
            if mathevent==False:
                encounter()
            print("You are in Dr. Jiderian's room. You feel simultaneously stressed and relaxed. You hope that you don't find another GA.")
            things(24)
            print("1. Leave room\n2. Look for another GA\n3. Item")
            if floortwokey==False:
                print("4. Take keys")
                position=chose(4)
            else:
                position=chose(3)
        if position==31:
            if kippevent==False:
                encounter()
            print("You are in Mrs. Kipp's room. Rows of monitors blink to life as you look around. You wonder why ctrl+alt+delete is a command.\n1. Leave room\n2. Ctrl alt delete\n3. Ctrl+c\n4. Item")
            things(31)
            if kippcad==False:
                print("5. Take flash drive")
                position=chose(5)
            else:
                position=chose(4)
        if position==23:
            if fangevent==False:
                encounter()
            else:
                print("You stand in Dr. Fang's room. Mr. Capodice's unconscious (or possibly dead) body lies at the front of the room.")







def option (instruct):
    global difficulty, itemlist, position, rafid, searcher, popquiz, eraser, floortwokey, table, hairspray
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
        if instruct==5:
            return item()
        return "retry"
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
        if instruct==3:
            return item()
        else:
            print("You already picked that up")
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
        if instruct==4:
            print("You enter the auditorium.")
            return 4
        if instruct==5:
            return item()
        return "retry"
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
        else:
            print("You already picked up the broom")
        return "retry"
    if position==4:
        if instruct==1:
            print("You leave the auditorium")
            return 1
        elif instruct==2:
            print("You flip the switch. Nothing happens.")
        elif instruct==3:
            print ("You give a speech to the empty room. You hear nothing, but sense that something is listening to you.")
            stress(2)
        elif instruct==4:
            if flooronekey==True:
                print("You open the closet. You see only water bottles and stacks of paper.")
                if searcher==True and hairspray==False:
                    print("You use Mrs. Gerstein's searcher (of seeking) and find a can of hair spray. It seems mostly full.")
                    hairspray=True
                    inventory.append("Hair spray")
                    stress(-1)
                else:
                    print("You can't see anything important, so you close the closet")
            else:
                print("The door is locked")
        elif instruct==5:
            return item()
        return "retry"
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
        if instruct==4:
            if flooronekey==True:
                print("You enter Mr. Sanservino's room")
                return 7
            else:
                print("The door is locked")
        if instruct==5:
            print("You enter Mrs. Gerstein's room")
            return 6
        if instruct==6:
            return item()
        return "retry"
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
        if instruct==6:
            return item()
        return "retry"
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
            else:
                print("You walk to the board and look at it. You see nothing but hilarious pictures and jokes.")
        if instruct==3:
            global nowbook
            if nowbook==False:
                print("You look over the books, recognizing several of the titles, when your finger passes over a familiar name. Mr. Nowakoski wrote a book! You pick it up and feel a rush of knowledge.")
                nowbook=True
                inventory.append("The Holy Book of Mr. Nowakoski")
            else:
                print("You look over the books remembering when you read some of them. None of the books look even remotely bad, of couse.")
        if instruct==4:
            return item()
        return "retry"
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
        if instruct==3:
            return item()
        if instruct==4 and popquiz==False:
            print("You approach the papers. The shadows wrap around you as you do so, but you persevere and pick up the papers.")
            popquiz=True
            difficulty+=0.2
            inventory.append("Mr. Sanservino's Test")
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
        if instruct==4:
            return item()
        return "retry"
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
            elif chance==19:
                print("You remember the war. Specifically the World War 1 game, in which your team bought 3 cavalry for $3000. You wince at the memory.")
                stress(3)
            else:
                print("You remember the stress of the DBQ, which hurt even more when it didn't count for anything. Your mind hurts.")
                stress(5)
        if instruct==3:
            return item()
        if instruct==4 and eraser==False:
            eraser=True
            inventory.append("Mr. McMenamin's Lucky Eraser")
            print("You pick up the eraser, and feel the stuff of miracles in your hand.")
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
        elif instruct==3 and workout==1:
            print("You continue to work out, and eventually become as strong as Mrs. Lebrun")
            inventory.append("Legs of LeBrun")
            inventory.remove("Strength of Stanko")
            workout=2
        elif instruct==3 and workout<100:
            print("You go around the machines, doing various exercises, in the hopes that you may one day become truly powerful.")
            workout+=1
        elif instruct==3 and workout==100:
            print("All that training, all that dedication, has culminated in this one beautiful moment. You have become as strong as Mrs. Valley. You briefly ponder pulverizing a mountain.")
            inventory.append("Mrs. Valley's Raw Power")
            inventory.remove("Legs of LeBrun")
            stress(-2)
            workout+=1
        elif instruct==3 and workout<200:
            print("You lift a few machines and the weight rack, but you don't feel much benefit.")
            workout+=1
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
            print("You go down the stairs")
            return 0
        if instruct==4:
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
        if instruct==4:
            print("You enter Mr. Straut's room")
            return 19
        if instruct==5:
            if floortwokey==True:
                print("You enter Mrs. OConnor's room")
                return 21
            else:
                print("The door is locked")
        if instruct==6:
            return item()
        return "retry"
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
        if instruct==4:
            print("You enter Dr. Jiderian's room")
            return 24
        if instruct==5:
            return item()
        return "retry"
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
        if instruct==5:
            return item()
        return "retry"
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
            if floortwokey==True:
                print("You enter Mrs. Kipp's room")
                return 31
            else:
                print("The door is locked")
        if instruct==5:
            if flooronekey==True:
                print("You enter Mr. Merkl's room")
                return 30
            else:
                print("The door is locked")
        if instruct==6:
            return item()
        return "retry"
    if position==21:
        if instruct==1:
            print("You leave the room")
            return 18
        if instruct==2:
            spinner=random.randint(1,10)
            for x in range(0,spinner):
                print("You spin in the chair")
                stress(-0.1)
            if spinner==9:
                print("You fall out of the chair, and hit your head. You get up, fairly dizzy, and quite disoriented.")
                stress(1)
            if spinner==10:
                print("You spin too fast and knock a computer on to the floor. It shatters, spraying shards of plastic and glass everywhere. Your legs are now bleeding, and you are going to have to pay some hefty fines.")
                stress(3)
                difficulty+=0.2
        if instruct==3:
            return item()
        if instruct==4:
            if terrycad==False:
                print("You pick up Mrs. OConnor's flash drive, wondering what designs she might have worked on while you were doing busywork.")
                inventory.append("Mrs. OConnor's flash drive")
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
                else:
                    print("You try to remove the leg, but can't manage to wrench it free.")
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
                papers=True
            elif ituse=="Mr. McMenamin's Lucky Eraser" and mathprobs==False:
                print("You wipe away the problems and homework clearly labeled 'DNE'. You feel satisfied.")
                stress(-2.5)
                mathprobs=True
            else:
                print("You don't know how to use that right now")
        return "retry"
    if position==24:
        if instruct==1:
            print("You leave the room.")
            return 22
        if instruct==2:
            search=random.randint(1,3)
            if search==3:
                print("You find another GA.")
                a=random.randint(2,10)
                b=random.randint(2,10)
                b=random.randint(2,10)
                c=random.randint(2,10)
                d=random.randint(2,10)
                e=random.randint(2,7)
                print(f"You read the problem. It says {a}*{b}+({c}*{d})^{e}. What is your answer? (Pencil and paper only, no calculator!)")
                answer=eventchoose(10000000000000000000000000000000000000000000000)
                rightans=(a*b)+((c*d)**e)
                if answer==rightans:
                    print("You solve another problem, feeling satisfied. Unless you used a calculator, in which case you are an AHP violator.")
                    stress(-2)
                else:
                    print("You thought that you were prepared, but you were wrong. Dr. J's 'easy test' just killed your soul.")
                    stress(4)
            else:
                print("You find nothing, and are slightly relieved")
        if instruct==3:
            return item()
        if instruct==4:
            if floortwokey==False:
                print("You take the keys, wondering why Dr. J had them.")
                inventory.append("Floor two keys")
                floortwokey=True
            else:
                print("You try to take the keys, but realize that you already have them. You feel stupid.")
        return "retry"
    if position==26:
        if instruct==1:
            print("You leave the room")
            return 27
        if instruct==2:
            return item()
        if instruct==3:
            global yearbook
            if yearbook==False:
                print("You take the yearbook")
                inventory.append("Yearbook")
                yearbook=True
            else:
                print("You try to take another yearbook, but your conscience stops you.")
        return "retry"
    if position==31:
        if instruct==1:
            print("You leave the room")
            return 29
        if instruct==2:
            print("You press ctrl, alt, and delete on one of the computers. Nothing happens. You contemplate pressing them at the same time, but decide against it")
        if instruct==3:
            yn=input("...you do know what ctrl+c does, right? It's not 'copy' in the context of python. Are you sure? Y/N: ")
            if yn=="y" or "Y":
                yn=input("You should definitely look up what that command does in python before doing it, because it's pretty common knowledge. Are you sure you're sure? Y/N: ")
                if yn=="y" or "Y":
                    print("Well if you say so")
                    exit()
            if yn!="y" or "Y":
                print("That's the right choice")
        return "retry"
    if position==23:
        pass





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
        global password
        password=input("Oh, really? What's the magic number then? ")
        try:
            int(password)
        except ValueError:
            print("That's not the magic number. That's not even a number. You aren't solving this with a mind like that.")
            dead(2)
        password=int(password)
        numb=0
        numbo=3
        numbos=password
        global numbon
        numbon=0
        ranger_rick=password**0.4
        ranger_rick=int(round(ranger_rick,0))
        password=str(password)
        if numbon>=1:
            quit()
        numbon+=1
        for break_this in range(0,ranger_rick):
            password=str(int(password)-42)
            if numbon<1:
                exit()
            numb=int(numb)
            numbo=int(numbo)
            stress(0.5)
            for x in password:
                numb=((int(x)+87)*(int(x)-94))**((int(x)+5)**3)
            if numb<0:
                numb=-numb
            numb=str(numb)
            for y in numb:
                numbo+=int(password)**2+(int(y)+1)**4
            numbo=str(numbo)
            for z in numbo:
                numbos*=(int(z)+int(password))**2
            stress(-0.5)
            password=str(int(password)-42)
        if numbos==133913151502626336183088446999206024774305557443382677357415561148792266425305710134211432673444656435441655751384220364525154532523876134105510523144703101160132721487776112642158663622061954147464428321511189405321149379629009361340742971022602761825097477626524272903566145920349000041223676324121470044839099731330039273198311834819276927366125563222052683832292873332813645869072554394072381509460213476336202818476375040740037462601564624995038157200659444574672135543143518531027914473735732049036894590960502068934136904804038776841256146071517228119961693182272763652049986750811443973737042788218200059265492336612798355175929797640857476425165819851572410181057163999361929147649820884649383708741894804240190204720728172373632496280150691064980493598448500436241271884783040672832387531198281384842741510350396028595354864694500260647767203585647744959572424771827032496865842586006414956492010436058620405682736957013752687834619598549859187808329654813808412719568353307308485997989037155512569309828326726881699733782702938340583374116110922732645183954071269211160778729739712814522497500232904528780619667760495850960755318716984195402564525850722093474405754415664765879516040383348404236322128555987294169188820107820547911472984747453194477657657205529363080582299986857414425272184140607235492056820078222838564882105170139151868117985835057772255661963834632582172699486495567927174209779858202907886941670941232260068711898987387883087735772024134709800846178248145402305685512638600048002086808937397478609986148817369347099321635844061435051649134668222949412582143409326893966480389500563703249403542366933926781162836322669604687940450625913083632710040889119917196862183036812155443531260293206996876038685858571043779319087942517430246400717873429014578965228911466003364467545153779595847440311271807026072098420882636564775158740986013487244589506491392721146116796034719407711921205558089171582982982489292145405477210309400472120662793454977992128546351642998931628447562230377166861062776912749380765617727415043191683436168425234872198780373107715768346902357342148463236373439759649892476205574975587582735570304752727427941578681887522195883177390974775959449270576308326361087400549642796335239355722491134361026936412625051971368106455772931085408979372372919890462485224727149307873386715024790256076254806302524836584206079154813914140202080665686873081538780440452142979216134120794823640672170218921470948099089995069845176124392705642598690541041923813547834463114381436459196673742498435863563956952031727167834134391939387331420961141209882271910707010772445737507537044954343458142991410037530243571370202316869990391499906824561599873132980994758503196792714557335239399409627616277286633037052239557735898515224057927710214894986495040917761996894697391567138933268343558504039887750633714351548660918302518032568875877958830426369578247009762790459132288647208809827720069061413632882883304850319598314871311525766259903340485321475034362138938054226729953664363073623312295569963577418244860221084866997227006380686031893378776342997378117493596825007154936867020751972178431897504564447985954508515757879376487956977058633091162193917310917088380428743734768028769026395310728473041686049926572801556984140008373528444836692434683795436754334730656584456601926704016958858455140939528454887415087549248761680661528852351304046526710648635625713765754775702287339930226844574124224524685717071499842826577660395585617141994013696385693696824474306895260566481879235874634120826438161636970740406246483269632967187004685801027209638124288169188310291784823322914880593104060730847882402816151437063688304400696558867681980200119515293719090366575508295774499115709345204541244218303122253427486024788534595488410086958565653763111610756434744630479741667869797978329820186616888556115508908776754748808801671298338565900894866857345125574652947116364580690809035729649287242331751505923546530150328933561945205071735837597543358325093527990431910933009049817676516125661131348117868928691625081390135323059688767411827502621105841335604674161167940118634963360620403344244994990467559307511095629120784630374337213110508036950032374484882914027027589111569325445154992791452961130311024144885789500134783737974353294904610039128449672932159771529682373438294301773782463502654167297193868363114852070193683021927178518548511324535756042724954855009825720463142253780781708593732900407663779518928001482232210661853200467543481119114233874340404108348961458584130191749478323207731636039059334653621845826407282568064010692416892401948256205458357708564584530478328422601324831092888438934986750311656126763244725230276751349232652927402068698178753166247372028764099652714548894450370691444321177080226061051142146888855338944795639066378580576100040857822563170039513824784106558905153487014197226569418909323669790038030123244764046423311032339352327445490944121223551043446650700692051017180042118448901674912726822210031675474545859503083536865947090304858818732097800261545865111234249275980296245588310846278056609877140259664104637736099966450671314362739570424992975871030876020282357196462643972994606533658475873273402432116690616188922396855665480460942054183181702718056968667093751239428739472373119670694809252781961781735402195794654659114837461296913000225192375537808486878608031727353204935756428165189168025265133952526190160569817638761393032775635258322769248807205359901036212419063630139226550472790512349797446426877768955819540337950283647786492080218803949825714339247928025290637954885689954237252784243286333885598592973945140163155552069922159282219387247339915452853120475927598160340647633350666887051796403824686505821372128529842023777142870672573029116749186687712502010103667340749396363055446780168797233499190986932465877689494131499681294166903353776021100533626420242218342747105009876030154326723448604612355344014568663296508949436201379963123017360420516088057949197530986060298023333177435807947635212300148008692893294061190366912473971122566697936349860749711877990530189438604563750057878934321995172271416361984515005948683431059184001383947449062584618862903208252068647227466111588081520963658805023726991844859694748859411604264764497228499754014308641564624086542835694712513812202406724338823411284811196578119038935185695522709517302301072172011185712889486370801924347269488922588671323065184704813782440929771421934211475632184045133542134752254153905853452269135435283333560847341764993484692117263166952983379910812218109550577719051020109866324238252255225585075361969407269574374124283326586107683101972818346345547212093357863501894635107330621482303487710622062514931050312619005947604645230986293793165976178033959330316436064648232032295947476413724865912406976334031860923470129228570449541680977150671370719857874291060077805029805824515189689495803389023226239931309624580775355613585191791045405617634263596357742356451829986242841902953923914257905803310290865689861588125913522187490813174232716741521764345770618247577732335315530430279540944320023143225479057902301054997166577729299626713574422175554180166434857462330511963514912875989500542793469328300205808934782173158826933783838079755876498188619802264510207802575704485456586211354131212819778549329655391543024753839286444746473366917829283913851626477759266468700715188915640250898753468901669208755620481415300090467364398451280323523785307444362016169696405767801733900478399264210094964856444563504716572553532934351830307127733842289731835001117863342864958782113324899966388357524066834903610312304952525130696286403630418812695987833583972020193898086009579741491256183688131421986326080078529105183536210207146490070647416784186581640027141399441745179521582978544876077688110358626116005671296462695634670135926911700534369993961564049309966092626070778476646693312256900175002284388037747513023120183754628098263604471123231139157569963245219921900971589389761869888651323696180091635017277628909915240936626366330015537182856945620100674777317343963495008078671790579233601494288138767380569019941176726126178505491976353006545823123784432033936096553267759227104166135639569837099554712077892007812506011482334620220968404323403671288675041409390047115978784673706310906566168589563614647101543862093561386906340088932609109804137830195903841389970406157399812424261837412997468806652280760258071098023377155831430831062965784063555970590792485745421348897170346371316420332954790335843149309819257145318716644150948884182946507835853746640116358298858273305713160137009892088288202531056379714318878351742017186161245938787457236207535561855005620466451594896415180588332089989748249703534707387359873898234475818036160242250362694892902134145958526045601127418497925867554418632141460167468511904862241156741719697778997653435083565882520963447347555137617233957943509116846426230286901216136274394934171094170075127957561312276169886125300202851253230133916525542881050207689050588381861640110403689592350225672716952005449636260303783794197944533534330649811702163525494605231667780840749525738600182529343179755446052295271738240836401646323746734765055651206678814471105056413154673437450780666593258124296383860272136822618821929918380273715056854588273071672328161113657061731912959082204259090186984471201886199885519752369093966742021486498684985621601665881072858942239491290452365820513759818182237255325852210174355110416652378060261467667888169028919665659854625122522644938009870530756207128055696106358141018223429680460853385463654249255879881718217889029143099215709538418249976012229362204698792631880927203556867298648101744135168249550840046727148196228012413635360046340471336555383281262482691152960067483796455290607522735175958751154709258516894668367337361582583938837445119177281635266179114515438256878532510102115077042919478548625964630572354891670116732607303682981849116167214937197275690718319089001520011765788458582821126164065657028669185829061367122590300377837293571984976937320934352357633991860494214209803183886113245747438583716198671751861865271666481364852685224260875733503118786511768701340625458664758106231809037135696173528989636861874492682233290710802286849889715151163071331913838644350455303159219735755127239346513531860585719219129041997532918021557677389026275205433769482689805991033709391167674894127401558534508919773855967270618866706032131564219385822803656644887845704306344403575031396222954690093436977272398751729571732453596869193168823075793950210956828355028295390375428056281072499086460009317096822665067251741960479587913258846325170660952697628289665618455257527795872801453550748748902172969600705134215353311603413272599214335683355968672144273509049453348496964291596787381821256717699744115107100758945951637785934971152603866634781119083349069335993697713318805023145882478890201873514084805690465979538878178487643202651069705183653563377228357915844179013869123874619254138042799470526323357322120740273410752613026760008112313455593037883122660862447319575328167587221210799192241604897061089556278918231084464953796155313486109984591309657110455656600972912481710738797522259873140603573117168457311828061133060988283605011860019938164898373589984243633950438750003623498952301880041260542777188817575037011837894344449357120732477900991353470981112978979015642871470713420600997897140606290247184965881480193898669806956552842118571786306768224313814269163957734204444283534416977503216421473322507507361807553445954216206545543201182260554158799136968726256502506183238716433057594358097999517661105815182051309304711876730241266776260304712655910305739522493883868802256010821419984437935488294285579189669199949724496584992720640999123242386632886260359760015650985590945128424567684800510436576259948576206845891700147837380246596170454802594721327610712871776681836176948008491494386258585136653133475123762038274651733049630018986688255719613841608852509365692951453346989871443342762197600107571570521045268711445227358482739062279527742756317944871378359124226922674559514614476007892268691526060043676617472488924523381755587636961130343359031476308668395704525422909620434125653466519783512233797173019081313249015624641457095554617923321475194108359877553967637159761803062725783418127048651705524077401797449607608856438654754049294379628222123656679552606778098852990190058162236302435004569724761933538298795910452867491074246687316468507233562475817780377501626842553709706708034785577417292530182283373922847973388761811045687385982972343799561894893954754969499425499996622751051863810704801309191356943481472398202799356971233367008181061158790742757263874774416502864256403192755737774987085756919791965872982911263131977935646795410541897890083999563917643935679360598805189392012603088375375778156029468479118247918244795673326759478862676152405480471479173816914694578677327608149513797511753310273126186568275293738678125372909384396939576029643149104587427951120657840875647896059560637137224993013319973130246179791308352050113821160518641530680367840678383315428661274591675370965708396070045150039229776775059914461048927966634489026960158620811774102902342930054045637974006408714906293314621210835652936303492213089811120318199879436355960469516282910447732968518258336785413652333400843326090828226895840877146007408396257422122504057776878252120186771952321602934110356895189902705147845375303503274416255037382577012088879079946702500084853430852028524375107905905924979615571248695388157433304009449716552010466141272613876980411878775351556245174094749240705391690965305391167729382426050496951259142447553804088366775405637286631595588876715844795506092401321861753766735209087847379687847715936414410514126609182309366207857773798832106660374530709493357115156810852005923104605839866043015238475935479079673659400997179666757484202607656300674537797297364368682525708389029694269969348089307734768224822633450487379269546537677623588036406572721774536759802005982576037656735159518501815363031355025459757653054084966924829674689016140741217325003442734982735476594562596083026201727704658017236480595886890184406518325506981626403542988342021174430244016160317508678038629163151623497991773833959434448518809368796686519893568917248455532900912550000939368493150817612923819011518171645666645150469853071229736551308675389205170186962151584470559798308265544133865501824605372702337257412869949071252449531226491401565155205113184476452907439946058345925342296664013397024055355147143016400430621232476646556715705246567247064969516035456255170707526933160735841484952206473705085359893092138085936847670958102300978122093110110417843042830958751185096572218256411157531418389072283643926707794126701983549738829489353819485479834304412768753066338206034280840961867328106002938179404352018060743450701527435307437279276302266181845557070549345213953809834798422555827031927040537209934925924970248872138162095995072571212348281560865460931933591293480587852220520057942058466131740067094678784842014973559927260427822132805746090809688526518945259944666079829818831735188937317552996535818809582402585481560849916280376834569505437202947120958383221218255267699359044915259985622671782380790664362804987651389614936357896366451637144072405679071835484574536412723316275997011084878515364627436871494292614551031738026983439734711040513763141497330049964384999029590562727503324051227961112096558478760751736506064870015037675647406361399219522457246417745564033241558199616873156525307482296862186875081904936566789753118812573213676113214986316856485493327000672628366562467958825541138012890991952287570689134217856871925298814270733743006616295614163844726674421167095149683299205720607808333869973801505097357062470091628378393996347714828557221524087506882134553193571665490517222953643689305810487904565496093474711310449655719059749910651581328788668543003677437084487167133563358781506374877205855553526697745657562682227962795096316693105612072742036006117412759954487120300564854838123546000402703606947143278305554507054939983515401422289287451390135310836951464102542349684860514179192403351997756419329848887604153197926964762931388103979926871545218193760644486609390601341435778343751003872575671090777348105240762655953150063004298796975448435844066317935420037642015907920931873945183552936287512907801197264244422761706616466055097464898557380551734165560841107328099103539200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:  #if you use this password, then shame on you. This is for me.
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
            while give!=1000 and give!=100:
                print("Would you like some items sir?\n1. Searcher\n2. Floor one keys\n3. Rafalowski's ID\n4. Eraser\n5. Bruce's broom\n6. Holy Book\n7. Mr. Sanservino's Test\n8. The Crucible\n9. Magnet Man\n10. Strength of Stanko\n11. Legs of LeBrun\n12. Mrs. Valley's Raw Power\n13. Floor two keys\n14. Lighter\n15. Hair spray\n16. Table, the Table Leg\n17. Loaf of bread\n18. Smelly fish (yummy fish)\n19. Yearbook\n20. Mrs. OConnor's Flash Drive\n100. All\n1000. Nope")
                give=eventchoose(1000)
                global workout
                if give!=100 and give!=1000:
                    inventory.append(itemdic[give])
                    if give==10:
                        workout=1
                    elif give==11:
                        workout=2
                    elif give==12:
                        workout=101
                elif give==100:
                    for x in itemdic:
                        inventory.append(itemdic[x])
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



def textbox(text):
    leng=len(text)
    brek=0
    sys.stdout.write("_____________________________________\n|")
    for x in text:
        sys.stdout.write(x)
        brek+=1
        if brek==35:
            sys.stdout.write("|\n|")
    if leng<=35:
        left=35-leng
    if leng>35:
        left=70-leng
    for y in range(left):
        sys.stdout.write(" ")
    if leng<=35:
        sys.stdout.write("|\n|                                   ")
    sys.stdout.write("|\n|___________________________________|")
    nex=input()
def fbr():
    print("""
_____________________________________
|    1. Fight          2. Bag       |
|       POKeMON        3. Run       |
|___________________________________|""")
    return eventchoose(3)

def fight():
    global shortname, bhealth, burn, poison, burned, poisoned, first, pcrit
    burn=False
    poison=False
    roll=random.randint(1,10)
    crit=0
    miss=1
    if roll>=pcrit:
        crit=2
    if roll<=2:
        miss=0
    option=1
    sys.stdout.write("""
_____________________________________
|    """)
    if itemdic[12] in inventory:
        sys.stdout.write("1. Close Combat   ")
        one="Close Combat"
    elif itemdic[11] in inventory:
        sys.stdout.write("1. Hi-jump Kick   ")
        one="High Jump Kick"
    elif itemdic[10] in inventory:
        sys.stdout.write("1. Jab            ")
        one="Jab"
    else:
        sys.stdout.write("1. Punch            ")
        one="Punch"
    option+=1
    if itemdic[16] in inventory:
        print(f"{option}. Rock Smash|")
        two="Rock Smash"
    elif itemdic[5] in inventory:
        print(f"{option}. Leg Sweep |")
        two="Leg Sweep"
    else:
        print(" ?????     |")
        two=0
        option-=1
    option+=1
    sys.stdout.write("|    ")
    if itemdic[14] in inventory and itemdic[5] in inventory:
        sys.stdout.write(f"{option}. Flamethrower   ")
        three="Flamethrower"
        burn=True
    elif itemdic[14] in inventory:
        sys.stdout.write(f"{option}. Ember          ")
        three="Ember"
    else:
        sys.stdout.write("   ?????          ")
        three=0
        option-=1
    option+=1
    if "Chemicals" in inventory:
        sys.stdout.write(f"{option}. Toxic     |")
        four="Toxic"
    else:
        sys.stdout.write("   ?????     |")
        four=0
    print("""
|___________________________________|""")
    zero=1
    moves=[zero,one,two,three,four]
    for x in moves:
        if x==0:
            moves.remove(0)
    if option==1:
        choice=input()
        return 0
    elif option==2:
        move=moves[eventchoose(1)]
    elif option==3:
        move=moves[eventchoose(2)]
    elif option==4:
        move=moves[eventchoose(3)]
    elif option==5:
        move=moves[eventchoose(4)]
    if move=="Close Combat":
            dam=(5+crit)*miss
    if move=="High Jump Kick":
            dam=(3+crit)*miss
    if move=="Jab":
            dam=(2+crit)*miss
    if move=="Punch":
            dam=(1+crit)*miss
    if move=="Rock Smash":
            dam=(4+crit)*miss
    if move=="Leg Sweep":
            dam=(2+crit)*miss
    if move=="Flamethrower":
            dam=(3+crit)*miss
            burn=True
    if move=="Ember":
            dam=(1+crit)*miss
            if roll>6:
                burn=True
    if move=="Toxic":
            dam=(3+crit)*miss
            poison=True
    textbox(f"{shortname} used {move}")
    if crit!=0:
        textbox("A critical hit!")
    if miss!=1:
        textbox(f"{shortname}'s attack missed")
        burn=False
        poison=False
    if miss==1:
        bdam(dam)
    if bhealth<=0:
        pass
    elif burn==True and burned==False:
        textbox("Mr. Capodice was burned")
        burned=True
    elif poison==True and poisoned==False:
        textbox("Mr. Capodice was poisoned")
        poisoned=True

def burne():
    global burn, burned, bhealth
    roll=random.randint(1,10)
    if burned==True:
        if roll>3 or burn==True:
            textbox("Mr. Capodice is still burning")
            textbox("Mr. Capodice took 1 damage from his burn")
            bhealth-=1
        else:
            textbox("Mr. Capodice is no longer burning")
            burned=False
    burn=False

def poissone():
    global poison,poisoned, bhealth
    roll=random.randint(1,10)
    if poisoned==True:
        if roll>3 or poison==True:
            textbox("Mr. Capodice is still poisoned")
            textbox("Mr. Capodice took 1 damage from his poison")
            bhealth-=1
        else:
            textbox("Mr. Capodice is no longer poisoned")
            poisoned=False
    poison=False

def bagitem(ba):
    print("""
            __
         _,/__\,_
        / |    | \ \n       / /  __  \ \ \n       | | /__\  | |
       | | \__/  | |
       | |       | |
       \_\_______/_/""")

    number=0
    for x in ba:
        number+=1
        number=str(number)
        print (number+". "+str(x))
        number=int(number)
    print(f"{number+1}. Cancel")
    while True:
        use=input("What do you use? ")
        try:
            int(use)
        except ValueError:
            textbox("Invalid command. Try again: ")
            use=input()
        use=int(use)
        if use<=number and use>=1:
            return ba[use-1]
        elif use==number+1:
            return False
        else:
            print("You don't have that.")
def pdam(dam):
    global phealth
    if dam<0:
        textbox(f"{shortname} healed {dam} damage")
    else:
        textbox(f"{shortname} took {dam} damage")
    phealth-=dam
def bdam(dam):
    global bhealth
    if dam<0:
        textbox(f"Mr. Capodice healed {dam} damage")
    else:
        textbox(f"Mr. Capodice took {dam} damage")
    bhealth-=dam
def bag():
    global tempbag, pcrit, shortname, bhealth, phealth
    if phealth>=15:
        phealth=15
    if bhealth>=15:
        bhealth=15
    roll=random.randint(0,10)
    deletelist=["Strength of Stanko", "Legs of LeBrun", "Miscellaneous Malign Papers", "Mrs. Valley's Raw Power", "Lighter", "Hair spray", "Floor one keys", "Floor two keys", "Bruce's broom", "Mrs. OConnor's flash drive", "Table, the Table Leg"]
    for ite in deletelist:
        if ite in tempbag:
            tempbag.remove(ite)
    ituse=bagitem(tempbag)
    if ituse==False:
        return False
    tempbag.remove(ituse)
    if ituse=="Loaf of Bread":
        textbox("Used Loaf of Bread")
        phealth+=6
    if ituse=="Slightly Smelly Fish (Trout?)":
        textbox("Ate smelly fish")
        phealth+=6
    if ituse=="Mr. Rafalowski's ID Card":
        textbox(f"{shortname} ninja threw the ID card")
        if roll>=pcrit:
            textbox("The card flies true and hits Mr. Capodice in the eye")
            textbox("A critical hit!")
            bhealth-=4
        elif roll>=3:
            bhealth-=2
        else:
            textbox(f"{shortname}'s attack missed!")
    if ituse=="Mrs. Gerstein's Searcher of Seeking":
        textbox("Used searcher")
        textbox("Weak point located")
        textbox(f"{shortname}'s critical chance increased")
        pcrit-=1
    if ituse=="The Holy Book of Mr. Nowakoski":
        textbox("Used holy book")
        if roll>=pcrit+1:
            textbox("A critical hit!")
            bhealth-=6
        else:
            bhealth-=2
    if ituse=="Mr. Sanservino's Test":
        textbox("Used evil test")
        if roll>14-pcrit:
            textbox("The test lashes out at Mr. Capodice")
            bhealth-=4
        else:
            textbox(f"The test lashes out at {shortname}")
            phealth-=4
    if ituse=="Mr. McMenamin's Lucky Eraser":
        textbox("Used lucky eraser")
        textbox(f"{shortname}'s critical chance sharply increased")
        pcrit-=2
    if ituse=="The Crucible":
        textbox("Used the crucible")
        textbox("More weight was added to Mr. Capodice")
        textbox("The devil gives you precision")
        textbox("Reverend Hale gives your soul peace")
        bhealth-=2
        pcrit-=1
        phealth+=1
    if ituse=="Yearbook":
        textbox(f"{shortname} reminisces about the good times")
        phealth+=4

def isdead():
    global phealth, bhealth
    if phealth<=0:
        money=random.randint(1,100)
        textbox(f"{shortname} has no more health left")
        textbox(f"{shortname} paid out ${money} to Mr. Capodice")
        textbox(f"{shortname} fainted")
        dead(2)
    elif bhealth<=0:
        print (bhealth)
        textbox("Mr. Capodice fainted")
        return True
    return False






def bossbattle():
    global tempbag, phealth, bhealth, pcrit, position, bdif
    bdif=0
    pcrit=10
    tempbag=[]
    for ite in inventory:
        tempbag.append(ite)
    phealth=15
    bhealth=15
    bossart()
    ok=True
    textbox("CHAMPION Capodice challenges you toa battle")
    while True:
        roll=random.randint(1,3)
        choice=fbr()
        if choice==1:
            fight()
        if choice==2:
            if bag()==False:
                ok=False
        if choice==3:
            highroll=random.randint(1,10)
            if highroll>8:
                textbox("Got away safely")
                position==22
                return False
            else:
                textbox("Can't escape!")
        if isdead()==True:
            textbox(f"{shortname} is victorious!")
            return True
        if ok!=False:
            bossmove()
            print(bhealth)
            poissone()
            burne()
            if isdead()==True:
                textbox(f"{shortname} is victorious!")
                return True
            if roll==3:
                bdif+=1
        bossart()

def bossmove():
    global invsave, bdif, phealth, bhealth
    roll=random.randint(1+bdif,10)
    hit=random.randint(1,10)+bdif
    if roll==10 and invsave!=[0]:
        textbox("Mr. Capodice used Delete Save")
        textbox("Your save files have been deleted!")
        invsave=[0]
    elif roll>=8:
        textbox("Mr. Capodice used Body Slam")
        if hit>=1:
            pdam(4+bdif)
            textbox("Mr. Capodice is hit by the recoil")
            bdam(1)
        else:
            textbox("Mr. Capodice's attack missed!")
    elif roll>=4:
        textbox("Mr. Capodice used Earthquake")
        if hit>=3:
            textbox(f"Magnitude {(roll-2)*2}!")
            pdam(roll-3+bdif)
    else:
        textbox("Mr. Capodice used Tackle")
        pdam(2+bdif)


def bossart():
    global shortname, phealth, bhealth
    shortname=""
    cha=1
    for c in name:
        if cha<=10:
            shortname+=str(c)
        cha+=1
    blanks=10-len(shortname)
    for b in range(blanks):
        shortname+=" "

    print("""
  _____________________
 | MR. CAPODICE   Lv100|""")
    sys.stdout.write(" |   HP ")
    pblank=15-phealth
    bblank=15-bhealth
    for x in range(bhealth):
        sys.stdout.write("|")
    for y in range(bblank):
        sys.stdout.write(" ")
    sys.stdout.write("""|
 |_____________________|                             ____
                                                    /.  .\ \n                                                    \ mm /
                                                  ---    ---
                                                | |   ||   | |
                                                | |   ||   | |
                                                | |   ||   | |
                                                \ |   \/   | /
                                               , -|--------| - ,
                                           , '    |   /\   |     ' ,
                                         ,        |  /  \  |         ,
                                        ,         | |    | |          ,
               ,_----                  ,         _| |    | |_          ,
            ----------|__,             ,        |___|    |___|         ,
         ------------/|                ,                               ,
       ,------------,,,~ ,             ,                               ,
     ,   ,,,,,,,,,,,,,    ,             ',                           ,'
   ,     ,,,,,,,,,,,,,     ,               ,                       ,
  ,      ,,,,,,,,,,,,        ,               '- , _ _ _ _ _ _ , -'
 ,    ---           ---       ,
 ,   |IWANNABETHEVERYBE|      ,
 ,   |STLIKENOONEEVERWA|     ,              ______________________
  ,  |STOCATCHTHEMISMYR|    ,              | """)
    print(f"{shortname}       Lv1 |")
    sys.stdout.write("""   , |EALTESTTOTRAINTHE|   ,               |    HP """)
    for x in range(phealth):
        sys.stdout.write("|")
    for y in range(pblank):
        sys.stdout.write(" ")
    print("""|
     ,MISMYCAUSEPOKEMON! '                 |______________________|
       ' - , _ _ _ ,  '""")
startup()


