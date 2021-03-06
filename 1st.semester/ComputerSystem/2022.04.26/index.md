# 2022.04.26.ComputerSystem
# Week3 コンピュータ構成要素
## 到達目標
- コンピュータの5大装置を知り、当人なりに説明できる。
- プログラム動作の仕組みを知り、当人なりに説明できる。
  - (計算問題の準備)コンピュータの補助単位を知る。
- フローチャートと疑似言語の、『分岐構造』を、読み書きできる。

# プログラム動作の仕組み
- コンピュータ
  - 入力する
  - 計算する
  - 出力する
    - などの基本動作を指示する「命令」によって動く。

## 主記憶上のプログラムは、命令サイクルと実行サイクルを繰り返すことで、処理を進めていく
- 命令サイクル(Iサイクル)
  - 命令フェッチ
    - 主記憶装置から命令を取り出し、解読する工程
- 実行サイクル(Eサイクル)
  - 命令を解読し、解読された命令やアドレスに基づいて、実行、処理結果の書き込みを行う工程

1. CPUは、命令アドレスレジスタに格納されているアドレスを主記憶装置へ送るとともに、読み出し信号を読み書き制御部に伝える。
2. 主記憶装置は、指定されたアドレスから命令を読み出し、CPU内の命令レジスタに格納する。CPUは命令を受け取り、命令レジスタに格納する。
3. 1つの命令の取り出しが終了すると、プログラムレジスタの値を次に実行すべき命令アドレスに変更する。
   1. 通常の命令の場合は、プログラムレジスタに命令長(1語長または2語長)をアドレス加算する
4. 命令レジスタに格納された命令のうち「オペレータ部(命令)」を命令解読器(デコーダ)で解読。
5. オペランドアドレス計算
   1. オペランドアドレスgit計算命令解読の結果に基づいて、「オペランド部(アドレス情報)」をアドレス変換機構へ送り、有効アドレスを計算。
6. オペランドの取り出し
   1. 有効アドレスにより、主記憶装置のデータを取り出す。
7. 命令を実行する。
   1. 通常の命令は、オペランド部で指定されたデータを使用して計算を行う。
   2. 分岐命令の場合は、分岐先の有効アドレスを命令アドレスレジスタに格納。
   3. SVC(Super Visor Call)命令では、有効アドレスを引数として、割り出し(OSの機能を呼び出す内部割込み)を行う。
8. 実行された演算結果をレジスタ、または主記憶装置へ格納する(格納の際は有効アドレスを計算する)


- 制御用レジスタ
  - 次に実行する命令のアドレスを記憶する
    - 別名: プログラムカウンタ、プログラムレジスタ、命令カウンタ、逐次制御カウンタ

- 処理装置を構成する要素
  - 分岐命令の実行によって更新されるもの
    - --> プログラムレジスタ
  - 命令の実行は、プログラムレジスタに格納されたアドレス値により、主記憶上の命令が命令レジスタに読み込まれる。

# 基本情報技術者試験
## 出典：平成20年春期　問18 プロセッサ　(全68問中38問目)
主記憶へのアクセスを伴う演算命令を実行するとき，命令解読とオペランド読出しの間に行われる動作はどれか。
--> 実行アドレス計算

## 出典：平成23年秋期　問10 プロセッサ　(全68問中27問目)
CPUのプログラムレジスタ(プログラムカウンタ)の役割はどれか。
--> 命令を読み出すために，次の命令が格納されたアドレスを保持する。

# ITパスポート
## 出典：平成24年春期　問61 プロセッサ　(全22問中16問目)
CPUにおけるプログラムカウンタの説明はどれか。
--> 次に実行する命令が入っている主記憶のアドレスを保持する。

## 出典：平成24年秋期　問76 プロセッサ　(全22問中15問目)
コンピュータにおける命令の実行順序に関する次の記述中のa，bに入れる字句の適切な組合せはどれか。
コンピュータの命令実行順序は，
プログラムカウンタの参照
命令のa
次の命令の主記憶アドレスをプログラムカウンタにセットする。
命令のb
命令に応じた処理を実行
(1)に戻る。
を繰り返す。

--> a = 読み込み, b = 解読

