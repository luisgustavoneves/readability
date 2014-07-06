#!/usr/bin/env python
# -*- coding: utf-8
import math

from utils import get_char_count
from utils import get_words
from utils import get_sentences
from utils import count_syllables
from utils import count_complex_words
from guess_language import guessLanguage


class Readability:
    analyzedVars = {}

    def __init__(self, text):
        self.analyze_text(text)

    def analyze_text(self, text):
        lang = guessLanguage(text)
        words = get_words(text)
        char_count = get_char_count(words)
        word_count = len(words)
        sentence_count = len(get_sentences(text))
        syllable_count = count_syllables(words, lang)
        complexwords_count = count_complex_words(text)
        avg_words_p_sentence = word_count / sentence_count
        syllables_per_hundred_words = syllable_count * 100. / word_count
        sentences_per_hundred_words = sentence_count * 100. / word_count

        self.analyzedVars = {
            'words': words,
            'char_cnt': float(char_count),
            'word_cnt': float(word_count),
            'sentence_cnt': float(sentence_count),
            'syllable_cnt': float(syllable_count),
            'complex_word_cnt': float(complexwords_count),
            'avg_words_p_sentence': float(avg_words_p_sentence),
            'syllables_per_hundred_words': syllables_per_hundred_words,
            'sentences_per_hundred_words': sentences_per_hundred_words
        }

    def ARI(self):
        score = 4.71 * (self.analyzedVars['char_cnt'] / self.analyzedVars['word_cnt']) + 0.5 * (
        self.analyzedVars['word_cnt'] / self.analyzedVars['sentence_cnt']) - 21.43
        return score

    def FleschReadingEase(self):
        score = 0.0
        score = 206.835 - (1.015 * (self.analyzedVars['avg_words_p_sentence'])) - (
        84.6 * (self.analyzedVars['syllable_cnt'] / self.analyzedVars['word_cnt']))
        return round(score, 4)

    def FleschKincaidGradeLevel(self):
        score = 0.39 * (self.analyzedVars['avg_words_p_sentence']) + 11.8 * (
        self.analyzedVars['syllable_cnt'] / self.analyzedVars['word_cnt']) - 15.59
        return round(score, 4)

    def GunningFogIndex(self):
        score = 0.4 * ((self.analyzedVars['avg_words_p_sentence']) + (
        100 * (self.analyzedVars['complex_word_cnt'] / self.analyzedVars['word_cnt'])))
        return round(score, 4)

    def SMOGIndex(self):
        score = (math.sqrt(self.analyzedVars['complex_word_cnt'] * (30 / self.analyzedVars['sentence_cnt'])) + 3)
        return score

    def ColemanLiauIndex(self):
        score = (5.89 * (self.analyzedVars['char_cnt'] / self.analyzedVars['word_cnt'])) - (
        30 * (self.analyzedVars['sentence_cnt'] / self.analyzedVars['word_cnt'])) - 15.8
        return round(score, 4)

    def LIX(self):
        longwords = 0.0
        for word in self.analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = self.analyzedVars['word_cnt'] / self.analyzedVars['sentence_cnt'] + float(100 * longwords) / \
                self.analyzedVars['word_cnt']
        return score

    def RIX(self):
        score = 0.0
        longwords = 0.0
        for word in self.analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = longwords / self.analyzedVars['sentence_cnt']
        return score

    def FernandezHuerta(self):
        score = 0.0
        score = 206.84 - (.60 * (self.analyzedVars['syllables_per_hundred_words'])) - (
        1.02 * (self.analyzedVars['sentences_per_hundred_words']))
        return round(score, 4)


if __name__ == "__main__":
    text = """We are close to wrapping up our 10 week Rails Course. This week we will cover a handful of topics commonly encountered in Rails projects. We then wrap up with part 2 of our Reddit on Rails exercise!  By now you should be hard at work on your personal projects. The students in the course just presented in front of the class with some live demos and a brief intro to to the problems their app were solving. Maybe set aside some time this week to show someone your progress, block off 5 minutes and describe what goal you are working towards, the current state of the project (is it almost done, just getting started, needs UI, etc.), and then show them a quick demo of the app. Explain what type of feedback you are looking for (conceptual, design, usability, etc.) and see what they have to say.  As we are wrapping up the course you need to be focused on learning as much as you can, but also making sure you have the tools to succeed after the class is over."""

    texto = """É um prazer muito grande estar aqui vivendo esse momento tão importante para mim, para o companheiro Pezão e para a nossa equipe. Não poderia deixar de agradecer muito, profundamente, a duas pessoas que foram leais, independentes e companheiras nessa jornada árdua, e ao mesmo tempo prazerosa, de governar o Estado do Rio de Janeiro. Quero muito agradecer ao Presidente da Assembleia Legislativa, Deputado Jorge Picciani, por tudo que V.Exa., com estatura e magnanimidade soube se conduzir à frente do parlamento que eu também tive a honra de presidir. (Palmas) Ao querido destemido, corajoso, justo, Presidente do Tribunal de Justiça, Luiz Zveiter, o meu muito obrigado. (Palmas) Quero agradecer a um querido amigo, Prefeito da Cidade mais bonita do planeta, Eduardo Paes. (Palmas); e na figura dele agradecer a todos os prefeitos aqui presentes. Quero agradecer muito a presença dos meus queridos prefeitos. Muito obrigado.
    """

    rd = Readability(texto)
    print 'Test text:'
    print '"%s"\n' % text
    print 'ARI: ', rd.ARI()
    print 'FleschReadingEase: ', rd.FleschReadingEase()
    print 'FernandezHuerta: ', rd.FernandezHuerta()
    print 'FleschKincaidGradeLevel: ', rd.FleschKincaidGradeLevel()
    print 'GunningFogIndex: ', rd.GunningFogIndex()
    print 'SMOGIndex: ', rd.SMOGIndex()
    print 'ColemanLiauIndex: ', rd.ColemanLiauIndex()
    print 'LIX: ', rd.LIX()
    print 'RIX: ', rd.RIX()

