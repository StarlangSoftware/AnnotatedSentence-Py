from abc import abstractmethod

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence


class SentenceAutoArgument:

    @abstractmethod
    def autoArgument(self, sentence: AnnotatedSentence) -> bool:
        """
        The method should set all the semantic role labels in the sentence. The method assumes that the predicates
        of the sentences were determined previously.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which semantic roles will be determined automatically.
        """
        pass
