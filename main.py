"""
    Title  : Minesweeper_Python
    Version: 05
    Author : Hiroyuki.Moriya
    Use    : https://makecode.microbit.org/#editor
"""
Mi_row = 0
Mi_col = 0
Mi_unq = 0
Wk_row = 0
Wk_col = 0
Wk_unq = 0
Ex_row = 0
Ex_col = 0
Ex_unq = 0
Result = ""
basic.show_string("Shake")

def on_gesture_shake():
    global Mi_unq, Mi_row, Mi_col
    Mi_unq = randint(1, 25)
    Mi_row = (Mi_unq - 1) // 5
    Mi_col = Mi_unq - (Mi_row * 5) - 1
    basic.pause(500)
    basic.show_string("Start")
    basic.show_arrow(ArrowNames.WEST)
    basic.pause(500)
    basic.clear_screen()
    basic.show_string("Attack")
    basic.show_arrow(ArrowNames.EAST)
    basic.pause(500)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_a():
    global Wk_unq, Wk_col, Wk_row, Ex_col, Ex_row
    basic.clear_screen()
    Wk_row = 0
    while Wk_row < 5:
        Wk_col = 0
        while Wk_col < 5:
            led.plot(Wk_col, Wk_row)
            Wk_unq = (Wk_row * 5) + Wk_col + 1
            basic.pause(500)
            led.unplot(Wk_col, Wk_row)
            Wk_col += 1
        Wk_row += 1
    # Plot Ex
    led.plot_brightness(Ex_col, Ex_row, 128)
    basic.pause(1000)
    basic.clear_screen()
    # Result announcement
    Result = Judgment(Mi_unq, Ex_unq)
    basic.show_string(Result)
    basic.pause(1000)
    basic.clear_screen()
    if Result == "Hit!":
        basic.show_icon(IconNames.HAPPY)
    else:
        if Result == "Near":
            basic.show_icon(IconNames.ASLEEP)
        else:
            basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Ex_col, Ex_row, Wk_col, Wk_row, Ex_unq, Result
    Ex_row = Wk_row
    Ex_col = Wk_col
    Ex_unq = (Ex_row * 5) + Ex_col + 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global Mi_unq, Mi_col, Mi_row, Ex_unq, Ex_col, Ex_row
    basic.show_number(Mi_unq)
    basic.pause(500)
    basic.clear_screen()
    basic.show_number(Ex_unq)
    basic.pause(500)
    basic.clear_screen()
    led.plot_brightness(Mi_col, Mi_row, 256)
    led.plot_brightness(Ex_col, Ex_row, 128)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def Judgment(Mi_unq: int, Ex_unq: int):
    Result = ""
    # Hit
    if Mi_unq == Ex_unq:
        Result = "Hit!"
    # Four corners
    if Mi_unq == 1 and Result == "":
        if Ex_unq in (2, 6, 7):
            Result = "Near"
    else:
        if Mi_unq == 5 and Result == "":
            if Ex_unq in (4, 9, 10):
                Result = "Near"
        else:
            if Mi_unq == 21 and Result == "":
                if Ex_unq in (16, 17, 22):
                    Result = "Near"
            else:
                if Mi_unq == 25 and Result == "":
                    if Ex_unq in (19, 20, 24):
                        Result = "Near"
    # Upper side
    if Mi_unq in (2, 3, 4) and Result == "":
        if Ex_unq in (Mi_unq - 1, Mi_unq + 1, Mi_unq + 4, Mi_unq + 5, Mi_unq + 6):
            Result = "Near"
    # lower side
    if Mi_unq in (22, 23, 24) and Result == "":
        if Ex_unq in (Mi_unq - 1, Mi_unq + 1, Mi_unq - 6 , Mi_unq - 5, Mi_unq - 4):
            Result = "Near"
    # left side
    if Mi_unq in (6, 11, 16) and Result == "":
        if Ex_unq in (Mi_unq + 1, Mi_unq - 5 , Mi_unq - 4, Mi_unq + 5, Mi_unq + 6):
            Result = "Near"
    # Right side
    if Mi_unq in (10, 15, 20) and Result == "":
        if Ex_unq in (Mi_unq - 6, Mi_unq - 5 , Mi_unq - 1, Mi_unq + 4, Mi_unq + 5):
            Result = "Near"
    # Center
    if Mi_unq in (7, 8, 9, 12, 13, 14, 17, 18, 19) and Result == "":
        if Ex_unq in (Mi_unq - 6, Mi_unq - 5 , Mi_unq - 4, Mi_unq - 1, Mi_unq + 1, Mi_unq + 4, Mi_unq + 5, Mi_unq + 6):
            Result = "Near"
    # Far
    if Result == "":
        Result = "Far"
    return Result