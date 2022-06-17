# 2022.05.10.ComputerSystem
# システム構成要素
この回ではシステムの性能指標となるクロックとクロック周波数について、そして言語処理ツールを学習します。
- 到達目標
  - プロセッサの実行時間に関する計算問題の過去問を解ける。
  - 言語処理ツールのさまざまを知り、当人なりに説明できる
  - 『変数』を利用して、フローチャートと疑似言語の『反復構造』を、読み書きできる。

## 出典：平成31年春期　問71 アルゴリズムとプログラミング　(全18問中6問目)
図1のように二つの正の整数A1，A2を入力すると，二つの数値B1，B2を出力するボックスがある。B1はA2と同じ値であり，B2はA1をA2で割った余りである。図2のように，このボックスを2個つないだ構成において，左側のボックスのA1として49，A2として11を入力したとき，右側のボックスから出力されるB2の値は幾らか。

11(A1)
49 % 11 = 5(A2)
11(A1) % 5(A2) = 1(B2)
答え -> (ア)1

## 出典：令和元年秋期 問70 アルゴリズムとプログラミング　(全18問中5問目)
大文字の英字から成る文字列の暗号化を考える。暗号化の手順と例は次のとおりである。この手順で暗号化した結果が"EGE"であるとき，元の文字列はどれか。

例1: FAXという英字を暗号化する
- 暗号化の手順
1. 表から英字を文字番号に変換する。
   1. F -> 5, A -> 0. X -> 23
2. 1文字目に1, 2文字目に2, n文字目にnを加算する。
   1. F -> 6(+1), A -> 2(+2), X -> 26(+3)
3. 26で割った余りを新たな文字番号とする。
   1. F -> 6(6%26), A -> 2(2%26), X -> 0(26%26)
4. 表から文字番号を英字に変換する。
   1. F -> G, A -> C, X -> A
   2. FAX -> GCAに変換される。

逆の手順でEGEを解読する。
1. 表から文字番号を英字に変換する。
   1. EGE -> 464
2. 26を足して26で割った余りを新たな文字番号とする。
   1. 464
3. 1文字目に1, 2文字目に2, n文字目にnを減算(加算の逆)する。
   1. 341
4. 表から英字を文字番号に変換する。
   1. DEB
答え -> (イ)

# 言語処理ツール
## ソフトウェア作成ツール 言語プロセッサ
- プログラム言語で記述したプログラム
  - 原始プログラム, ソースコード, ソースプログラム
  - -> コンピュータが実行できる機械語にする必要がある
1. 言語プロセッサ(言語処理プログラム)で原始プログラムを翻訳する
2. 機械語の目的プログラム(オブジェクトモジュール)を作成する
   1. 実行形式にするために、リンカ(連係編集プログラム)による工程が必要

### 言語プロセッサの種類
- アセンブラ(assembler)
  - アセンブラ言語を機械語命令に翻訳するプロセッサ
  - 原則として、アセンブラ言語の1命令が、機械語の1命令と対応する
- コンパイラ(compiler)
  - 高水準・手続き型言語で記述された原始プログラムを目的プログラムに翻訳するプロセッサ
  1. 字句解析
  2. 構文解析
  3. 意味解析
  4. 最適化
  5. コード生成
  - コンパイラの多くは、プログラムの実行を高速化する最適化機能(オプティマイズ)を持つ
- インタプリタ(interpreter)
  - 命令を1つずつ解釈し、そのつど翻訳しながら、即時に実行する
- ジェネレータ(generator)
  - RPG(Report Program Generator)に代表される非手続き型プログラムから、パラメータに従ってプログラムを自動生成する

### コンパイラによる実行工程
1. コンパイラによる翻訳作業
   1. プログラムに文法上のミス(文法エラー)があった場合
      1. 言語プロセッサがエラーメッセージを出力する
      2. 言語プログラムに戻る
      3. 修正する
      4. 再びコンパイラに掛ける
   2. 文法上のミスではなく、誤った動作をする場合(実行エラー)は、上記同様の処理が行われる
2. リンカによる結合編集作業
   1. コンパイラが翻訳作業の後、機械語の目的プログラムを出力するが、そのままでは実行できない
   2. コンピュータで動作させるためには、プログラムが参照している他のモジュールを結合するなどの作業が必要になる
   3. この2の作業を連係作業といい、これを行うのがリンカ(連携編集プログラム)
   4. 連携編集がエラーなく終了すると、実行形式のロードモジュール(実行ファイル)が出力される

- 動的リンキング
  - プログラムの実行時に必要となった共用ライブラリや、システムライブラリを動的に連携して使用する方法
  - このモジュールの集合を、動的リンクライブラリ(DLL)という