# プロセッサの性能と高速化技術
## 動作速度を決めるクロック周波数
- クロック
  - コンピュータのマザーボード(CPUやメモリなどが取り付けられている基盤)状にある複数の装置が、タイミングを合わせて動作するために発生させる信号のこと
- クロック周波数
  - 上記の信号の周波数(時間あたりの発生回数)を表す
- 「基本的には」クロック周波数が高い = 高速に動作する
  - CPUはクロックに同期して動作するため
  - ※ただし、CPUにはさまざまな動作方式(アーキテクチャ)があり、クロック周波数の値だけでは正確な性能比較はできない
- 1つの命令は、複数クロックで実行される
### クロック周波数の単位
- MHz(メガヘルツ) または、GHz(ギガヘルツ)
  - 例: 200MHzなら1秒間の信号は200*10⁶回, 1GHzなら10⁹回
#### CPI(Cycles Per Instruction)
- 1命令の実行に必要なクロック数を表す単位
  - 例: 10CPIなら10クロック/命令
- 1クロック当たりの実行時間の計算
  - 1秒 / (クロック周波数 * 10⁶) ...MHzの場合
- 平均命令実行時間(1命令当たりの実行時間)の計算
  - 1クロック当たりの実行時間 * 1命令実行に必要なクロック数
###### 問
あるCPUが500MHzで8CPIの場合の平均命令実行時間(1命令当たりの実行時間)を求めよ

<!-- 平均命令実行時間 = 1クロック当たりの実行時間 * 1命令実行に必要なクロック数 -->
<!-- 1クロック当たりの実行時間 = 1秒 / (クロック周波数 * 10⁶) ...MHzの場合 -->
<!-- 1命令実行に必要なクロック数 = CPI -->
1/(500 * 10⁶)
0.002 * 10⁻⁶
2 * 10⁻⁹
2n秒(ナノ) // 1クロック当たりの実行時間が出る

2n秒 * 8CPI
16n秒

#### MIPS(Million Instructions Per Second)


# プロセッサとCPU
試験問題で使われる「プロセッサ」という用語は、処理を行う装置全般を含んでいる。
CPU(中央処理装置)はプロセッサの1種で、一般に制御装置や演算装置を持つコンピュータの中核を成す装置を指す。
- FPU
  - 浮動小数点演算を行う
- GPU
  - 表示用の画像処理を専門に行う
- DSP(デジタルシグナルプロセッサ)
  - 音声処理などを行う

# ITパスポート
## 出典：令和3年春期　問90
CPUのクロックに関する説明のうち，適切なものはどれか。
--> クロックは，命令実行のタイミングを調整する。
(CPUのクロックは、一定の周期で発生し、コンピュータの各回路が処理動作を行う基準となる信号のことで、各回路が処理のタイミングを合わせるために使用されている。)

## 出典：平成27年秋期　問63 プロセッサ　(全22問中12問目)
CPUのクロック周波数に関する記述のうち，適切なものはどれか。
--> 同一種類のCPUであれば，クロック周波数を上げるほどCPU発熱量も増加するので，放熱処置が重要となる。
(クロック周波数が高いほど発熱量も増加する。発熱量が多くなるとCPUが熱暴走を起こす可能性が高まるため、冷却装置等による放熱が重要である)

## 出典：平成23年特別　問60 プロセッサ　(全22問中17問目)
クロック周波数が1.6GHzのCPUは，4クロックで処理される命令を1秒間に何回実行できるか。
1600000000 / 4クロック
400,000,000
4億

## 出典：平成22年秋期　問57 プロセッサ　(全22問中19問目)
クロック周波数2GHzのプロセッサにおいて一つの命令が5クロックで実行できるとき，1命令の実行に必要な時間は何ナノ秒か。
1 / (2 * 10⁹)
0.5 * 10⁻⁹
0.5n秒 * 5クロック
2.5n秒

# 基本情報技術者試験
## 出典：平成16年秋期　問19 プロセッサ　(全68問中64問目)
1GHzで動作するCPUがある。このCPUは，機械語の1命令を平均0.8クロックで実行できることが分かっている。このCPUは1秒間に約何万命令実行できるか。
10⁹ / 0.8
1.25 * 10⁹
1,250,000 * 10⁴
1,250,000万回

