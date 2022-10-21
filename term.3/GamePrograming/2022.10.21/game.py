# ゲームの基本情報クラス
class Game:

    # ========== クラス定数 ==========
    WIDTH = 12  # フィールドの横のサイズ（10 + 両端の壁）
    HEIGHT = 22  # フィールドの縦のサイズ（21 + 下の壁）
    # 各ブロックの色リスト
    COLORS = (
        (0, 0, 0),  # 枠内
        # 7種類のブロック
        (255, 165, 0),
        (0, 0, 255),
        (0, 255, 255),
        (0, 255, 0),
        (255, 0, 255),
        (255, 255, 0),
        (255, 0, 0),
        (128, 128, 128),  # 外枠
    )

    # ========== クラス変数 ==========
    surface = None  # 表示するウィンドウ
    field = None  # ブロックが置かれるフィールド（２次元のデータ）
    now_block = None  # 現在操作中のブロック
    next_block = None  # 次に出てくるブロック
    interval = 40  # ゲームスピードの間隔
    count = 0  # ゲームカウンタ
    score = 0  # スコア
    is_gameover = False  # ゲームオーバーフラグ

    # ========== クラスメソッド ==========
    # ゲームオーバーチェック
    @classmethod
    def check_gameover(cls):
        filled = 0  # 一番上の列にあるブロックの数
        # 一番上の列にあるブロックを数える
        for cell in Game.filled[0]:
            if cell != 0:
                filled += 1
        # 2を超えていたらゲームオーバーにする(左右の壁で最低2はあるため)
        cls.is_gameover = True if filled > 2 else False

    # ========== クラス定数 ==========
    # 各ブロックのデータ: 3次元データ
    # 3x3のブロック 0: ブロック無し 0<=: ブロック有り
    # 種類: 回転させた時のブロックの描画
    BLOCK_DATA = (
        (
            (0, 0, 1, 1, 1, 1, 0, 0, 0),
            (0, 1, 0, 0, 1, 0, 0, 1, 1),
            (0, 0, 0, 1, 1, 1, 1, 0, 0),
            (1, 1, 0, 0, 1, 0, 0, 1, 0),
        ),
        (
            (2, 0, 0, 2, 2, 2, 0, 0, 0),
            (0, 2, 2, 0, 2, 0, 0, 2, 0),
            (0, 0, 0, 2, 2, 2, 0, 0, 2),
            (0, 2, 0, 0, 2, 0, 2, 2, 0),
        ),
        (
            (0, 3, 0, 3, 3, 3, 0, 0, 0),
            (0, 3, 0, 0, 3, 3, 0, 3, 0),
            (0, 0, 0, 3, 3, 3, 0, 3, 0),
            (0, 3, 0, 3, 3, 0, 0, 3, 0),
        ),
        (
            (4, 4, 0, 0, 4, 4, 0, 0, 0),
            (0, 0, 4, 0, 4, 4, 0, 4, 0),
            (0, 0, 0, 4, 4, 0, 0, 4, 4),
            (0, 4, 0, 4, 4, 0, 4, 0, 0),
        ),
        (
            (0, 5, 5, 5, 5, 0, 0, 0, 0),
            (0, 5, 0, 0, 5, 5, 0, 0, 5),
            (0, 0, 0, 0, 5, 5, 5, 5, 0),
            (5, 0, 0, 5, 5, 0, 0, 5, 0),
        ),
        ((6, 6, 6, 6), (6, 6, 6, 6), (6, 6, 6, 6), (6, 6, 6, 6)),
        (
            (0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0),
            (0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 7, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0),
        ),
    )
