# 演習２
#
# このファイルとは別に、以下の関数を持つモジュールを作成します。

# 関数
# 引数に数値（整数）を受け取り、
# １からその数までの、順番のリストを作成し、
# そのリストを戻り値にする
# このプログラムでは、以下のことをして下さい。

# 数字（整数）を１つ入力してもらう
list_num = []
num = int(input("整数を１つ入力してください："))

# 数字を数値に変換したものを引数として、
# 別に作成したモジュールの関数を実行し、
# 結果のリストを変数に代入する
for i in range(1, num + 1):
  ret_num = print(i)
  list_num.append(ret_num)

# 代入した変数（リスト）を出力する

print(list_num)
