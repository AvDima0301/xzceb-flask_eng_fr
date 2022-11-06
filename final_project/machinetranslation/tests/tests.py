import unittest
from ibm_cloud_sdk_core import ApiException
from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(None), "")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(None), "")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()