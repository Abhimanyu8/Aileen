# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image eileen happy = "eileen_happy.png"
image eileen vhappy = "eileen_vhappy.png"
image eileen concerned = "eileen_concerned.png"

image creditscroll:
    Text([
'{size=40}Made By: \n',
"{size=30}Avimanyu Dutta\n",
'{size=40}Music: \n',
"{size=30}'East of the sun' by Eric Hamilton (dilvie), Creative Commons License\n",
'{size=40}Made Using: \n',
"{size=30}Ren'Py by renpytom (Tom Rothamel), MIT license\n",
'pyAIML by Cort Stratton, FreeBSD license\n',
"'class AIMLBot' by Sergey Zakharov\n",
'{size=40}AI personality: \n',
"{size=30}'Free A.L.I.C.E. AIML Set' by the AI Foundation (GNU Lesser GPL)\n",
'{size=40}Images:\n',
'{size=30}character art by Piroshki (from the Lemmasoft forums), MIT license \n',
"{size=40}'AIleen'\n",
"{size=30}is a 'Proof of Concept' demonstration,\n",
'to show that AIML, or Artificial Intelligence Markup Language, can be used with RenPy.\n',
"This Demonstration is a GUIST 6th Semester Project\n"],text_align=0.5)
    anchor (0.5, 0.0)
    pos (0.5, 1.0)
    linear 30.0 ypos 0.0 yanchor 1.0

# Declare characters used by this game.
define e = Character('Aileen', color="#c8ffc8")

init:
    $ import AIMLBot
    image bg grey = "#aaaaaa"
    $user_input=[]

# The game starts here.
label start:

    play music "music/dilvie_-_east_of_the_sun.ogg"

    window show 

    scene bg grey

    show eileen happy at center
    with pixellate

    show eileen happy at left
    with move

    $ response = AIMLBot.AimlBot().run('Hi')

    $renpy.say(nvl,"[response]", interact = False)

    while True:

        if user_input == "bye":
            pause 1.0
            jump end

        nvl clear

        $user_input = renpy.input(prompt = "Your input ('bye' to leave chat):", allow="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ /.,'?!")

        $ response = AIMLBot.AimlBot().run(user_input)

        $renpy.say(nvl,"[response]", interact = False)
     
       



label end:
    
    nvl clear
    show eileen concerned at center
    with move
    e "But... You already want to leave me?"
    show eileen happy at center
    e "You'll visit me again, will you?"
    show eileen vhappy at center
    e "See you next time !!!"
    window hide
    pause 1.0
    hide eileen concerned at center
    with pixellate
    scene black
    with dissolve
    show creditscroll
    $ renpy.pause(30.0, hard=True)
    hide creditscroll
    stop music fadeout 5.0
    show text "Thanks For Playing !\n{size=60}" #+ renpy.version() #Show RenPy Version
    with dissolve
    pause 3.0
    

    return


