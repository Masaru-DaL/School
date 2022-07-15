import tkinter          # tkinterのインポート
import random           # randomのインポート

root = tkinter.Tk()                                 # ウィンドウの作成
root.title("落ち物パズル「ねこねこ」")              # タイトルの設定
root.resizable(False, False)                        # 画面のリサイズの抑制

# 猫ブロック画像リスト（最初の１つ目は空にしておく）
neko_images = [
    None,
    tkinter.PhotoImage(file="../image/neko1.png"),
    tkinter.PhotoImage(file="../image/neko2.png"),
    tkinter.PhotoImage(file="../image/neko3.png"),
    tkinter.PhotoImage(file="../image/neko4.png"),
    tkinter.PhotoImage(file="../image/neko5.png"),
    tkinter.PhotoImage(file="../image/neko6.png"),
    tkinter.PhotoImage(file="../image/neko_niku.png")
]

# ねこフィールドの作成
neko_field = []
# チェックフィールドの作成
check_field = []
for y in range(10):
    neko_field.append([0,0,0,0,0,0,0,0])
    check_field.append([0,0,0,0,0,0,0,0])

# 並びチェック関数
def check_neko():
    # 盤面の情報を全て、チェックフィールドにコピー
    for y in range(10):
        for x in range(8):
            check_field[y][x] = neko_field[y][x]

    # 横の並びのチェック(内側の6列のみ)
    for y in range(10):
        for x in range(1, 7):
            check_pos = check_field[y][x]
            # その場所にねこがいる場合で、左右とも同じねこの場合
            if check_pos > 0 and check_field[y][x-1] == check_pos and check_field[y][x+1] == check_pos:
                # 3マスとも肉球に変える
                neko_field[y][x] = 7
                neko_field[y][x-1] = 7
                neko_field[y][x+1] = 7

    # 縦の並びをチェック（一番下と一番上以外）
    for y in range(1, 9):
        for x in range(8):
            # その場所のねこを取得
            check_pos = check_field[y][x]
            # マスにねこがいる場合で
            # 上下ともに同じねこの場合
            if check_pos > 0 \
               and check_field[y-1][x] == check_pos \
               and check_field[y+1][x] == check_pos:
                # ３マスとも肉球に変える
                neko_field[y][x] = 7
                neko_field[y-1][x] = 7
                neko_field[y+1][x] = 7

    # 斜めの並びをチェック（一番外枠以外）
    for y in range(1, 9):
        for x in range(1, 7):
            # その場所のねこを取得
            check_pos = check_field[y][x]
            # マスにねこがいる場合
            if check_pos > 0:
                # 左上と右下がともに同じねこの場合
                if check_field[y-1][x-1] == check_pos \
                   and check_field[y+1][x+1] == check_pos:
                    # ３マスとも肉球に変える
                    neko_field[y][x] = 7
                    neko_field[y-1][x-1] = 7
                    neko_field[y+1][x+1] = 7
                # 右上と左下がともに同じねこの場合
                if check_field[y-1][x+1] == check_pos \
                   and check_field[y+1][x-1] == check_pos:
                    # ３マスとも肉球に変える
                    neko_field[y][x] = 7
                    neko_field[y-1][x+1] = 7
                    neko_field[y+1][x-1] = 7



def draw_neko():
    cvs.delete("NEKO")
    # 盤面全部に対して繰り返す
    for y in range(10):
        for x in range(8):
            # その位置の画像番号を取得
            image_number = neko_field[y][x]
            if image_number > 0:
                # その番号のねこを描画
                cvs.create_image(x*72+24, y*72+24,
                                 image = neko_images[image_number],
                                 anchor = "nw", tag = "NEKO")


# ねこ落下関数
def fall_neko():
    is_fall = False             # ねこ落下ありフラグ
    # 2次元リストの繰り返しをするが、縦方向は下から順に処理をする
    # 上からチェックするようにしてしまうと一気に下に落ちてしまう
    for y in range(8, -1, -1):
        for x in range(8):
            # その位置が空でない、かつ1つ下が空の場合
            if neko_field[y][x] != 0 and neko_field[y+1][x] == 0:
                # 1つ下の位置に、この位置のねこを設定する
                neko_field[y+1][x] = neko_field[y][x]
                # この位置のねこを空にする
                neko_field[y][x] = 0
                is_fall = True

    return is_fall              # ねこ落下ありフラグを戻り値にする
cvs = tkinter.Canvas(root, width=912, height=768)   # キャンバスの作成
cvs.pack()                                          # キャンバスの配置

bg = tkinter.PhotoImage(file="../image/neko_bg.png")            # 背景画像
cursor = tkinter.PhotoImage(file="../image/neko_cursor.png")    # カーソル画像

cvs.create_image(456, 384, image=bg)                # 背景画像の表示

mouse_x, mouse_y, mouse_click = 0, 0, False

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x, mouse_y = e.x, e.y                     # イベントのマウス位置を保持

def mouse_press(e):
    global mouse_click
    mouse_click = True

root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)

step = 0

# ゲームメイン処理
def game_main():

    global mouse_x, mouse_y, mouse_click, step

    # タイトル表示
    if step == 0:
        step = 1

    # スタート待ち
    elif step == 1:
        if mouse_click == True:
            # ねこフィールドをクリア
            for y in range(10):
                for x in range(8):
                    neko_field[y][x] = 0
            mouse_click = False
            step = 2

    # ねこ落下処理
    elif step == 2:
        if fall_neko() == False:
            step = 3
        draw_neko()

    elif step == 3:
        check_neko()
        draw_neko()
        step = 4

    elif step == 4:
        step = 5
        mouse_click = False

    elif step == 5:
        # ※数値は、画像に合わせて計算済みの値となっています
        if 24 <= mouse_x < 24+72*8 and 24 <= mouse_y < 24+72*10:
            # カーソル位置を計算
            cursor_x = int((mouse_x-24)/72)
            cursor_y = int((mouse_y-24)/72)

            if mouse_click == True:
                # クリックしたカーソル位置にねこの画像をランダムで配置(仮処理)
                neko_field[cursor_y][cursor_x] = random.randint(1, 6)
                mouse_click = False
                step = 2

        else:
            # 盤面外の場合、カーソル位置をマイナスにしておく
            cursor_x = -1

        cvs.delete("CURSOR")
        # カーソルが盤面内なら
        if cursor_x != -1:
            cvs.create_image(cursor_x*72+24, cursor_y*72+24,
                            image = cursor, anchor = "nw",
                            tag = "CURSOR")
        draw_neko()

    # ゲームオーバー判定
    elif step == 6:
        pass

    root.after(100, game_main)                      # ゲームメイン処理を繰り返す

game_main()                                         # ゲームメイン処理の呼び出し
root.mainloop()                                     # ウィンドウの表示
