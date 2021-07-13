"""
    Title  : Minesweeper_Python
    Version: 04
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
    Result = Judgment(Mi_unq, Ex_unq, Ex_col, Ex_row)
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
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def Judgment(Mi_unq: int, Ex_unq: int, Ex_col: int, Ex_row: int):
    Result = ""
    # Hit
    if Mi_unq == Ex_unq:
        Result = "Hit!"
    # Upper side
    if Ex_row > 0 and Result == "":
        if (Ex_row - Mi_row) == 1:
            Result = "Near"
    # lower side
    if Ex_row < 4 and Result == "":
        if (Ex_row - Mi_row) == -1:
            Result = "Near"
    # left side
    if Ex_col > 0 and Result == "":
        if (Ex_col - Mi_col) == 1:
            Result = "Near"
    # Right side
    if Ex_col < 4 and Result == "":
        if (Ex_col - Mi_col) == -1:
            Result = "Near"
    # Upper left side
    if Ex_row > 0 and Ex_col > 0 and Result == "":
        if (Ex_unq - Mi_unq) == 6:
            Result = "Near"
    # Upper right side
    if Ex_row > 0 and Ex_col < 4 and Result == "":
        if (Ex_unq - Mi_unq) == -4:
            Result = "Near"
    # Lower left side
        if Ex_row < 4 and Ex_col > 0 and Result == "":
            if (Ex_unq - Mi_unq) == 4:
                Result = "Near"
    # Lower left side
    if Ex_row < 4 and Ex_col < 4 and Result == "":
        if (Ex_unq - Mi_unq) == -6:
            Result = "Near"
    # Far
    if Result == "" or Result not in("Hit!" ,"Near"):
        Result = "Far"
    return Result