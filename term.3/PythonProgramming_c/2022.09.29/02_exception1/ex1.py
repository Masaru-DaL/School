# 演習１
# 1～12のキーと月の英語名が格納された辞書型「ENGLISH_MONTHS」があります。
ENGLISH_MONTHS = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

# 1～12が入力されたらその月の英語名を
# 「"Ｘ月は英語でYYYYYYです。" と出力するプログラムを作ります。
#
# １）入力と出力はずっと繰り返します。「0」が入力されたら終了します。
try:
    while True:
        num = input("1~12を間の数字を入力してください：")
        if num == 0:
            break
        print(num + "月は英語で" + ENGLISH_MONTHS[num] + "です")
except KeyError as e:
    print(f"入力された文字{e}に対応する月が見つかりませんでした。")  # eには入力された情報が入ってくる
else:
    print("0が入力されたので終了します。")
finally:
    print("プログラム終了")


# ２）辞書型では該当するキーが無いと「KeyError」が発生します。
#     例外処理を入れて「入力された文字eに対応する月が見つかりませんでした。」
#     と出力してプログラムを終了してください。
#     このeは、KeyError を as で別名にしたエラー内容としてください。
# ３）正常に終了した場合「0が入力されたので終了します。」と出力してください。
#     これには try に対応した else 文を使用してください。
# ４）正常終了でも例外終了でも、最後に「プログラム終了。」と出力してください。
#     これには try に対応した finally 文を使用してください。
#
# ヒント：0で終了する処理を考えると、例外処理は、while文の外側で
#        囲うようにしたほうがプログラムを作りやすいと思います。