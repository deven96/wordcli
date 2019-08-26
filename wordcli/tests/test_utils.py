"""
Test the utility functions
"""
import nltk
from unittest import TestCase

from wordcli import utils

class TestCore(TestCase): 
    def test_color_function(self):
        """
        Check if color is correct word
        """
        word_cli = utils.color_this("String", "G")
        # check that text gets printed as green
        self.assertTrue(word_cli.startswith('\033[92m'))
        # check that [word_cli] isn't printed
        no_cli = utils.color_this("String", "G", None)
        self.assertFalse("[word_cli]" in no_cli)

    def test_corpus_download(self):
        """
        Download corpora and test with word
        """
        utils.download_corpus()
        self.assertTrue(nltk.data.find("corpora/wordnet.zip"))