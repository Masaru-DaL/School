# 演習２
# 入力された数字を加算してくプログラムです。
# 加算するのはadd_numという関数で行います。
#
# このプログラム自体はすでに完成しています。
# 以下の改造を加えてください。
#
# １）例外クラス「OverMaxError」を作成してください。
#     中の処理はpass（無処理）でかまいません。
#     関数add_numで、totalが最大値（定数:MAX_NUM）を超えたら
#     上記の例外を発生させてください。
#     関数外の処理で、この例外について例外処理をし、
#     「プログラムの上限を超えたため、終了します。」と出力して
#     プログラムを終了してください。
class OverMaxError(Exception):
    pass


# ２）このプログラムでは、他にも例外が発生することがあります。
#     それを個別の例外として処理してください。
#     こちらは、想定している以外にも例外があるかもしれません。
# １）２）どちらも例外処理のみで、プログラムの処理や判定は変えないでOKです。

# 入力された数字を加算して、戻り値にする
def add_num(total, num):
    MAX_NUM = 99999999
    # 加算する
    total += num
    if total > MAX_NUM:
        raise OverMaxError

    # 戻り値にする
    return total


total = 0
while True:

    ch = input("数字を入力してください（やめるときは０）：")
    try:
        num = int(ch)
    except ValueError as e:
        print("ValueError: 数字を入力してください")
        continue
    if num == 0:
        print("終了します。")
        break

    try:
        total = add_num(total, num)
    except OverMaxError as e:
        print("OverMaxError, プログラムを終了します。")
        break
    print(f"現在の合計値は{total}です。")
    print(f"-------------")
