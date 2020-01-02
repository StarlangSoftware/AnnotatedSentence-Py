from Corpus.Corpus import Corpus
import os

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence


class AnnotatedCorpus(Corpus):

    """
    A constructor of AnnotatedCorpus class which reads all AnnotatedSentence files with the file
    name satisfying the given pattern inside the given folder. For each file inside that folder, the constructor
    creates an AnnotatedSentence and puts in inside the list parseTrees.

    PARAMETERS
    ----------
    folder : str
        Folder where all sentences reside.
    pattern : str
        File pattern such as "." ".train" ".test".
    """
    def __init__(self, folder: str, pattern: str = None):
        self.sentences = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                fileName = os.path.join(root, file)
                if pattern is None or pattern in fileName:
                    f = open(fileName, "r")
                    sentence = AnnotatedSentence(f)
                    self.sentences.append(sentence)
