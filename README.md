This resource allows for matching of Turkish words or expressions with their corresponding entries within the Turkish dictionary, the Turkish PropBank TRopBank, morphological analysis, named entity recognition, word senses from Turkish WordNet KeNet, shallow parsing, and universal dependency relation.

## Data Format

The structure of a sample annotated word is as follows:

	{turkish=Gelir}
	{morphologicalAnalysis=gelir+NOUN+A3SG+PNON+NOM}
	{metaMorphemes=gelir}
	{semantics=TUR10-0289950}
	{namedEntity=NONE}
	{propbank=ARG0$TUR10-0798130}
	{shallowParse=ÖZNE}
	{universalDependency=10$NSUBJ}

As is self-explanatory, 'turkish' tag shows the original Turkish word; 'morphologicalAnalysis' tag shows the correct morphological parse of that word; 'semantics' tag shows the ID of the correct sense of that word; 'namedEntity' tag shows the named entity tag of that word; 'shallowParse' tag shows the semantic role of that word; 'universalDependency' tag shows the index of the head word and the universal dependency for this word; 'propbank' tag shows the semantic role of that word for the verb synset id (frame id in the frame file) which is also given in that tag.

Video Lectures
============

[<img src="https://github.com/StarlangSoftware/AnnotatedSentence/blob/master/video1.jpg" width="50%">](https://youtu.be/FtoCdIELkG8)[<img src="https://github.com/StarlangSoftware/AnnotatedSentence/blob/master/video2.jpg" width="50%">](https://youtu.be/jHxZ2aMimoQ)

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/AnnotatedSentence-Cy), [Java](https://github.com/starlangsoftware/AnnotatedSentence), [C++](https://github.com/starlangsoftware/AnnotatedSentence-CPP), [C](https://github.com/starlangsoftware/AnnotatedSentence-C), [Swift](https://github.com/starlangsoftware/AnnotatedSentence-Swift), [Js](https://github.com/starlangsoftware/AnnotatedSentence-Js), or [C#](https://github.com/starlangsoftware/AnnotatedSentence-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-AnnotatedSentence
	
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

# Cite

	@INPROCEEDINGS{8374369,
  	author={O. T. {Yıldız} and K. {Ak} and G. {Ercan} and O. {Topsakal} and C. {Asmazoğlu}},
  	booktitle={2018 2nd International Conference on Natural Language and Speech Processing (ICNLSP)}, 
  	title={A multilayer annotated corpus for Turkish}, 
  	year={2018},
  	volume={},
  	number={},
  	pages={1-6},
  	doi={10.1109/ICNLSP.2018.8374369}}

For Contibutors
============

### Setup.py file
1. Do not forget to set package list. All subfolders should be added to the package list.
```
    packages=['Classification', 'Classification.Model', 'Classification.Model.DecisionTree',
              'Classification.Model.Ensemble', 'Classification.Model.NeuralNetwork',
              'Classification.Model.NonParametric', 'Classification.Model.Parametric',
              'Classification.Filter', 'Classification.DataSet', 'Classification.Instance', 'Classification.Attribute',
              'Classification.Parameter', 'Classification.Experiment',
              'Classification.Performance', 'Classification.InstanceList', 'Classification.DistanceMetric',
              'Classification.StatisticalTest', 'Classification.FeatureSelection'],
```
2. Package name should be lowercase and only may include _ character.
```
    name='nlptoolkit_math',
```

### Python files
1. Do not forget to comment each function.
```
    def __broadcast_shape(self, shape1: Tuple[int, ...], shape2: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Determines the broadcasted shape of two tensors.

        :param shape1: Tuple representing the first tensor shape.
        :param shape2: Tuple representing the second tensor shape.
        :return: Tuple representing the broadcasted shape.
        """
```
2. Function names should follow caml case.
```
    def addItem(self, item: str):
```
3. Local variables should follow snake case.
```
	det = 1.0
	copy_of_matrix = copy.deepcopy(self)
```
4. Class variables should be declared in each file.
```
class Eigenvector(Vector):
    eigenvalue: float
```
5. Variable types should be defined for function parameters and class variables.
```
    def getIndex(self, item: str) -> int:
```
6. For abstract methods, use ABC package and declare them with @abstractmethod.
```
    @abstractmethod
    def train(self, train_set: list[Tensor]):
        pass
```
7. For private methods, use __ as prefix in their names.
```
    def __infer_shape(self, data: Union[List, List[List], List[List[List]]]) -> Tuple[int, ...]:
```
8. For private class variables, use __ as prefix in their names.
```
class Matrix(object):
    __row: int
    __col: int
    __values: list[list[float]]
```
9. Write \_\_repr\_\_ class methods as toString methods
10. Write getter and setter class methods.
```
    def getOptimizer(self) -> Optimizer:
        return self.optimizer
    def setValue(self, value: Optional[Tensor]) -> None:
        self._value = value
```
11. If there are multiple constructors for a class, define them as constructor1, constructor2, ..., then from the original constructor call these methods.
```
    def constructor1(self):
        self.__values = []
        self.__size = 0

    def constructor2(self, values: list):
        self.__values = values.copy()
        self.__size = len(values)

    def __init__(self,
                 valuesOrSize=None,
                 initial=None):
        if valuesOrSize is None:
            self.constructor1()
        elif isinstance(valuesOrSize, list):
            self.constructor2(valuesOrSize)
```
12. Extend test classes from unittest and use separate unit test methods.
```
class TensorTest(unittest.TestCase):

    def test_inferred_shape(self):
        a = Tensor([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual((2, 2), a.getShape())

    def test_shape(self):
        a = Tensor([1.0, 2.0, 3.0])
        self.assertEqual((3, ), a.getShape())
```
13. Enumerated types should be used when necessary as enum classes.
```
class AttributeType(Enum):
    """
    Continuous Attribute
    """
    CONTINUOUS = auto()
    """
    Discrete Attribute
    """
    DISCRETE = auto()
```
