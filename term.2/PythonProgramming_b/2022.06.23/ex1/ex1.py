# osモジュールのインポート
import os
##########################################################
# 空のファイルを作る関数
# ※中身はまだ理解する必要はありません
def make_file(path):

    if os.path.isfile(path):
        print("エラー！！ すでにファイルが存在します！")
        return

    try:
        f = open(path, 'w')
        f.close()
    except:
        print("エラー！！ ファイルを作れませんでした！")
##########################################################

# 演習１（１）
# このex1フォルダにあるex1.pyを実行して、
# ex1フォルダ内にtext.txtを作って下さい。
# プログラムの内容自体は、makefile.pyと同じです

# 演習１（２）
# ファイル名にフォルダ表記を追加して、
# test8フォルダにtext.txtを作って下さい。

# 演習１（３）…やや難問
# 上記まで出来たら、「絶対パス」でフォルダを指定して、
# test9フォルダにtext.txtを作って下さい。

# make_file 関数で、ファイルを作成する


make_file("C:/Users/220093/Documents/YSE/2nd.semester/PythonProgramming_b/2022.06.23/test7/test.txt")
