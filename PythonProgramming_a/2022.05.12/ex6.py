# 演習６
# ※プログラムの不足箇所を記述してください
#
# 以下の処理を、強制終了（Ctrl-c）されるまで
# 繰り返すプログラムを作成してください。
# 
# 文字列を入力してもらい、
# それを１文字１文字のリストにしたものを、
# 「リスト」に追加します。
# その後すぐに１回取り出します。
# 
# これを、「スタックのリスト」と「キューのリスト」
# 両方作成して並行して実行してください。
#
# 出力例
# 文字列を入力（終了はctrl+c)：abc
# スタックから「c」を取出しました
# スタックリスト：['a', 'b']
# キューから「a」を取出しました
# キューリスト：['b', 'c']

# スタックのリスト
stack_list = []

# キューのリスト
queue_list = []

# ずっとループ
while True:
    # 入力してもらう
    ch = input("文字列を入力（終了はctrl+c)：")
    # 入力文字をリストにする
    list_ch = list(ch)
    














    print('-----')












