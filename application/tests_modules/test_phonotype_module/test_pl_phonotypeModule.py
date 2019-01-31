from pipe import Pipe
from queue import Queue
from threading import Condition
from phonotype_module import PhonotypeModule
from word import Text, TextPhonotypes
from constants import SONOR, CONS, VOWEL, SPEC, SUBUNIT
from end import End
from config_data import ConfigData
from pathlib import Path
import unittest

class TestPlPhonotypeModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mod.start()

    @classmethod
    def tearDownClass(cls):
        run_through_module(End())

    def test_maria(self):
        word = run_through_module(Text('maria'))
        self.assertEqual(word.get_text(), 'maria')
        self.assertEqual(word.get_phonotypes(), [SONOR, VOWEL, SONOR, SUBUNIT, VOWEL])

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

data = ConfigData(str(Path(__file__).parents[2]) + '\config\conf_pl_lat.json')
pin = Pipe(Queue(), Condition())
pout = Pipe(Queue(), Condition())
mod = PhonotypeModule([pin, pout], data)

if __name__ == '__main__':
    unittest.main()
