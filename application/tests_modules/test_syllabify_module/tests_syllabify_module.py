from pipe import Pipe
from queue import Queue
from threading import Condition
from syllabify_module import SyllabifyModule
from word import TextPhonotypes
from constants import SONOR, CONS, VOWEL, SPEC, SUBUNIT
from end import End
import unittest

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mod.start()

    @classmethod
    def tearDownClass(cls):
        run_through_module(End())

    def test_farmaceuticky(self):
        word = run_through_module(TextPhonotypes('farmaceutický',
                               [CONS, VOWEL, SONOR, SONOR, VOWEL, CONS, SUBUNIT, VOWEL, CONS, VOWEL, CONS, CONS,
                                VOWEL]))
        self.assertEqual(word.get_syllables(), ['fa', 'rma', 'ceu', 'ti', 'cký'])
        self.assertEqual(word.get_phonotypes(),
                        [[CONS, VOWEL], [SONOR, SONOR, VOWEL], [CONS, SUBUNIT, VOWEL], [CONS, VOWEL],
                         [CONS, CONS, VOWEL]])

    def test_pouze(self):
        word = run_through_module(TextPhonotypes('pouze', [CONS, SUBUNIT, VOWEL, CONS, VOWEL]))
        self.assertEqual(word.get_syllables(), ['pou', 'ze'])
        self.assertEqual(word.get_phonotypes(), [[CONS, SUBUNIT, VOWEL], [CONS, VOWEL]])

    def test_pouzil(self):
        word = run_through_module(TextPhonotypes('použil', [CONS, VOWEL, VOWEL, CONS, VOWEL, SONOR]))
        self.assertEqual(word.get_syllables(),['po', 'u', 'žil'])
        self.assertEqual(word.get_phonotypes(),[[CONS, VOWEL], [VOWEL], [CONS, VOWEL, SONOR]])

    def test_neurcity(self):
        word = run_through_module(TextPhonotypes('neurčitý', [SONOR, VOWEL, VOWEL, SONOR, CONS, VOWEL, CONS, VOWEL]))
        self.assertEqual(word.get_syllables(), ['ne', 'ur', 'či', 'tý'])
        self.assertEqual(word.get_phonotypes(), [[SONOR, VOWEL], [VOWEL, SONOR], [CONS, VOWEL], [CONS, VOWEL]])

    def test_automaticky(self):
        word = run_through_module(TextPhonotypes('automatický',
                                    [SUBUNIT, VOWEL, CONS, VOWEL, SONOR, VOWEL, CONS, VOWEL, CONS, CONS, VOWEL]))
        self.assertEqual(word.get_syllables(), ['au', 'to', 'ma', 'ti', 'cký'])
        self.assertEqual(word.get_phonotypes(), [[SUBUNIT, VOWEL], [CONS, VOWEL], [SONOR, VOWEL],
                                                  [CONS, VOWEL], [CONS, CONS, VOWEL]])

    def test_vlna(self):
        word = run_through_module(TextPhonotypes('vlna', [CONS, VOWEL, SONOR, VOWEL]))
        self.assertEqual(word.get_syllables(), ['vl', 'na'])
        self.assertEqual(word.get_phonotypes(), [[CONS, VOWEL], [SONOR, VOWEL]])

    def test_osm(self):
        word = run_through_module(TextPhonotypes('osm', [VOWEL, CONS, VOWEL]))
        self.assertEqual(word.get_syllables(), ['o', 'sm'])
        self.assertEqual(word.get_phonotypes(), [[VOWEL], [CONS, VOWEL]])

    def test_bijologije(self):
        word = run_through_module(TextPhonotypes('bijologije', [CONS, VOWEL, SONOR, VOWEL,
                                                                SONOR, VOWEL, CONS, VOWEL, SONOR, VOWEL]))
        self.assertEqual(word.get_syllables(), ['bi', 'jo', 'lo', 'gi', 'je'])
        self.assertEqual(word.get_phonotypes(), [[CONS, VOWEL], [SONOR, VOWEL], [SONOR, VOWEL],
                                                  [CONS, VOWEL], [SONOR, VOWEL]])

    def test_srozpadem(self):
        word = run_through_module(TextPhonotypes('srozpadem',
                                                 [CONS, SONOR, VOWEL, CONS, CONS, VOWEL, CONS, VOWEL, SONOR]))
        self.assertEqual(word.get_syllables(), ['sro', 'zpa', 'dem'])
        self.assertEqual(word.get_phonotypes(), [[CONS, SONOR, VOWEL], [CONS, CONS, VOWEL], [CONS, VOWEL, SONOR]])

    def test_vedomi(self):
        word = run_through_module(TextPhonotypes('vědomí', [CONS, VOWEL, CONS, VOWEL, SONOR, VOWEL]))
        self.assertEqual(word.get_syllables(), ['vě', 'do', 'mí'])
        self.assertEqual(word.get_phonotypes(), [[CONS, VOWEL], [CONS, VOWEL], [SONOR, VOWEL]])

    def test_sex(self):
        word = run_through_module(TextPhonotypes('sex', [CONS, VOWEL, CONS]))
        self.assertEqual(word.get_syllables(), ['sex'])
        self.assertEqual(word.get_phonotypes(), [[CONS, VOWEL, CONS]])

    def test_wrobl(self):
        word = run_through_module(TextPhonotypes('wrobl', [SONOR, SONOR, VOWEL, CONS, VOWEL]))
        self.assertEqual(word.get_syllables(), ['wro', 'bl'])
        self.assertEqual(word.get_phonotypes(), [[SONOR, SONOR, VOWEL], [CONS, VOWEL]])

    def test_sneh(self):
        word = run_through_module(TextPhonotypes('sněh', [CONS, SONOR, VOWEL, CONS]))
        self.assertEqual(word.get_syllables(), ['sněh'])
        self.assertEqual(word.get_phonotypes(), [[CONS, SONOR, VOWEL, CONS]])

    def test_sahac(self):
        word = run_through_module(TextPhonotypes('sahać', [CONS, VOWEL, CONS, VOWEL, CONS]))
        self.assertEqual(word.get_syllables(), ['sa', 'hać'])
        self.assertEqual(word.get_phonotypes(), [[CONS, VOWEL,], [CONS, VOWEL, CONS]])

    def test_українськогож(self):
        word = run_through_module(TextPhonotypes('українськогож', [VOWEL, CONS, SONOR, VOWEL, VOWEL, SONOR, CONS,
                                                                       SPEC, CONS, VOWEL, CONS, VOWEL, CONS]))
        self.assertEqual(word.get_syllables(), ['у', 'кра', 'їн', 'сько', 'гож'])
        self.assertEqual(word.get_phonotypes(), [[VOWEL], [CONS, SONOR, VOWEL], [VOWEL, SONOR],
                                                  [CONS, SPEC, CONS, VOWEL], [CONS, VOWEL, CONS]])

    def test_rz(self):
        word = run_through_module(TextPhonotypes('rž', [VOWEL, CONS]))
        self.assertEqual(word.get_syllables(), ['rž'])
        self.assertEqual(word.get_phonotypes(), [[VOWEL, CONS]])

    def test_maria(self):
        word = run_through_module(TextPhonotypes('maria', [SONOR, VOWEL, SONOR, SUBUNIT, VOWEL]))
        self.assertEqual(word.get_syllables(), ['ma', 'ria'])
        self.assertEqual(word.get_phonotypes(), [[SONOR, VOWEL], [SONOR, SUBUNIT, VOWEL]])


def run_through_module(word):
    pin.acquire()
    pin.put(word)
    pin.notify()
    pin.release()
    pout.acquire()
    if pout.empty():
        pout.wait()
    word = pout.get()
    pout.release()
    return word



pin = Pipe(Queue(), Condition())
pout = Pipe(Queue(), Condition())
mod = SyllabifyModule([pin, pout])

if __name__ == '__main__':
    unittest.main()

