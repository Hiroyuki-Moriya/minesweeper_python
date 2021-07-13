/** 
    Title  : Minesweeper_Python
    Version: 04
    Author : Hiroyuki.Moriya
    Use    : https://makecode.microbit.org/#editor

 */
let Mi_row = 0
let Mi_col = 0
let Mi_unq = 0
let Wk_row = 0
let Wk_col = 0
let Wk_unq = 0
let Ex_row = 0
let Ex_col = 0
let Ex_unq = 0
let Result = ""
basic.showString("Shake")
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    Mi_unq = randint(1, 25)
    Mi_row = Math.idiv(Mi_unq - 1, 5)
    Mi_col = Mi_unq - Mi_row * 5 - 1
    basic.pause(500)
    basic.showString("Start")
    basic.showArrow(ArrowNames.West)
    basic.pause(500)
    basic.clearScreen()
    basic.showString("Attack")
    basic.showArrow(ArrowNames.East)
    basic.pause(500)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.clearScreen()
    Wk_row = 0
    while (Wk_row < 5) {
        Wk_col = 0
        while (Wk_col < 5) {
            led.plot(Wk_col, Wk_row)
            Wk_unq = Wk_row * 5 + Wk_col + 1
            basic.pause(500)
            led.unplot(Wk_col, Wk_row)
            Wk_col += 1
        }
        Wk_row += 1
    }
    //  Plot Ex
    led.plotBrightness(Ex_col, Ex_row, 128)
    basic.pause(1000)
    basic.clearScreen()
    //  Result announcement
    let Result = Judgment(Mi_unq, Ex_unq, Ex_col, Ex_row)
    basic.showString(Result)
    basic.pause(1000)
    basic.clearScreen()
    if (Result == "Hit!") {
        basic.showIcon(IconNames.Happy)
    } else if (Result == "Near") {
        basic.showIcon(IconNames.Asleep)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Ex_row = Wk_row
    Ex_col = Wk_col
    Ex_unq = Ex_row * 5 + Ex_col + 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    basic.showNumber(Mi_unq)
    basic.pause(500)
    basic.clearScreen()
    basic.showNumber(Ex_unq)
    basic.pause(500)
    basic.clearScreen()
    led.plotBrightness(Mi_col, Mi_row, 256)
    led.plotBrightness(Ex_col, Ex_row, 128)
})
function Judgment(Mi_unq: number, Ex_unq: number, Ex_col: number, Ex_row: number): string {
    let Result = ""
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
    
    return Result
}

