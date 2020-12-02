from FrameNet.FrameNet import FrameNet

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from AnnotatedSentence.AutoProcessor.AutoPredicate.SentenceAutoFramePredicate import SentenceAutoFramePredicate


class TurkishSentenceAutoFramePredicate(SentenceAutoFramePredicate):

    __frameNet: FrameNet

    def __init__(self, frameNet: FrameNet):
        """
        Constructor for TurkishSentenceAutoFramePredicate. Gets the Frames as input from the user, and sets
        the corresponding attribute.

        PARAMETERS
        ----------
        frameNet : FrameNet
            FrameNet containing the Turkish frameNet frames.
        """
        self.__frameNet = frameNet

    def autoPredicate(self, sentence: AnnotatedSentence) -> bool:
        """
        The method uses predicateFrameCandidates method to predict possible predicates. For each candidate, it sets for that
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
        candidateList = sentence.predicateFrameCandidates(self.__frameNet)
        for word in candidateList:
            if isinstance(word, AnnotatedWord):
                word.setFrameElement("PREDICATE$NONE$" + word.getSemantic())
        if len(candidateList) > 0:
            return True
        return False
