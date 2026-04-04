default shooting_score = 0
default shooting_time = 60
default shooting_combo = 0

init python:
    shooting_positions = [
        [(860, 540)] * 10,
        [(860, 540)] * 10,
        [(860, 540)] * 10,
    ]

    def generate_positions():
        for i in range(3):
            store.shooting_positions[i] = [
                (renpy.random.randint(150, 1750), renpy.random.randint(150, 900))
                for _ in range(10)
            ]


transform shooting_blink():
    block:
        ease 0.4 alpha 0.3
        ease 0.4 alpha 1.0
        repeat

transform shooting_shake():
    block:
        linear 0.05 xoffset 6
        linear 0.05 xoffset -6
        linear 0.05 xoffset 4
        linear 0.05 xoffset -4
        linear 0.05 xoffset 0
        repeat

transform shooting_pulse():
    block:
        ease 0.2 zoom 1.2
        ease 0.2 zoom 1.0
        repeat

transform shooting_move_0():
    subpixel True
    xpos shooting_positions[0][0][0] ypos shooting_positions[0][0][1]
    alpha 0
    ease 0.3 alpha 1
    block:
        ease 3.5 xpos shooting_positions[0][1][0] ypos shooting_positions[0][1][1]
        ease 3.5 xpos shooting_positions[0][2][0] ypos shooting_positions[0][2][1]
        ease 3.5 xpos shooting_positions[0][3][0] ypos shooting_positions[0][3][1]
        ease 3.5 xpos shooting_positions[0][4][0] ypos shooting_positions[0][4][1]
        ease 3.5 xpos shooting_positions[0][5][0] ypos shooting_positions[0][5][1]
        ease 3.5 xpos shooting_positions[0][6][0] ypos shooting_positions[0][6][1]
        ease 3.5 xpos shooting_positions[0][7][0] ypos shooting_positions[0][7][1]
        ease 3.5 xpos shooting_positions[0][8][0] ypos shooting_positions[0][8][1]
        ease 3.5 xpos shooting_positions[0][9][0] ypos shooting_positions[0][9][1]
        repeat

transform shooting_move_1():
    subpixel True
    xpos shooting_positions[1][0][0] ypos shooting_positions[1][0][1]
    alpha 0
    ease 0.3 alpha 1
    block:
        ease 2.0 xpos shooting_positions[1][1][0] ypos shooting_positions[1][1][1]
        ease 2.0 xpos shooting_positions[1][2][0] ypos shooting_positions[1][2][1]
        ease 2.0 xpos shooting_positions[1][3][0] ypos shooting_positions[1][3][1]
        ease 2.0 xpos shooting_positions[1][4][0] ypos shooting_positions[1][4][1]
        ease 2.0 xpos shooting_positions[1][5][0] ypos shooting_positions[1][5][1]
        ease 2.0 xpos shooting_positions[1][6][0] ypos shooting_positions[1][6][1]
        ease 2.0 xpos shooting_positions[1][7][0] ypos shooting_positions[1][7][1]
        ease 2.0 xpos shooting_positions[1][8][0] ypos shooting_positions[1][8][1]
        ease 2.0 xpos shooting_positions[1][9][0] ypos shooting_positions[1][9][1]
        repeat

transform shooting_move_2():
    subpixel True
    xpos shooting_positions[2][0][0] ypos shooting_positions[2][0][1]
    alpha 0
    ease 0.3 alpha 1
    parallel:
        shooting_blink
    parallel:
        block:
            ease 1.0 xpos shooting_positions[2][1][0] ypos shooting_positions[2][1][1]
            ease 1.0 xpos shooting_positions[2][2][0] ypos shooting_positions[2][2][1]
            ease 1.0 xpos shooting_positions[2][3][0] ypos shooting_positions[2][3][1]
            ease 1.0 xpos shooting_positions[2][4][0] ypos shooting_positions[2][4][1]
            ease 1.0 xpos shooting_positions[2][5][0] ypos shooting_positions[2][5][1]
            ease 1.0 xpos shooting_positions[2][6][0] ypos shooting_positions[2][6][1]
            ease 1.0 xpos shooting_positions[2][7][0] ypos shooting_positions[2][7][1]
            ease 1.0 xpos shooting_positions[2][8][0] ypos shooting_positions[2][8][1]
            ease 1.0 xpos shooting_positions[2][9][0] ypos shooting_positions[2][9][1]
            repeat


label shooting_game:
    $ shooting_score = 0
    $ shooting_time = 60
    $ shooting_combo = 0
    $ generate_positions()

    stop music fadeout 0.5
    play music "audio/shooting minigame music.mp3"

    call screen shooting_game_screen

    stop music fadeout 0.5

    if shooting_score >= 30:
        "Неймовірно!  Ти набрав [shooting_score] очок."
    elif shooting_score >= 20:
        "Відмінно! Ти набрав [shooting_score] очок!"
    elif shooting_score >= 10:
        "Непогано! [shooting_score] очок. Є куди рости."
    elif shooting_score > 0:
        "Час вийшов. Лише [shooting_score] очок... Треба тренуватись."
    else:
        "Жодного влучання. Може наступного разу пощастить?"

    return