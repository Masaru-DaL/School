# 2022.04.12.Computer System
- テクノロジー分野の学習

・基本情報技術者試験ドットコム
https://www.fe-siken.com/
・ITパスポート試験ドットコム
https://www.itpassportsiken.com/

- 基本情報技術者試験は年々必須科目が増えているため、早めに受ける事が推奨
  - 午前試験 / 午後試験
  - プログラミング・アルゴリズム必修
  - データ構造及びアルゴリズム必修

# 基本情報合格教本
- 勉強法
  - こういう勉強法もあり
    - 試験はこう出る
    - 出題分析
      - を攻める
  - 参照ページを見ながら勉強する方法がおすすめ
  - 計算が苦手の場合
    - 501p～ 計算問題の実践攻略
  - インプットとアウトプットのバランスが大事
- 章末まとめ問題
  - 電子媒体は最新じゃないのでドットコムサイトで補強したほうが良い
  - 解説もドットコムのほうが優しい
- 苦手分野を克服すれば合格の可能性は上がる！
  - 苦手分野にフォーカスして攻めていくのもあり

### プログラミング的思考とは
- 自分が意図する一連の活動を実現するためには、どんな動きの組合せが必要かを論理的に考える力のことです。 アルゴリズムは、組み立てた動きをなんらかの形にしたもの

### アルゴリズム
- 知識レベルで解けない設問もありますが、トータルでみると その時点の、その人の『考える力』が、どれぐらい養われているかを図るために出題される

### データ構造とは
- コンピュータ上にデータを格納する論理構造のこと
- 様々なデータ構造が存在するが、用途に応じてどれを選ぶかが重要

# アルゴリズムと流れ図
- 流れ図
  - ※フローチャートのこと

- アルゴリズム
  - 処理の手順を表したもの
    - 順番に処理が行われるように1つ1つ必要な処理を記述していく
  - 論理が正しく行われているかしっかりと検証する必要がある
  - 表現には、流れ図や疑似言語などが使われる

## フローチャートと疑似言語
- フローチャート
  - ボックスと矢印を用いて表現する
  - プログラムの開始と終了の間に処理を記述し、流れを表現する

- 疑似言語
  - 午後試験で使われる(ITパスポートで使われる)
    - 流れ
      - プログラムの名前を入れる
      - 型付け
      - 開始と終了は書かない
        - 下に行ったら終わり
  - テキストベースで処理の流れを表現する
  - 「・」を先頭に付ける
  - インデントを揃える(分岐があった場合を考える)
  - 試験用に作られた言語
  - 分岐の書き方
    - プログラム名称(駅)の下に条件式(条件式: 本屋に用事がある？)を入れる
    - 条件に合う場合(YES)の処理を下に書く
    - 真ん中に線を入れて、上下で分岐を分け、下側にNOの場合の処理を書く
    - YES, NOの処理の共通項目で分岐を合体させる
    - 最終的なゴールを記述する

- フローチャートと疑似言語
  - 考え方は同じ
  - 表現の仕方が違う
    - フローチャート
      - 分かりやすい
      - 表現が長くなりやすい
    - 疑似言語
      - 分かりにくい(視覚的)
      - 字列だけ書くため短く表現できる

- 順次処理 / 分岐処理
  - 順次処理
    - 順番に処理を行っていく
  - 分岐処理
    - 特定の条件に応じて処理を分岐していく
    - if文
      - 条件に応じて処理を行った結果、行わない処理がある場合もある

## アルゴリズムの基本と流れ図
- アルゴリズムの基本
  - 順次構造
    - 上から下へと順番に処理が行われる
  - 選択構造
    - 分岐
    - 条件によって次に行う処理を選択する
  - 繰り返し構造
    - 処理を何回か繰り返し行う
      - あるいは条件がクリアするまで繰り返す
    - 同じ処理を繰り返す

- 流れ図
  - アルゴリズムを表現する、もっとも一般的な手法
    - 端子
      - 角を丸める
      - border radius
    - 処理
      - 長方形
    - 定義済み処理
      - 関数
      - ほかの場所で定義された処理
      - 長方形の左右に縦に1本線
    - 判断
      - 記述された条件によってかえる
      - 菱形
    - 入出力
      - ゆがんだ長方形
    - ループ端記号
      - 台形
        - 上向き台形でスタート、下向き台形でエンドとする
      - 入れ子のループ処理
        - 繰り返しの中に繰り返しがあるなどで分かりづらくなる、見づらくなるなどの理由で使われる
        - 例: ループ1の中にループ2がある時など

