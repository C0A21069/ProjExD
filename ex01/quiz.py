import random
import datetime

def mondai():
    quiz = [sazae, katuo, tarao]
    q = random.choice(quiz)
    q()
    st = datetime.datetime.now()
    ans = input("解答：")
    ed = datetime.datetime.now()
    q(ans)
    print(f"解答時間：{(ed-st).seconds}秒")

def sazae(ans = None):
    toi = "サザエの旦那の名前は？"
    kotae = ["マスオ", "ますお"]
    if ans == None:
        print(f"問題：{toi}")
    elif ans in kotae:
        return print("正解")
    else:
        return print("不正解")

def katuo(ans = None):
    toi = "カツオの妹の名前は？"
    kotae = ["ワカメ", "わかめ"]
    if ans == None:
        print(f"問題：{toi}")
    elif ans in kotae:
        return print("正解")
    else:
        return print("不正解")

def tarao(ans = None):
    toi = "タラオはカツオから見てどんな関係？"
    kotae = ["甥", "おい", "甥っ子", "おいっこ"]
    if ans == None:
        print(f"問題：{toi}")
    elif ans in kotae:
        return print("正解")
    else:
        return print("不正解")

if __name__ == "__main__":
    mondai()