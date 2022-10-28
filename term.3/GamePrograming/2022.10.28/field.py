import random
from game import Game
from chip import Chip

# フィールドクラス（マップの１画面分のクラス）
class Field:

    # コンストラクタ
    def __init__(self, map_no):
        self.chip_list = None  # フィールドのチップのリスト
        self.map_no = map_no  # マップ番号
        self.read_map_info()  # マップ番号に対応した情報を設定

    # フィールド情報を読み込み
    def read_map_info(self):
        # 表示用のマスのリストを作成（初回のみ）
        if self.chip_list == None:
            # チップクラスのインスタンスをチップ数作成
            self.chip_list = [[Chip() for _ in range(Game.FIELD_WIDTH)] for _ in range(Game.FIELD_HEIGHT)]
            # チップリストの数だけ２重ループ
            for pos_y in range(Game.FIELD_HEIGHT):
                for pos_x in range(Game.FIELD_WIDTH):
                    # 位置と初期画像を指定
                    self.chip_list[pos_y][pos_x].set_pos(pos_x, pos_y)
                    self.chip_list[pos_y][pos_x].set_chip_no(0)

        # フィールド情報の設定
        new_field = Field.MAP_LIST[self.map_no]
        # チップリストの数だけ２重ループ
        for pos_y in range(Game.FIELD_HEIGHT):
            for pos_x in range(Game.FIELD_WIDTH):
                # フィールドの該当位置の情報を設定
                self.chip_list[pos_y][pos_x].set_chip_no(new_field[pos_y][pos_x])

    # フィールドチェンジ（移動方向をfld_x, fld_yのプラスマイナス１でもらう）
    def change_field(self, fld_x, fld_y):
        pass  # フィールド数
        # 左右に移動した場合は１を足す／引く
        # ただし、移動後の位置が上下のフィールドになってしまう場合は調整する
        # （移動前後のフィールドの段がずれる場合：１始まりなので１を引いてから割って比較）
        pass
        # フィールドの横の数－１だけ、逆方向に移動
        pass
        # 上下に移動した場合は３（横マップ数）を足す／引く
        pass

        # フィールド数を超えた場合は、マップ数を引く
        pass
        # ０以下になった場合は、マップ数を足す
        pass
        # フィールド情報を読み込み
        pass

        # モンスターの再配置
        pass
        # マスのピッタリの位置に配置する
        pass
        # 配置できるまでループする（100回で諦める）
        pass
        # プレイヤーが端からくるので、端には配置しない
        pass
        # モンスターが移動できない位置に配置されてしまった場合はやり直し
        pass
        # 移動できる位置ならそこに配置
        pass

    # 移動可能チェック
    def check_movable(self, pos_list, unmovable_chip_list):
        # チェック対象だけ繰り返し
        pass
        # １つでも移動不可ならFalseを返却
        pass
        # すべての対象チップが移動可能な場合はTrueを返却
        pass
        return True

    # 画面に描画
    def draw(self):
        # チップリストの数だけ２重ループ
        for y in range(Game.FIELD_HEIGHT):
            for x in range(Game.FIELD_WIDTH):
                self.chip_list[y][x].draw()

    # クラス変数：マップ情報
    MAP1 = (
        (3, 3, 3, 0, 0, 0, 0, 0, 2, 2),
        (3, 0, 0, 0, 1, 1, 0, 2, 2, 2),
        (3, 0, 0, 0, 0, 1, 0, 2, 2, 2),
        (0, 0, 0, 0, 0, 1, 0, 2, 2, 2),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 3, 0, 1, 1, 1, 0, 0, 0),
        (0, 3, 3, 3, 0, 0, 0, 0, 0, 0),
        (0, 0, 3, 3, 3, 0, 0, 0, 0, 0),
    )
    MAP2 = (
        (2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (2, 0, 0, 1, 1, 1, 0, 0, 0, 0),
        (2, 0, 1, 0, 0, 0, 1, 0, 0, 0),
        (2, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 2),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 2),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 3),
        (0, 0, 0, 0, 1, 0, 0, 0, 0, 3),
        (0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
        (0, 3, 3, 0, 0, 0, 0, 0, 0, 3),
    )
    MAP3 = (
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 3),
        (0, 0, 0, 1, 1, 1, 1, 0, 0, 3),
        (0, 0, 1, 0, 0, 0, 0, 1, 0, 3),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
        (2, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (2, 0, 0, 0, 0, 0, 0, 1, 0, 0),
        (3, 0, 1, 0, 0, 0, 0, 1, 0, 0),
        (3, 0, 0, 1, 1, 1, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (3, 3, 3, 3, 2, 2, 0, 0, 0, 0),
    )
    MAP4 = (
        (0, 0, 3, 3, 3, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 3),
        (0, 0, 1, 0, 0, 0, 1, 0, 0, 3),
        (0, 0, 1, 0, 0, 0, 1, 0, 0, 3),
        (2, 0, 1, 0, 0, 0, 1, 0, 0, 0),
        (2, 0, 1, 1, 1, 1, 1, 0, 0, 0),
        (2, 2, 0, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 2, 2, 2, 0, 1, 0, 0, 0),
        (0, 2, 2, 3, 2, 3, 0, 0, 0, 0),
    )
    MAP5 = (
        (0, 2, 2, 0, 0, 0, 0, 0, 0, 3),
        (3, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (3, 3, 1, 1, 1, 1, 1, 0, 0, 0),
        (3, 0, 1, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 0, 0, 0, 2),
        (0, 3, 3, 0, 0, 0, 0, 2, 2, 2),
    )
    MAP6 = (
        (3, 3, 2, 2, 2, 2, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
        (0, 0, 1, 0, 0, 0, 2, 2, 2, 0),
        (0, 0, 1, 0, 0, 0, 0, 0, 2, 2),
        (0, 0, 1, 1, 1, 1, 1, 0, 0, 2),
        (0, 0, 1, 0, 0, 0, 0, 1, 0, 2),
        (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
        (2, 0, 0, 1, 1, 1, 1, 0, 0, 0),
        (2, 0, 0, 0, 0, 2, 3, 3, 0, 0),
    )
    MAP7 = (
        (0, 2, 2, 2, 2, 2, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 1, 1, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
        (3, 3, 3, 0, 0, 0, 0, 0, 2, 3),
    )
    MAP8 = (
        (0, 3, 3, 0, 0, 0, 0, 2, 2, 2),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    )
    MAP9 = (
        (2, 0, 0, 0, 0, 2, 3, 3, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
        (0, 3, 3, 1, 1, 0, 0, 0, 0, 0),
        (0, 3, 3, 3, 2, 2, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 3),
    )

    MAP_LIST = (0, MAP1, MAP2, MAP3, MAP4, MAP5, MAP6, MAP7, MAP8, MAP9)
