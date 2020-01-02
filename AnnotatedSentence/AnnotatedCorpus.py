from Corpus.Corpus import Corpus
import os

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord


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
                    sentence = AnnotatedSentence(f, fileName)
                    self.sentences.append(sentence)

    """
    The method traverses all words in all sentences and prints the words which do not have a morphological analysis.
    """
    def checkMorphologicalAnalysis(self):
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getParse() is None:
                            print("Morphological Analysis does not exist for sentence " + sentence.getFileName())
                            break

    """
    The method traverses all words in all sentences and prints the words which do not have named entity annotation.
    """
    def checkNer(self):
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getNamedEntityType() is None:
                            print("NER annotation does not exist for sentence " + sentence.getFileName())
                            break

    """
    The method traverses all words in all sentences and prints the words which do not have shallow parse annotation.
    """
    def checkShallowParse(self):
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getShallowParse() is None:
                            print("Shallow parse annotation does not exist for sentence " + sentence.getFileName())
                            break

    """
    The method traverses all words in all sentences and prints the words which do not have sense annotation.
    """
    def checkSemantic(self):
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getSemantic() is None:
                            print("Semantic annotation does not exist for sentence " + sentence.getFileName())
                            break
