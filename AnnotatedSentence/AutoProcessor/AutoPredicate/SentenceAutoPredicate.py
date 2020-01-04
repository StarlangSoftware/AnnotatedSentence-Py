from abc import abstractmethod

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence


class SentenceAutoPredicate:

    """
    The method should set determine all predicates in the sentence.

    PARAMETERS
    ----------
    sentence : AnnotatedSentence
        The sentence for which predicates will be determined automatically.
    """
    @abstractmethod
    def autoPredicate(self, sentence: AnnotatedSentence) -> bool:
        pass
