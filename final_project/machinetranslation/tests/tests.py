import unittest
from ibm_cloud_sdk_core import ApiException
from translator import englishToFrench, frenchToEnglish 
print(englishToFrench('Hello'))
print(frenchToEnglish('Bonjour'))
print(englishToFrench(""))
print(frenchToEnglish(""))

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench("Hello"),"Hello")
        self.assertEqual(englishToFrench(""),None)


class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish("Bonjour"),"Bonjour")
        self.assertEqual(frenchToEnglish(""),None)

unittest.main()