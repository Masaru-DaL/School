# 演習２
# jokergame.pyにJokerGameクラスが用意されています。
#
# 下記のコメントに沿って、プログラムを完成させて下さい。
# プログラムが必要な箇所には
# pass # ここにプログラムを追加
# と書いてあります

# JokerGameクラスをインポートする
from jokergame import JokerGame # ここにプログラムを追加

# JokerGameクラスのインスタンスを２つ用意する
queen = JokerGame() # ここにプログラムを追加
king = JokerGame()

# インスタンスのset_name関数を使って、
# ２つのインスタンスそれぞれに名前を設定する。（例：「森の中」「洞窟」など）
queen.set_name("森の中") # ここにプログラムを追加
king.set_name("山の上") # ここにプログラムを追加

# インスタンスのset_joker関数を使って、
# ２つのインスタンスそれぞれのジョーカーの位置を設定する
queen.set_joker() # ここにプログラムを追加
king.set_joker() # ここにプログラムを追加

# ルールのメッセージを出力
print("２つのエリアそれぞれの１～１０のどこかにジョーカーがいます")
print("どちらにもジョーカーのいないところを選んで下さい")

# 未使用番号リスト
no_list = {1,2,3,4,5,6,7,8,9,10}
# 生存数カウンタ
live = 0
# ずっと繰り返す
while True:

    # １～１０の数字を入力してもらう（数字以外のエラー処理は省略）
    no = int(input("１～１０の数字を入力："))
    # 数字チェック
    if not(no in no_list):
        print("まだ入力してない１～１０から選んで下さい")
        continue
    else:
        no_list.remove(no)

    # ２つのインスタンスそれぞれ、入力された数字を引数にして、
    # is_gameover関数を呼び出す。戻り値も別々で受け取る
    result_1 = queen.is_gameover(no)
    result_2 = king.is_gameover(no)


    # ２つの戻り値のどちらかが「True」だったらゲームオーバーのため、
    # ゲームオーバーのメッセージを出力して、whileを抜ける
    if result_1 or result_2 == True:
        print("ゲームオーバー") # ここにプログラムを追加
        break


    # 生存数カウンタを増やして出力
    live += 1
    print(f"{live}回目の生き残りに成功！")
