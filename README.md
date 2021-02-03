For Developers
============

You can also see [Java](https://github.com/starlangsoftware/AnnotatedSentence), [C++](https://github.com/starlangsoftware/AnnotatedSentence-CPP), or [C#](https://github.com/starlangsoftware/AnnotatedSentence-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called AnnotatedSentence will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/AnnotatedSentence-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `AnnotatedSentence-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [AnnotatedCorpus](#annotatedcorpus)
+ [AnnotatedSentence](#annotatedsentence)
+ [AnnotatedWord](#annotatedword)
+ [Automatic Annotation](#automatic-annotation)


## AnnotatedCorpus

To load the annotated corpus:

	AnnotatedCorpus(self, folder: str, pattern: str = None)
	a = AnnotatedCorpus("/Turkish-Phrase", ".train")
	b = AnnotatedCorpus("/Turkish-Phrase")

To access all the sentences in a AnnotatedCorpus:

	for i in range(a.sentenceCount()):
		annotatedSentence = a.getSentence(i)
		....

## AnnotatedSentence

Bir AnnotatedSentence'daki tüm kelimelere ulaşmak için de

	for j in range(annotatedSentence.wordCount()):
		annotatedWord = annotatedSentence.getWord(j)
		...

## AnnotatedWord

An annotated word is kept in AnnotatedWord class. To access the morphological analysis of 
the annotated word:

	getParse(self) -> MorphologicalParse

Meaning of the annotated word:

	getSemantic(self) -> str

NER annotation of the annotated word:

	getNamedEntityType(self) -> NamedEntityType

Shallow parse tag of the annotated word (e.g., subject, indirect object):

	getShallowParse(self) -> str

Dependency annotation of the annotated word:

	getUniversalDependency(self) -> UniversalDependencyRelation
	
## Automatic Annotation

To detect predicates of a sentence automatically

	TurkishSentenceAutoPredicate(self, framesetList: FramesetList)

this class is used. For example, with

	a = TurkishSentenceAutoPredicate(FramesetList())
	a.autoPredicate(sentence)

the predicates of the sentence "sentence" are annotated automatically.

To detect arguments of a sentence automatically

	TurkishSentenceAutoArgument()

this class is used. For example, with

	a = TurkishSentenceAutoArgument()
	a.autoArgument(sentence)

arguments of the sentence "sentence" are annotated automatically.

To disambiguate the morphological ambiguity in a sentence automatically

        TurkishSentenceAutoDisambiguator(RootWordStatistics rootWordStatistics)
        TurkishSentenceAutoDisambiguator(FsmMorphologicalAnalyzer fsm, RootWordStatistics rootWordStatistics)

this class is used. For example, with

        a = TurkishSentenceAutoDisambiguator(RootWordStatistics())
        a.autoDisambiguate(sentence)

morphological disambugiation of the sentence "sentence" is done automatically.

To make a named entity recognition in a sentence

	TurkishSentenceAutoNER()

this class is used. For example, with

	a = TurkishSentenceAutoNER()
	a.autoNER(sentence)

named entity recognition in the sentence "sentence" is done automatically.

To make a semantic annotation in a sentence

	TurkishSentenceAutoSemantic()

this class is used. For example, with

	a = TurkishSentenceAutoSemantic()
	a.autoSemantic(sentence)

semantic annotation of the sentence "sentence" is done automatically.
