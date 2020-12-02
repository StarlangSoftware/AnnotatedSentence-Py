from abc import abstractmethod

from FrameNet.FrameNet import FrameNet

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence


class SentenceAutoFramePredicate:

    frameNet: FrameNet

    @abstractmethod
    def autoPredicate(self, sentence: AnnotatedSentence) -> bool:
        """
        The method should set determine all predicates in the sentence.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which predicates will be determined automatically.
        """
        pass
