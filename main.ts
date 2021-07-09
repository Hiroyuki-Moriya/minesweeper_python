let Mi_col = 0
let Mi_row = 0
let Mi_unq = 0
let Wk_col = 0
let Wk_row = 0
let Wk_unq = 0
let Ex_col = 0
let Ex_row = 0
let Ex_unq = 0
let Result = ""
basic.showString("SHAKE")
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    basic.showString("Bit turn")
    Mi_unq = randint(1, 25)
    Mi_row = Math.idiv(Mi_unq - 1, 5)
    Mi_col = Mi_unq - Mi_row * 5 - 1
    basic.showString("Push A")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showString("Your turn")
    basic.showArrow(ArrowNames.East)
    basic.clearScreen()
    Wk_row = 0
    while (Wk_row < 5) {
        Wk_col = 0
        while (Wk_col < 5) {
            led.plot(Wk_col, Wk_row)
            Wk_unq = Wk_row * 5 + Wk_col + 1
            basic.pause(500)
            Wk_col += 1
        }
        Wk_row += 1
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Ex_col = Wk_col
    Ex_row = Wk_row
    Ex_unq = Ex_row * 5 + Ex_col + 1
    //  Judgment
    basic.showString("Judgment")
    Result = ""
    //  Hit
    if (Mi_unq == Ex_unq) {
        Result = "Hit!"
    }
    
    //  Upper side
    if (Ex_row > 0 && Result == "") {
        if (Ex_row - Mi_row == 1) {
            Result = "Near"
        }
        
    }
    
    //  lower side
    if (Ex_row < 4 && Result == "") {
        if (Ex_row - Mi_row == -1) {
            Result = "Near"
        }
        
    }
    
    //  left side
    if (Ex_col > 0 && Result == "") {
        if (Ex_col - Mi_col == 1) {
            Result = "Near"
        }
        
    }
    
    //  Right side
    if (Ex_col < 4 && Result == "") {
        if (Ex_col - Mi_col == -1) {
            Result = "Near"
        }
        
    }
    
    //  Upper left side
    if (Ex_row > 0 && Ex_col > 0 && Result == "") {
        if (Ex_unq - Mi_unq == 6) {
            Result = "Near"
        }
        
    }
    
    //  Upper right side
    if (Ex_row > 0 && Ex_col < 4 && Result == "") {
        if (Ex_unq - Mi_unq == -4) {
            Result = "Near"
        }
        
        //  Lower left side
        if (Ex_row < 4 && Ex_col > 0 && Result == "") {
            if (Ex_unq - Mi_unq == 4) {
                Result = "Near"
            }
            
        }
        
    }
    
    //  Lower left side
    if (Ex_row < 4 && Ex_col < 4 && Result == "") {
        if (Ex_unq - Mi_unq == -6) {
            Result = "Near"
        }
        
    }
    
    //  Far
    if (Result == "" || ["Hit!", "Near"].indexOf(Result) < 0) {
        Result = "Far"
    }
    
    basic.showString(Result)
})
