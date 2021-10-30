from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-AnnotatedSentence',
    version='1.0.35',
    packages=['AnnotatedSentence'],
    url='https://github.com/olcaytaner/AnnotatedSentence-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Annotated Sentence Processing Library',
    install_requires=['NlpToolkit-WordNet', 'NlpToolkit-NamedEntityRecognition', 'NlpToolkit-PropBank', 'NlpToolkit-DependencyParser', 'NlpToolkit-FrameNet', 'NlpToolkit-SentiNet'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
