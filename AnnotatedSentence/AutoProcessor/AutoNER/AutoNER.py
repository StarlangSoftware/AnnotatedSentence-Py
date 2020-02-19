from abc import abstractmethod


from NamedEntityRecognition.AutoNER import AutoNER

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord


class SentenceAutoNER(AutoNER):

    @abstractmethod
    def autoDetectPerson(self, sentence: AnnotatedSentence):
        """
        The method should detect PERSON named entities. PERSON corresponds to people or
        characters. Example: {\bf Atatürk} yurdu düşmanlardan kurtardı.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which PERSON named entities checked.
        """
        pass

    @abstractmethod
    def autoDetectLocation(self, sentence: AnnotatedSentence):
        """
        The method should detect LOCATION named entities. LOCATION corresponds to regions,
        mountains, seas. Example: Ülkemizin başkenti Ankara'dır.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which LOCATION named entities checked.
        """
        pass

    @abstractmethod
    def autoDetectOrganization(self, sentence: AnnotatedSentence):
        """
        The method should detect ORGANIZATION named entities. ORGANIZATION corresponds to companies,
        teams etc. Example:  IMKB günü 60 puan yükselerek kapattı.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which ORGANIZATION named entities checked.
        """
        pass

    @abstractmethod
    def autoDetectMoney(self, sentence: AnnotatedSentence):
        """
        The method should detect MONEY named entities. MONEY corresponds to monetarial
        expressions. Example: Geçen gün 3000 TL kazandık.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which MONEY named entities checked.
        """
        pass

    @abstractmethod
    def autoDetectTime(self, sentence: AnnotatedSentence):
        """
        The method should detect TIME named entities. TIME corresponds to time
        expressions. Example: Cuma günü tatil yapacağım.

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which TIME named entities checked.
        """
        pass

    def autoNER(self, sentence: AnnotatedSentence):
        """
        The main method to automatically detect named entities in a sentence. The algorithm
        1. Detects PERSON(s).
        2. Detects LOCATION(s).
        3. Detects ORGANIZATION(s).
        4. Detects MONEY.
        5. Detects TIME.
        For not detected words, the algorithm sets the named entity "NONE".

        PARAMETERS
        ----------
        sentence : AnnotatedSentence
            The sentence for which named entities checked.
        """
        self.autoDetectPerson(sentence)
        self.autoDetectLocation(sentence)
        self.autoDetectOrganization(sentence)
        self.autoDetectMoney(sentence)
        self.autoDetectTime(sentence)
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            if isinstance(word, AnnotatedWord):
                if word.getNamedEntityType() is None:
                    word.setNamedEntityType("NONE")