- ローダ
  - プログラムの実行時に、補助記憶装置などから実行形式のプログラムを主記憶装置へ組み込む役割を持つプログラム

### インタプリタによる実行工程
1. 目的プログラムを作らない(*プログラム全体を翻訳するのではない)
   1. 1命令ずつ取り出し
   2. 翻訳を行う
   3. 実行する
2. プログラムが未完成でも動作可能
   1. 完成したところまでをテスト的に実行させてみることができる
3. 実行速度が遅い
   1. 1命令ずつ処理するため、実行速度が遅い
   2. プログラムの規模が大きくなると効率が落ちる

## 出典：平成31年春期　問19 開発ツール　(全28問中1問目)
インタプリタの説明として，適切なものはどれか。
-> (ア)原始プログラムを，解釈しながら実行するプログラムである。

> インタプリタ(Interpreter)は、プログラム言語の処理系の1つで、実行時にソースコードを1文ずつ解釈しながらプログラムを実行していくソフトウェアです。これに対して、高水準語で記述されたソースコードを機械語などに一括して翻訳するソフトウェアをコンパイラ(Compiler)といいます。

> インタプリタ方式は、コンパイラ方式と比較してプログラムの実行速度が遅くなる傾向にありますが、開発時にプログラム作成とテストの繰返しを容易に行える利点があります。JavaScript、PHP、Pythonなどのプログラム言語がインタプリタ方式を採用しています。

## 出典：平成21年春期　問22 開発ツール　(全28問中17問目)
-> (ア)

## 出典：平成20年秋期　問38 開発ツール　(全28問中18問目)
動的リンクライブラリ(DLL)の特徴として，適切なものはどれか。
-> (イ)アプリケーションの実行中，必要になったときにOSによって連係される。

## 出典：平成22年秋期　問22 開発ツール　(全28問中14問目)
コンパイラによる最適化の主な目的はどれか。
-> (ア)プログラムの実行時間を短縮する。
> コンパイラは、高水準言語で書かれたソースプログラムを機械語にコンパイル(翻訳)し、プログラムを生成するソフトウェアです。
> コンパイルの手順は、1.字句解析、2.構文解析、3.意味解析、4.最適化、5.コード生成の順番で行われ、このうち最適化では、処理時間や使用するメモリ量が少なくなるようにプログラムを再編成します。
> 具体的には、
> - 累乗を乗算に、乗算を加算にする。(加算のほうが処理速度が速い)
> - 値の変わらない変数を定数にする。
> - ループを展開・関数のインライン展開。
> などの変換を行います

## 出典：平成23年秋期　問22 開発ツール　(全28問中11問目)
コンパイラにおける最適化の説明として，適切なものはどれか。
-> (ウ)
> コンパイラは、高水準語で記述されたソースコードを機械語などに一括して翻訳するソフトウェアです。
> コンパイラにおける最適化とは、そのプログラムが動作するコンピュータの設計・仕様に合わせて実行速度が速くなるような機械語に変換することをいい「不要な変数の省略」「関数のインライン展開」「レジスタ割当て」などの手法を用いることで、与えられたソースコードを最適化された機械語に変換します。

## 出典：平成16年春期　問44 開発ツール　(全28問中28問目)
次の文はある二つの言語処理系について記述したものである。Bと比べたAの利点を記述しているものはどれか。
A：高水準言語で作成されたプログラムを，中間言語，アセンブラ言語又は機械語で記述されたプログラムに翻訳する。
B：原始プログラム中の命令文を一文ずつ解釈し，実行する。
-> (ア)
> コンパイル方式では、コンパイルの過程でソースコードの最適化を行ってから実行ファイルを生成します。インタプリタでは、ソースコードを1行ずつ翻訳しながら実行するため処理の最適化は行われません。

## 出典：平成30年秋期　問20 開発ツール　(全28問中3問目)
リンカの機能として，適切なものはどれか。
-> (ウ)相互参照の解決などを行い，複数の目的モジュールなどから一つのロードモジュールを生成する。
> リンカ(Linker)は、複数個のコンパイル済みプログラムや、そのプログラムで使用するライブラリを連結・統合し、1つの実行可能なプログラムファイルとして出力するソフトウェアです。

