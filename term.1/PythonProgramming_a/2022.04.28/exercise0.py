# 演習０【前回の復習】
# 整数を入力してもらう。
# その整数が奇数の場合は「奇数です」と１度だけ出力する。
# その整数が偶数の場合は「偶数です」と入力された数の回数出力する。
# というプログラムを作成してください。
# 例１）
# 整数を入力してください：5
# 結果：
# 奇数です
ch = input("数字を入力してください")
num = int(ch)

# if num % 2 == 1:
#   print("奇数です")
# else:
#   print("偶数です")

if num % 2 == 0:
  count = num # 入力された値
  msg = "偶数です"
else:
  count = 1
  msg = "奇数です"

for i in range(count):
  print(msg)


# 例２）
# 整数を入力してください：4
# 結果：
# 偶数です
# 偶数です
# 偶数です
# 偶数です
# ch = input("整数を入力してください")
# num = int(ch)

# if num % 2 == 1:
#   print("奇数です" * num)
# else:
#   print("偶数です\n" * num)


# プログラムの流れも自分で考えてみましょう。
# 難しい場合は、分かる部分からプログラムを書いてみましょう。