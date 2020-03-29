import random
from settings.settings import *


class Phrase(object):
    """
    フレーズと、次に来るフレーズの管理
    """

    def __init__(self, name):
        self.name = name
        self.next_phrases = None

    def __repr__(self):
        return self.name

    def get_phrase(self):
        return self.name

    def set_next_phrases(self, next_phrases):
        self.next_phrases = next_phrases

    def get_next_phrase(self):
        r = random.random()
        p = 0
        for key in self.next_phrases:
            p += self.next_phrases[key]
            if r < p:
                return key


class MixPhrase(Phrase):
    """
    複数のフレーズを確率的に返す
    """

    def __init__(self, name):
        super().__init__(name)
        self.my_phrases = None

    def set_phrases(self, phrases):
        self.my_phrases = phrases

    def get_phrase(self):
        r = random.random()
        p = 0
        for key in self.my_phrases:
            p += self.my_phrases[key]
            if r < p:
                return key.get_phrase()


class NullPhrase(Phrase):

    def get_phrase(self):
        return None


class EndPhrase(Phrase):

    def get_phrase(self):
        return END


class Jikkyo(object):
    """
    実況クラス
    """
    def __init__(self):
        self.jikkyo_list = []  # フレーズのリスト

    def add_phrase(self, phrase):
        if phrase is not None:
            self.jikkyo_list.append(phrase)

    def get_jikkyo_list(self):
        return self.jikkyo_list

    def get_jikkyo_sentence(self):
        jikkyo = ""
        for p in self.jikkyo_list:
            jikkyo += p + "\n"
        return jikkyo


# class Team(object):
#
#     def __init__(self, name, passer1, passer2, scorer, scorer_full):
#         self.name = name
#         self.passer1 = passer1
#         self.passer2 = passer2
#         self.scorer = scorer
#         self.scorer_full = scorer_full
#
#
# class JikkyoGenerator(object):
#
#     def __init__(self, start_phrase):
#         self.start_phrase = start_phrase
#
#     def generete_jikkyo(self):
#         p = self.start_phrase
#         jikkyo = ""
#         while True:
#             if p.get_phrase() == END:
#                 break
#             jikkyo += p.get_phrase()
#             p = p.get_next_phrase()
#
#         return jikkyo