## 出典：平成25年秋期　問55 オフィスツール　(全22問中12問目)
プログラムの実行方式としてインタプリ夕方式とコンパイラ方式がある。図は，データを入力して結果を出力するプログラムの，それぞれの方式でのプログラムの実行の様子を示したものである。a，bに入れる字句の適切な組合せはどれか。
-> (イ)
> インタプリタ方式とコンパイラ方式は次のような特徴をもっています。
> - インタプリタ方式
>   - ソースコードを1行ずつ解釈しながらプログラムを実行していく方式。一般にコンパイラによって作成される実行ファイル形式よりも解釈と実行が同時進行のため処理時間がかかる。
> - コンパイラ方式
>   - ソースコードを翻訳して、機械語の目的プログラム(実行ファイル／ロードモジュール)を生成する方式。
> aは、ソースプログラムの入力を受けてa自身が処理を実行しているのでインタプリタ、bは、ソースプログラムの入力を受けて目的プログラムを出力し、実際の処理はその目的プログラムが行っているのでコンパイラとわかります。

# ハードウエア・ヒューマンインタフェース
この回では、ハードウエアとヒューマンインタフェースについて学習します。
- 到達目標
  - ヒューマンインタフェースのコード設計を理解し、当人なりに説明できる。
  - マルチメディア技術の基礎的な計算問題を解ける。
  - あまり算(剰余算)を利用した処理を知り、疑似言語で再現できる。

## 出典：平成29年秋期　問58 情報デザイン　(全5問中1問目)
キーボード入力を補助する機能の一つであり，入力中の文字から過去の入力履歴を参照して，候補となる文字列の一覧を表示することで，文字入力の手間を軽減するものはどれか。
-> (イ)オートコンプリート
> オートコンプリートは、先頭の数文字を入力すると入力履歴から候補を探し出し自動的に表示する機能です。上手く活用すれば素早い入力が可能になるためユーザビリティが向上します。ブラウザやワープロソフトなどに搭載されています。

## 出典：平成29年秋期　問74 コンピュータ・入出力装置　(全30問中10問目)
停電や落雷などによる電源の電圧の異常を感知したときに，それをコンピュータに知らせると同時に電力の供給を一定期間継続して，システムを安全に終了させたい。このとき，コンピュータと電源との間に設置する機器として，適切なものはどれか。
-> (ウ)UPS
> UPS(Uninterruptible Power Supply，無停電電源装置)は、停電や落雷などによる突発的な電源異常が発生したときに、内部に蓄えた電力をサーバなどに一定時間だけ供給する役割をもつ機器です。電源の瞬断時にシステムを安全に終了する時間を与えたり、自家発電装置による電源供給までの間の「つなぎ」の役目を担ったりすることでシステムやデータを保護します。

## 出典：平成29年春期　問21 ハードウェア　(全60問中14問目)
変形を感知するセンサを用いると，高架道路などの状態を監視してメンテナンスすることが可能である。この目的で使用されているセンサはどれか。
-> (ウ)ひずみゲージ
> ひずみゲージは、物体のひずみを測定するためのセンサです。薄い絶縁体上にジグザグ形状にレイアウトされた金属の抵抗体(金属箔)が取り付けられた構造をしており、変形による電気抵抗の変化を測定することによりひずみ量に換算します。

- センサの種類
  - 光センサ
    - 光を検知して、電気信号に変換する
    - カメラの露出計、リモコン受信部、街灯など
  - 温度センサ
    - 湿度を検知する
      - 接触式と非接触式、湿度範囲によって分けられる
    - サーミスタ(感熱抵抗体)
      - 湿度上昇に対して抵抗が増加するもの
        - サーモスタットなどに利用
      - 湿度減少するもの
        - 電子体温計などに利用
  - 加速度センサ
    - 物体の動きや振動、傾きなどを検知する
  - ジャイロセンサ
    - 物体の回転(角速度)を検知する
    - スマホ、カーナビ、デジカメの手振れ補正などに利用
  - 磁気センサ
    - 磁気を検出するセンサ
    - 代表的なもの: ホール素子
    - 電流計、開閉検出、位置検出など多用途に利用
  - 圧力センサ
    - 物質間の力学エネルギーを検出
      - ひずみゲージ
        - 変形の検出、重要測定、強度測定などに利用される

- UPS(無停電電源装置) / 自家発電設備 [Uninterruptible Power Supply]
  - 停電や遮断に備えて、内部にバッテリを備えた装置のこと
  - システムを安全に停止させるなどが可能
  - 自家発電設備
    - 災害等により電力会社からの提供が途絶えたときに、エンジンやタービンを使って発電する設備のこと
    - 数十～数日に渡る発電が可能だが、提供はすぐに開始できないため、UPSなどと組み合わせて利用する

