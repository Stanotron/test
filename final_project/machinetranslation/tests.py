import unittest
from translator import englishToFrench, frenchToEnglish

class english_to_french(unittest.TestCase):
    def test1_1(self):
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)
    def test1_2(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")

class french_to_english(unittest.TestCase):
    def test2_1(self):
        self.assertNotEqual(frenchToEnglish("Rien"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)
    def test2_2(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()