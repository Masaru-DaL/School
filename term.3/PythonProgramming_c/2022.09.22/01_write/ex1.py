# 演習１
# このファイルがある上の階層の「09_output」のフォルダに、
# プログラムからファイルを作成して、
# 「任意のファイル名」で「任意の文章」を書き込んでください。
#
# プログラムを実行したら、その場所に指定の名前のファイルができ、
# 書こうとした内容がファイルに書かれていることを確認してください。

my_file = open("./folder2/myfile.txt", "w", encoding="UTF-8")

my_file.write("演習１用に\n書き込みました。")

my_file.close()
