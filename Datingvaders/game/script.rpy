# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Justin-Vader")
define a = Character("Arianne-Samus")
define h = Character("Hungry-Cat")
define l = Character("Lumy-Star")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgstars

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "calm.ogg" fadeout 1.0 fadein 1.0
    "Look what a beautiful night we have tonight.. The sky is full of stars !"
    #
    play sound "teleport.wav"
    stop music fadeout 1.0
    play music "tempest.ogg" fadeout 1.0 fadein 1.0
    "How what was that sound ?!"
    scene bginvaders
    "Oh my God the sky is now full of invaders"
    "Your only chance that you have is to seduce the invaders to convince them not to destroy our planet"
    "Will you save the planet Earth ?"
menu:
    "Yes":
        jump saveearth
    "No, I don't see the point":
        jump nopoint
label nopoint:
    "Without your action ..."
    jump badend

label badend:
    play sound "explo.wav"
    stop music fadeout 1.0
    play music "tempest.ogg" fadeout 1.0 fadein 1.0
    "...the invaders destroyed our planet"
    ".:. Bad Ending."
    return

label goodend:
    play sound "coin.wav"
    stop music fadeout 1.0
    play music "calm.ogg" fadeout 1.0 fadein 1.0
    "... Wow you convinced all this invaders to go away"
    "... Well done alien's lover"
    return

label saveearth:
    scene bgstars
    show justin-vader suspicious at top
    queue music "whatareyoutrying.ogg"
    # These display lines of dialogue.

    j "What are you trying weak human ?"

menu:
    "Hack your brain":
        jump brain
    "To be polite":
        jump polite
    "Use the Power of love":
        jump powerlove

label brain:
    play sound "piou.wav"
    stop music fadeout 1.0
    play music "datingvaders.ogg" fadeout 1.0 fadein 1.0
    show justin-vader happy at top
    j "Hey you seems to be most funny than expected"
    j "Maybe I'll reconsider invading Earth"
    play sound "teleport.wav"
    hide justin-vader

    show arianne-samus angry at top
    a "Hey what did you do to my friend Justin ?"

menu:
    "He think I have a good sens of humour, can you pull my finger ?":
        jump badend
    "Don't know he maybe had an heart attack":
        jump badend
    "Just sending him visiting Uranus":
        jump uranus

label polite:
    show justin-vader mischievous at top
    j "It would'nt save you to be polite !"
    jump badend
    return

label powerlove:
    show justin-vader schocked at top
    j "Wow what are you thinking I'm not an easy Alien"
    jump badend
    return

label uranus:
    play sound "piou.wav"
    show arianne-samus happy at top
    a "How your so kind, I really wanting him to visiting this place"
    a "I think I'll join him as soon as possible"
    play sound "teleport.wav"
    hide arianne-samus

    show hungry-cat at top
    h "Meow..."
menu:
    "You looks like a schrödinger's cat to me do you want do go to this box ?":
        jump box
    "Do you wana some space cat food ?":
        jump catfood
    "Oh your such a beautiful pussycat":
        jump box

label box:
    h "Shhh... Shhh"
    jump badend
    return


label catfood:
    play sound "piou.wav"
    h "rrr rrr"
    play sound "teleport.wav"
    hide hungry-cat

    show lumy-star at top
    l "What do you think of me ?"
menu:
    "I am dazzled by your beauty could you go away so that I can admire you":
        jump dazzled
    "You're flashing, I am so excited":
        jump badend
    "Never gonna give you up":
        jump badend
        
label dazzled:
    play sound "piou.wav"
    l "You're so kind I am gonna please you"
    play sound "teleport.wav"
    hide lumy-star
    jump goodend




    # This ends the game.
    return
