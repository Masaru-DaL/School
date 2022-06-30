# 演習１
# まず、monster.pyにMonsterクラスを作成して下さい。
# Monsterクラスの内容はmonster.pyに書いてあります。
#
# 続いて、このプログラムファイルに以下の処理を書きます。
# １）Monsterクラスをインポートする
# ２）Monsterクラスのインスタンスを作る
# ３）作ったインスタンスのset_name関数で、モンスター名を設定する
# ４）作ったインスタンスのset_level関数で、モンスターのレベルを設定する
# ５）作ったインスタンスのappear関数で、
#     引数に出現数を設定して、モンスターを登場させる


from monster import Monster

hiyoko = Monster()
hiyoko.set_name("ひよこ")
hiyoko.set_level(10)
hiyoko.appear(3)
