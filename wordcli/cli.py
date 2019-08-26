#! /usr/bin/env python
"""
Implements the command line interface handler
"""
import os
import sys
import pyttsx3
#sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# import libraries
from utils import color_this, download_corpus, logo, texttospeech
from core import Dictionary, WordDoesNotExist


def introduction():
    """
    CLI intoduction
    """
    print(color_this(logo(), "G", None))
    print(color_this("\nWord CLI is a command line based dictionary implementation that uses WordNET and NLTK\n", "C", None))

def section(header, itr):
    """
    Print Header of section if iterable length is over one

        Args:
            header:  (str) Section header
            itr: (iterable) iterable to print
    """
    if len(itr) >= 1:
        print(color_this(header, 'G', None))
        for i in itr:
            print(color_this(i, "W", None))
        print("\n\n")

def main():
    """
    Cli function to be installed by setup script
    """
    
    # OS Compatibility : Coloring
       
    if sys.platform.startswith('win'):
        try:
            import win_unicode_console, colorama
            win_unicode_console.enable()
            colorama.init()
        except:
            print(color_this('Error: Coloring libraries not installed', "R"))
            sys.exit()
    introduction()
    # test out corpus existence, else download
    download_corpus()

    # initialize speech engine
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
    except:
        print(color_this("Please install espeak"))
        sys.exit()
        
    # endless loop until ctrl+c is pressed
    try:
        while True:
            # reset the color
            print(color_this("", "W", None))
            lookup = input("Enter a word you would like to lookup: ")
            try:
                dic = Dictionary(lookup)
            except WordDoesNotExist as ex:
                print(color_this("The word you are searching for does not exist! \n", "R"))
                continue
            else:
                print('\n Synset length', len(dic), '\n\n')
        
                print(color_this('__Definitions__', 'G', None))
                for word, definitions in dic.definitions.items():
                    print(color_this(f"'{word}'  -> {definitions}", "W", None))
                print("\n\n")
                
                section_arguments = (
                    ('__Examples__', dic.examples),
                    ('__Synonyms__', dic.synonyms),
                    ('__Antonyms__', dic.antonyms),
                )
                
                for i in section_arguments:
                    section(*i)
            pronounce_word = input("Do you want me to pronounce the word? [Y/n]")
            if pronounce_word in ("Y", "y", "Yes", "yes"):
                texttospeech(engine, lookup)
            else:
                print(color_this("I'll assume that's a no on the pronunciation"))            
    except KeyboardInterrupt:
        print(color_this("\nClosing now...", "Y"))
        sys.exit()

if __name__=="__main__":
    main()