## 出典：平成18年秋期　問19 プロセッサ　(全68問中49問目)
PCのCPUのクロック周波数に関する記述のうち，適切なものはどれか。
--> クロック周波数によってCPUの命令実行タイミングが変化する。クロック周波数が高くなるほど命令実行速度が上がる。
(クロック周波数は、1秒間に何回のクロックが発振されるかを表す数値でプロセッサの性能指標として使われます。クロックはメトロノームのように複数の回路の同期をとるために使用されているので、一般にコンピュータの機種・製品が同じであればクロック周波数が高いほど処理速度は高くなります。)

# ネットワーク(IoT)
- 通信手段
  - 直接指定方式
    - デバイスそのものを直接インターネットに接続する方式のこと
    - 固定回線、携帯電話の3G, 4G回線, Wi-Fi
    - 広範囲の通信を実現するが、身近なIoTデバイスを全てこの方式でネット接続すれば、コストだけでなく、消費電力もかかる。
  - デバイスゲートウェイ方式
    - インターネットなどを経由してクラウド上のサーバと直接通信する方式のこと
    - ゲートウェイ
      - モノとインターネットを中継する役割を持っており、いわゆるルータの働きをする機器
    - モノそのものに通信機器を搭載する直接指定方式よりも、コストや消費電力を抑える点で優れる
    - ゲートウェイの使用範囲は屋内とは限らない
      - 農業用の機器であれば屋外での適用も必要だが、設定される場所や環境によっては電波が安定しなかったり、電源を最適な設置場所などの課題もある。

- ZigBee(ジグビー)
  - よりIoTに適した通信規格
  - センサーネットワークを主目的とする近距離無線通信規格の一つ
  - スリープ時の待機電力が小さく、復帰時間が短い
    - 一定間隔を空けてデータ通信を行うケースに適する
    - 電池駆動可能な超小型機器への実装が向いている
      - 超低消費電力！乾電池1個で数年間の動作が可能

- Z-Wave
  - 相互運用性を持つ無線通信プロトコル
  - アメリカやヨーロッパを中心に普及している、IoT用の無線通信規格の一つ
  - 長時間運用を想定した規格
    - ホームオートメーションと、センサーネットワークのような低電力、長時間運用を要求する装置のために設計された低電力
      - 家電や防犯センサーなどの自宅の電化製品を制御するシステムに利用される

- 無線ネットワークが必要不可欠
  - 近距離通知
    - Wi-Fi
    - ZigBee
    - Bluetooth
  - 長距離通知
    - LTE
    - 3G
    - LPWA

# ITパスポート
## 出典：令和元年秋期　問81 ネットワーク方式　(全65問中13問目)
IoTシステム向けに使われる無線ネットワークであり，一般的な電池で数年以上の運用が可能な省電力性と，最大で数十kmの通信が可能な広域性を有するものはどれか。
--> LPWA
### LPWA(解説)
LPWA(Low Power Wide Area)は、LP:LowPower=省電力、WA:WideArea=広範囲の名称の通り、省電力・広範囲を特徴とする無線通信規格の総称です。伝送速度は遅いものの、省電力でWi-fiやBluetoothが届かない数キロメートルから数十キロメートル間の通信をカバーします。

IoT(Internet of Things)では、各所に配置された個々のIoTデバイスが内部バッテリーのみで長期間続けて稼働することになるので、バッテリー消費をいかに抑えるかがポイントになります。またIoTデバイス同士は、制御や情報取得のためにお互いに通信することになりますが、この個々の通信はそれほど大きいデータ量ではないので、通信回線の高速性は重要ではありません。
これらの特徴を踏まえると、IoTネットワークには省電力、低速、広範囲のネットワークが適していることになります。LPWAは、小型デバイスを多数配置した広範囲のIoTネットワークの運用を実現する手段として期待されています。

## 出典：令和3年春期　問80 ネットワーク方式　(全65問中5問目)
IoTデバイス，IoTゲートウェイ及びIoTサーバで構成された，温度・湿度管理システムがある。IoTデバイスとその近傍に設置されたIoTゲートウェイとの間を接続するのに使用する，低消費電力の無線通信の仕様として，適切なものはどれか。
--> BLE
### BLE(解説)
BLE(Bluetooth Low Energy)は、無線通信規格Bluetoothの一部で、その名前の通り低消費電力に特化した通信モードのことです。通信速度は低速ながら、ボタン電池1個で数カ月から1年程度稼働できるほど省電力性に優れ、低コストであることからIoTネットワークでの活用が期待されています。最大通信距離は選択する速度によって異なり10ｍ～400ｍ程度です。

