import unittest
from decompose import decompose


class TestsCase(unittest.TestCase):
    diacritics = 'éàèùâêîôûëïüÿçñ'
    decomposed_diacritics = 'eaeuaeioueiuycn'
    ligatures = 'œæ'
    decomposed_ligatures = 'oeae'

    def test_diacritics(self):
        self.assertEqual(
            self.decomposed_diacritics,
            decompose(self.diacritics)
        )

    def test_capitalized_diacritics(self):
        self.assertEqual(
            self.decomposed_diacritics.upper(),
            decompose(self.diacritics.upper())
        )

    def test_ligatures(self):
        self.assertEqual(
            self.decomposed_ligatures,
            decompose(self.ligatures)
        )

    def test_capitalized_ligatures(self):
        self.assertEqual('Oe', decompose(u'\N{Latin capital ligature OE}'))
        self.assertEqual('Ae', decompose(u'\N{Latin capital letter AE}'))

    def test_german_sharp_s(self):
        print(f"ß {self.ligatures.upper().lower()}")
        self.assertEqual('ss', decompose('ß'))
        self.assertEqual('SS', decompose('ẞ'))






if __name__ == '__main__':
    unittest.main()