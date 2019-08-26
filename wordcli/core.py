""" Implements the core Dictionary parser class used in the package """
import nltk
from nltk.corpus import wordnet

class WordDoesNotExist(Exception):
    """ Base exception for a non-existent word in the dictionary """
    pass

class Dictionary:
    """
    Embeds all information available about a particular word available from 
    """
    def __init__(self, word):
        """
        Args:
            word: (str) word to obtain info from wordnet corpus
        """
        self.word = self.set_word(word)
        self.syn = wordnet.synsets(self.word)
        
    @property
    def definitions(self):
        """
        Returns definition dictionary for word

        Returns:
            def_: (dict) dictionary of words and meanings
        """
        def_ = dict()
        
        for i in self.syn:
            def_[i.name()] = i.definition()
        return def_

    @property
    def examples(self):
        """
        Example usage sentences

        Returns:
            exmpl_: (list) example statements 
        """
        exmpl_ = list()
        for i in self.syn:
            # show only examples where the word is exactly the same as request
            if i.name().rsplit('.', 2)[0] == self.word:
                for case in i.examples():
                    exmpl_.append(case)
        return exmpl_

    @property
    def antonyms(self):
        """
        Antonyms of word

        Returns:
            anton_: (set) antonym words
        """
        anton_ = set()
        for syn in self.syn:
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    anton_.add(lemma.antonyms()[0].name())
        return anton_

    @property
    def synonyms(self):
        """
        Synonyms of word

        Returns:
            syns_: (set) synonyms of word
        """
        syns_ = set()
        for i in self.syn:
            word = i.name().rsplit('.', 2)[0]
            syns_.add(word)
        # try to remove the original word if it is counted as synonym
        try:
            syns_.remove(self.word)
        except KeyError:
            pass
        return syns_

    def set_word(self, word):
        """
        Set the word to be used in to search wordnet

            Raises:
                WordDoesNotExist: word does not exist in wordnet dictionary
        """
        english_vocab = set(w.lower() for w in nltk.corpus.words.words())
        if word.lower() in english_vocab:
            return word.lower()
        else:
            raise WordDoesNotExist

    def __len__(self):
        return len(self.syn)