# アルゴリズム
### 線形探索
### ハッシュ探索
- ハッシュ値

### 整列のアルゴリズム
- ソートと付く
  - ☆選択法
    - 基本法
      - 選択ソート
    - 改良法
      - ヒープソート
  - ☆交換法
    - 基本法
      - バブルソート
    - 改良法
      - シェーカーソート
      - クイックソート
        - 一番速い
        - これより速いアルゴリズムが見つけられたら歴史に名前を残せる
  - ☆挿入法
      - 基本法
        - 挿入ソート
      - 改良法
        - シェルソート

### 整列とは？どうやって探す？
- 並び替えしてあるほうが速いよね
  - どうやって並び替えするの？
    - PCのメモリ空間で処理を行う
    - データの入れ替え(交換)が必要
    - 例: AとBのデータを交換する場合、一時的に置く場所が必要
    - = 一時的な格納領域が必要 --> TMPと付けられる(慣習)
      - [A <--> B を交換する場合] + [□(データを交換する為の領域)]
      - メモリ空間では切り取りは出来ない、コピペのみ

# データの管理とファイルシステム
## ディレクトリ管理
- ファイルの概念
  - 単なるビット列の集まりとして扱われる
  - ディレクトリという階層構造を持つ仕組みで管理される
    - ルートディレクトリ
      - 最上位階層
      - (/)
      - Windowsでは見れない？(Git Bashで移動可)
      - 最初に入った先がルート
    - サブディレクトリ
      - ディレクトリの直下のディレクトリ
      - 親子階層
    - カレント
      - 現在いるディレクトリ
      - (~)

- パスの指定
  - Window -> \
    - コマンドプロンプト
      - 現在のフォルダの詳細 -> dir (directory) = ls
      - 移動 -> cd (change directory)
  - UNIX系 -> /
    - 絶対パス
      - ルートから見た時のパスを指定する
    - 相対パス
      - カレントから見た時のパスを指定する
    - ../ or ..\
      - 1個上の階層を指定する

- PCのファイルシステムの役割
  - アプリケーションプログラムが，ハードディスクやDVDなど記憶媒体の違いを意識しなくてもファイルにアクセスできるように，統一したインタフェースを提供する。

# IoTとは？
- アイオーティーと、発音
- Internet of Things
- 今までインターネットにつながらなかったモノがつながるようになる技術
  - 建築業
    - 人員不足と労働そのものの危険性にIoT技術が利活用される
  - 物流生産
    - IoTの他にAIやビッグデータの活用
    - 労働生産性の向上　2割向上の目標
  - 交通機関
    - 運行管理の取り組み
    - 不確定要素で運行が左右される為、ロケーションサービスが活用される
      - 運行状況を可視化して配信する
  - マーケティング
    - デジタルマーケティングの進化
    - ネット通販の拡充化、購買促進
    - ビッグデータが行きかうことになる
      - 購買行動の把握、対話データなどを利活用する
  - 医療や介護の産業現場でも活用される
    - 高齢者が介護を必要している現場
    - 人材不足　さらに介護職員の負担が増えることが予想される
      - バイタルセンサーを利用した見守りシステム
      - 専用機器を利用した排泄予知システム
      - 入浴介助を行うロボット、ケアプランの作成をするAI
    - 医療現場 地域医療の格差の社会問題
      - 遠隔の対面診療、画像診断
      - 聴診器を遠隔で聴ける状況に
      - 医療スタッフの慢性的な不足にテクノロジーの導入で解決を図る
      - 処方ミス、医療ミスなどの人的なミスをケア
      - 動物の健康を管理するIoT機器
        - 餌やり、健康管理など
  - 家庭におけるIoT化
    - スマートロック
    - スマートフォンで操作するIoT家電の増加
    - スマートハウスや、小型ロボット
- 取り巻く環境の急激な変化
  - 人を介して実空間とサイバー空間を行き来する
  - 何もないところからモノを創造する難しさ