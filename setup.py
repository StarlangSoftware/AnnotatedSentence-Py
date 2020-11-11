from setuptools import setup

setup(
    name='NlpToolkit-AnnotatedSentence',
    version='1.0.20',
    packages=['AnnotatedSentence', 'AnnotatedSentence.AutoProcessor', 'AnnotatedSentence.AutoProcessor.AutoNER',
              'AnnotatedSentence.AutoProcessor.AutoArgument', 'AnnotatedSentence.AutoProcessor.AutoSemantic',
              'AnnotatedSentence.AutoProcessor.AutoPredicate', 'AnnotatedSentence.AutoProcessor.AutoDisambiguation'],
    url='https://github.com/olcaytaner/AnnotatedSentence-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Annotated Sentence Processing Library',
    install_requires=['NlpToolkit-WordNet', 'NlpToolkit-NamedEntityRecognition', 'NlpToolkit-PropBank', 'NlpToolkit-DependencyParser']
)
