from random import randint

class Scene(object) :

    def __init__ (self):
        pass

    def enter(self) :
        print("This scene is not yet configured, Subclass it and implement enter().")

class Finish(Scene) :
    def enter(self):
        print("Good job\n")
        exit(1)

class Death(Scene) :

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    def enter(self) :
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene) :

    def enter(self) :

        print("The gothons of plant percal #25 have invaded your ship and destroyed")
        print("youe wntire crew. you are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons armory,")
        print("put it in the bridge, and blow the ship up after getting into an")
        print("escpae pod. \n")
        print("You're running down the central corridor to the weapons armory when")
        print("a Gothon jumps out, red scaly skinm dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. he's blokcing the door to the")
        print("armory and about to pull a weapon to blast you")

        action = input("> ")

        if action == "shoot!" :

            print("""Quick on the draw you yank out your plaster and fire it at the Gothon.
            His clown costume is flowing and moving around his body, which throws
            off your aim. your laster hiys his costume but misses him entirely. this
            completely ruins his brad new costume his mother bought him, which
            makes him fly into a rage and blast you repeatedly in the face until
            you are dead. the he eats you.""")

            return 'death'

        elif action == "dodge!" :

            print("""Like a world calss boxer you dodge, weave, slip and slide right
            as the Gothon's blaster cranks a laser past youe head.
            In the middle of your artful dodge your foot slips and you
            bang your head in the metal wall and pass out.
            You wake up shortly after only to die as the Gothon stomps on
            your head and eats you.""")

            return 'death'

        elif action == "tell a joke" :

            print("""Lucky for you they made you learn gothon insults in the academy.
            You tell the one gothon joke you know:
            lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr , fur fvgf nebhaq gur ubhfr.
            The Gothon stops, trues not to laughm then busts out laughing and can't move.
            While he's laughing you run up and shoot him square in the head
            putting him downm then jump through the weapon armory door.""")

            return 'laser_weapon_armory'

        else :

            print("Does NOT COMPUTE!")

            return('central_corridor')

class LaserWeaponArmory(Scene) :

    def enter(self) :

        print("""You do a dive roll into the weapon Armory, crouch a nd scan the room
        for more Gothons that might be hiding. it's dead quiet, too quiet.
        You stand up and run to the far side of the room and find the
        neurton bomb in its container. there's a keypad lock on the box
        and you need the code to get the bomb out.if you get the code
        wrong 10 times the lock closes forever and you can't
        get the bomb.   the code is 3 digits.""")

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        if guess == "habra kadabra" : # cheat code ;)
            return "escape_pod"

        while guess != code and guesses < 9 :

            print("BZZZZZZEDD!")
            guesses += 1
            guess = input("[keypad> ]")

        if guess == code :

            print("""The cordinator clicks open and the seal breaks, letting gas out.
            You grab the neutron bomb and run as fast as you can to the
            bridge where you must place it in the right spot.""")

            return 'the_bridge'

        else:

            print("""The lock buzzes one last time and then you hear a sickening
            melting sound as the mechanism is fused together.
            Yopu decide to sit there, and finally the Gothons blow up the
            ship from their ship and you die. """)

            return 'death'

class TheBridge(Scene) :

    def enter(Self) :

        print("""You must burst onto the bridge with the neutron destruct bomb
        inder your arm and surprise 5 Gothns who are trying to
        take control of the ship.   Each of them has an even uglier
        clown costume that the last. They haven't pulled their
        weapons out yet, as they see the active bomb under Your
        arm abd don't want to set it off. """)

        action = input("> ")

        if action == "throw the bomb" :

            print("""In a panic you throw the bomb at the group of gothons
            and make a leap for the door. Right as you drop it a
            Gothon shoots you right in the the back killing you.
            as you die you see another gothon frantically try to disarm
            the bomb. you die knowing they will probably blow up when
            it goes off.""")

            return 'death'

        elif action == "slowly place the bomb" :

            print("""You point your blaster at the bomb under your arm
            abd theGothons put their hands up and start to sweat.
            You inch backward to the door, open it, then carefully
            place the bomb on the floorm pointing your blaster at it.
            You then jumb back through the door, punch the close button
            and blast the lock so the Gothons can't get out.
            Now that the bomb is placed you run to the escape pod to
            get off this tin can""")

            return "escape_pod"

        else :
            print("DOES NOT COMPUTE")
            return "the_bridge"

class EscapePod(Scene) :

    def enter(Scene) :

        print("""You rush through the ship desperately trying to make it to
        the escape pod before the whole ship explodes.  it seems Like
        hardly any Gothons are on the ship, so your run is clear of
        interference. you get to the chamber with the escape pods, and
        now need to pick one to take.   some of them could be damaged
        but you don't have tyime to look.   there's 5 pods, whiche one
        do you take?""")

        good_pod = randint(1,5)
        guess = int(input("[pod #]> "))

        if int(guess) != good_pod:

            print("You jump into pod %s and hit the eject button." % guess)
            print("""the pod escapes out into the void of space, then
            implodes as the hull ruptures, crushing your body
            into jam jelly.""")

            return 'death'

        else:

            print("""You jump into pod %s abd hit the eject button.
            The pod easily slides out into space heading to
            the planet below. As it flies to the planet, you look
            back and see your ship implode then explode like a
            bright star, taking out the Gothon ship at the same
            time.   You won!""" % guess)

            return 'finished'
