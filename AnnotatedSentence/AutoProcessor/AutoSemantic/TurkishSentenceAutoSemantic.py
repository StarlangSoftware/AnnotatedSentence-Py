from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from WordNet.WordNet import WordNet

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from AnnotatedSentence.AutoProcessor.AutoSemantic.SentenceAutoSemantic import SentenceAutoSemantic


class TurkishAutoSemantic(SentenceAutoSemantic):

    __turkishWordNet: WordNet
    __fsm: FsmMorphologicalAnalyzer

    def __init__(self, turkishWordNet: WordNet, fsm: FsmMorphologicalAnalyzer):
        """
        Constructor for the {@link TurkishSentenceAutoSemantic} class. Gets the Turkish wordnet and Turkish fst based
        morphological analyzer from the user and sets the corresponding attributes.

        PARAMETERS
        ----------
        turkishWordNet : WordNet
            Turkish wordnet
        fsm : FsmMorphologicalAnalyzer
            Turkish morphological analyzer
        """
        self.__turkishWordNet = turkishWordNet
        self.__fsm = fsm

    def autoLabelSingleSemantics(self, sentence: AnnotatedSentence):
        """
        The method checks
        1. the previous two words and the current word; the previous, current and next word, current and the next
        two words for a three word multiword expression that occurs in the Turkish wordnet.
        2. the previous word and current word; current word and the next word for a two word multiword expression that
        occurs in the Turkish wordnet.
        3. the current word
        if it has only one sense. If there is only one sense for that multiword expression or word; it sets that sense.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which word sense disambiguation will be determined automatically.
        """
        for i in range(sentence.wordCount()):
            current = sentence.getWord(i)
            if i > 1:
                twoPrevious = sentence.getWord(i - 2)
            if i > 0:
                previous = sentence.getWord(i - 1)
            if i != sentence.wordCount() - 1:
                next = sentence.getWord(i + 1)
            if i < sentence.wordCount() - 2:
                twoNext = sentence.getWord(i + 2)
            if isinstance(current, AnnotatedWord) and current.getSemantic() is None and current.getParse() is not None:
                if twoPrevious is not None and isinstance(twoPrevious, AnnotatedWord) \
                        and twoPrevious.getParse() is not None and isinstance(previous, AnnotatedWord) \
                        and previous.getParse() is not None:
                    idioms = self.__turkishWordNet.constructIdiomSynSets(self.__fsm, twoPrevious.getParse(),
                                                                         twoPrevious.getMetamorphicParse(),
                                                                         previous.getParse(),
                                                                         previous.getMetamorphicParse(),
                                                                         current.getParse(),
                                                                         current.getMetamorphicParse())
                    if len(idioms) == 1:
                        current.setSemantic(idioms[0].getId())
                        continue
                if previous is not None and isinstance(previous, AnnotatedWord) \
                        and previous.getParse() is not None and next is not None and isinstance(next, AnnotatedWord) \
                        and next.getParse() is not None:
                    idioms = self.__turkishWordNet.constructIdiomSynSets(self.__fsm, previous.getParse(),
                                                                         previous.getMetamorphicParse(),
                                                                         current.getParse(),
                                                                         current.getMetamorphicParse(),
                                                                         next.getParse(),
                                                                         next.getMetamorphicParse())
                    if len(idioms) == 1:
                        current.setSemantic(idioms[0].getId())
                        continue
                if next is not None and isinstance(next, AnnotatedWord) \
                        and next.getParse() is not None and twoNext is not None and isinstance(twoNext, AnnotatedWord) \
                        and twoNext.getParse() is not None:
                    idioms = self.__turkishWordNet.constructIdiomSynSets(self.__fsm, current.getParse(),
                                                                         current.getMetamorphicParse(),
                                                                         next.getParse(),
                                                                         next.getMetamorphicParse(),
                                                                         twoNext.getParse(),
                                                                         twoNext.getMetamorphicParse())
                    if len(idioms) == 1:
                        current.setSemantic(idioms[0].getId())
                        continue
                if previous is not None and isinstance(previous, AnnotatedWord) and previous.getParse() is not None:
                    idioms = self.__turkishWordNet.constructIdiomSynSets(self.__fsm, previous.getParse(),
                                                                         previous.getMetamorphicParse(),
                                                                         current.getParse(),
                                                                         current.getMetamorphicParse())
                    if len(idioms) == 1:
                        current.setSemantic(idioms[0].getId())
                        continue
                if next is not None and isinstance(next, AnnotatedWord) and next.getParse() is not None:
                    idioms = self.__turkishWordNet.constructIdiomSynSets(self.__fsm, current.getParse(),
                                                                         current.getMetamorphicParse(),
                                                                         next.getParse(),
                                                                         next.getMetamorphicParse())
                    if len(idioms) == 1:
                        current.setSemantic(idioms[0].getId())
                        continue
                meanings = self.__turkishWordNet.constructSynSets(current.getParse().getWord().getName(),
                                                                  current.getParse(), current.getMetamorphicParse(),
                                                                  self.__fsm)
                if current.getSemantic() is None and len(meanings) == 1:
                    current.setSemantic(meanings[0].getId())
