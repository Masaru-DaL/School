# 演習４
# 以下の関数を作成します

# 関数
# 引数に数値（整数）を受け取ります
# 引数の値が０以下の場合、何もせずに終了します。
# そうでない場合、引数の数だけ「＄」を続けて出力し、
# その後、「引数-2」を新たな引数として、自身を呼び出します
# 出力例：引数が5の場合、「＄＄＄＄＄」と出力。最後に改行する。

# ＄出力関数
def catch_num(num):
    # 引数が０以下の場合は終了する
    if num <= 0:
        return

    # num の数だけ繰り返し
    for i in range(num):
        # ＄を繋げて出力
        print('$', end = '')
    #最後に改行を出力する
    print()
    # num-2を引数にして再帰呼び出し
    catch_num(num - 2)

# このプログラムでは、以下のことをして下さい。

# 数字（整数）を１つ入力してもらう
ch = int(input("整数を入力してください: "))

# 数字を数値に変換したものを引数として、
# 上記で作成した関数を実行する
catch_num(ch)
