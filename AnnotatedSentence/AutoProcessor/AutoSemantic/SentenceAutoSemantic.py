from abc import abstractmethod

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence


class SentenceAutoSemantic:

    @abstractmethod
    def autoLabelSingleSemantics(self, sentence: AnnotatedSentence):
        """
        The method should set the senses of all words, for which there is only one possible sense.

        PARAMETERS
        ----------
        sentence: AnnotatedSentence
            The sentence for which word sense disambiguation will be determined automatically.
        """
        pass

    def autoSemantic(self, sentence: AnnotatedSentence):
        self.autoLabelSingleSemantics(sentence)