## 出典：平成27年秋期　問22:ハードウェア　(全60問中21問目)
機械式接点の押しボタンスイッチを1回押したときに，押してから数ミリ秒の間，複数回のON，OFFが発生する現象はどれか
-> (ウ)チャタリング
> チャタリング(chattering)とは、リレーやスイッチの接点が切り替わった際に、微細で非常に速い機械的振動によって、電気信号が断続を繰り返す現象です。
> PC用の古いキーボードを操作したとき、キーを一度押しただけなのに、複数回入力されることがある。あるいは、マウスのシングルクリックが、意図せずダブルクリックとして入力されてしまう。これは、接点の劣化によってチャタリングが発生し、細かいオンオフがキー入力と判定されるためです。

# ヒューマンインターフェース
## 人とコンピュータを結ぶ接点
- ヒューマンインターフェース
  - 人とコンピュータとの間を結ぶ入出力機器や入出力方式のこと

## GUIは「見ればわかる」インターフェース
- GUI(Graphical User Interface)
  - 一般的なOSで使われるアイコンやボタン、メニューなどを使って利用者が直感的に操作できるようなヒューマンインターフェースを指す

- ポップアップメニュー
  - 選択が必要になったとき、マウスカーソルのすぐ近くに出現するメニュー
  - デスクトップ上で右クリックしたときのメニューが代表的
- テキストボックス
  - 文字列などを直接入力
- チェックボックス
  - 複数の項目を選択できる
- ラジオボタン
  - 複数の項目から1つのみを選択
- リストボックス
  - 複数の項目をリスト表示し、その中の1つを選択
- プルダウンメニュー
  - 随時利用可能なメニュー
  - メニューバーから垂れ下がるように表示され、さらにサブメニューも付加できる
- スピンエディットボックス
  - 特定の値を増減させる

## 出典：平成31年春期　問24:ヒューマンインタフェース技術　(全7問中1問目)
GUIの部品の一つであるラジオボタンの用途として，適切なものはどれか。
-> (ウ)
> GUI(Graphical User Interface)とは、アイコンなどの画像とマウスなどのポインティングデバイスを使って、直感的な操作でコンピュータを操作することのできるユーザインターフェースのことです。
> ラジオボタン(Radio Button)は、"同意する／同意しない"のように、互いに排他的な複数の項目の中から1つだけを選択させる場合に使われるコントロールです。試験のマークシートをイメージするとわかりやすいでしょう。

## 出典：平成21年秋期　問26:ヒューマンインタフェース技術　(全7問中6問目)
頻繁に行う操作を効率よく行えるようにしたユーザインタフェースはどれか。
-> (ウ)ショートカットキー
> ショートカットキーとは、キーボードを使ってパソコンの操作を簡単に行うための機能です。 ショートカットキーを使用すると、キーボードから手を離してマウスに持ち替える必要がないので、文書の編集を行っている場合などに効率よく作業を行うことができます。
> Windowsでは、コピーがCtrl+C, 切り取りCtrl+X, 貼付Ctrl+Vが、文書編集などによく使用するショートカットキーです。OSのGUIに実装されているショートカットだけでなく、ソフトウェア開発者がアプリケーションの使用性を向上させる目的で独自に設定することもできます。

## コード設計
- コード設計
  - データを扱う際にはコード化を行うことで、入力の手間を省力化する
  - コンピュータ上でのデータ処理を行いやすくする
    - コード化は、将来も重複しない桁数を確保し、人にとっても認識できるような工夫が求められる

- 順番コード
  - データの発生順やアイウエオ順に一連番号を付けたいもの
  - 例: JIS都道府県コード
- 区分コード
  - 対称を一定のブロックに分け、その範囲内で付けたい一連番号
  - 例: JIS市区町村コード
- 桁別コード
  - 各桁に大・中・小分類などの意味を持たせたもの
  - 例: 勘定科目コード、職業分類コード
- 表意コード
  - 内容を表す略号
  - 例: JIS国名コード
- 合成コード
  - 上記コードを組み合わせて用いる

## ヒューマンインターフェース設計
人とコンピュータの接点として、もっとも一般的なのが文字や数字の入力や出力である。
ミスしにくいこと、見やすく分かりやすいことが設計に求められる。

- 項目のレイアウト
  - 視線は左から右、上から下に動くのが自然であり、項目の配置もこれに従う
  - 重要な項目は特別な色や
- メッセージガイド
  - 利用者に操作ミスの内容や対処方法を具体的に示す仕組み(エラーメッセージや警告音など)を用意する
- 操作性の標準化
  - 操作内容や画面の表示方法、使用する帳簿類を統一化する
  - 操作方法を画面上で調べられるオンラインヘルプの導入を検討する
