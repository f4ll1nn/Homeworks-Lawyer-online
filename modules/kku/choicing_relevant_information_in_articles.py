""" Module of realisation choice relevant information in articles """
import langdetect
import pandas as pd
from nltk.corpus import wordnet

from kku.trans.mtranslate.mtranslate import translate


class Article:
    """ Class of articles """

    def __init__(self, number: int, name: str, punkt1=None, punkt2=None,
                 punkt3=None, punkt4=None, punkt5=None, punkt6=None,
                 punkt7=None, punkt8=None) -> None:
        """ Creates article """
        self.number = number
        self.name = name
        self.punkt1 = punkt1
        self.punkt2 = punkt2
        self.punkt3 = punkt3
        self.punkt4 = punkt4
        self.punkt5 = punkt5
        self.punkt6 = punkt6
        self.punkt7 = punkt7
        self.punkt8 = punkt8
        self.translated_name = None
        self.translated_punkt1 = None
        self.translated_punkt2 = None
        self.translated_punkt3 = None
        self.translated_punkt4 = None
        self.translated_punkt5 = None
        self.translated_punkt6 = None
        self.translated_punkt7 = None
        self.translated_punkt8 = None
        self.relevant_words = None

    def transalte_name(self) -> None:
        """ Translates name into english in order to use later Natural language
        Google Api. This information will be in self.translated_name """
        translated = translate(self.name, "en")
        self.translated_name = translated

    def translate_punkts(self) -> None:
        """ Translates punkt into english in order to use later Natural
        language Google Api."""
        punkts = [self.punkt1, self.punkt2, self.punkt3, self.punkt4,
                  self.punkt5, self.punkt6, self.punkt7, self.punkt8]
        for i in range(8):
            try:
                translated = translate(punkts[i], "en")
                if i == 0:
                    self.translated_punkt1 = translated
                if i == 1:
                    self.translated_punkt2 = translated
                if i == 2:
                    self.translated_punkt3 = translated
                if i == 3:
                    self.translated_punkt4 = translated
                if i == 4:
                    self.translated_punkt5 = translated
                if i == 5:
                    self.translated_punkt6 = translated
                if i == 6:
                    self.translated_punkt7 = translated
                if i == 7:
                    self.translated_punkt8 = translated
            except TypeError:
                pass

    def relevant_information_in_name(self) -> None:
        """ Choising relevant information in name of articles
        This words will be in self.relevant_name """
        pass

    def relevant_information_in_punkts(self) -> list:
        """ Choising relevant indormation in each punkts of articles
         This words will be in self.relevant_point(number)"""
        pass

    def find_synonyms(self, relevant_words_list) -> set:
        """ Returns list of synonyms and this words, that can be relevant
        to each article """
        synonyms = []
        for word in relevant_words_list:
            try:
                for syn in wordnet.synsets(word):
                    for k in syn.lemmas():
                        translated = translate(k.name(), "uk")
                        synonyms.append(translated)
            except AttributeError:
                pass
        return set(self.synonyms_check(synonyms))

    def synonyms_check(self, set_syn) -> list:
        """ Check are all word in synonyms set ukrainian """
        for word in set_syn:
            try:
                if langdetect.detect(word) == "uk":
                    pass
                else:
                    set_syn.remove(word)
            except langdetect.lang_detect_exception.LangDetectException:
                set_syn.remove(word)
        return set_syn

    def write_to_exel(self, file: str) -> None:
        """ Write to exel the relevant words for each articles """
        pass


if __name__ == "__main__":
    RESULT = pd.read_excel("articles_with_punkts.xlsx")
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    # for i in result.index:
    #     article = result.loc[[i]]
    #     index = int(article["Рядки"].str.find("."))
    #     number = int(article["Рядки"].str[6:index].str.strip())
    #     name = article["Рядки"].str[index + 1:].str.strip().to_string()[3:].strip()
    #     punkts = []
    #     for k in article:
    #         if article[k].to_string().find("NaN") == -1:
    #             if k != "Рядки":
    #                 punkts.append(k)
    #     article_cl = Article(number, name)
    #     try:
    #         article_cl.punkt1 = article[punkts[0]].to_string()[3:].strip()
    #         article_cl.punkt2 = article[punkts[1]].to_string()[3:].strip()
    #         article_cl.punkt3 = article[punkts[2]].to_string()[3:].strip()
    #         article_cl.punkt4 = article[punkts[3]].to_string()[3:].strip()
    #         article_cl.punkt5 = article[punkts[4]].to_string()[3:].strip()
    #         article_cl.punkt6 = article[punkts[5]].to_string()[3:].strip()
    #         article_cl.punkt7 = article[punkts[6]].to_string()[3:].strip()
    #         article_cl.punkt8 = article[punkts[7]].to_string()[3:].strip()
    #     except IndexError:
    #         pass
    #     article_cl.transalte_name()
    #     article_cl.translate_punkts()

    ARTICLE = RESULT.loc[[0]]
    INDEX = int(ARTICLE["Рядки"].str.find("."))
    NUMBER = int(ARTICLE["Рядки"].str[6:INDEX].str.strip())
    NAME = ARTICLE["Рядки"].str[INDEX + 1:].str.strip().to_string()[3:].strip()
    PUNKTS = []
    for k in ARTICLE:
        if ARTICLE[k].to_string().find("NaN") == -1:
            if k != "Рядки":
                PUNKTS.append(k)
    ARTICLE_CL = Article(NUMBER, NAME)
    try:
        ARTICLE_CL.punkt1 = ARTICLE[PUNKTS[0]].to_string()[3:].strip()
        ARTICLE_CL.punkt2 = ARTICLE[PUNKTS[1]].to_string()[3:].strip()
        ARTICLE_CL.punkt3 = ARTICLE[PUNKTS[2]].to_string()[3:].strip()
        ARTICLE_CL.punkt4 = ARTICLE[PUNKTS[3]].to_string()[3:].strip()
        ARTICLE_CL.punkt5 = ARTICLE[PUNKTS[4]].to_string()[3:].strip()
        ARTICLE_CL.punkt6 = ARTICLE[PUNKTS[5]].to_string()[3:].strip()
        ARTICLE_CL.punkt7 = ARTICLE[PUNKTS[6]].to_string()[3:].strip()
        ARTICLE_CL.punkt8 = ARTICLE[PUNKTS[7]].to_string()[3:].strip()
    except IndexError:
        pass

    ARTICLE_CL.transalte_name()
    ARTICLE_CL.translate_punkts()
    TASK = ARTICLE_CL.translated_punkt2.split()
    print(ARTICLE_CL.find_synonyms(TASK))
    # print(article_cl.punkt2)
