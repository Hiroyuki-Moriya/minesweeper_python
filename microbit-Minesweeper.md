microbit-Minesweeper.md  

## Ver 05 変更点  
* 関数Judgmentにバグがあったのと、ロジックがわかりづらいので、ロジック含め修正した。  
* このV05をもって完成版とします。  
* This V05 will be the completed version.  

## Ver 04 変更点  
* Aボタンを押した位置がわかるようにLEDを点灯させた。  
* ソース整理。判定ロジックを関数Judgementとして独立させた。  
* AボタンとBボタンを押すと答えを表示する機能を追加。  

## Ver 03 変更点  
* LEDの点灯が全て終わってから結果表示するように修正。  
* 結果表示の時にでるスマイルマークを変更。  
* メッセージを修正。  

## Ver 02 変更点  
* Bit turnのLEDの点灯を現在の位置の１個だけにした。  
* Hitの時にスマイルマークが出るように変更。  
* メッセージを修正。  

## Ver 01  
シェイクするとゲームが始まります。  
Aボタンを押すとLEDが順番に点灯します。  
機雷があると思う位置でBボタンを押してください。  
当たれば "Hit!" 、近ければ "Near" 、遠ければ "Far" の表示が出ます。  
シェイクするまで何度でもできますので、  
"Near" と "Far" の手がかりを使って位置を当ててください。  
答えを知りたいときは、AボタンとBボタンを同時に押してください。

Shake to start the game.  
When you press the A button, the LEDs will light up in order.  
Press the B button at the position where you think there is a mine.  
If it hits, "Hit!" Will be displayed, if it is close, "Near" will be displayed, and if it is far, "Far" will be displayed.  
You can do it as many times as you like until you shake it, so use the "Near" and "Far" clues to locate it.  
If you want to know the answer, press the A and B buttons at the same time.

メイクコードはこちら。 Makecode is here↓  
　https://makecode.microbit.org/_0cPX1Ycvgc5g  

## microbit-Minesweeper 仕様 specification  for V00  

機雷(Mine)の位置を予想(Expect)して当てるゲーム  
  位置はLEDの５×５配列とし、(row,col)で表すことにする  
      col,rowがとる値は、0～4の整数  
      機雷の位置変数 Mine(Mi_row,Mi_col)  
      予想する位置変数 Exp(Ex_row,Ex_col)  
  位置番号はLEDの左上から右下へ1～25の一意な数字(Unq)を割り当てたもの  
      機雷の位置番号 Mi_unq  
      予想する位置番号 Ex_unq  
    ※位置→Unq変換  
        Mi_unq = (Mi_row * 5) + Mi_col + 1  
    ※Unq→位置変換  
        Mi_row = (Mi_unq - 1) // 5　商は整数  
        Mi_col = Mi_unq - (Mi_row * 5) - 1  
  機雷の位置と予想の位置によってHit判定して、その結果を表示する。  
    "Hit" 位置が一致する  
    "Near" 上下左右斜め方向に距離1だけ離れている。  
        距離1とは、Mi_rowとEx_rowの差の絶対値が1であること  
        または、Mi_colとEx_colの差の絶対値が1であることを指す。  
    "Far"  上下左右斜め方向に距離2以上離れている。    

機雷の位置を決める  
  Bit Turn 表示。  
  振られたら乱数でMi_unq(1～25)を決める。  
  機雷の位置はMine(Mi_row,Mi_col)に格納する  

予想する  
  Your Turn表示。  
  AボタンでLEDの光る位置を動かしBボタンで決定。  
  位置はExp(Ex_row,Ex_col)とEx_unqに格納する。  

判定する  
  if Mi_unq = Ex_unq:  
      Result = "Hit!"  
  elif Mi_unq と Ex_unqの距離が±1:  
      Result = "Near"  
  Else:
      Result = "Far"  

## Source code V05
```
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
```
