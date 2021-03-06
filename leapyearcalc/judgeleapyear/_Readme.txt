Readme.txt

-----------------------------------------------------------------

◎コアプログラム：JudgeLeapYear.py（クラスの実装のみ、メインルーチン無し）
  この中のメソッド "__isLeapYear()" が中心になります。
  
  拡張版として、"isLeapYear()" を実装しています。
  基本的にはこのメソッドから__isLeapYear()を呼び出して使う形にしました。
  
  特徴：
  ・入力文字の例外処理もこの "isLeapYear()" で実装しています。
    試しに半角数字以外も入力してみてください。
    弾かれてエラーメッセージが出てきます。
  ・オプションを付ければ、うるう年が始まった古い時代の特例規則も判断できるようにしています。
  
  他の内容はコンストラクタやセッター、ゲッターなどです。

-----------------------------------------------------------------

◎メインルーチンの実装は３パターン作成してみました。
  動作の確認はこちらの各ファイルをそれぞれ実行してください。

  1 一番単純な閏年判定のCLI実装（simple_leap_year_calc.py）
    …isLeapYear()メソッドをオプション無しで使用

  2 古い時代の特殊な周期（単純な4年に一回ではなかった）と、
    うるう年運用開始以前の判定をCLIで実装（leap_year_calc.py）
    …isLeapYear()にオプションを適用して返答メッセージを追加。

  3 Webページへの実装（Djangoバックエンド、AWS Cloud9で開発、Herokuへデプロイ）
    isLeapYear()を、オプション付き、バックエンドで実行するWebアプリ。
    上記1,2は使わず、views.pyから直接JudgeLeapYearをインポートして利用しています。
    
    herokuにアップロードしてあります。下記よりアクセスください。
    https://leapyearcalc.herokuapp.com/
   
    ・htmlにて入力制限を実装しています。
    ・一応メディアクエリを使ってスマホ表示に対応させています。
    ・閏年に直接関係のないイースターエッグは、DjangoのTemplate側で条件分岐させています。

-----------------------------------------------------------------

2019/12/18 てくぽこ(tekupoko3)
