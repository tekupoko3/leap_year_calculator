# coding: UTF-8
# JudgeLeapYearクラスの動作確認用CLIプログラムその１
# シンプルな閏年判定用プログラム。
import os

import JudgeLeapYear as JLP


# メインルーチン
def main():
    print("==========閏年判定プログラム==========")
    test_year = JLP.JudgeLeapYear() # インスタンス生成
    while True:
        while True:
            try:
                test_year.setYear() # 判定対象の西暦を取得
                break
            except (ValueError, TypeError) as e:
                print(e)
                print("\n")
                continue
            
        print(test_year.isLeapYear()) #判定結果を標準出力
        if input("引き続き他の年も調べますか？(y/n)：") is "y":
            print("\n")
            continue
        else:
            print("\n")
            break

    return test_year.isLeapYear() #最後の判定結果を返り値として出力

main()