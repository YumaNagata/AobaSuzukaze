import tkinter as tk
import tkinter.filedialog as fd
import tkinter.scrolledtext as st
import sys, os.path

from tkinter import filedialog

import chardet



root = tk.Tk()
root.title('メモ帳＋＋') #タイトル
root.geometry("800x400") #サイズ
#window.maxsize()　#最小ウィンドウサイズ
#window.minisize() #最大ウィンドウサイズ

###

path_name = os.getcwd()

# ファイル選択
def load_file():
    global path_name
    filename = fd.askopenfilename(filetypes = [('テキスト文章', ('.txt')),('すべてのファイル', ('.*'))],
                               initialdir = path_name)
    rawdate = open(filename, "rb").read()
    result = chardet.detect(rawdate)
    char_code = result['encoding']
    # 文字コードを認識させる処理 頑張ったんや(´；ω；｀) #

    if filename != "":
        path_name = os.path.dirname(filename)
        fi = open(filename,encoding = char_code)
        text_widget.delete('1.0', 'end')
        for x in fi:
            text_widget.insert('end', x)
        fi.close()
        text_widget.mark_set(tk.INSERT, '1.0')
        text_widget.focus_set()

###


###

#ファイル保存
def load_overwriting():
    
    result=text_widget.get(1.0, tk.END+"-1c")
    root.filename =  filedialog.asksaveasfilename(initialdir = path_name, title = "名前をつけて保存",
                                                  filetypes =  [('テキスト文章', (".txt")), ('すべてのファイル', ('.*'))])
    with open(root.filename, 'w') as f:
        f.write(result)

###



def start(): pass #ダミー（仮り）


menubar = tk.Menu(root)
root.configure(menu = menubar)
#メニューバー


file = tk.Menu(menubar,tearoff = False)
edit = tk.Menu(menubar,tearoff = False)
format = tk.Menu(menubar,tearoff = False)
display = tk.Menu(menubar,tearoff = False)
help = tk.Menu(menubar,tearoff = False)
#メニューバー設定


menubar.add_cascade(label = "ファイル", underline = 0, menu = file)
menubar.add_cascade(label = "編集", underline = 0, menu = edit)
menubar.add_cascade(label = "書式", underline = 0, menu = format)
menubar.add_cascade(label = "表示", underline = 0, menu = display)
menubar.add_cascade(label = "ヘルプ", underline = 0, menu = help)
#メニューバー表示（表示）

###



###

file.add_command(label = "新規", underline = 0, command = start)
file.add_command(label = "新しいウィンドウ", underline = 0, command = start)
file.add_command(label = "開く", underline = 0, command = load_file)
file.add_command(label = "上書き保存", underline = 0, command = start)
file.add_command(label = "名前を付けて保存", underline = 0, command = load_overwriting)
file.add_separator()
file.add_command(label = "印刷", underline = 0, command = start)
file.add_separator()
file.add_command(label = "メモ帳＋＋の終了", underline = 0, command = start)
#ファイルのメニューバーのメニューバー（表示）

###


###

edit.add_command(label = "元に戻す", underline = 0, command = start)
edit.add_separator()
edit.add_command(label = "切り取り", underline = 0, command = start)
edit.add_command(label = " コピー", underline = 0, command = start)
edit.add_command(label = "貼り付け", underline = 0, command = start)
edit.add_command(label = "消去", underline = 0, command = start)
edit.add_separator()
edit.add_command(label = "検索", underline = 0, command = start)
edit.add_command(label = "次を検索", underline = 0, command = start)
edit.add_command(label = "前を検索", underline = 0, command = start)
edit.add_command(label = "置換", underline = 0, command = start)
edit.add_command(label = "行へ移動", underline = 0, command = start)
edit.add_separator()
edit.add_command(label = "すべて選択", underline = 0, command = start)
#編集のメニューバーのメニューバー（表示）

format.add_command(label = "右端で折り返す", underline = 0, command = start)
#書式のメニューバーのメニューバー（表示）

display.add_command(label = "ステータス バー", underline = 0, command = start)
#表示のメニューバーのメニューバー（表示）

help.add_command(label = "バージョンの推奨", underline = 0, command = start)
#ヘルプのメニューバーのメニューバー（表示）

###


###

text_widget = st.ScrolledText()
#テキストウィジェットの表示

text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#テキストウィジェットの位置、大きさ

###

text_widget.delete('1.0', 'end')


filename = sys.argv[1]

path_name = os.path.dirname(filename)
rawdate = open(filename, "rb").read()
result = chardet.detect(rawdate)
char_code = result['encoding']
fi = open(filename,encoding = char_code)
for i in fi:
    text_widget.insert('end', i)

#ここの動作は何故かソフトのある住所をアクセスしてしまう

###



root.mainloop()








