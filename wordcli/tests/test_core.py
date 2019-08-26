from unittest import TestCase

from wordcli import core

class TestCore(TestCase):
    case = core.Dictionary("valid")
    
    def test_is_valid_word(self):
        """
        Use a valid english word
        """
        self.assertTrue(isinstance(self.case, core.Dictionary))

    def test_is_invalid_word(self):
        """
        Assert exception is raised for invalid words
        """
        with self.assertRaises(core.WordDoesNotExist) as context:
            s = core.Dictionary("iaminvalid")

    def test_definitions_match_syn_length(self):
        """
        Definition dictionary should be same length as synset length
        """
        self.assertEqual(len(self.case.definitions), len(self.case))

    def test_word_not_in_synonyms(self):
        """
        Word should not reappear in synonym
        """
        self.assertFalse(self.case.word in self.case.synonyms)