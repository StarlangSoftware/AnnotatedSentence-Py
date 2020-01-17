from Corpus.Sentence import Sentence


class AnnotatedPhrase(Sentence):

    __wordIndex: int
    __tag: str

    """
    Constructor for AnnotatedPhrase. AnnotatedPhrase stores information about phrases such as
    Shallow Parse phrases or named entity phrases.
    
    PARAMETERS
    ----------
    wordIndex : int
        Starting index of the first word in the phrase w.r.t. original sentence the phrase occurs.
    tag : str
        Tag of the phrase. Corresponds to the shallow parse or named entity tag.
    """
    def __init__(self, wordIndex: int, tag: str):
        super().__init__()
        self.__wordIndex = wordIndex
        self.__tag = tag

    """
    Accessor for the wordIndex attribute.
    
    RETURNS
    -------
    int
        Starting index of the first word in the phrase w.r.t. original sentence the phrase occurs.
    """
    def getWordIndex(self) -> int:
        return self.__wordIndex

    """
    Accessor for the tag attribute.
    
    RETURNS
    -------
    str
        Tag of the phrase. Corresponds to the shallow parse or named entity tag.
    """
    def getTag(self) -> str:
        return self.__tag
