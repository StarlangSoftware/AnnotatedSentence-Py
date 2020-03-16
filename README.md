# AnnotatedSentence

This resource allows for matching of Turkish words or expressions with their corresponding entries within the Turkish dictionary and the Turkish PropBank, morphological analysis, named entity recognition and shallow parsing.

For Developers
============
You can also see either [Java](https://github.com/olcaytaner/AnnotatedSentence) 
or [C++](https://github.com/olcaytaner/AnnotatedSentence-CPP) repository.
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

	git clone https://github.com/olcaytaner/AnnotatedSentence-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `AnnotatedSentence-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run AnnotatedSentence-Py.


## Data Format

The structure of a sample annotated word is as follows:

	{turkish=yatırımcılar}
	{analysis=yatırımcı+NOUN+A3PL+PNON+NOM}
	{semantics=0841060}
	{namedEntity=NONE}
	{shallowParse=ÖZNE}
	{propbank=ARG0:0006410}

As is self-explanatory, 'turkish' tag shows the original Turkish word; 'analysis' tag shows the correct morphological parse of that word; 'semantics' tag shows the ID of the correct sense of that word; 'namedEntity' tag shows the named entity tag of that word; 'shallowParse' tag shows the semantic role of that word; 'propbank' tag shows the semantic role of that word for the verb synset id (frame id in the frame file) which is also given in that tag.

Detailed Description
============
+ [AnnotatedCorpus](#annotatedcorpus)
+ [AnnotatedSentence](#annotatedsentence)
+ [AnnotatedWord](#annotatedword)
+ [Automatic Annotation](#automatic-annotation)


## AnnotatedCorpus

İşaretlenmiş corpusu yüklemek için

	AnnotatedCorpus(self, folder: str, pattern: str = None)
	a = AnnotatedCorpus("/Turkish-Phrase", ".train")
	b = AnnotatedCorpus(new File("/Turkish-Phrase"))

Bir AnnotatedCorpus'daki tüm cümlelere erişmek için

	for i in range(a.sentenceCount()):
		annotatedSentence = a.getSentence(i)
		....

## AnnotatedSentence

Bir AnnotatedSentence'daki tüm kelimelere ulaşmak için de

	for j in range(annotatedSentence.wordCount()):
		annotatedWord = annotatedSentence.getWord(j)
		...

## AnnotatedWord

İşaretlenmiş bir kelime AnnotatedWord sınıfında tutulur. İşaretlenmiş kelimenin morfolojik
analizi

	getParse(self) -> MorphologicalParse

İşaretlenmiş kelimenin anlamı

	getSemantic(self) -> str

İşaretlenmiş kelimenin NER anotasyonu

	getNamedEntityType(self) -> NamedEntityType

İşaretlenmiş kelimenin özne, dolaylı tümleç, vs. shallow parse tagı

	getShallowParse(self) -> str

İşaretlenmiş kelimenin dependency anotasyonu

	getUniversalDependency(self) -> UniversalDependencyRelation
	
## Automatic Annotation

Bir cümlenin Predicatelarını otomatik olarak belirlemek için

	TurkishSentenceAutoPredicate(self, framesetList: FramesetList)

sınıfı kullanılır. Örneğin,

	a = TurkishSentenceAutoPredicate(FramesetList())
	a.autoPredicate(sentence)

ile sentence cümlesinin predicateları otomatik olarak işaretlenir.

Bir cümlenin argümanlarını otomatik olarak belirlemek için

	TurkishSentenceAutoArgument()

sınıfı kullanılır. Örneğin,

	a = TurkishSentenceAutoArgument()
	a.autoArgument(sentence)

ile sentence cümlesinin argümanları otomatik olarak işaretlenir.

Bir cümlede adlandırılmış varlık tanıma yapmak için

	TurkishSentenceAutoNER()

sınıfı kullanılır. Örneğin,

	a = TurkishSentenceAutoNER()
	a.autoNER(sentence)

ile sentence cümlesinde varlık tanıma otomatik olarak yapılır.

Bir cümlede anlamsal işaretleme için

	TurkishSentenceAutoSemantic()

sınıfı kullanılır. Örneğin,

	a = TurkishSentenceAutoSemantic()
	a.autoSemantic(sentence)

ile sentence cümlesinde anlamsal işaretleme otomatik olarak yapılır.
