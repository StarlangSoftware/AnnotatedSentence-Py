from Corpus.WordFormat import WordFormat
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation
from Dictionary.Word import Word
from FrameNet.FrameElement import FrameElement
from MorphologicalAnalysis.FsmParse import FsmParse
from MorphologicalAnalysis.MetamorphicParse import MetamorphicParse
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse
from MorphologicalAnalysis.MorphologicalTag import MorphologicalTag
from NamedEntityRecognition.Gazetteer import Gazetteer
from NamedEntityRecognition.NamedEntityType import NamedEntityType
from NamedEntityRecognition.Slot import Slot
from PropBank.Argument import Argument
from SentiNet.PolarityType import PolarityType

import re

from AnnotatedSentence.Language import Language
from AnnotatedSentence.ViewLayerType import ViewLayerType


class AnnotatedWord(Word):
    """
     * In order to add another layer, do the following:
     * 1. Select a name for the layer.
     * 2. Add a new constant to ViewLayerType.
     * 3. Add private attribute.
     * 4. Add an if-else to the constructor, where you set the private attribute with the layer name.
     * 5. Update toString method.
     * 6. Add initial value to the private attribute in other constructors.
     * 7. Update getLayerInfo.
     * 8. Add getter and setter methods.
    """
    __parse: MorphologicalParse
    __metamorphic_parse: MetamorphicParse
    __semantic: str
    __named_entity_type: NamedEntityType
    __argument: Argument
    __frame_element: FrameElement
    __shallow_parse: str
    __universal_dependency: UniversalDependencyRelation
    __slot: Slot
    __polarity: PolarityType
    __ccg: str
    __pos_tag: str
    __language: Language

    def __init__(self,
                 word: str,
                 layerType=None):
        """
        Constructor for the AnnotatedWord class. Gets the word with its annotation layers as input and sets the
        corresponding layers.

        PARAMETERS
        ----------
        word : str
            Input word with annotation layers
        """
        self.__parse = None
        self.__metamorphic_parse = None
        self.__semantic = None
        self.__named_entity_type = None
        self.__argument = None
        self.__frame_element = None
        self.__shallow_parse = None
        self.__universal_dependency = None
        self.__slot = None
        self.__polarity = None
        self.__ccg = None
        self.__pos_tag = None
        self.__language = Language.TURKISH
        if layerType is None:
            split_layers = re.compile("[{}]").split(word)
            for layer in split_layers:
                if len(layer) == 0:
                    continue
                if "=" not in layer:
                    self.name = layer
                    continue
                layerType = layer[:layer.index("=")]
                layer_value = layer[layer.index("=") + 1:]
                if layerType == "turkish" or layerType == "english" or layerType == "persian":
                    self.name = layer_value
                    self.__language = AnnotatedWord.getLanguageFromString(layerType)
                elif layerType == "morphologicalAnalysis":
                    self.__parse = MorphologicalParse(layer_value)
                elif layerType == "metaMorphemes":
                    self.__metamorphic_parse = MetamorphicParse(layer_value)
                elif layerType == "namedEntity":
                    self.__named_entity_type = NamedEntityType.getNamedEntityType(layer_value)
                elif layerType == "propbank" or layerType == "propBank":
                    self.__argument = Argument(layer_value)
                elif layerType == "framenet" or layerType == "frameNet":
                    self.__frame_element = FrameElement(layer_value)
                elif layerType == "shallowParse":
                    self.__shallow_parse = layer_value
                elif layerType == "semantics":
                    self.__semantic = layer_value
                elif layerType == "slot":
                    self.__slot = Slot(layer_value)
                elif layerType == "polarity":
                    self.setPolarity(layer_value)
                elif layerType == "universalDependency":
                    values = layer_value.split("$")
                    self.__universal_dependency = UniversalDependencyRelation(int(values[0]), values[1])
                elif layerType == "ccg":
                    self.__ccg = layer_value
                elif layerType == "posTag":
                    self.__pos_tag = layer_value
        elif isinstance(layerType, NamedEntityType):
            super().__init__(word)
            self.__named_entity_type = layerType
            self.__argument = Argument("NONE")
        elif isinstance(layerType, MorphologicalParse):
            super().__init__(word)
            self.__parse = layerType
            self.__named_entity_type = NamedEntityType.NONE
            self.__argument = Argument("NONE")
        elif isinstance(layerType, FsmParse):
            super().__init__(word)
            self.__parse = layerType
            self.__named_entity_type = NamedEntityType.NONE
            self.setMetamorphicParse(layerType.withList())
            self.__argument = Argument("NONE")

    def __str__(self) -> str:
        """
        Converts an AnnotatedWord to string. For each annotation layer, the method puts a left brace, layer name,
        equal sign and layer value finishing with right brace.

        RETURNS
        -------
        str
            String form of the AnnotatedWord.
        """
        result = ""
        if self.__language == Language.TURKISH:
            result = "{turkish=" + self.name + "}"
        elif self.__language == Language.ENGLISH:
            result = "{english=" + self.name + "}"
        elif self.__language == Language.PERSIAN:
            result = "{persian=" + self.name + "}"
        if self.__parse is not None:
            result = result + "{morphologicalAnalysis=" + self.__parse.__str__() + "}"
        if self.__metamorphic_parse is not None:
            result = result + "{metaMorphemes=" + self.__metamorphic_parse.__str__() + "}"
        if self.__semantic is not None:
            result = result + "{semantics=" + self.__semantic + "}"
        if self.__named_entity_type is not None:
            result = result + "{namedEntity=" + NamedEntityType.getNamedEntityString(self.__named_entity_type) + "}"
        if self.__argument is not None:
            result = result + "{propbank=" + self.__argument.__str__() + "}"
        if self.__frame_element is not None:
            result = result + "{framenet=" + self.__frame_element.__str__() + "}"
        if self.__slot is not None:
            result = result + "{slot=" + self.__slot.__str__() + "}"
        if self.__shallow_parse is not None:
            result = result + "{shallowParse=" + self.__shallow_parse + "}"
        if self.__polarity is not None:
            result = result + "{polarity=" + self.getPolarityString() + "}"
        if self.__universal_dependency is not None:
            result = result + "{universalDependency=" + self.__universal_dependency.to().__str__() + "$" + \
                     self.__universal_dependency.__str__() + "}"
        if self.__ccg is not None:
            result = result + "{ccg=" + self.__ccg + "}"
        if self.__pos_tag is not None:
            result = result + "{posTag=" + self.__pos_tag + "}"
        return result

    def getLayerInfo(self, viewLayerType: ViewLayerType) -> str:
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
        if viewLayerType == ViewLayerType.INFLECTIONAL_GROUP:
            if self.__parse is not None:
                return self.__parse.__str__()
        elif viewLayerType == ViewLayerType.META_MORPHEME:
            if self.__metamorphic_parse is not None:
                return self.__metamorphic_parse.__str__()
        elif viewLayerType == ViewLayerType.SEMANTICS:
            return self.__semantic
        elif viewLayerType == ViewLayerType.NER:
            if self.__named_entity_type is not None:
                return self.__named_entity_type.__str__()
        elif viewLayerType == ViewLayerType.SHALLOW_PARSE:
            return self.__shallow_parse
        elif viewLayerType == ViewLayerType.TURKISH_WORD:
            return self.name
        elif viewLayerType == ViewLayerType.PROPBANK:
            if self.__argument is not None:
                return self.__argument.__str__()
        elif viewLayerType == ViewLayerType.FRAMENET:
            if self.__frame_element is not None:
                return self.__frame_element.__str__()
        elif viewLayerType == ViewLayerType.SLOT:
            if self.__slot is not None:
                return self.__slot.__str__()
        elif viewLayerType == ViewLayerType.POLARITY:
            if self.__polarity is not None:
                return self.getPolarityString()
        elif viewLayerType == ViewLayerType.DEPENDENCY:
            if self.__universal_dependency is not None:
                return self.__universal_dependency.to().__str__() + "$" + self.__universal_dependency.__str__()
        elif viewLayerType == ViewLayerType.CCG:
            return self.__ccg
        elif viewLayerType == ViewLayerType.POS_TAG:
            return self.__pos_tag
        else:
            return None

    def getParse(self) -> MorphologicalParse:
        """
        Returns the morphological parse layer of the word.

        RETURNS
        -------
        MorphologicalParse
            The morphological parse of the word.
        """
        return self.__parse

    def setParse(self, parseString: MorphologicalParse):
        """
        Sets the morphological parse layer of the word.

        PARAMETERS
        ----------
        parseString : str
            The new morphological parse of the word in string form.
        """
        if parseString is not None:
            self.__parse = MorphologicalParse(parseString)
        else:
            self.__parse = None

    def getMetamorphicParse(self) -> MetamorphicParse:
        """
        Returns the metamorphic parse layer of the word.

        RETURNS
        -------
        MetamorphicParse
            The metamorphic parse of the word.
        """
        return self.__metamorphic_parse

    def setMetamorphicParse(self, parseString: str):
        """
        Sets the metamorphic parse layer of the word.

        PARAMETERS
        ----------
        parseString : str
            The new metamorphic parse of the word in string form.
        """
        self.__metamorphic_parse = MetamorphicParse(parseString)

    def getSemantic(self) -> str:
        """
        Returns the semantic layer of the word.

        RETURNS
        -------
        str
            Sense id of the word.
        """
        return self.__semantic

    def setSemantic(self, semantic: str):
        """
        Sets the semantic layer of the word.

        PARAMETERS
        ----------
        semantic : str
            New sense id of the word.
        """
        self.__semantic = semantic

    def getNamedEntityType(self) -> NamedEntityType:
        """
        Returns the named entity layer of the word.

        RETURNS
        -------
        NamedEntityType
            Named entity tag of the word.
        """
        return self.__named_entity_type

    def setNamedEntityType(self, namedEntity: str):
        """
        Sets the named entity layer of the word.

        PARAMETERS
        ----------
        namedEntity : str
            New named entity tag of the word.
        """
        if namedEntity is not None:
            self.__named_entity_type = NamedEntityType.getNamedEntityType(namedEntity)
        else:
            self.__named_entity_type = None

    def getArgument(self) -> Argument:
        """
        Returns the semantic role layer of the word.

        RETURNS
        -------
        Argument
            Semantic role tag of the word.
        """
        return self.__argument

    def setArgument(self, argument: str):
        """
        Sets the semantic role layer of the word.

        PARAMETERS
        ----------
        argument : Argument
            New semantic role tag of the word.
        """
        if argument is not None:
            self.__argument = Argument(argument)
        else:
            self.__argument = None

    def getFrameElement(self) -> FrameElement:
        """
        Returns the framenet layer of the word.

        RETURNS
        -------
        FrameElement
            Framenet tag of the word.
        """
        return self.__frame_element

    def setFrameElement(self, frameElement: str):
        """
        Sets the framenet layer of the word.

        PARAMETERS
        ----------
        frameElement : str
            New framenet tag of the word.
        """
        if frameElement is not None:
            self.__frame_element = FrameElement(frameElement)
        else:
            self.__frame_element = None

    def getSlot(self) -> Slot:
        """
        Returns the slot layer of the word.

        RETURNS
        -------
        Slot
            Slot tag of the word.
        """
        return self.__slot

    def setSlot(self, slot: str):
        """
        Sets the slot layer of the word.

        PARAMETERS
        ----------
        slot : str
            New slot tag of the word.
        """
        if slot is not None:
            self.__slot = Slot(slot)
        else:
            self.__slot = None

    def getPolarity(self) -> PolarityType:
        """
        Returns the polarity layer of the word.

        RETURNS
        -------
        PolarityType
            Polarity tag of the word.
        """
        return self.__polarity

    def getPolarityString(self) -> str:
        """
        Returns the polarity layer of the word.

        RETURNS
        -------
        str
            Polarity string of the word.
        """
        if self.__polarity == PolarityType.POSITIVE:
            return "positive"
        elif self.__polarity == PolarityType.NEGATIVE:
            return "negative"
        elif self.__polarity == PolarityType.NEUTRAL:
            return "neutral"
        else:
            return "neutral"

    def setPolarity(self, polarity: str):
        """
        Sets the polarity layer of the word.

        PARAMETERS
        ----------
        polarity : str
            New polarity tag of the word.
        """
        if polarity is not None:
            if polarity == "positive" or polarity == "pos":
                self.__polarity = PolarityType.POSITIVE
            elif polarity == "negative" or polarity == "neg":
                self.__polarity = PolarityType.NEGATIVE
            else:
                self.__polarity = PolarityType.NEUTRAL
        else:
            self.__polarity = None

    def getShallowParse(self) -> str:
        """
        Returns the shallow parse layer of the word.

        RETURNS
        -------
        str
            Shallow parse tag of the word.
        """
        return self.__shallow_parse

    def setShallowParse(self, parse: str):
        """
        Sets the shallow parse layer of the word.

        PARAMETERS
        ----------
        parse : str
            New shallow parse tag of the word.
        """
        self.__shallow_parse = parse

    def getCcg(self) -> str:
        """
        Returns the ccg layer of the word.

        RETURNS
        -------
        str
            Ccg tag of the word.
        """
        return self.__ccg

    def setCcg(self, ccg: str):
        """
        Sets the ccg layer of the word.

        PARAMETERS
        ----------
        parse : str
            New ccg tag of the word.
        """
        self.__ccg = ccg

    def getPosTag(self) -> str:
        """
        Returns the posTag layer of the word.

        RETURNS
        -------
        str
            Pos tag of the word.
        """
        return self.__pos_tag

    def setPosTag(self, posTag: str):
        """
        Sets the posTag layer of the word.

        PARAMETERS
        ----------
        posTag : str
            New pos tag of the word.
        """
        self.__pos_tag = posTag

    def getUniversalDependency(self) -> UniversalDependencyRelation:
        """
        Returns the universal dependency layer of the word.

        RETURNS
        -------
        UniversalDependencyRelation
            Universal dependency relation of the word.
        """
        return self.__universal_dependency

    def setUniversalDependency(self, to: int, dependencyType: str):
        """
        Sets the universal dependency layer of the word.

        PARAMETERS
        ----------
        to : int
            to Word related to.
        dependencyType : str
            type of dependency the word is related to.
        """
        if to < 0:
            self.__universal_dependency = None
        else:
            self.__universal_dependency = UniversalDependencyRelation(to, dependencyType)

    def getUniversalDependencyFormat(self, sentenceLength: int) -> str:
        if self.__parse is not None:
            uPos = self.__parse.getUniversalDependencyPos()
            result = self.name + "\t" + self.__parse.getWord().getName() + "\t" + \
                     uPos + "\t_\t"
            features = self.__parse.getUniversalDependencyFeatures(uPos)
            if len(features) == 0:
                result = result + "_"
            else:
                first = True
                for feature in features:
                    if first:
                        first = False
                    else:
                        result += "|"
                    result += feature
            result += "\t"
            if self.__universal_dependency is not None and self.__universal_dependency.to() <= sentenceLength:
                result += self.__universal_dependency.to().__str__() + "\t" + \
                          self.__universal_dependency.__str__().lower() + "\t"
            else:
                result += "_\t_\t"
            result += "_\t_"
            return result
        else:
            return self.name + "\t" + self.name + "\t_\t_\t_\t_\t_\t_\t_"

    def getFormattedString(self, wordFormat: WordFormat):
        if wordFormat == WordFormat.SURFACE:
            return self.name
        return self.name

    def checkGazetteer(self, gazetteer: Gazetteer):
        word_lower_case = self.name.lower()
        if gazetteer.contains(word_lower_case) and self.__parse.containsTag(MorphologicalTag.PROPERNOUN):
            self.setNamedEntityType(gazetteer.getName())
        if "'" in word_lower_case and gazetteer.contains(word_lower_case[:word_lower_case.index("'")]) and \
                self.__parse.containsTag(MorphologicalTag.PROPERNOUN):
            self.setNamedEntityType(gazetteer.getName())

    def getLanguage(self) -> Language:
        """
        Returns the language of the word.

        RETURNS
        ----------
        The language of the word.
        """
        return self.__language

    @staticmethod
    def getLanguageFromString(languageString: str) -> Language:
        """
        Converts a language string to language.

        PARAMETERS
        ----------
        languageString : str
            String defining the language name.

        RETURNS
        ----------
        Language corresponding to the languageString.
        """
        if languageString == "turkish" or languageString == "Turkish":
            return Language.TURKISH
        elif languageString == "english" or languageString == "English":
            return Language.ENGLISH
        elif languageString == "persian" or languageString == "Persian":
            return Language.PERSIAN
        else:
            return Language.TURKISH
