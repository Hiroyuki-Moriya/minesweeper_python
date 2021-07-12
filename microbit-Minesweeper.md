microbit-Minesweeper.md  

## Ver 03  
  変更点  
* LEDの点灯が全て終わってから結果表示するように修正。  
* 結果表示の時にでるスマイルマークを変更。  
* メッセージを修正。  

## Ver 02  
  変更点  
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

Shake to start the game.  
When you press the A button, the LEDs will light up in order.  
Press the B button at the position where you think there is a mine.  
If it hits, "Hit!" Will be displayed, if it is close, "Near" will be displayed, and if it is far, "Far" will be displayed.  
You can do it as many times as you like until you shake it, so use the "Near" and "Far" clues to locate it.  

メイクコードはこちら。 Makecode is here↓  
　https://makecode.microbit.org/_FieMWecbviY9  

microbit-Minesweeper_Python_v01.hex 2021‎/‎7‎/‎9‎ ‏‎11:49:37  
microbit-Minesweeper_Python_v01debug.hex  2021‎/‎7‎/‎9‎ ‏‎‏‎9:52:09  

## microbit-Minesweeper 仕様 specification  
  """  
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
"""  


"""  
機雷の位置を決める  
  Bit Turn 表示。  
  振られたら乱数でMi_unq(1～25)を決める。  
  機雷の位置はMine(Mi_row,Mi_col)に格納する  
"""  


"""  
予想する  
  Your Turn表示。  
  AボタンでLEDの光る位置を動かしBボタンで決定。  
  位置はExp(Ex_row,Ex_col)とEx_unqに格納する。  
"""  

"""  
判定する  
  Judgment表示。  
Hit:
  if Mi_unq = Ex_unq:  
     Hit表示  

上判定:  
  if Ex_row > 0 and Result == "":  
    if (Ex_row - Mi_row) == 1:  
      Result = "Near"  

下判定:  
  if Ex_row < 4 and Result == "":  
    if (Ex_row - Mi_row) == -1:  
      Result = "Near"  

左判定:  
  if Ex_col > 0 and Result == "":  
    if (Ex_col - Mi_col) == 1:  
      Result = "Near"  

右判定:  
  if Ex_col < 4 and Result == "":  
    if (Ex_col - Mi_col) == -1:  
      Result = "Near"  

左上判定:  
  if Ex_row > 0 and Ex_col > 0 and Result == "":  
    if (Ex_unq - Mi_unq) == 6:  
      Result = "Near"  


右上判定:  
  if Ex_row > 0 and Ex_col < 4 and Result == "":  
    if (Ex_unq - Mi_unq) == -4:  
      Result = "Near"  

左下判定:  
  if Ex_row < 4 and Ex_col > 0 and Result == "":  
    if (Ex_unq - Mi_unq) == 4:  
      Result = "Near"  

右下判定:  
  if Ex_row < 4 and Ex_col < 4 and Result == "":  
    if (Ex_unq - Mi_unq) == -6:  
      Result = "Near"  

  Result = "Far"  
  Result表示  
