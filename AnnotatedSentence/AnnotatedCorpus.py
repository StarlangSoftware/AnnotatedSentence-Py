import os
import re

from Corpus.Corpus import Corpus

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord


class AnnotatedCorpus(Corpus):

    def __init__(self, folder: str, pattern: str = None):
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
        self.sentences = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                fileName = os.path.join(root, file)
                if (pattern is None or pattern in fileName) and re.match("\\d+\\.", file):
                    f = open(fileName, "r", encoding='utf8')
                    sentence = AnnotatedSentence(f, fileName)
                    self.sentences.append(sentence)

    def exportUniversalDependencyFormat(self, outputFileName: str):
        file = open(outputFileName, "w")
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                file.write(sentence.getUniversalDependencyFormat())
        file.close()

    def checkMorphologicalAnalysis(self):
        """
        The method traverses all words in all sentences and prints the words which do not have a morphological analysis.
        """
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getParse() is None:
                            print("Morphological Analysis does not exist for sentence " + sentence.getFileName())
                            break

    def checkNer(self):
        """
        The method traverses all words in all sentences and prints the words which do not have named entity annotation.
        """
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getNamedEntityType() is None:
                            print("NER annotation does not exist for sentence " + sentence.getFileName())
                            break

    def checkShallowParse(self):
        """
        The method traverses all words in all sentences and prints the words which do not have shallow parse annotation.
        """
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getShallowParse() is None:
                            print("Shallow parse annotation does not exist for sentence " + sentence.getFileName())
                            break

    def checkSemantic(self):
        """
        The method traverses all words in all sentences and prints the words which do not have sense annotation.
        """
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                for j in range(sentence.wordCount()):
                    word = sentence.getWord(j)
                    if isinstance(word, AnnotatedWord):
                        if word.getSemantic() is None:
                            print("Semantic annotation does not exist for sentence " + sentence.getFileName())
                            break
