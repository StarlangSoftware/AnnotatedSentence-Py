from __future__ import annotations

import os
import re

from Corpus.Corpus import Corpus

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from DependencyParser.ParserEvaluationScore import ParserEvaluationScore


class AnnotatedCorpus(Corpus):

    def __init__(self,
                 folder: str,
                 pattern: str = None):
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
                file_name = os.path.join(root, file)
                if (pattern is None or pattern in file_name) and re.match("\\d+\\.", file):
                    f = open(file_name, "r", encoding='utf8')
                    sentence = AnnotatedSentence(f, file_name)
                    self.sentences.append(sentence)

    def compareParses(self, corpus: AnnotatedCorpus) -> ParserEvaluationScore:
        """
        Compares the corpus with the given corpus and returns a parser evaluation score for this comparison. The result
        is calculated by summing up the parser evaluation scores of sentence by sentence dependency relation comparisons.
        :param corpus: Corpus to be compared.
        :return: A parser evaluation score object.
        """
        result = ParserEvaluationScore()
        for i in range(len(self.sentences)):
            sentence1 = self.sentences[i]
            sentence2 = corpus.getSentence(i)
            result.add(sentence1.compareParses(sentence2))
        return result

    def exportUniversalDependencyFormat(self,
                                        outputFileName: str,
                                        path: str = None):
        """
        Exports the annotated corpus as a UD file in connlu format. Every sentence is converted into connlu format and
        appended to the output file. Multiple paths are possible in the annotated corpus. This method outputs the
        sentences in the given path.
        :param outputFileName: Output file name in connlu format.
        :param path: Current path for the part of the annotated corpus.
        """
        file = open(outputFileName, "w")
        for i in range(self.sentenceCount()):
            sentence = self.getSentence(i)
            if isinstance(sentence, AnnotatedSentence):
                file.write(sentence.getUniversalDependencyFormat(path))
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
