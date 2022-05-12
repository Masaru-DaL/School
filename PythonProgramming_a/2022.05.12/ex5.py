# 演習５
# ※print文の引数部分を記載して下さい
#
# 出力プログラムが書かれています。
# sep や end 、必要なら追加のプログラムを記述して、
# 指定どおりの出力になるようにして下さい。
# 「」自体は出力例をわかりやすくしているだけなので、出力不要です

# 問題１：「1 2 3 4 5」と出力
for i in range(1, 6):
    print(i, end=' ')
print('\n---')

# 問題２：「1 1,2 2,3 3,4 4,5 5,」と出力
for i in range(1, 6):
    print(i, i, sep=' ', end=',')
print('\n---')

# 問題３：「1 1,2-2|3 3,4-4|5 5,」と出力
# 奇数の場合と偶数の場合で処理を分ける
for i in range(1, 6):
    if i % 2 == 0:
        print(i, i, sep='-', end='|')
    else:
        print(i, i, sep=' ', end=',')
