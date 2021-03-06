# 演習４－ａ
# まず、gachar.pyにGachaクラスを作成して下さい。
# Gachaクラスの内容はgacha.pyに書いてあります。
#
# 下記のコメントに沿って、プログラムを完成させて下さい。
# プログラムが必要な箇所には
# pass # ここにプログラムを追加
# と書いてあります

# Gachaクラスをインポートする
from gacha import Gacha # ここにプログラムを追加

# Gachaクラスのインスタンスを以下の３つ作成します
# name：きつきつガチャ、percent：1
# name：まぁまぁガチャ、percent：5
# name：ゆるゆるガチャ、percent：25
gacha1 = Gacha("きつきつガチャ", 1) # ここにプログラムを追加
gacha2 = Gacha("まぁまぁガチャ", 5) # ここにプログラムを追加
gacha3 = Gacha("ゆるゆるガチャ", 25) # ここにプログラムを追加


# 以下の処理をずっと繰り返す
while True:
    # どのガチャを引くかユーザに聞く
    print("どのガチャを引きますか？「0:終了」「9:天井情報表示」")
    num = int(input("「1:きつきつ」「2:まぁまぁ」「3:ゆるゆる」："))
    # 0が入力された場合、ガチャを終了する
    if num == 0:
        print("ガチャを終了します")
        break

    # 9が入力された場合、クラスメソッドの info_tenjo を実行し、
    # 次のガチャをどうするか聞く（continueする）
    if num == 9:
        Gacha.info_tenjo() # ここにプログラムを追加
        continue

    # 1から3が入力された場合、数字に合わせたインスタンスの、
    # roll_gacha を実行する
    if num == 1: # ここにプログラムを追加
        gacha1.roll_gacha()
    elif num ==2: # ここにプログラムを追加
        gacha2.roll_gacha()
    elif num ==3: # ここにプログラムを追加
        gacha3.roll_gacha()

    # クラスメソッドの is_tenjo を実行し戻り値をもらう
    # 戻り値が true の場合「たなばたのプレゼント！レアをもらいました！」
    # と表示して、クラス変数の no_rare_count を０にする
    T_flag = Gacha.is_tenjo() # ここにプログラムを追加

    if T_flag == True:
        print(f"たなばたのプレゼント！レアをもらいました！")
        Gacha.no_rare_count = 0
        break
