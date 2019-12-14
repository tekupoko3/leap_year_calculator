# coding: UTF-8
import os
import re

class LeapYearError(Exception):
    """ 西暦が紀元前47年以前である場合の例外 """
    pass

class JudgeLeapYear(object):
    """
    class JudgeLeapYear(object)
    -----------------------------
    閏年の判定を行うためのクラス

    メンバ
    __year：int型, 判定対象となる西暦を格納する。デフォルト値：None
    __str_year：str型, __yearを文字列にて格納する。0以下の値については紀元前表記となる。デフォルト値：None

    メソッド
    void __init__([year])：コンストラクタ。
        year：（オプション）西暦。int型。この値を用いてメンバ変数が初期化される。デフォルトではNoneTypeが格納される。

    void __del__()：デストラクタ。

    void setYear([year])：メンバ変数__yearの値を設定する。
        year：（オプション）西暦。int型。デフォルトではユーザ標準入力を待ち受ける。入力は半角数字。

    void __setStrYear()：メンバ変数__str_yearの値を設定する。

    int getYear()：メンバ変数__yearの値を取得する。

    str getStrYear()：メンバ変数__str_yearを値を取得する。

    boolean([NoneType]) isLeapYear(["checkBC46"],[returnType])：メンバ変数__yearが閏年であるか否かを判定する。
        <boolean> True ：__yearは閏年である。
        <boolean> False：__yearは平年である。
        "checkBC46"：（オプション）紀元前47年以前に閏年の概念がなかったことを判断に含める。
        returnType：（オプション）オプション"checkBC46"が有効な場合、紀元前47年以前である場合はisLeapYearの返り値を平年Falseと区別する。
            "none"：返り値をNoneとする。
                <NoneType> None：（オプション）__yearの期間においては閏年は未定義。
            "exception"：例外LeapYearErrorを返す。
                <exception> LeapYearError：（オプション）__yearの期間においては閏年は未定義。

    boolean([NoneType]) __isLeapYear()：メンバ変数__yearが閏年であるか否かを判定する。グレゴリオ暦の閏年判定ルールの実装部。
        <boolean> True ：__yearは閏年である。
        <boolean> False：__yearは平年である。
    

    """

    __year = None
    __str_year = None


    def __init__(self, *args):
        if len(args) == 1:
            if (type(args[0]) is int):
                self.__year = args[0]
                self.__setStrYear()
            else:
                raise TypeError("Invalid input type args[0] for __init__([int:year]) in <class JudgeLeapYear> object.")
        elif len(args) == 0:
            self.__year = None
        else:
            raise SyntaxError("Too many arguments for __init__([int:year]) of <class JudgeLeapYear> object.")


    # 閏年判定の対象となる西暦を返す
    def setYear(self, *args):
        # 西暦の入力受付
        if len(args) == 0 or type(args[0]) is str: # 引数のない場合
            if len(args) == 0:
                str_year = input("西暦を入力してください（単位不要、半角数字、西暦0年=紀元前1年、紀元前2年以前は負数値）：")
            elif type(args[0]) is str:
                str_year = args[0]
            # 入力値の型確認
            # 正規表現のマッチングパターン
            pattern_noinput = re.compile(r'^$')
            pattern_multibyteDigit = re.compile(r'^.*[０-９]+．?[０-９]*.*$')
            pattern_notDigit = re.compile(r'^.*[^\-0-9\.].*$')
            pattern_integer = re.compile(r'^\-?[0-9]+$')
            # 入力された文字との比較
            matchNoInput = pattern_noinput.match(str_year)
            matchMultibyteDigit = pattern_multibyteDigit.match(str_year)
            matchNotDigit = pattern_notDigit.match(str_year)
            matchInteger = pattern_integer.match(str_year)
            # 半角整数以外の入力に対する例外処理
            if matchNoInput:
                # 無入力に対する例外処理
                raise ValueError("エラー（無入力）：値を入力してください")
            elif matchMultibyteDigit:
                # 全角数字の入力に対する例外処理
                raise ValueError("エラー（全角数字の入力）：全角数字は無効です。西暦は半角数字で整数を入力してください")                
            elif matchNotDigit:
                # 数字以外の入力に対する例外処理
                raise ValueError("エラー（非数文字の入力）：半角数字以外の文字（半角マイナスを除く）の入力は無効です。西暦は単位など付けず、半角数字で整数を入力してください")
            elif not matchInteger:
                # 小数の入力に対する例外処理
                raise ValueError("エラー（非整数値の入力）：小数は無効です。西暦は半角数字で整数を入力してください")
            # 入力をメンバ変数に反映
            self.__year = int(str_year)
            self.__setStrYear()
        elif len(args) == 1 and not type(args[0]) is str:
            if (type(args[0]) is int): # 西暦を直接引数に取る場合
                self.__year = args[0]
                self.__setStrYear()
            else:
                raise TypeError("Invalid input type args[0] for __init__([int:year]) in <class JudgeLeapYear> object.")
        else:
            raise SyntaxError("Too many arguments for getYearInput([int:year]).")


    def __setStrYear(self): #西暦0以下の場合に出力年数の表示を紀元前にする
        if self.__year <= 0:
            yearBC = abs(self.__year) + 1
            self.__str_year = "紀元前" + str(yearBC)
        else:
            self.__str_year = str(self.__year)


    def getYear(self):
        return self.__year


    def getStrYear(self):
        return self.__str_year


    # 閏年判定用プログラム（返り値：Boolean または None(オプション), 例外：LeapYearError(オプション)）
    def isLeapYear(self, *args):
        # 可変長引数の例外処理
        if len(args) > 2:
            raise SyntaxError("Too many arguments for isLeapYear(['checkBC46'],[str:returnType]).")
        elif (len(args) != 0) and (args[0] is not "checkBC46"):
            raise SyntaxError("Invalid argument args[0] for isLeapYear(['checkBC46'],[str:returnType]).")
        elif (len(args) == 2):
            if not( args[1] is "none" or args[1] is "exception"):
                raise SyntaxError("Invalid argument args[1] for isLeapYear(['checkBC46'],[str:returnType]).")

        # 紀元前46年（負数表示で-45年）にユリウス暦で初めて閏年が採用された為、その年より前は閏年の概念が本来存在しない
        # 加えて、紀元前44年〜紀元8年までは例外的な閏年運用がなされていた（３年周期や、閏年を適用しない期間など）
        # 第１引数が"checkBC46"であれば、上記考慮する
        if (1 <= len(args) <= 2) and (args[0] is "checkBC46"):
            # 紀元前47年以前には閏年の概念が存在しなかった
            if self.__year < -45:
                # さらに第２引数が"None"または"exception"であれば、返り値を平年Falseと区別する
                if (len(args) == 2) and (args[1] is "none"): # 返り値Noneとする場合
                    return None
                elif (len(args) == 2) and (args[1] is "exception"): # 例外を返す場合
                    raise LeapYearError
                else: # オプションを付けない場合（紀元前47年以前はすべて平年扱いとする）
                    return False
            # ユリウス暦成立の紀元前46年頃から紀元8年頃までの、例外的な閏年運用史実に基づく判定
            # 参考：https://ja.wikipedia.org/wiki/ユリウス暦#運用
            if -45 <= self.__year <= -7: # 紀元前46年と紀元前45年は平年、紀元前44年は閏年、以後紀元前８年まで3年に１回閏年
                if (self.__year + 7) % 3 == 0:
                    return True
                else:
                    return False
            elif -6 <= self.__year < 8: # 紀元前7年〜紀元7年までは、閏年を適用しなかった。紀元8年は閏年、以後グレゴリオ暦に基づく  
                    return False
        
        # 主たる閏年判定部分
        return self.__isLeapYear()

    # シンプルな閏年判定（グレゴリオ暦）
    def __isLeapYear(self):
        if (self.__year % 100 == 0) and (self.__year % 400 == 0): # 西暦が100の倍数かつ400の倍数ならば閏年
            return True
        elif (self.__year % 100 != 0) and (self.__year % 4 == 0): # 西暦が100の倍数でないかつ4の倍数ならば閏年
            return True
        else:
            return False


    def __del__(self):
        del self
