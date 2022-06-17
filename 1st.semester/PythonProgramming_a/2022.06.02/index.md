# テスト用復習
- quit()
  - インタラクティブモードの終了
- //
  - 余りなし
- ()
  - 計算の優先

- 変数 (_)
  - 一つ前の計算結果
    - _ * 4 =
  - 変数への代入
    - 文字列はクォーテーションで囲む
    - a = 'apple'

- 文字列
  - クォーテーションの使用
    - 別のクォーテーションで囲むか、\(バックスラッシュ)を先に付ける
  - 文字列の結合
    - 固定文字列(変数に入ってない文字列のこと)
    - 'py' "thon" (+を必要としない)
      - python
    - 変数は＋が必要

- print
  - 標準出力(ターミナル)
    - 関数

- int(整数型)
- float(小数点型)
- str(文字列型)

- 命名規則
  - 数字から初めてはいけない
  - pythonで命令で使う文字は使えない
    - if, forなど
- コメントアウト
  - #

- 引数
  - input(), print() などの()の中に書くもの

- 優先順位 >
  - **, +n-n, * / // %, +-
    - -3 ** 4 -> -81
    - (-3) ** 4 -> 81
    - or 変数に-nを代入

- 条件分岐
  - if, else, elif
    - elifはいくつでも書くことが可能
  - インデントを下げる

- ブール型
  - true or false
  - 比較演算子
    - ==
      - 等しい
    - !=
      - 等しくない
  - 論理演算子
    - and or not

- ループ文
  - while
    - 条件に当てはまっているまで繰り返す
  - for
- range
  - (1, 10)
    - 1つ目から10の1個手前まで
  - (1, 10, 3)
    - 1つ目から10の1個手前まで3回繰り返す
- break, continue, pass
  - break
    - そこに来ると終了
  - continue
    - 1つスキップさせる
  - pass
    - 何もせず終了

- append
  - 追加
- pop
  - 取り出し
- index
  - 要素が何番目か
- remove
  - 指定した値と同じ要素を検索し、最初の要素を削除できる
  - 削除
  - list_a.remove("c")
- sort
- reverse
  - 逆ソート
- del
  - del list_a[2]
  - インデックス番号を指定する
- in
  - リストに要素があるかどうか判断する演算子
    - true, false
    - in list_a[]

- 文字列の変更は不可
  - popなどは使えない

- for eto in eto_list
  - 干支リストにある要素の分だけ繰り返す

- タプル
  - リストとは違って後から要素の変更ができない
  - a =(x)
- 集合型(セット)
  - 重複する値が1つになる
  - 順序が不定
  - a = {x}
- 辞書型
  - key, value
  - a = {x:1, y:2}
  - sorted
  - items()
    - keyと値をセットでループ

- アルゴリズム
  - 問題を解決するための計算方法や処理方法
- フローチャート
  - アルゴリズムを図式化し、資格的にわかりやすく表したもの

- 順次構造
  - 長方形
- 選択構造
  - 条件分岐
  - ひし形
- 反復構造
  - 繰り返し
  - 台形で挟む

- print
  - ,で区切ることで何個も出力できる
  - sep
    - 要素と要素の間の処理
  - end
    - 要素の最後の処理

- スタックとキュー
  - スタック
    - LIFO
      - Last In First Out
    - プッシュ、ポップ
    - append(), pop()
  - キュー
    - FIFO
      - First In First Out
    - エンキュー、デキュー
    - append(), pop(0)

- 関数
  - def my_print(引数を指定):
    - インデントで記述した部分が引数
  - 使い場所より上に定義
  - 引数の順番が重要
  - return
    - 途中で終了させる
    - 戻り値
      - returnの後ろに返したい値を書く

- ローカル変数
  - 関数の中でのみ使用できる変数
- グローバル変数
  - 関数の外でも中でも使用できる変数

- モジュール
  - ファイル名.py から.pyを除いた形で指定
  - import モジュール名
  - ファイル名.関数名
  - from モジュール名 import 関数名

- 標準モジュールライブラリ
  - sys
  - プロンプトの種類が出る
- 組み込み関数
  - dir()
  - 指定モジュールが定義している名前の一覧が表示される

- 再起呼び出し
  - 自分自身の関数を実行