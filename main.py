Mi_col = 0
Mi_row = 0
Mi_unq = 0
Wk_col = 0
Wk_row = 0
Wk_unq = 0
Ex_col = 0
Ex_row = 0
Ex_unq = 0
Result = ""
basic.show_string("SHAKE")

def on_gesture_shake():
    global Mi_unq, Mi_row, Mi_col
    basic.show_string("Bit turn")
    Mi_unq = randint(1, 25)
    Mi_row = (Mi_unq - 1) // 5
    Mi_col = Mi_unq - (Mi_row * 5) - 1
    # Debug ↓
    basic.show_arrow(ArrowNames.EAST)
    basic.show_number(Mi_unq)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_number(Mi_row)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_number(Mi_col)
    # Debug ↑
    basic.show_string("Push A")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_a():
    global Wk_unq,Wk_col,Wk_row
    basic.show_string("Your turn")
    basic.show_arrow(ArrowNames.EAST)
    basic.clear_screen()
    Wk_row = 0
    while Wk_row < 5:
        Wk_col = 0
        while Wk_col < 5:
            led.plot(Wk_col, Wk_row)
            Wk_unq = (Wk_row * 5) + Wk_col + 1
            basic.pause(500)
            Wk_col += 1
        Wk_row += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Ex_col, Ex_row, Wk_col, Wk_row, Ex_unq, Result
    Ex_col = Wk_col
    Ex_row = Wk_row
    Ex_unq = (Ex_row * 5) + Ex_col + 1
    # Debug ↓
    basic.show_arrow(ArrowNames.EAST)
    basic.show_number(Ex_unq)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_number(Ex_row)
    basic.show_arrow(ArrowNames.EAST)
    basic.show_number(Ex_col)
    # Debug ↑

  # Judgment
    basic.show_string("Judgment")
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
    basic.show_string(Result)
input.on_button_pressed(Button.B, on_button_pressed_b)
