/** 
    Title  : Minesweeper_Python
    Version: 05
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
    let Result = Judgment(Mi_unq, Ex_unq)
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
    basic.pause(1000)
    basic.clearScreen()
})
function Judgment(Mi_unq: number, Ex_unq: number): string {
    let Result = ""
    //  Hit
    if (Mi_unq == Ex_unq) {
        Result = "Hit!"
    }
    
    //  Four corners
    if (Mi_unq == 1 && Result == "") {
        if ([2, 6, 7].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    } else if (Mi_unq == 5 && Result == "") {
        if ([4, 9, 10].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    } else if (Mi_unq == 21 && Result == "") {
        if ([16, 17, 22].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    } else if (Mi_unq == 25 && Result == "") {
        if ([19, 20, 24].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    }
    
    //  Upper side
    if ([2, 3, 4].indexOf(Mi_unq) >= 0 && Result == "") {
        if ([Mi_unq - 1, Mi_unq + 1, Mi_unq + 4, Mi_unq + 5, Mi_unq + 6].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    }
    
    //  lower side
    if ([22, 23, 24].indexOf(Mi_unq) >= 0 && Result == "") {
        if ([Mi_unq - 1, Mi_unq + 1, Mi_unq - 6, Mi_unq - 5, Mi_unq - 4].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    }
    
    //  left side
    if ([6, 11, 16].indexOf(Mi_unq) >= 0 && Result == "") {
        if ([Mi_unq + 1, Mi_unq - 5, Mi_unq - 4, Mi_unq + 5, Mi_unq + 6].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    }
    
    //  Right side
    if ([10, 15, 20].indexOf(Mi_unq) >= 0 && Result == "") {
        if ([Mi_unq - 6, Mi_unq - 5, Mi_unq - 1, Mi_unq + 4, Mi_unq + 5].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    }
    
    //  Center
    if ([7, 8, 9, 12, 13, 14, 17, 18, 19].indexOf(Mi_unq) >= 0 && Result == "") {
        if ([Mi_unq - 6, Mi_unq - 5, Mi_unq - 4, Mi_unq - 1, Mi_unq + 1, Mi_unq + 4, Mi_unq + 5, Mi_unq + 6].indexOf(Ex_unq) >= 0) {
            Result = "Near"
        }
        
    }
    
    //  Far
    if (Result == "") {
        Result = "Far"
    }
    
    return Result
}