- 操作環境
  - 初心者向けのメニューに加え、習熟者向けにキーボード入力によるショートカット操作などを用意する

### チェックディジットチェック
- 主にコード入力に用いる
  - 例: スーパーで手打ちで打つなど
- チェックディジットチェック
  - あらかじめコードの末尾に、コードから計算によって求めたチェック用の桁のこと

## 出典：令和元年秋期　問23:インタフェース設計　(全17問中1問目)
コードから商品の内容が容易に分かるようにしたいとき，どのコード体系を選択するのが適切か。
-> (ウ)表意コード
> 表意コードは、ニモニックコード(Mnemonic Code)とも言い、値から対象のデータが容ｍｐｍｐ連想できる英数字・記号の組合せをコードとして割り当てる方式です。他のコードよりも桁数が多くなりますが、利用者が記憶しやすい利点があり、商品番号や製品の型番としてよく使用されています。
>
> 例)
> 国名：日本→JP，アメリカ→US
> 色名：黒→BK，白→WH
> プロジェクトマネージャ→PM　など
>
> 記述中の「コードから商品の内容が容易に分かるようにしたい」という目的に叶うのは表意コードです。

## 出典：平成16年春期　問51:インタフェース設計　(全17問中16問目)
業務システムのコード設計に関する記述のうち，最も適切なものはどれか。
-> (ウ)コードの入力ミスが業務に重大な影響を及ぼすと判断されるときは，検査文字(チェックディジットなど)を採用すべきである。

## 出典：平成18年春期　問48:インタフェース設計　(全17問中13問目)
バーコードには，検査数字(チェックディジット)を付加するのが一般的である。JANコード(標準タイプ，13 けた)では，12けたの数の検査数字を次の方式で算出している。この方式で算出した図のバーコード(123456789012)の検査数字として適切な値はどれか。


〔JAN コードにおける検査数字の算出及び付加方式〕
1. 検査数字を付加する前の右端の数字の位置を奇数けたとし，左に向かって交互に奇数けたと偶数けたとする。
2. 偶数けたの数字の合計を求める。
3. 奇数けたの数字の合計を求め，その値を3倍する。
4. (2)と(3)の合計を求める。
5. (4)の値の1の位の数字を10から引く。ただし，1の位が0のときは0とする。例えば (4)の値が123のときは10－3＝7，120のときは0とする。
7. (5)で求めた数字を検査数字とし，右端けたの右に付加する。

->(エ)8
*問題を良く読み解かなければならない！！
奇数 -> 奇数ではなく、奇数桁が偶数であるところが引っ掛けポイント

## 出典：平成22年春期　問75:マルチメディア技術　(全22問中17問目)
電子掲示板やブログに投稿するとき，図のようなゆがんだ文字の画像が表示され，それを読み取って入力するように求められることがある。その目的はどれか。
-> (エ)プログラムによる自動投稿を防止する。
> 設問で説明されている投稿時に画像上の文字を読み取って入力する認証方式をCaptcha（キャプチャ）と言います。
>
> Captchaは、チャレンジレスポンス型テストの一種で、その主たる目的はプログラムによる自動・大量送信を防止することです。ページ表示の度に異なっている画像上の文字はプログラム処理では容易に判読できません。これを利用して自動プログラムで無差別に投稿するスパム行為や、サーバに負担のかかる短時間における連続リクエストが送信されることを防ぎます。実際には表示される画像はゆがんでいたり、様々な色が付いていたりします。これには、画像中の文字を解析するパターンマッチングなどの技術を使ったプログラムへの耐性を高めるという目的があります。

## 出典：平成28年秋期　問78:マルチメディア応用　(全10問中3問目)
300×600ドットで構成され，1画素の情報を記録するのに24ビットを使用する画像データがある。これを150×300ドットで構成され，1画素の情報を記録するのに8ビットを使用する画像データに変換した。必要な記憶容量は何倍になるか。
-> (ア)1/12

300 * 600 = 180000
24bit = 3byte
180000 * 3 = 540000

150 * 300 = 45000

540000 / 45000 = 12

## 出典：平成18年秋期　問26:マルチメディア技術　(全33問中30問目)
横1,600画素，縦1,200画素で，24ビットのカラー情報をもつ画像が撮影できるディジタルカメラがある。このカメラに8Mバイトの記録用メモリを使用すると，何枚の画像が記録できるか。ここで，画像は圧縮しないものとする。
-> (ア)1枚
1920000 * 24(bit) = 46080000
46080000 / 8(1byte分) = 5760000 // byteに直す処理
8000000 / 5760000 = 1.3~ // 8Mbyteを5760000byteで割る
2枚は記憶できない