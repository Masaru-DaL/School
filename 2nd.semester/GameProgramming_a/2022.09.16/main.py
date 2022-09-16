import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from random import randint

# タイルの横方向、縦方向の数
TILE_COUNT_X = 20
TILE_COUNT_Y = 15
# タイルの幅、高さ
TILE_WIDTH = 50
TILE_HEIGHT = 50
# 設置する爆弾の数
SET_BOMB_COUNT = 20
# タイルの状態（空、爆弾、オープン済み）
TILE_STATUS_EMPTY = 0
TILE_STATUS_BOMB = 1
TILE_STATUS_OPENED = 2
# 数字表示用の文字リスト
DISP_NUMBERS = ["","１","２","３","４","５","６","７","８"]
# クリア、ゲームオーバーのメッセージ
MSG_CLEAR = "クリアー！"
MSG_GAMEOVER = "ゲームオーバー"
# 各描画の色
COLOR_BG = (0, 0, 0)
COLOR_TILE = (192, 192, 192)
COLOR_LINE = (96, 96, 96)

COLOR_NUM = (255, 255, 0)
COLOR_BOMB = (255, 100, 100)
COLOR_MSG_CLEAR = (0, 0, 255)
COLOR_MSG_GAMEOVER = (255, 0, 0)

open_count = 0  # オープン済みタイル数
# チェック済みタイルリスト（２重のリスト）をすべて「False」で作成する
checked_tiles = [[False for x in range(TILE_COUNT_X)] for y in range(TILE_COUNT_Y)]

# Pygameの初期化処理等
pygame.init()
surface = pygame.display.set_mode([TILE_WIDTH * TILE_COUNT_X, TILE_HEIGHT * TILE_COUNT_Y])
clock = pygame.time.Clock()

# -------------- 周囲の爆弾の数を数える --------------
def count_bombs(field, x_pos, y_pos):
    pass

# -------------- タイルのオープン処理 --------------
def open_tile(field, x_pos, y_pos):
    pass

# -------------- メイン処理 --------------
def main():
    # フォントを２種類用意
    # 日本語フォントを使うためには、SysFont ではなくFontで、
    # フォントファイルの置いてあるパスを指定します
    # ゲームを配布する場合は、フォント（配布可能なもの）も合わせて配布すると良いでしょう
    # 参考サイト例（https://helpx.adobe.com/jp/x-productkb/global/cq08041028.html）
    # small_font = pygame.font.Font("C:/Windows/Fonts/meiryo.ttc", 42)
    # large_font = pygame.font.Font("C:/Windows/Fonts/meiryo.ttc", 120)
    small_font = pygame.font.Font("C:/Windows/Fonts/HGRGY.TTC", 42)
    large_font = pygame.font.Font("C:/Windows/Fonts/HGRGY.TTC", 120)
    msg_clear = large_font.render(MSG_CLEAR, True, COLOR_MSG_CLEAR)
    msg_gameover = large_font.render(MSG_GAMEOVER, True, COLOR_MSG_GAMEOVER)
    # ゲームオーバーフラグの初期値をFalseにする
    is_gameover = False
    # フィールドの情報リスト(2重リスト)をすべて「空」で作成する
    field = [[TILE_STATUS_EMPTY for x in range(TILE_COUNT_X)] for y in range(TILE_COUNT_Y)]

    ###### 爆弾設置処理 ######

    ###### メイン繰り返し処理 ######
    while True:

        ### イベント処理 ###
        for event in pygame.event.get():
            # 終了イベント処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ### 描画 ###
        surface.fill(COLOR_BG)

        for ypos in range(TILE_COUNT_Y):
            for xpos in range(TILE_COUNT_X):
                # その位置のタイルの情報を取得
                tile_status = field[ypos][xpos]
                # タイル描画用の四角形情報(四角形の左上のx座標、四角形の左上のy座標、縦幅、横幅)
                rect = (xpos * TILE_WIDTH, ypos * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
                # タイルが「空」か「爆弾」の場合
                if tile_status == TILE_STATUS_EMPTY or tile_status == TILE_STATUS_BOMB:
                    # タイルを描画する(画面、色、位置)
                    pygame.draw.rect(surface, COLOR_TILE, rect)
                    # ゲームオーバーで、タイルが「爆弾」の場合
                    if is_gameover and tile_status == TILE_STATUS_BOMB:
                        # 爆弾を描画
                        pygame.draw.ellipse(surface, COLOR_BOMB, rect)

        # 線の描画: 縦線
        for index in range(0, TILE_COUNT_X * TILE_WIDTH, TILE_WIDTH):
            pygame.draw.line(surface, COLOR_LINE,
                            # TILE_COUNT_Y * TILE_HEIGHT -> 15*50(定数値)
                            (index, 0), (index, TILE_COUNT_Y * TILE_HEIGHT))

        # 線の描画: 横線
        for index in range(0, TILE_COUNT_Y * TILE_HEIGHT, TILE_HEIGHT):
            pygame.draw.line(surface, COLOR_LINE,
                            # TILE_COUNT_X * TILE_WIDTH -> 20*50(定数値)
                            (0, index), (TILE_COUNT_X * TILE_WIDTH, index))

        # ゲームオーバーの場合
        if is_gameover:
            # メッセージ領域の四角形を取得し、その中央の位置を設定する
            msg_rect = msg_gameover.get_rect()
            msg_rect.center = (TILE_COUNT_X * TILE_WIDTH / 2, TILE_COUNT_Y * TILE_HEIGHT / 2)
            surface.blit(msg_gameover, msg_rect.topleft)

        # 画面の更新
        pygame.display.update()
        # 一定周期での繰り返し
        clock.tick(15)

# メイン関数の呼び出し
if __name__ == '__main__':
    main()
