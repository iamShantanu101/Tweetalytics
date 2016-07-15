from unittest import TestCase
from smm.classifier.textprocessing import SimpleProcessor
__author__ = 'shantanu'


class TestSimpleProcessor(TestCase):

    def setUp(self):
        self.text = "hello my name is Timor "

    def test_clean(self):
        result = SimpleProcessor.clean(self.text)
        expect = "hello my name is timor"
        self.assertEqual(expect, result)

    def test_getSearchTokens(self):
        result = SimpleProcessor.getSearchTokens(SimpleProcessor.clean(self.text))
        expect = "hello my name is timor".split()
        self.assertEqual(expect, result)

    def test_getClassifierTokens(self):
        result = SimpleProcessor.getClassifierTokens(SimpleProcessor.clean(self.text))
        expect = "hello my name is timor".split()
        self.assertEqual(expect, result)

    def test_getFeatures(self):
        result = SimpleProcessor.getFeatures(SimpleProcessor.clean(self.text))
        expect = {'timor': 1, 'is': 1, 'my': 1, 'hello': 1, 'name': 1}
        self.assertEqual(expect, result)
