""" Utility functions used in the package"""
import nltk

def color_this(text, color="W", handler="[word_cli]"):
    """
    Returned colored text for console
    Makes use of win_coloroma and colorama on windows

    Args:
        text: (str) Text to be printed using color
        color: (str) color to use
        handler: (str) info level to use
    """
    colors = {
        "R": '\033[1;31m',
        "B": '\033[1;37m',
        "Y": '\033[93m',
        "C": '\033[1;30m',
        "W": '\033[0m',
        "G": '\033[92m',
    }
    if handler:
        full_text = f'%s{handler} {text}'%(colors[color])
    else:
        full_text = f'%s{text}'%(colors[color])
    return full_text
        

def logo():
    """
    Return the header design for the package
    """    
    return """
                                                                ___   ___ 
    ||   / |  / /                           //   ) )  / /          / /    
    ||  /  | / /  ___      __      ___   / //        / /          / /     
    || / /||/ / //   ) ) //  ) ) //   ) / //        / /          / /      
    ||/ / |  / //   / / //      //   / / //        / /          / /       
    |  /  | / ((___/ / //      ((___/ / ((____/ / / /____/ / __/ /___     
     """

def download_corpus():
    """
    Tests for existing wordnet corpus and downloads if not existing
    """
    try:
        from nltk.corpus import wordnet, words
        wordnet.synsets("test")
        print(color_this("Found wordnet corpus"))
        words.words()
        print(color_this("Found words corpus"))
    except LookupError:
        print(color_this("Resource not found", "R"))
        print(color_this("Initiating WordNET, Words corpora download"))
        nltk.download('wordnet')
        nltk.download('words')

def texttospeech(engine, text):
    """
    Pronounce text as speech

        Args:
            engine: (pyttsx.engine) text to speech engine
            text: (str) to be pronounced
    """
    engine.say(text)
    engine.runAndWait()    

if __name__=="__main__":
    head = logo()
    print(color_this(head, "G", None))