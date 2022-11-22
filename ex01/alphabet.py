import datetime
import random

ta = 10
ke = 2
sa = 5

def shutudai(al_lst):
    global ta
    al_t = random.sample(al_lst, ta)
    return al_t

def kaitou(al_t):
    global ke, sa
    for ka in range(sa):
        al_k = random.sample(al_t, ke)
        al_h = [moji for moji in al_t if moji not in al_k]
        al_c = al_k.copy()
        random.shuffle(al_t)
        t = " ".join(al_t)
        h = " ".join(al_h)
        print(f"対象文字：{t}")
        print(f"表示文字：{h}")
        ans = input("欠損文字はいくつあるでしょうか？：")
        if ke == int(ans):
            print("正解です。それでは、具体的に欠損文字を1つずつ入力してください。")
            for i in range(ke):
                kotae = input(f"{i+1}つ目の文字を入力してください。：")
                if kotae in al_c:
                    al_c.remove(kotae)
                else:
                    print("不正解です。またチャレンジしてください。")
                    break
            else:
                print("正解です。")
                break
        else:
            print("不正解です。またチャレンジしてください。")


if __name__ == "__main__":
    st = datetime.datetime.now()
    al_lst = [chr(al) for al in range(65, 65+26)]
    al_t = shutudai(al_lst)
    kaitou(al_t)
    ed = datetime.datetime.now()
    print(f"実行時間：{(ed-st).seconds}秒")