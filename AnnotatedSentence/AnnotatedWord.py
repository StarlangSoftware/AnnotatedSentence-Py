from Corpus.WordFormat import WordFormat
from DependencyParser.UniversalDependencyRelation import UniversalDependencyRelation
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmParse import FsmParse
from MorphologicalAnalysis.MetamorphicParse import MetamorphicParse
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse
from MorphologicalAnalysis.MorphologicalTag import MorphologicalTag
from NamedEntityRecognition.Gazetteer import Gazetteer
from NamedEntityRecognition.NamedEntityType import NamedEntityType
from PropBank.Argument import Argument

import re

from AnnotatedSentence.ViewLayerType import ViewLayerType


class AnnotatedWord(Word):
    __parse: MorphologicalParse
    __metamorphicParse: MetamorphicParse
    __semantic: str
    __namedEntityType: NamedEntityType
    __argument: Argument
    __shallowParse: str
    __universalDependency: UniversalDependencyRelation

    """
    Constructor for the AnnotatedWord class. Gets the word with its annotation layers as input and sets the
    corresponding layers.

    PARAMETERS
    ----------
    word : str
        Input word with annotation layers
    """

    def __init__(self, word: str, layerType=None):
        self.__parse = None
        self.__metamorphicParse = None
        self.__semantic = None
        self.__namedEntityType = None
        self.__argument = None
        self.__shallowParse = None
        self.__universalDependency = None
        if layerType is None:
            splitLayers = re.compile("[{}]").split(word)
            for layer in splitLayers:
                if len(layer) == 0:
                    continue
                if "=" not in layer:
                    self.name = layer
                    continue
                layerType = layer[:layer.index("=")]
                layerValue = layer[layer.index("=") + 1:]
                if layerType == "turkish":
                    self.name = layerValue
                elif layerType == "morphologicalAnalysis":
                    self.__parse = MorphologicalParse(layerValue)
                elif layerType == "metaMorphemes":
                    self.__metamorphicParse = MetamorphicParse(layerValue)
                elif layerType == "namedEntity":
                    self.__namedEntityType = NamedEntityType.getNamedEntityType(layerValue)
                elif layerType == "propbank":
                    self.__argument = Argument(layerValue)
                elif layerType == "shallowParse":
                    self.__shallowParse = layerValue
                elif layerType == "universalDependency":
                    values = layerValue.split("$")
                    self.__universalDependency = UniversalDependencyRelation(int(values[0]), values[1])
        elif isinstance(layerType, NamedEntityType):
            super().__init__(word)
            self.__namedEntityType = layerType
            self.__argument = Argument("NONE")
        elif isinstance(layerType, MorphologicalParse):
            super().__init__(word)
            self.__parse = layerType
            self.__namedEntityType = NamedEntityType.NONE
            self.__argument = Argument("NONE")
        elif isinstance(layerType, FsmParse):
            super().__init__(word)
            self.__parse = layerType
            self.__namedEntityType = NamedEntityType.NONE
            self.setMetamorphicParse(layerType.withList())
            self.__argument = Argument("NONE")

    """
    Converts an AnnotatedWord to string. For each annotation layer, the method puts a left brace, layer name,
    equal sign and layer value finishing with right brace.

    RETURNS
    -------
    str
        String form of the AnnotatedWord.
    """

    def __str__(self) -> str:
        result = "{turkish=" + self.name + "}"
        if self.__parse is not None:
            result = result + "{morphologicalAnalysis=" + self.__parse.__str__() + "}"
        if self.__metamorphicParse is not None:
            result = result + "{metaMorphemes=" + self.__metamorphicParse.__str__() + "}"
        if self.__semantic is not None:
            result = result + "{semantics=" + self.__semantic + "}"
        if self.__namedEntityType is not None:
            result = result + "{namedEntity=" + self.__namedEntityType.__str__() + "}"
        if self.__argument is not None:
            result = result + "{propbank=" + self.__argument.__str__() + "}"
        if self.__shallowParse is not None:
            result = result + "{shallowParse=" + self.__shallowParse + "}"
        if self.__universalDependency is not None:
            result = result + "{universalDependency=" + self.__universalDependency.to().__str__() + "$" + self.__universalDependency.__str__() + "}"
        return result

    """
    Returns the value of a given layer.

    PARAMETERS
    ----------
    viewLayerType : ViewLayerType
        Layer for which the value questioned.
        
    RETURNS
    -------
    str
        The value of the given layer.
    """

    def getLayerInfo(self, viewLayerType: ViewLayerType) -> str:
        if viewLayerType == ViewLayerType.INFLECTIONAL_GROUP:
            if self.__parse is not None:
                return self.__parse.__str__()
        elif viewLayerType == ViewLayerType.META_MORPHEME:
            if self.__metamorphicParse is not None:
                return self.__metamorphicParse.__str__()
        elif viewLayerType == ViewLayerType.SEMANTICS:
            return self.__semantic
        elif viewLayerType == ViewLayerType.NER:
            if self.__namedEntityType is not None:
                return self.__namedEntityType.__str__()
        elif viewLayerType == ViewLayerType.SHALLOW_PARSE:
            return self.__shallowParse
        elif viewLayerType == ViewLayerType.TURKISH_WORD:
            return self.name
        elif viewLayerType == ViewLayerType.PROPBANK:
            if self.__argument is not None:
                return self.__argument.__str__()
        elif viewLayerType == ViewLayerType.DEPENDENCY:
            if self.__universalDependency is not None:
                return self.__universalDependency.to().__str__() + "$" + self.__universalDependency.__str__()
        else:
            return None

    """
    Returns the morphological parse layer of the word.
    
    RETURNS
    -------
    MorphologicalParse
        The morphological parse of the word.
    """

    def getParse(self) -> MorphologicalParse:
        return self.__parse

    """
    Sets the morphological parse layer of the word.
    
    PARAMETERS
    ----------
    parseString : str
        The new morphological parse of the word in string form.
    """

    def setParse(self, parseString: MorphologicalParse):
        if parseString is not None:
            self.__parse = MorphologicalParse(parseString)
        else:
            self.__parse = None

    """
    Returns the metamorphic parse layer of the word.
    
    RETURNS
    -------
    MetamorphicParse
        The metamorphic parse of the word.
    """

    def getMetamorphicParse(self) -> MetamorphicParse:
        return self.__metamorphicParse

    """
    Sets the metamorphic parse layer of the word.

    PARAMETERS
    ----------
    parseString : str
        The new metamorphic parse of the word in string form.
    """

    def setMetamorphicParse(self, parseString: str):
        self.__metamorphicParse = MetamorphicParse(parseString)

    """
    Returns the semantic layer of the word.

    RETURNS
    -------
    str
        Sense id of the word.
    """

    def getSemantic(self) -> str:
        return self.__semantic

    """
    Sets the semantic layer of the word.

    PARAMETERS
    ----------
    semantic : str
        New sense id of the word.
    """

    def setSemantic(self, semantic: str):
        self.__semantic = semantic

    """
    Returns the named entity layer of the word.

    RETURNS
    -------
    NamedEntityType
        Named entity tag of the word.
    """

    def getNamedEntityType(self) -> NamedEntityType:
        return self.__namedEntityType

    """
    Sets the named entity layer of the word.

    PARAMETERS
    ----------
    namedEntity : str
        New named entity tag of the word.
    """

    def setNamedEntityType(self, namedEntity: str):
        if namedEntity is not None:
            self.__namedEntityType = NamedEntityType.getNamedEntityType(namedEntity)
        else:
            self.__namedEntityType = None

    """
    Returns the semantic role layer of the word.
    
    RETURNS
    -------
    Argument
        Semantic role tag of the word.
    """

    def getArgument(self) -> Argument:
        return self.__argument

    """
    Sets the semantic role layer of the word.

    PARAMETERS
    ----------
    argument : Argument
        New semantic role tag of the word.
    """

    def setArgument(self, argument: str):
        if self.__argument is not None:
            self.__argument = Argument(argument)
        else:
            self.__argument = None

    """
    Returns the shallow parse layer of the word.

    RETURNS
    -------
    str
        Shallow parse tag of the word.
    """

    def getShallowParse(self) -> str:
        return self.__shallowParse

    """
    Sets the shallow parse layer of the word.

    PARAMETERS
    ----------
    parse : str
        New shallow parse tag of the word.
    """

    def setShallowParse(self, parse: str):
        self.__shallowParse = parse

    """
    Returns the universal dependency layer of the word.
    
    RETURNS
    -------
    UniversalDependencyRelation
        Universal dependency relation of the word.
    """
    def getUniversalDependency(self) -> UniversalDependencyRelation:
        return self.__universalDependency

    """
    Sets the universal dependency layer of the word.

    PARAMETERS
    ----------
    to : int
        to Word related to.
    dependencyType : str
        type of dependency the word is related to.
    """
    def setUniversalDependency(self, to: int, dependencyType: str):
        self.__universalDependency = UniversalDependencyRelation(to, dependencyType)

    def getFormattedString(self, wordFormat: WordFormat):
        if wordFormat == WordFormat.SURFACE:
            return self.name
        return self.name

    def checkGazetteer(self, gazetteer: Gazetteer):
        wordLowercase = self.name.lower()
        if gazetteer.contains(wordLowercase) and self.__parse.containsTag(MorphologicalTag.PROPERNOUN):
            self.setNamedEntityType(gazetteer.getName())
        if "'" in wordLowercase and gazetteer.contains(wordLowercase[:wordLowercase.index("'")]) and \
                self.__parse.containsTag(MorphologicalTag.PROPERNOUN):
            self.setNamedEntityType(gazetteer.getName())
