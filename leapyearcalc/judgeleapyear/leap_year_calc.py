# coding: UTF-8
# オプション付きの閏年判定ルーチン
# 閏年運用開始以前は例外、紀元前後の特殊運用も史実に基づいて判定。
import os

import JudgeLeapYear as JLP


# メインルーチン
def main():
    print("==========閏年判定プログラム（詳細）==========")
    test_year = JLP.JudgeLeapYear()
    while True:
        while True:
            try:
                test_year.setYear() # 判定対象の西暦を取得
                break
            except (ValueError, TypeError) as e:
                print(e)
                print("\n")
                continue

        try:
            if ( test_year.isLeapYear("checkBC45","exception")) : # 閏年か否か判定
                answer = "True：" + test_year.getStrYear() + "年は閏年です"
            else:
                answer = "False：" + test_year.getStrYear() + "年は平年です"
        # 紀元前45年（負数表示で-44年）にユリウス暦で初めて閏年が採用された為、その年より前は閏年の概念が本来存在しない
        except JLP.LeapYearError:
            answer = "Undefined：紀元前46年以前には閏年は導入されていません"

        print(answer) # answerを標準出力

        if input("引き続き他の年も調べますか？(y/n)：") is "y":
            print("\n")
            continue
        else:
            print("\n")
            break

main()