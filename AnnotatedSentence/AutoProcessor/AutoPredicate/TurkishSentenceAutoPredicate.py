from PropBank.FramesetList import FramesetList

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from AnnotatedSentence.AutoProcessor.AutoPredicate.SentenceAutoPredicate import SentenceAutoPredicate


class TurkishSentenceAutoPredicate(SentenceAutoPredicate):

    __framesetList: FramesetList

    """
    Constructor for TurkishSentenceAutoPredicate. Gets the FrameSets as input from the user, and sets
    the corresponding attribute.

    PARAMETERS
    ----------
    framesetList : FramesetList
        FramesetList containing the Turkish propbank frames.
    """
    def __init__(self, framesetList: FramesetList):
        self.__framesetList = framesetList

    """
    The method uses predicateCandidates method to predict possible predicates. For each candidate, it sets for that
    word PREDICATE tag.

    PARAMETERS
    ----------
    sentence : AnnotatedSentence
        The sentence for which predicates will be determined automatically.

    RETURNS
    -------
    bool
        If at least one word has been tagged, true; false otherwise.
    """
    def autoPredicate(self, sentence: AnnotatedSentence) -> bool:
        candidateList = sentence.predicateCandidates(self.__framesetList)
        for word in candidateList:
            if isinstance(word, AnnotatedWord):
                word.setArgument("PREDICATE$" + word.getSemantic())
        if len(candidateList) > 0:
            return True
        return False
