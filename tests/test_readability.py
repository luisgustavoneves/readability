#-*- coding:utf-8 -*-
u"""
Created on 22/05/14
by fccoelho
license: GPL V3 or Later
"""

__docformat__ = 'restructuredtext en'

import unittest
from readability import Readability
import codecs

class TestReadability(unittest.TestCase):
    def setUp(self):
        with codecs.open('discurso.txt') as f:
            self.texto = f.read()
    def test_portuguese_text(self):
        rd = Readability(self.texto)
        self.assertIsInstance(rd.ARI(), float)
        self.assertIsInstance(rd.ColemanLiauIndex(), float)
        self.assertIsInstance(rd.FernandezHuerta(), float)
        self.assertIsInstance(rd.FleschKincaidGradeLevel(), float)
