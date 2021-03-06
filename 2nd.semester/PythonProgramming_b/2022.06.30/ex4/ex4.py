# 演習４
# まず、monster.pyにMonsterクラスを作成して下さい。
#　Monsterクラスの内容はmonster.pyに書いてあります。
#
# 下記のコメントに沿って、プログラムを完成させて下さい。
# プログラムが必要な箇所には
# pass # ここにプログラムを追加
# と書いてあります

# Monsterクラスとランダムモジュールをインポートする
from monster import Monster # ここにプログラムを追加
import random

# Monsterのインスタンスを以下の３つ作成します
# name：ドラゴン、HP：30、power：4
# name：スケルトン、HP：20、power：3
# name：スライム、HP：15、power：2
dragon = Monster("ドラゴン", 30, 4) # ここにプログラムを追加
skelton = Monster("スケルトン", 20, 3) # ここにプログラムを追加
slime = Monster("スライム", 15, 2) # ここにプログラムを追加

# 変数としてプレイヤーHPを用意し、初期値を60にする
player_hp = 60

# 以下の処理をずっと繰り返す
while True:
    # プレイヤーの攻撃力を「４～１０」の範囲ランダムで求め、変数に代入する
    atk = random.randint(4, 10)
    # 今回のプレイヤーの攻撃力を表示する
    print(f"今回のプレイヤーの攻撃力は {atk} です。")
    # どの敵を攻撃するかメッセージを出力する。
    print("どの敵を攻撃しますか？")
    # １：ドラゴン、２：スケルトン、３：スライムで、入力してもらう（数字以外のエラー処理は省略）
    no = int(input("１：ドラゴン、２：スケルトン、３：スライム："))
    # 選ばれた敵のインスタンスに対して、damege関数を、atkを引数にして実行する
    # ここにプログラムを追加
    if no == 1:
        dragon.damaged(atk)
    elif no == 2:
        skelton.damaged(atk)
    else:
        slime.damaged(atk)


    # このターンにプレイヤーが受けるダメージの変数を用意し、０を代入する
    p_damage = 0
    # それぞれの敵のインスタンスに対して、attack関数を実行する
    # それぞれ戻り値を、このターンプレイヤーが受けるダメージに加算する
    # 合計のダメージが分かるようにする
    p_damage = p_damage + dragon.attack() # ここにプログラムを追加
    p_damage = p_damage + skelton.attack() # ここにプログラムを追加
    p_damage = p_damage + slime.attack() # ここにプログラムを追加


    # このターンプレイヤーが受けるダメージが０の場合、
    # 敵はすべてやっつけているので、プレイヤーの勝利のメッセージを出して、
    # 繰り返しを終了する
    if p_damage == 0:
        print("敵をすべてやっつけた！ プレイヤーの勝利！！")
        break

    # プレイヤーのヒットポイントを、このターンに受けたダメージ分減らす
    player_hp -= p_damage
    # プレイヤーのヒットポイントが０以下になった場合、
    # プレイヤーの敗北のメッセージを出して繰り返しを終了する
    if player_hp <= 0:
        print("プレイヤーは負けてしまった……GAME OVER")
        break
    # プレイヤーのヒットポイントが残っている場合、受けたダメージと残りのHPを出力する
    print(f"{p_damage}点のダメージを受けた！（残りHP{player_hp}）")
