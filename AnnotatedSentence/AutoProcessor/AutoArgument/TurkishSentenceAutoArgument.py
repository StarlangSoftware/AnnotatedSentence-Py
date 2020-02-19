from MorphologicalAnalysis.MorphologicalTag import MorphologicalTag

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from AnnotatedSentence.AutoProcessor.AutoArgument.SentenceAutoArgument import SentenceAutoArgument


class TurkishSentenceAutoArgument(SentenceAutoArgument):

    def autoArgument(self, sentence: AnnotatedSentence) -> bool:
        """
        Given the sentence for which the predicate(s) were determined before, this method automatically assigns
        semantic role labels to some/all words in the sentence. The method first finds the first predicate, then
        assuming that the shallow parse tags were preassigned, assigns ÖZNE tagged words ARG0; NESNE tagged words ARG1.
        If the verb is in passive form, ÖZNE tagged words are assigned as ARG1.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which semantic roles will be determined automatically.

        RETURNS
        -------
        bool
            If the method assigned at least one word a semantic role label, the method returns true; false otherwise.
        """
        modified = False
        predicateId = None
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            if isinstance(word, AnnotatedWord):
                if word.getArgument() is not None and word.getArgument().getArgumentType() == "PREDICATE":
                    predicateId = word.getArgument().getId()
                    break
        if predicateId is not None:
            for i in range(sentence.wordCount()):
                word = sentence.getWord(i)
                if isinstance(word, AnnotatedWord) and word.getArgument() is None:
                    if word.getShallowParse() is not None and word.getShallowParse() == "ÖZNE":
                        if word.getParse() is not None and word.getParse().containsTag(MorphologicalTag.PASSIVE):
                            word.setArgument("ARG1$" + predicateId)
                        else:
                            word.setArgument("ARG0$" + predicateId)
                        modified = True
                    else:
                        if word.getShallowParse() is not None and word.getShallowParse() == "NESNE":
                            word.setArgument("ARG1$" + predicateId)
                            modified = True
        return modified
