from Phrase.phrase import *
import random


def main():


    # 実況を生成
    n = 999
    with open("kurashiki.txt", "w", encoding="utf-8") as f:

        for _ in range(n):
            # print(make_jikkyo(scorer))
            scorer = random.choice(SCORERS_LIST_FOR_SHINDAN)
            j = make_jikkyo(scorer)
            f.write(j)
            f.write("\n")


def make_jikkyo(scorer):
    """
    チームが決まったうえで、実況を生成し返す
    :param scorer:
    :return:
    """

    # チームの定義

    # フレーズの定義
    start = NullPhrase("")  # 最初

    setup3 = Phrase(scorer + "。")

    end_setup = NullPhrase("")

    assist1 = Phrase("ラストパス！")
    assist2 = Phrase("センターに入れる！")
    assist3 = Phrase("シンプルなクロス。")
    assist4 = Phrase("クロス！")
    assist5 = Phrase("シュートレンジ。")
    assist6 = Phrase("反転して")
    assist7 = Phrase("狙ってきました")

    center_attack = NullPhrase("")
    side_attack = NullPhrase("")

    shoot1 = Phrase("シュート！")
    shoot2 = Phrase(scorer + "ー！")
    shoot3 = Phrase("ヘディングシュート！")

    normal_goal = MixPhrase("普通のゴール")
    normal_goal1 = Phrase("ゲットォ～！")
    normal_goal2 = Phrase("ゲット！")
    normal_goal3 = Phrase("ゴール！")
    normal_goal4 = Phrase("うわぁ決めた～！")
    normal_goal5 = Phrase("オフサイドなければゴール！")

    golazo = MixPhrase("ゴラッソ")
    golazo1 = Phrase("うわぁゴラッソ～！")
    golazo2 = Phrase("うわぁ素晴らしい～！")

    after1 = Phrase("きれいな崩しでしたね～。")
    after2 = Phrase(scorer + "です！")

    # situation = MixPhrase("ゴール時のシチュエーション")
    # situation1 = Phrase(team_name + "先制。")
    # situation2 = Phrase("同点に追いつきました" + team_name + "。")
    # situation3 = Phrase("逆転に成功しました" + team_name + "。")
    # situation4 = Phrase("一点を返しました" + team_name + "。")
    # situation5 = NullPhrase("")
    situation = NullPhrase("")

    # after3 = Phrase(scorer_full + "、" + str(random.randint(0, 90)) + "分のゴールです。")
    after4 = Phrase(str(random.randint(0, 90)) + "分のゴールです。")

    end = EndPhrase(END)

    # 次のフレーズの確率定義
    start.set_next_phrases({end_setup: 0.7,
                           setup3: 0.3})
    # setup1.set_next_phrases({end_setup: 0.5,
    #                          setup2: 0.3,
    #                          setup3: 0.2})
    # setup2.set_next_phrases({end_setup: 0.7,
    #                          setup3: 0.3})
    setup3.set_next_phrases({center_attack: 0.4,
                             assist5: 0.2,
                             assist7: 0.2,
                             assist6: 0.1,
                             golazo: 0.1})
    end_setup.set_next_phrases({assist1: 0.25,
                                assist2: 0.3,
                                assist3: 0.1,
                                assist4: 0.1,
                                assist5: 0.25})
    assist1.set_next_phrases({center_attack: 1})
    assist2.set_next_phrases({center_attack: 1})
    assist3.set_next_phrases({side_attack: 1})
    assist4.set_next_phrases({side_attack: 1})
    assist5.set_next_phrases({center_attack: 1})
    assist6.set_next_phrases({shoot1: 1})
    assist7.set_next_phrases({golazo: 1})
    center_attack.set_next_phrases({shoot1: 0.7,
                                    shoot2: 0.3})
    side_attack.set_next_phrases({center_attack: 0.5,
                                  shoot3: 0.5})
    shoot1.set_next_phrases({normal_goal: 1})
    shoot2.set_next_phrases({normal_goal: 1})
    shoot3.set_next_phrases({normal_goal: 1})
    normal_goal.set_next_phrases({after1: 0.2,
                                  after2: 0.2,
                                  situation: 0.6})
    normal_goal.set_phrases({normal_goal1: 0.5,
                             normal_goal2: 0.2,
                             normal_goal3: 0.1,
                             normal_goal4: 0.1,
                             normal_goal5: 0.1})
    golazo.set_next_phrases({situation: 1})
    golazo.set_phrases({golazo1: 0.5,
                        golazo2: 0.5})
    after1.set_next_phrases({situation: 1})
    after2.set_next_phrases({situation: 1})
    situation.set_next_phrases({after4: 0.4,
                                end: 0.6})
    # situation.set_phrases({situation1: 0.3,
    #                        situation2: 0.2,
    #                        situation3: 0.1,
    #                        situation4: 0.1,
    #                        situation5: 0.3})
    # after3.set_next_phrases({end: 1})
    after4.set_next_phrases({end: 1})

    # 実況の生成
    p = start
    jikkyo = ""
    while True:
        if p.get_phrase() == END:
            break
        jikkyo += p.get_phrase()
        p = p.get_next_phrase()
        # print(p)

    return jikkyo


if __name__ == "__main__":
    main()
