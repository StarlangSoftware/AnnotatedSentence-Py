from setuptools import setup

setup(
    name='NlpToolkit-AnnotatedSentence',
    version='1.0.32',
    packages=['AnnotatedSentence'],
    url='https://github.com/olcaytaner/AnnotatedSentence-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Annotated Sentence Processing Library',
    install_requires=['NlpToolkit-WordNet', 'NlpToolkit-NamedEntityRecognition', 'NlpToolkit-PropBank', 'NlpToolkit-DependencyParser', 'NlpToolkit-FrameNet', 'NlpToolkit-SentiNet']
)