# センサー技術に関する出題
## 出典：平成30年秋期　問71 産業機器　(全4問中1問目)
IoTの構成要素に関する記述として，適切なものはどれか。
--> インターネット又は閉域網に接続できる全てのものが対象となる。
IoTの構成要素には、インターネットに接続でき、物理的な実体をもつ全てのものが含まれます。

## 出典：平成28年春期　問65 産業機器　(全4問中4問目)
IoT(Internet of Things)を説明したものはどれか。
--> コンピュータなどの情報通信機器だけでなく様々なものに通信機能をもたせ，インターネットに接続することによって自動認識や遠隔計測を可能にし，大量のデータを収集・分析して高度な判断サービスや自動制御を実現することである。

## 出典：平成30年春期　問71 産業機器　(全4問中2問目)
IoT(Internet of Things)の実用例として，適切でないものはどれか。
(✖はIoTの実用例)

✅: インターネットにおけるセキュリティの問題を回避する目的で，サーバに接続せず，単独でファイルの管理，演算処理，印刷処理などの作業を行うコンピュータ
✖: 大型の機械などにセンサと通信機能を内蔵して，稼働状況，故障箇所，交換が必要な部品などを，製造元がインターネットを介してリアルタイムに把握できるシステム
✖: 検針員に代わって，電力会社と通信して電力使用量を送信する電力メータ
✖: 自動車同士及び自動車と路側機が通信することによって，自動車の位置情報をリアルタイムに収集して，渋滞情報を配信するシステム
### 解説
✅は、インターネットに繋がっていないという時点で適切でない。

## 出典：令和元年秋期　問13 IoTシステム・組込みシステム　(全19問中8問目)
IoTに関する記述として，最も適切なものはどれか。
--> センサを搭載した機器や制御装置などが直接インターネットにつながり，それらがネットワークを通じて様々な情報をやり取りする仕組み
### 解説
IoT(Internet of Things，モノのインターネット)は、情報端末ではない電子機器や機械類などの「モノ」にインターネット接続・通信機能やセンサ機能を持たせ、収集した情報を処理したり蓄積したりすることで、"監視"、"制御"、"最適化"、"自律化"などの新たな付加価値を得る仕組みです。IoTでは、情報機器以外のあらゆる「モノ」が直接インターネットに繋がるということがポイントとなります。

# クラウド技術(IoT)
1. IoTを利用し、様々なデバイスからデータをクラウドに転送し、蓄積される
   1. 蓄積されたデータをビッグデータと呼ぶ
2. 蓄積されたデータを活用する
   1. 主にICT(情報通信技術)企業が提供する
3. その情報がまたクラウドに送り出され、蓄積し、新たに入手した情報と再度解析するという流れが繰り返される。
4. クラウド内の情報は、加速度的に深化していく。

# 言語処理ツール
## ソフトウェア作成ツール -言語プロセッサ
- プログラムで記述したプログラムは、コンピュータが実行できる機械語にする必要がある。
  - プログラム = 原子プログラム, ソースコード, ソースプログラム
  - その際に用いられるのが言語プロセッサ(言語処理プログラム)
  - 原子プログラムを翻訳し、機械語の目的プログラム(オブジェクトモジュール)を作成する
  - さらに実行形式にするためにはリンカ(連携編集プログラム)による工程が必要

## 言語プロセッサの種類
- アセンブラ(assembler)
  - アセンブラ言語を機械語命令に翻訳するプロセッサ
  - 原則として、アセンブラ言語の1命令が、機械語の1命令と対応する
- コンパイラ(compiler)
  - 高水準・手続き型言語で記述された原子プログラムを目的プログラムに翻訳するプロセッサ
  - コンパイラの多くは、プログラムの実行を高速化する最適化機能(オプティマイズ)を持つ
- インタプリタ(interpreter)
  - 命令を1つずつ解釈し、そのつど翻訳しながら即時に実行する
  - PerlやPHPなど、多くのスクリプト言語もインタプリタ方式を採用している
- ジェネレータ(generator)
  - RPG(Report Program Generator)に代表される非手続き型プログラムから、パラメータに従ってプログラムを自動生成する
