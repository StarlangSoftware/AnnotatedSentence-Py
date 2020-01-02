from __future__ import annotations
from enum import Enum, auto

"""
Enumerator class for View layer types.
"""


class ViewLayerType(Enum):
    PART_OF_SPEECH = auto()
    INFLECTIONAL_GROUP = auto()
    META_MORPHEME = auto()
    META_MORPHEME_MOVED = auto()
    TURKISH_WORD = auto()
    PERSIAN_WORD = auto()
    ENGLISH_WORD = auto()
    WORD = auto()
    SEMANTICS = auto()
    NER = auto()
    DEPENDENCY = auto()
    PROPBANK = auto()
    SHALLOW_PARSE = auto()
    ENGLISH_PROPBANK = auto()
    ENGLISH_SEMANTICS = auto()
