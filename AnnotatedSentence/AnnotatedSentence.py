from io import TextIOWrapper

from Corpus.Sentence import Sentence
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from PropBank.FramesetList import FramesetList
from WordNet.WordNet import WordNet

from AnnotatedSentence.AnnotatedWord import AnnotatedWord


class AnnotatedSentence(Sentence):

    __fileName: str

    """
    Converts a simple sentence to an annotated sentence

    PARAMETERS
    ----------
    fileOrStr : str
        Simple sentence
    """

    def __init__(self, fileOrStr=None, fileName=None):
        self.words = []
        wordArray = []
        if fileOrStr is not None:
            if fileName is not None:
                self.__fileName = fileName
            if isinstance(fileOrStr, TextIOWrapper):
                line = fileOrStr.readline()
                wordArray = line.rstrip().split(" ")
            elif isinstance(self, str):
                wordArray = fileOrStr.split(" ")
            for word in wordArray:
                if len(word) > 0:
                    self.words.append(AnnotatedWord(word))

    """
    The method constructs all possible shallow parse groups of a sentence.
    
    RETURNS
    -------
    list
        Shallow parse groups of a sentence.
    """
    def getShallowParseGroups(self) -> list:
        shallowParseGroups = []
        previousWord = None
        current = None
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if previousWord is None:
                    current = AnnotatedSentence()
                else:
                    if isinstance(previousWord, AnnotatedWord) and previousWord.getShallowParse() is not None \
                            and previousWord.getShallowParse() != word.getShallowParse():
                        shallowParseGroups.append(current)
                        current = AnnotatedSentence()
                current.addWord(word)
                previousWord = word
        shallowParseGroups.append(current)
        return shallowParseGroups

    """
    The method checks all words in the sentence and returns true if at least one of the words is annotated with
    PREDICATE tag.

    RETURNS
    -------
    bool
        True if at least one of the words is annotated with PREDICATE tag; False otherwise.
    """

    def containsPredicate(self) -> bool:
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if word.getArgument() is not None and word.getArgument().getArgumentType() == "PREDICATE":
                    return True
        return False

    def updateConnectedPredicate(self, previousId: str, currentId: str) -> bool:
        modified = False
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if word.getArgument() is not None and word.getArgument().getId() is not None and \
                        word.getArgument().getId() == previousId:
                    word.setArgument(word.getArgument().getArgumentType() + "$" + currentId)
                    modified = True
        return modified

    """
    The method returns all possible words, which is
    1. Verb
    2. Its semantic tag is assigned
    3. A frameset exists for that semantic tag

    PARAMETERS
    ----------
    framesetList : FramesetList
        Frameset list that contains all frames for Turkish
        
    RETURNS
    -------
    A list of words, which are verbs, semantic tags assigned, and framesetlist assigned for that tag.
    """

    def predicateCandidates(self, framesetList: FramesetList) -> list:
        candidateList = []
        for word in self.words:
            if isinstance(word, AnnotatedWord):
                if word.getParse() is not None and word.getParse().isVerb() and word.getSemantic() is not None \
                        and framesetList.frameExists(word.getSemantic()):
                    candidateList.append(word)
        for i in range(2):
            for j in range(len(self.words) - i - 1):
                annotatedWord = self.words[j]
                nextAnnotatedWord = self.words[j + 1]
                if isinstance(annotatedWord, AnnotatedWord) and isinstance(nextAnnotatedWord, AnnotatedWord):
                    if annotatedWord not in candidateList and nextAnnotatedWord in candidateList \
                            and annotatedWord.getSemantic() is not None \
                            and annotatedWord.getSemantic() == nextAnnotatedWord.getSemantic():
                        candidateList.append(annotatedWord)
        return candidateList

    """
    Returns the nearest predicate to the index'th word in the sentence.

    PARAMETERS
    ----------
    index : int
        Word index
        
    RETURNS
    -------
    str
        The nearest predicate to the index'th word in the sentence.
    """

    def getPredicate(self, index: int) -> str:
        count1 = 0
        count2 = 0
        data = ""
        word = []
        parse = []
        if index < self.wordCount():
            for i in range(self.wordCount()):
                word.append(self.getWord(i))
                parse.append(self.getWord(i).getParse())
            for i in range(index, -1, -1):
                if parse[i] is not None and parse[i].getRootPos() is not None and parse[i].getPos() is not None \
                        and parse[i].getRootPos() == "VERB" and parse[i].getPos() == "VERB":
                    count1 = index - i
                    break
            for i in range(index, self.wordCount() - index):
                if parse[i] is not None and parse[i].getRootPos() is not None and parse[i].getPos() is not None \
                        and parse[i].getRootPos() == "VERB" and parse[i].getPos() == "VERB":
                    count2 = i - index
                    break
            if count1 > count2:
                data = word[count1].getName()
            else:
                data = word[count2].getName()
        return data

    """
    Returns file name of the sentence

    RETURNS
    -------
    str
        File name of the sentence
    """
    def getFileName(self) -> str:
        return self.__fileName

    """
    Removes the i'th word from the sentence

    PARAMETERS
    ----------
    index : int
        Word index
    """

    def removeWord(self, index: int):
        self.words.pop(index)

    """
    Saves the current sentence.
    """
    def save(self):
        self.writeToFile(self.__fileName)

    """
    Creates a list of literal candidates for the i'th word in the sentence. It combines the results of
    1. All possible root forms of the i'th word in the sentence
    2. All possible 2-word expressions containing the i'th word in the sentence
    3. All possible 3-word expressions containing the i'th word in the sentence

    PARAMETERS
    ----------
    wordNet : WordNet
        Turkish wordnet
    fsm : FsmMorphologicalAnalyzer
        Turkish morphological analyzer
    wordIndex : int
        Word index
        
    RETURNS
    -------
    list
        List of literal candidates containing all possible root forms and multiword expressions.
    """

    def constructLiterals(self, wordNet: WordNet, fsm: FsmMorphologicalAnalyzer, wordIndex: int) -> list:
        word = self.getWord(wordIndex)
        possibleLiterals = []
        if isinstance(word, AnnotatedWord):
            morphologicalParse = word.getParse()
            metamorphicParse = word.getMetamorphicParse()
            possibleLiterals.extend(wordNet.constructLiterals(morphologicalParse.getWord().getName(),
                                                              morphologicalParse, metamorphicParse, fsm))
            firstSucceedingWord = None
            secondSucceedingWord = None
            if self.wordCount() > wordIndex + 1:
                firstSucceedingWord = self.getWord(wordIndex + 1)
                if self.wordCount() > wordIndex + 2:
                    secondSucceedingWord = self.getWord(wordIndex + 2)
            if firstSucceedingWord is not None and isinstance(firstSucceedingWord, AnnotatedWord):
                if secondSucceedingWord is not None and isinstance(secondSucceedingWord, AnnotatedWord):
                    possibleLiterals.extend(wordNet.constructIdiomLiterals(fsm, word.getParse(),
                                                                           word.getMetamorphicParse(),
                                                                           firstSucceedingWord.getParse(),
                                                                           firstSucceedingWord.getMetamorphicParse(),
                                                                           secondSucceedingWord.getParse(),
                                                                           secondSucceedingWord.getMetamorphicParse()))
                possibleLiterals.extend(wordNet.constructIdiomLiterals(fsm, word.getParse(), word.getMetamorphicParse(),
                                                                       firstSucceedingWord.getParse(),
                                                                       firstSucceedingWord.getMetamorphicParse()))
        return possibleLiterals

    """
    Creates a list of synset candidates for the i'th word in the sentence. It combines the results of
    1. All possible synsets containing the i'th word in the sentence
    2. All possible synsets containing 2-word expressions, which contains the i'th word in the sentence
    3. All possible synsets containing 3-word expressions, which contains the i'th word in the sentence

    PARAMETERS
    ----------
    wordNet : WordNet
        Turkish wordnet
    fsm : FsmMorphologicalAnalyzer
        Turkish morphological analyzer
    wordIndex : int
        Word index
        
    RETURNS
    -------
    list
        List of synset candidates containing all possible root forms and multiword expressions.
    """
    def constructSynSets(self, wordNet: WordNet, fsm: FsmMorphologicalAnalyzer, wordIndex: int) -> list:
        word = self.getWord(wordIndex)
        possibleSynSets = []
        if isinstance(word, AnnotatedWord):
            morphologicalParse = word.getParse()
            metamorphicParse = word.getMetamorphicParse()
            possibleSynSets.extend(wordNet.constructSynSets(morphologicalParse.getWord().getName(),
                                                            morphologicalParse, metamorphicParse, fsm))
            firstPrecedingWord = None
            secondPrecedingWord = None
            firstSucceedingWord = None
            secondSucceedingWord = None
            if wordIndex > 0:
                firstPrecedingWord = self.getWord(wordIndex - 1)
                if wordIndex > 1:
                    secondPrecedingWord = self.getWord(wordIndex - 2)
            if self.wordCount() > wordIndex + 1:
                firstSucceedingWord = self.getWord(wordIndex + 1)
                if self.wordCount() > wordIndex + 2:
                    secondSucceedingWord = self.getWord(wordIndex + 2)
            if firstPrecedingWord is not None and isinstance(firstPrecedingWord, AnnotatedWord):
                if secondPrecedingWord is not None and isinstance(secondPrecedingWord, AnnotatedWord):
                    possibleSynSets.extend(wordNet.constructIdiomSynSets(fsm, secondPrecedingWord.getParse(),
                                                                         secondPrecedingWord.getMetamorphicParse(),
                                                                         firstPrecedingWord.getParse(),
                                                                         firstPrecedingWord.getMetamorphicParse(),
                                                                         word.getParse(), word.getMetamorphicParse()))
                possibleSynSets.extend(wordNet.constructIdiomSynSets(fsm, firstPrecedingWord.getParse(),
                                                                     firstPrecedingWord.getMetamorphicParse(),
                                                                     word.getParse(), word.getMetamorphicParse()))
            if firstSucceedingWord is not None and isinstance(firstSucceedingWord, AnnotatedWord):
                if secondSucceedingWord is not None and isinstance(secondSucceedingWord, AnnotatedWord):
                    possibleSynSets.extend(wordNet.constructIdiomSynSets(fsm, word.getParse(),
                                                                         word.getMetamorphicParse(),
                                                                         firstSucceedingWord.getParse(),
                                                                         firstSucceedingWord.getMetamorphicParse(),
                                                                         secondSucceedingWord.getParse(),
                                                                         secondSucceedingWord.getMetamorphicParse()))
                possibleSynSets.extend(wordNet.constructIdiomSynSets(fsm, word.getParse(), word.getMetamorphicParse(),
                                                                     firstSucceedingWord.getParse(),
                                                                     firstSucceedingWord.getMetamorphicParse()))
        return possibleSynSets
